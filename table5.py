from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from scipy.stats import chi2
import numpy as np

pdf = canvas.Canvas("table5.pdf", pagesize=letter)
width, height = letter
pdf.setFont("Helvetica-Bold", 12)
pdf.drawCentredString(width / 2.0, height - 50, "Table 5: Loi de Chi²")

# Calcul des valeurs
alpha = np.array([0.999, 0.99, 0.95, 0.9, 0.5, 0.1, 0.05, 0.025, 0.01, 0.005, 0.001])
ddl = np.array(range(1, 31)).reshape(-1, 1)
table = chi2.isf(alpha, ddl)

# Position de départ pour le tableau
start_x = 5
start_y = height - 100

# Entête du tableau
pdf.setFont("Helvetica-Bold", 10)
pdf.drawString(start_x, start_y, "alpha")
for i in range(len(alpha)):
    pdf.drawString(start_x + 50*(i+1), start_y, f"{alpha[i]}")
start_y -= 20
pdf.drawString(start_x, start_y, "ddl")

# écriture des lignes et colonnes de la table
pdf.setFont("Helvetica", 10)
y = start_y - 20
cpt=0
for row in table:
    pdf.drawString(start_x, y, str(ddl[cpt]))  # Degrés de liberté
    cpt+=1
    for i in range(len(row)):
        pdf.drawString(start_x + 50*(i+1), y, f"{row[i]:3.2f}")
    y -= 20
pdf.save()