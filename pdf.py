from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

# genero un pdf con la imagen guardada que se ha generado con la visualizacion del codigo
def generate_pdf():
    ancho, alto = A4
    c=canvas.Canvas("pipeline.pdf", pagesize=A4)
    c.setFont('Times-Roman', 18)
    c.drawString(200, 750, "Terrorist Attacks in the USA")
    c.drawImage('Terrorist-Attacks-in-the-USA.png', 90, 200, width=450, height=450)
    text = c.beginText(50,680 )  # empieza el texto
    text.setFont("Times-Roman", 14)  # selecciona fuente
    text.textLine("Below are the images that show both the number of terrorist attacks in the USA and the")
    text.textLine("number of casualties.")
    c.drawText(text)
    c.showPage()
    c.save()