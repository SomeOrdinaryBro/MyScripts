# OCR PDF to Word Converter (Python Script)

This is a small script I put together to convert scanned/image-based PDFs into editable Word (.docx) files using OCR.  
Just follow the steps — no coding skills needed.

---

## First time setup (one-time things)

1. **Install Python (v3.11 or newer)**  
   Download it from: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
   *Important:* when installing, make sure to tick the box that says **"Add Python to PATH."**

2. **Install the required Python libraries**  
   Open PowerShell and run this:
   ```bash
   py -3.11 -m pip install pytesseract pdf2image python-docx
   ```

3. **Install Tesseract OCR**  
   Download it from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)  
   Example install path:  
   `D:\Tesseract-OCR\tesseract.exe`

4. **Download Poppler for Windows**  
   Grab it from: [https://github.com/oschwartz10612/poppler-windows/releases](https://github.com/oschwartz10612/poppler-windows/releases)  
   Extract it to somewhere like:  
   `D:\Tools\poppler\poppler-24.08.0\Library\bin`

> You don’t need to mess with adding Poppler to PATH — the script already points to it directly.

---

## How to use the script

1. **Put your PDF files here:**  
   `C:\Users\Sajid.Sabreen\Downloads\ai\pdfs`

2. **Run the script**  
   Open PowerShell and run:
   ```bash
   py -3.11 main.py
   ```

3. **Where you’ll find the converted Word docs:**  
   `C:\Users\Sajid.Sabreen\Downloads\ai\pdfs\converted_docs`

Each page will get OCR scanned and converted into a Word file.

---

## If something breaks

- **DO NOT CONTACT SAJID**

- **Package not found error?**  
  Just re-run:
  ```bash
  py -3.11 -m pip install pytesseract pdf2image python-docx
  ```

- **Poppler not found?**  
  Double-check the Poppler folder path inside the script. Make sure it's pointing correctly.

- **Tesseract not found?**  
  Make sure the `tesseract.exe` path is correct inside the script — and not commented out by mistake.

---

This script doesn’t touch your original PDFs. It just reads them, OCRs the text, and spits out a fresh Word document.
