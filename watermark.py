import PyPDF2 as pyd
pdf1file=open('meetingminutes.pdf','rb') #Name of first pdf file
pdfwater=open('watermark.pdf','rb') #watermark pdf

p1read=pyd.PdfFileReader(pdf1file)
pwater=pyd.PdfFileReader(pdfwater)

pwrite= pyd.PdfFileWriter()

for pages in range(p1read.numPages):
	pageobj=p1read.getPage(pages)
	pageobj.mergePage(pwater.getPage(0))
	pwrite.addPage(pageobj)


pout =open('combined.pdf','wb') #Name of combined pdf file
pwrite.write(pout)
pout.close()
pdf1file.close()
pdfwater.close()