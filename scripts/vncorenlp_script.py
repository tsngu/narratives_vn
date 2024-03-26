import py_vncorenlp
import os

# Automatically download VnCoreNLP components from the original repository
# and save them in some local working folder
#py_vncorenlp.download_model(save_dir='../vncorenlp/')

# Charger VnCoreNLP depuis le dossier de travail local qui contient à la fois `VnCoreNLP-1.2.jar` et `models`
model = py_vncorenlp.VnCoreNLP(save_dir='../vncorenlp/')

# Récupérer la liste de tous les fichiers .txt dans le dossier output/btt/
input_folder = "../output/btt/"
output_folder = "../output/vncorenlp/btt/"
txt_files = [file for file in os.listdir(input_folder) if file.endswith(".txt")]

# Boucler sur chaque fichier .txt
for txt_file in txt_files:
    input_file_path = os.path.join(input_folder, txt_file)
    output_file_path = os.path.join(output_folder, txt_file)
    
    # Annoter le fichier d'entrée et enregistrer le résultat dans le dossier de sortie avec le même nom de fichier
    model.annotate_file(input_file=input_file_path, output_file=output_file_path)
