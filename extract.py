import PyPDF2
object = open('The_Living_World.pdf','rb')
reader = PyPDF2.PdfFileReader(object)
n = int(reader.numPages)
s1 = []
f = open("sample.txt", "a")
for i in range(n):
	page = reader.getPage(i)
	s =page.extractText()
	#s1.append(s)
	print(s)
	f.write(s)
f.close()
