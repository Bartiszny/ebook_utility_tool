import os
import PyPDF2
import math
import ebooklib
from ebooklib import epub

# directory = 'C:\\Users\\Bartiszny\\Desktop'
directory = 'C:\\Users\\Bartiszny\\Downloads'

for filename in os.listdir(directory):
    path = directory + "\\" + os.path.join(filename)
    if filename.endswith(".epub"):
        book = epub.read_epub(path)
        num = 0
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                tmp = str(item.get_content())
                num += len(tmp.split())
        print(os.path.join(filename) + "\t\ttotal pages approximate number (for 257 words/page): "
              + str(math.ceil(num/257)))
    elif filename.endswith(".pdf"):
        num = PyPDF2.PdfFileReader(path).getNumPages()
        print(os.path.join(filename) + "\t\t\ttotal pages number: " + str(num))









