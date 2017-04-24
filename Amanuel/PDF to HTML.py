#pdf2txt.py
import sys
import pyPdf
import os
import pyttsx

def getPDFContent(path):
    content = ""
    path = 'C:/Users/Amanuel/Desktop/new/Let Us Pray.pdf'
# Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, 'rb'))
# Iterate pages
    for i in range(0, pdf.getNumPages()):
# Extract text from page and add to content
        content += pdf.getPage(i).extractText() + " \n"
# Collapse whitespace
# content = u" ".join(content.replace(u"\xa0", u" ").strip().split())

    engine = pyttsx.init()
    #engine.say(content)
    #engine.runAndWait()
    return content


pdf = sys.argv[0]
filedir,filename = os.path.split(pdf)
nameonly = os.path.splitext(filename)
newname = nameonly[0] + ".txt"
outtxt = os.path.join(filedir,newname)
f = open(outtxt,'w')
f.write(getPDFContent(pdf))
f.close()
print f




#exit()