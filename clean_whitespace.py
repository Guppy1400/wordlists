def clean_whitespace(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    cleaned_lines = [line.replace(' ', '').strip() for line in lines]
    
    with open(output_file_path, 'w') as file:
        for line in cleaned_lines:
            if line:  # This ensures not to write empty lines
                file.write(line + '\n')

# Specify the path to your input file
input_file = 'Animals1.txt'  # This should be your uploaded file path
output_file = 'Cleaned_Animals.txt'  # Path where the cleaned file will be saved

clean_whitespace(input_file, output_file)
