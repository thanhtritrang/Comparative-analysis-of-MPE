def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        with open(output_file, 'w') as file:
            for line in lines:
                line = line.strip()  # Remove any leading/trailing whitespace
                modified_line = f"{line} 0\n"  # Add ' 0' at the end of the line
                file.write(modified_line)
        
        print(f"File '{output_file}' has been created successfully.")

    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'Wiki-Vote.txt'  # Replace with your input file name
output_file = 'Wiki-Vote0.txt'  # Replace with your desired output file name
process_file(input_file, output_file)
