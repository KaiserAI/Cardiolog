import subprocess

# Función para ejecutar el comando
def execute_command(command, output_file):
    try:
        print(f"Execute command: {command}")
        with open(output_file, 'w') as output:
            # Redirect output
            result = subprocess.run(command, shell=True, check=True, stdout=output, stderr=subprocess.PIPE, input=b'\n')

        # Show result
        print(f"Exit save in {output.name}.")

    except subprocess.CalledProcessError as e:
        print(f"Error in command: {e}")



# If wanna tryout by itself:
if __name__ == "__main__":
    """
    # Rute to scasp
    scasp_path = '/home/walter/.ciao/build/bin/scasp' # put yours here

    # Execute
    file_name = 'final_dataset_and_rules_with_explainability.pl'
    command = f'bash -i -c "{scasp_path} {file_name} --tree --html --human"'
    output_file = 'output_final_dataset.txt'

    execute_command(command, output_file)
    """