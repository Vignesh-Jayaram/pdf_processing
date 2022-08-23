import PyPDF2

# Creating a tilted pdf file from dummy pdf:
with open ('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open ('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)