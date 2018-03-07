import PyPDF2 as pyd
pdf1file=open('meetingminutes.pdf','rb') #Name of first pdf file
pdf2file=open('meetingminutes2.pdf','rb') #Name of second pdf file

p1read=pyd.PdfFileReader(pdf1file)
p2read=pyd.PdfFileReader(pdf2file)

pwrite= pyd.PdfFileWriter()

for pages in range(p1read.numPages):
	pageobj=p1read.getPage(pages)
	pwrite.addPage(pageobj)

for pages in range(p2read.numPages):
	pageobj=p2read.getPage(pages)
	pwrite.addPage(pageobj)

pout =open('combined.pdf','wb') #Name of combined pdf file
pwrite.write(pout)
pout.close()
pdf1file.close()
pdf2file.close()

