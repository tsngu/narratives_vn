import os
import csv
import spacy

# Load the French language model
nlp = spacy.load("fr_core_news_sm")

# Function to extract subject, verb, and object from the dependency parsed text
def extract_subject_verb_object(text):
    doc = nlp(text)
    subject = ""
    verb = ""
    obj = ""
    for token in doc:
        if token.dep_ == "nsubj":
            subject = token.text
        elif token.dep_ == "ROOT":
            verb = token.text
        elif token.dep_ == "obj":
            obj = token.text
    return subject, verb, obj

# Folder path containing input files
input_folder = "vnp_fr"
output_file = "extracted_info_vnp.csv"

# Function to process each file in the folder
def process_files_in_folder(folder_path):
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["File", "Subject", "Verb", "Object"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Iterate over files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()
                    subject, verb, obj = extract_subject_verb_object(text)
                    writer.writerow({"File": filename, "Subject": subject, "Verb": verb, "Object": obj})

# Process files in the input folder
process_files_in_folder(input_folder)

print("Extraction complete. Results written to", output_file)

