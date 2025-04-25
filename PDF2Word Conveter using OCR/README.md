# OCR PDF to Word Converter (Python Script)

This script converts scanned or image-based PDF files into editable Word (.docx) documents using OCR (Optical Character Recognition).

--------------------
What you need to do first
--------------------

1. Install Python (version 3.11 or later)
   Download from: https://www.python.org/downloads/
   Make sure to check the box that says "Add Python to PATH" during installation.

2. Install required Python libraries
   Open PowerShell and run:
   py -3.11 -m pip install pytesseract pdf2image python-docx

3. Install Tesseract OCR
   Download the Windows installer from:
   https://github.com/UB-Mannheim/tesseract/wiki
   Example install path: D:\Tesseract-OCR\tesseract.exe

4. Download Poppler for Windows
   Download from: https://github.com/oschwartz10612/poppler-windows/releases
   Extract it to a folder like:
   D:\Tools\poppler\poppler-24.08.0\Library\bin

You don’t need to add Poppler to PATH — the script will point to it directly.

--------------------
How to run the script
--------------------

1. Place your PDF files into this folder:
   C:\Users\Sajid.Sabreen\Downloads\ai\pdfs

2. Open PowerShell and run:
   py -3.11 main.py

3. The converted Word files will be saved to:
   C:\Users\Sajid.Sabreen\Downloads\ai\pdfs\converted_docs

Each page in the PDF will be scanned, the text extracted, and saved into a .docx file.

--------------------
If something breaks
--------------------

- If you get a “package not found” error, re-run the install command:
  py -3.11 -m pip install pytesseract pdf2image python-docx

- If it says “Poppler not found”, double-check that the Poppler folder path is correct in the script.

- If it says “Tesseract not found”, make sure the path to tesseract.exe is correct and not commented out.

This script doesn’t modify your files. It reads the PDFs, extracts text using OCR, and saves it to a new Word file.

--------------------
No coding knowledge needed. Just follow the steps and it should work.
