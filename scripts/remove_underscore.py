import os

def replace_underscores(input_directory, output_directory):
    # Vérifie si le chemin spécifié est un dossier existant
    if not os.path.isdir(input_directory):
        print("Le chemin spécifié n'est pas un dossier valide.")
        return
    
    # Crée le dossier de sortie s'il n'existe pas
    os.makedirs(output_directory, exist_ok=True)
    
    # Parcourt tous les fichiers dans le dossier spécifié
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Vérifie si le fichier est un fichier texte
            if file_path.endswith('.txt'):
                # Lit le contenu du fichier
                with open(file_path, 'r') as f:
                    content = f.read()
                # Remplace les underscores par des espaces dans le contenu
                modified_content = content.replace('_', ' ')
                # Chemin du fichier de sortie avec le même nom de fichier
                output_file_path = os.path.join(output_directory, file)
                # Écrit le contenu modifié dans le nouveau fichier
                with open(output_file_path, 'w') as f:
                    f.write(modified_content)
                print(f"Les underscores ont été remplacés par des espaces dans '{file_path}' et sauvegardés dans '{output_file_path}'.")

# Chemin du dossier d'entrée
input_directory_path = "../output/vnp/"
# Chemin du dossier de sortie
output_directory_path = "../output/vnp_notoken/"

# Remplace les underscores par des espaces dans les fichiers texte du dossier d'entrée
# et sauvegarde les fichiers modifiés dans le dossier de sortie
replace_underscores(input_directory_path, output_directory_path)
