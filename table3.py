import aspose.words as aw
from scipy.stats import norm

cpty=0
cptx=0
with open("table3.txt", "w") as file: # Ouverture du fichier en mode écriture pour écrire les résultats

    # écriture de l'entête de la table
    file.write("                                      Table 3\n")
    file.write("                             Loi Normale Centree Reduite\n")
    file.write("                          Fonction de repartition F(z)=P(Z<z)\n\n\n\n")
    file.write("Z")
    file.write("     ")
    
    # écriture des valeurs de z
    for i in range(0,10):
        file.write(f"0.0{i}  ")
        if i==4:
            file.write(" ")

    file.write("\n\n")

    # écriture des lignes et colonnes de la table
    for x in range(0, 35):
        file.write(f"{x/10}  ")
        for y in range(0, 10):
            file.write(f"{norm.cdf(x/10 + y/100):.3f} ")
            cpty+=1
            if cpty==5:
                file.write("  ")
                cpty=0
        cptx+=1
        if cptx==5:
            file.write("\n\n")
            cptx=0
        else:
            file.write("\n")
        
file.close()

# Création d'un document pdf à partir du fichier texte ça ne marche pas d'ailleurs

txt = aw.Document("table3.txt")


txt.save("table3.pdf", aw.SaveFormat.PDF)