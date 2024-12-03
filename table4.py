import aspose.words as aw
from scipy.stats import *
α = [1,0.8,0.6,0.4,0.2,0.1,0.05,0.01,0.005,0.001]

cpt=1
cptx=0
with open("table4.txt", "w") as file: # Ouverture du fichier en mode écriture pour écrire les résultats

    # écriture de l'entête de la table
    file.write("                                      Table 4\n")
    file.write("                             Loi de Student\n\n\n\n")
    for i in range(0,70):
        file.write("_")
    # écriture des valeurs de z
    file.write("\n")
    file.write(" a|")
    file.write("  ")
    
    for elem in α:
        file.write(f"{elem} | ")



    file.write("\n")

    # écriture des lignes et colonnes de la table
    x=1
    while x <= 200:
        if x<10:
            file.write(f" {x}| ")
        else:
            file.write(str(x)+"| ")
        for a in α:
            if t.ppf(1-a, x) < -1000000000000000:
                file.write(f"0 | ")
            else :
                file.write(f"{t.ppf(1-a, x):.3f}|")
        cptx+=1
        if cptx==5:
            file.write("\n\n")
            cptx=0
        else:
            file.write("\n")
        if x==30 :
            cpt=10
        if x==100:
            cpt=100
        x+=cpt
        
file.close()

# Création d'un document pdf à partir du fichier texte ça ne marche pas d'ailleurs

txt = aw.Document("table4.txt")


txt.save("table4.pdf", aw.SaveFormat.PDF)