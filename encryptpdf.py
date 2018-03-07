import PyPDF2 as pyd
pdf1file=open('meetingminutes.pdf','rb') #Name of first pdf file
p1read=pyd.PdfFileReader(pdf1file)

pwrite= pyd.PdfFileWriter()

for pages in range(p1read.numPages):
	pageobj=p1read.getPage(pages)
	pwrite.addPage(pageobj)
print("Enter password for encryption")
k=input()
pwrite.encrypt(k)
pout =open('combined.pdf','wb') #Name of combined pdf file
pwrite.write(pout)
pout.close()
pdf1file.close()

