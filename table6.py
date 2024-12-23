import numpy as np
from scipy.stats import f
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

alpha = 0.975
# degrés de liberté
ddl_v1 = [x for x in range(1, 11)] + [20, 50, 100, 500]
ddl_v2 = [x for x in range(1, 11)] + [20, 50, 100, 500]

# Calcul des valeurs
table = []
for v1 in ddl_v1:
    row = []
    for v2 in ddl_v2:
        value = f.ppf(alpha, v2, v1)
        row.append(value)
    table.append(row)

# Création du PDF
pdf = canvas.Canvas("table6.pdf", pagesize=letter)
width, height = letter

# Titre
pdf.setFont("Helvetica-Bold", 16)
pdf.drawCentredString(width / 2.0, height - 50, "Table de Fisher 6 (loi de Fisher)")

# Sous-titre
pdf.setFont("Helvetica", 12)
pdf.drawCentredString(width / 2.0, height - 70, f"α = {alpha}")

# Position de départ pour le tableau
start_x = 5
start_y = height - 100

# Largeurs des colonnes
col_width = 40

# Entête du tableau
pdf.setFont("Helvetica-Bold", 10)
pdf.drawString(start_x, start_y, "V1")
for i in range(len(ddl_v1)):
    pdf.drawString(start_x + col_width*(i+1), start_y, str(ddl_v1[i]))
start_y -= 20
pdf.drawString(start_x, start_y, "V2")

# Contenu du tableau
pdf.setFont("Helvetica", 10)
y = start_y - 20
for i in range(len(ddl_v2)):
    pdf.drawString(start_x, y, str(ddl_v2[i])) 
    for j in range(len(table[i])):
        pdf.drawString(start_x + col_width*(j+1), y, f"{table[i][j]:3.2f}")
    y -= 20
pdf.save()
