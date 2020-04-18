# @talg
# req: Python 3.7

import os
import PyPDF2
from tkinter import *
from tkinter import filedialog

def run_program():

    #Ask user for the name to save the file as
    userfilename="combined_pdf"

    #Get all the PDF filenames
    pdf2merge = []

    while True:

        temp_path = get_files()
        
        if len(temp_path) == 0:
            break
        pdf2merge.append(temp_path)
    
    #Sets the scripts working directory to the location of the PDF #1
    os.chdir(os.path.dirname(pdf2merge[0]))

    pdfWriter = PyPDF2.PdfFileWriter()

    #loop through all PDFs
    for filename in pdf2merge:
        
        pdfFileObj = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    #save PDF to file, wb for write binary
    pdfOutput = open(userfilename + '.pdf', 'wb')
    #Outputting the PDF
    pdfWriter.write(pdfOutput)
    #Closing the PDF writer
    pdfOutput.close()


def get_files():

    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("pdf files","*.pdf")])
    root.destroy()
    return root.filename


if __name__ == "__main__":
    run_program()