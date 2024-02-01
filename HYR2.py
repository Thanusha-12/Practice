import os
import PyPDF2
import unittest
from PyPDF2 import PDFReader
class PDFReader(unittest.TestCase):

    def test_ReadPDFFile(self):
        file_path = os.path.join("C:\\Users\\Reddy\\Downloads", "file-sample_150kB.pdf")
        with open(file_path, 'rb') as file:
            pdf_reader = PdfFileReader(file)
            print("Number of Pages:", pdf_reader.numPages)
            doc_text = ""
            for page_num in range(1, 4):  # Assuming you want to read pages 1 to 3
                page = pdf_reader.getPage(page_num - 1)
                doc_text += page.extractText()
            print(doc_text)
            self.assertTrue("Maecenas" in doc_text)

if __name__ == '__main__':
    unittest.main()