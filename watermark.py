import PyPDF2
import sys

# define the arguments, the first (after program name)
# is the file to write on top of all other pages
watermark = sys.argv[1]
# list of pdfs to put watermark on
inputs = sys.argv[2:]


def merge_pdf(water, inputs):
    # reader object for watermark
    water_merge = PyPDF2.PdfFileReader(water).getPage(0)
    # writer object
    # iterating through all pdfs in the inputs list
    for pdf in inputs:
        writer = PyPDF2.PdfFileWriter()
        reader = PyPDF2.PdfFileReader(pdf)
        print(pdf)
        num_pages = reader.getNumPages()
        for i in range(0, num_pages):
            page = reader.getPage(i)
            # mergePage overlays the argument pdf page on top of the
            # "page"
            page.mergePage(water_merge)

            writer.addPage(page)
        # if you want separate pdf documents use this
        with open(f'New_{pdf}.pdf', 'wb') as new_file:
            writer.write(new_file)

    # to merge all pdf pages into one document use this -
    # with open('works.pdf', 'wb') as new_file:
    #     writer.write(new_file)

merge_pdf(watermark, inputs)
