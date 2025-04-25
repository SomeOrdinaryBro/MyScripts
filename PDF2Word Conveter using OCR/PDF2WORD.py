# OCR PDF to Word (.docx) converter using Tesseract and Poppler

# This script converts scanned or image-based PDF files into editable Word documents.
# It uses OCR (optical character recognition) to extract text.

# ----------------------------
# Setup instructions (one time)
# ----------------------------

# Step 1 - install required Python packages (using Python 3.11):
# py -3.11 -m pip install pytesseract pdf2image python-docx

# Step 2 - install Tesseract OCR:
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Example path after install: D:\Tesseract-OCR\tesseract.exe

# Step 3 - download and unzip Poppler for Windows:
# Download from: https://github.com/oschwartz10612/poppler-windows/releases
# Example extracted path: D:\Tools\poppler\poppler-24.08.0\Library\bin

# ----------------------------
# Script starts here
# ----------------------------

import os
from pdf2image import convert_from_path
import pytesseract
from docx import Document

# Input and output folders - update these paths
pdf_folder = r""
output_folder = r""

# Path to Tesseract OCR executable
tesseract_path = r""

# Path to Poppler 'bin' folder (this is where pdftoppm.exe is)
poppler_path = r""

# Tell pytesseract where tesseract.exe is
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each PDF in the folder
for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        try:
            pdf_path = os.path.join(pdf_folder, filename)

            # Convert PDF pages to images (Poppler is used here)
            pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

            # Create a new Word document
            doc = Document()

            # Run OCR on each page and write to the Word doc
            for i, page in enumerate(pages):
                text = pytesseract.image_to_string(page)
                doc.add_paragraph(f"--- Page {i+1} ---\n{text}\n")

            # Save the output Word file
            docx_filename = filename.replace(".pdf", ".docx")
            doc.save(os.path.join(output_folder, docx_filename))

            print(f"Converted: {filename}")

        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

print("\nDone converting all PDFs.")
