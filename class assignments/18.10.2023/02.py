def extract_names(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        filtered_names = [name.strip() for name in lines if name.strip().endswith('h')]
        with open(output_file, 'w') as f:
            for name in filtered_names:
                f.write(name + '\n')
        print('name extracted to ', output_file)
    except FileNotFoundError:
        print("The file", input_file, "does not exist.")
    except Exception as e:
        print("error:", str(e))


input_file = 'names.txt'
output_file = 'end_h.txt'
extract_names(input_file, output_file)
