import PyPDF2
import sys


#  pdf merger without watermark:
# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')

# pdf_combiner(inputs)

# pdf merger with watermarks:

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
water_mark= PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.merge_page(water_mark.getPage(0))
    output.addPage(page)

with open('super_watermarked.pdf', 'wb') as file:
    output.write(file)

