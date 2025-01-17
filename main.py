import os

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from translator import save_rules_to_file, save_examples_to_prolog, merge_examples_and_rules, \
    merge_rules_and_explainability
from consultScasp import execute_command
from insertPatient import translate_and_insert_new_patient
import webbrowser


def menu():
    print("Selecciona una opción:")
    print("1. Insertar un nuevo paciente")
    print("2. Realizar consulta con paciente introducido")
    print("3. Generar reglas")
    print("4. Realizar consulta con pacientes de ejemplo")
    print("5. Salir")


def insert_new_patient(columns):
    #patient_id = input("Introduce el ID del nuevo paciente: ")
    translate_and_insert_new_patient("Generated", columns)#patient_id


def consulta_con_pacientes_de_ejemplo(df):
    rule_files = 'rules_with_explainability.pl'
    # Save examples in Prolog format
    dataset_examples = save_examples_to_prolog(df, percentage=2)

    # Merge examples and rules into a single file
    final_prolog_file = "final_dataset_and_rules_with_explainability.pl"
    explainability_file = "explainability.pl"
    consult_file = "consult.pl"
    merge_examples_and_rules(dataset_examples, rule_files, final_prolog_file, explainability_file, consult_file)
    print(f"\nFinal file generated: {final_prolog_file}")

    # Make consult
    # Rute to scasp
    scasp_path = '/home/walter/.ciao/build/bin/scasp'  # put yours here
    # Execute
    command = f'bash -i -c "{scasp_path} {final_prolog_file} --tree --html --human"'
    output_file = 'output_consult.txt'
    execute_command(command, output_file)

    # Abrir el archivo HTML generado en el navegador
    html_file = os.path.abspath(final_prolog_file.replace(".pl", ".html"))  # Ruta absoluta
    if os.path.exists(html_file):
        webbrowser.open(f"file://{html_file}")
    else:
        print(f"Error: No se encontró el archivo HTML en {html_file}")


def consulta_con_pacientes_introducido():
    new_patient = "patientGenerated.pl"
    # Leer el archivo del paciente generado
    with open(new_patient, 'r') as f:
        new_patient_examples = [line.strip() for line in f if line.strip()]  # Convertir líneas en lista y omitir vacías

    # Rute to scasp
    scasp_path = '/home/walter/.ciao/build/bin/scasp'  # put yours here
    # Execute
    file_name = 'rules_with_explainability.pl'
    #merge_rules_and_consult(file_name, consult_file)
    inter_file = "inter.pl"
    explainability_file = "explainability.pl"
    consult_file = "consult.pl"
    merge_examples_and_rules(new_patient_examples, file_name, inter_file, explainability_file, consult_file)
    command = f'bash -i -c "{scasp_path} {inter_file} --tree --html --human"'
    output_file = 'output_consult.txt'
    execute_command(command, output_file)

    # Abrir el archivo HTML generado en el navegador
    html_file = os.path.abspath(inter_file.replace(".pl", ".html"))  # Ruta absoluta
    if os.path.exists(html_file):
        webbrowser.open(f"file://{html_file}")
    else:
        print(f"Error: No se encontró el archivo HTML en {html_file}")



def train_random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train the Random Forest
    random_forest = RandomForestClassifier(n_estimators=6, max_depth=4)
    random_forest.fit(X_train, y_train)

    # Evaluate the Random Forest
    rf_preds = random_forest.predict(X_test)
    print("\nMetrics:")
    print(classification_report(y_test, rf_preds))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, rf_preds))
    print("Accuracy:", accuracy_score(y_test, rf_preds))

    return random_forest


def generate_rules(X, y, df):
    random_forest = train_random_forest(X, y)
    # Save rules from the trees to .pl files
    rule_files = []
    for idx, tree in enumerate(random_forest.estimators_):
        filename = f"diagnosis_{idx + 1}.pl"
        print(f"\nGenerating rules for tree {idx + 1}...")
        save_rules_to_file(tree, X.columns, df, filename, idx)
        rule_files.append(filename)

    # Merge rules in one file with the explainability
    prolog_file = "rules_with_explainability.pl"
    explainability_file = "explainability.pl"
    consult_file = "consult.pl"
    merge_rules_and_explainability(rule_files, prolog_file, explainability_file, consult_file)


def load_dataset():
    # Load the dataset
    columns = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach",
        "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]

    df = pd.read_csv("Heart_disease_cleveland_new.csv", header=0, names=columns)

    X = df.drop("target", axis=1)
    y = df["target"]

    return df, X, y, columns


def main():
    df, X, y, columns = load_dataset()
    while True:
        menu()
        choice = input("Introduce el número de opción: ")

        if choice == "1": # Insertar paciente nuevo
            insert_new_patient(columns)
        elif choice == "2": # Consulta con paciente introducido
            consulta_con_pacientes_introducido()
        elif choice == "3": # Generar reglas
            generate_rules(X, y, df)
        elif choice == "4": # Hacer consulta con pacientes de ejemplo
            consulta_con_pacientes_de_ejemplo(df)
        elif choice == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")


if __name__ == "__main__":
    main()
