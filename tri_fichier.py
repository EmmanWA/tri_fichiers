import os
import glob
import shutil
from pprint import pprint


"""
mp3, wav : Musique
mp4, mov : Videos
jpg, jpeg, png : Images
pdf : Documents
"""

chemin_glo = "C:/Users/Emmanuel/projet_python/tri_fichiers_sources/**"
chemin = "C:/Users/Emmanuel/projet_python/tri_fichiers_sources"

liste_dos = ["Musique", "Videos", "Images", "Documents"]


files = glob.glob(chemin_glo, recursive=True)
pprint(files)


#creation dossier
for i in liste_dos:
    dos_crea = os.path.join(chemin, i)
    os.makedirs(dos_crea, exist_ok= True)



for i in files:
    if i.endswith(".mp3") or i.endswith(".wav"):
        shutil.move(i, "C:/Users/Emmanuel/projet_python/tri_fichiers_sources/Musique")
    elif i.endswith(".mp4") or i.endswith(".mov"):
        shutil.move(i, "C:/Users/Emmanuel/projet_python/tri_fichiers_sources/Videos")
    elif i.endswith(".pdf"):
        shutil.move(i , "C:/Users/Emmanuel/projet_python/tri_fichiers_sources/Documents")
    elif i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
        shutil.move(i, "C:/Users/Emmanuel/projet_python/tri_fichiers_sources/Images")
        