import os
import py_vncorenlp
from tqdm import tqdm

# Charger VnCoreNLP depuis le dossier de travail local qui contient à la fois `VnCoreNLP-1.2.jar` et `models`
model = py_vncorenlp.VnCoreNLP(save_dir='../vncorenlp/')

# Récupérer la liste de tous les fichiers .txt dans le dossier output/btt/
input_folder = "../nd_notoken"
output_folder = "../output/vncorenlp_output/nd/"
txt_files = [file for file in os.listdir(input_folder) if file.endswith(".txt")]

# Créer une barre de progression avec tqdm
progress_bar = tqdm(total=len(txt_files), desc="Annotating Files")

# Boucler sur chaque fichier .txt
for txt_file in txt_files:
    input_file_path = os.path.join(input_folder, txt_file)
    output_file_path = os.path.join(output_folder, txt_file)
    
    try:
        # Annoter le fichier d'entrée et enregistrer le résultat dans le dossier de sortie avec le même nom de fichier
        model.annotate_file(input_file=input_file_path, output_file=output_file_path)
    except Exception as e:
        print(f"Error processing file: {txt_file}")
        print(f"Exception: {e}")
        continue
    
    # Mettre à jour la barre de progression
    progress_bar.update(1)

# Fermer la barre de progression à la fin du traitement
progress_bar.close()
