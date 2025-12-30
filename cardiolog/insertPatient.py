def translate_and_insert_new_patient(patient_id, columns):
    values = []
    examples = []

    # Value per column
    for column in columns:
        value = input(f"What is your {column}?\n")
        while value == "":
            value = input(f"What is your {column}?\n")
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)  # Convert flots to int
        except ValueError:
            pass  # Non-numeric as strings
        values.append(value)

    patient_name = f"patient{patient_id}"

    # Create relations in Prolog
    for col_name, value in zip(columns, values):
        examples.append(f"{col_name}({patient_name}, {value}).")

    # Create file name
    output_file = f"prolog/patient{patient_id}.pl"

    # Save relations in file
    with open(output_file, 'w') as f:
        f.write("% Examples:\n")
        for line in examples:
            f.write(line + "\n")

    print(f"Prolog file generated: {output_file}")


# If wanna tryout by itself:
if __name__ == "__main__":
    """
    # Call function with a specific ID for a patient
    translate_and_insert_new_patient("_generated")
    """