from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from scipy.stats import chi2
import numpy as np

pdf = canvas.Canvas("table5.pdf", pagesize=letter)
width, height = letter
pdf.setFont("Helvetica-Bold", 12)
pdf.drawCentredString(width / 2.0, height - 50, "Table 5: Loi de Chi²")

alpha = np.array([0.999, 0.99, 0.95, 0.9, 0.5, 0.1, 0.05, 0.025, 0.01, 0.005, 0.001])
ddl = np.array(range(1, 31)).reshape(-1, 1)
# Position de départ pour le tableau
start_x = 5
start_y = height - 100
col_widths = 0
pdf.setFont("Helvetica-Bold", 10)
pdf.drawString(start_x, start_y, "alpha")
for i, level in enumerate(alpha):
    pdf.drawString(start_x + 50*(i+1), start_y, f"{level}")
start_y -= 20
pdf.drawString(start_x, start_y, "ddl")

# écriture des lignes et colonnes de la table
table = chi2.isf(alpha, ddl)
pdf.setFont("Helvetica", 10)
y = start_y - 20
cpt=0
for row in table:
    pdf.drawString(start_x, y, str(ddl[cpt]))  # Degrés de liberté
    cpt+=1
    for i, value in enumerate(row):
        pdf.drawString(start_x + 50*(i+1), y, f"{value:3.2f}")
    y -= 20
pdf.save()

"""
with open("table5.txt", "w") as file: # Ouverture du fichier en mode écriture pour écrire les résultats
    # écriture de l'entête de la table
    file.write("                                      Table 5\n")
    file.write("                                    Loi du chi2\n")
    file.write("1-a") # le caractère alpha est remplacé par a car celui ci créer une erreur
    file.write("     ")
    
    # écriture des valeurs de 1-a
    alpha = np.array([0.001, 0.01, 0.05, 0.1, 0.5, 0.9, 0.95, 0.095, 0.99, 0.0995, 0.999])
    for a in alpha:
        file.write(f"{a}  ") 
    file.write("\n\n")

    dll = np.array(range(1, 31)).reshape(-1, 1) 
    # écriture des lignes et colonnes de la table
    table = chi2.isf(alpha, dll)
    for i in range(0, len(dll)):
        file.write(f"{dll[i][0]:2}")
        file.write("  ")
        for j in range(1, len(alpha)+1):
            float=lambda x: "%5.2f" % x
            space = " " * (7 - len(float(table[i][-j])))
            file.write(f"{float(table[i][-j])}" + space)
        file.write("\n")
        
file.close()

# Création d'un document pdf à partir du fichier texte ça ne marche pas d'ailleurs

txt = aw.Document("table5.txt")


txt.save("table5.pdf", aw.SaveFormat.PDF)
"""