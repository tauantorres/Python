# EXEMPLO 13

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

cnv = canvas.Canvas("meu_pdf.pdf")
cnv.drawString(250, 450, 'Testando')
cnv.save()
