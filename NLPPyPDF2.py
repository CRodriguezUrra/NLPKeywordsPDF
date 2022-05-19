import PyPDF2

pdfFileObj = open('.pdf', "rb")     #Your pdf directory here

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)  #print(pdfReader.numPages) # will give total number of pages in pdf



for keyword in ['Example1', 'Example2'] :  #Your own keywords separated by commas and between "''"

  for pag in range(1,pdfReader.getNumPages()) :
    pageObj = pdfReader.getPage(pag)

    text=(pageObj.extractText())
    text2=text.split(",")
    #text

    encontrado = False
    for t in text2:
      if keyword in t :
          encontrado = True
    if (encontrado) :
      print (pag, keyword)
      
