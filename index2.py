import fitz

pdffile = "./pdf/BANBIF.pdf"
doc = fitz.open(pdffile)
page = doc.load_page(0)  # number of page
pix = page.get_pixmap()
output = "./png/BCP.png"
pix.save(output)