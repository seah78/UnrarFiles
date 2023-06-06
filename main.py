# pip install rarfile

import rarfile

def decompress_rar(file_path, output_dir):
    with rarfile.RarFile(file_path) as rf:
        rf.extractall(output_dir)
        print("Décompression terminée.")

# Exemple d'utilisation
file_path = "chemin/vers/fichier.rar"
output_dir = "chemin/vers/repertoire_de_sortie"

decompress_rar(file_path, output_dir)
