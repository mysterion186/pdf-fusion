
from PyPDF2 import PdfFileMerger
#from PyPDF2 import PdfFileReader
import os



list_files=os.listdir("fusion/")   #on obtient une liste de str contenant l'ensemble des fichier/dossier du répertoire (même des fichier non pdf)

nom_fichier =  input("Nom du pdf fusionné ")

#on crée une liste contenant QUE les noms des fichier pdf
"""
be sure that there is only pdf files in the directory
"""
pdfs = []

for file in list_files:
    i = 0
    
    if file[len(file)-4:len(file)] == ".pdf":
        pdfs.append(file)
        i+=1

pdfs.sort()
print(pdfs)
#fusion des pdf déterminés à l'issu de l'étape précédente

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append("fusion/"+pdf)

merger.write(nom_fichier+".pdf")
merger.close()
print("the pdf is ready")

