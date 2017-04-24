import pyPdf
import os
import sys
import pyttsx

class pdf_text(object):

    def __init__(self,path):
        self.path=path

    def extract_text(self):

        content = ""

        pdf = pyPdf.PdfFileReader(file(self.path, 'rb')) # load the pdf to pypdf
        for i in range(0, pdf.getNumPages()):
            # Extract text from page and add to content
            content += pdf.getPage(i).extractText() + " \n"
        content = " ".join(content.replace(u"\xa0", " ").strip().split())
        return content

    def open_txt(self):
        #f = open('test4.txt', 'w')
        pdf = sys.argv[0]
        filedir, filename = os.path.split(pdf)
        nameonly = os.path.splitext(filename)
        newname = nameonly[0] + ".txt"
        outtxt = os.path.join(filedir, newname)
        f = open(outtxt, 'w')

        f.write(self.extract_text().encode("ascii", "ignore"))
        f.close()
        #f = open('test4.txt', 'w')


    def read_text(self):
        engine = pyttsx.init()
        engine.say(self.extract_text())
        engine.runAndWait()



obj = pdf_text('C:/Users/Amanuel/Desktop/new/prayer.pdf')
obj.read_text()
obj.open_txt()
