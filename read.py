import re

def find_heritability():

    # Define the regular expression pattern to match words related to heritability
    pattern = r'\b(heritable|inherit|inheritance|inherited|heritability|inheritabily|inheritable)\b'

    # Input and output file names
    input_file_name = 'origin.txt'
    output_file_name = 'output.txt'

    # Open the input file for reading and the output file for writing
    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        line_number = 0  # Initialize line number counter
        for line in input_file:
            line_number += 1 # Add to the number counter for each line to be iterated
            matches = re.finditer(pattern, line, re.IGNORECASE) # Look for the pattern on each line and ignore the casing of every word
            for match in matches:
                word = match.group(0)
                output_line = f"{line_number}\t{word}"
                output_file.write(output_line + '\n') # Write the line number and matched word to the output file with a new line between each match

if __name__ == '__main__':
    find_heritability()
