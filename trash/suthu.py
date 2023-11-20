def sort_file_content(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            lines = file.readlines()
            # Sort the lines alphabetically
            sorted_lines = sorted(lines)

        # Open the output file for writing
        with open(output_file, 'w') as file:
            # Write the sorted lines back to the file
            file.writelines(sorted_lines)

        print(f"Content sorted and saved to {output_file}")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define input and output file paths
input_file_path = 'input.txt'
output_file_path = 'sorted_output.txt'

# Call the custom function to sort the content
sort_file_content(input_file_path, output_file_path)
