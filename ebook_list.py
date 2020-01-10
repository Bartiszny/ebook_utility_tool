import os
import PyPDF2
import ebooklib
from ebooklib import epub

def epub_counter(dircty):
    book = epub.read_epub('test.epub')
    content = book.get_content()
    with open(dircty) as infile:
        words = 0
        characters = 0
        for line in infile:
            wordslist=line.split()
            lines=lines+1
            words=words+len(wordslist)
            characters += sum(len(word) for word in wordslist)
    
    return charakters
   # print(lineno)
    #print(words)
    #print(characters)
    
# directory = 'C:\\Users\\bhoriszny\\Desktop'
directory = 'C:\\Users\\bhoriszny\\Downloads'

for filename in os.listdir(directory):
    path = directory + "\\" + os.path.join(filename)
    if filename.endswith(".epub"):# or filename.endswith(".pdf"): 
        print(os.path.join(filename) +" ")
    elif filename.endswith(".pdf"):
        
        num = PyPDF2.PdfFileReader(path).getNumPages()
        print(os.path.join(filename)+ " " + str(num))







