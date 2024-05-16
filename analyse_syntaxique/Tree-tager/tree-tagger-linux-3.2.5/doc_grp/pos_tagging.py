import subprocess

# Function to annotate tokens with POS using TreeTagger
def annotate_with_pos(input_file, output_file):
    # Open input and output files
    with open(input_file, 'r', encoding='utf-8') as f_input, open(output_file, 'w', encoding='utf-8') as f_output:
        # Read lines from input file
        lines = f_input.readlines()

        # Process each line
        for line in lines:
            # Run TreeTagger on the current line
            process_echo = subprocess.Popen(["echo", line], stdout=subprocess.PIPE)
            process_tree_tagger = subprocess.Popen("./cmd/tree-tagger-french", stdin=process_echo.stdout, stdout=subprocess.PIPE)
            output, _ = process_tree_tagger.communicate()
            tagged_tokens = output.decode('utf-8').split('\n')

            # Write annotated tokens to the output file
            for token in tagged_tokens:
                if token.strip():  # Check if the token is not empty
                    f_output.write(token + '\n')

# Example usage of the function
if __name__ == "__main__":
    input_file = "dataset2.tsv"  # Replace with the path to your input file
    output_file = "output.txt"  # Replace with the desired path for the output file
    annotate_with_pos(input_file, output_file)

