# Justification for Library Use (Aligned with ISO 9001 and Secure Software Practices)

This script uses a limited and controlled set of Python libraries, each selected with data security, traceability, and audit compliance in mind. Below is a detailed justification for each module in relation to your organization's secure development practices and adherence to ISO 9001:2015 principles.

---

### 1. `import os`

**Purpose:**  
Enables basic file and directory handling within the local filesystem — e.g., navigating folders, checking file paths, creating output folders.

**Security Consideration:**  
- Part of Python's **standard library**, maintained by the Python Software Foundation.
- No external network calls, telemetry, or data exposure.
- Fully local and sandboxed; interacts only with file paths the user explicitly defines.

**ISO 9001 Relevance:**  
Supports maintainable and traceable process control by enabling clear input/output management.

---

### 2. `from pdf2image import convert_from_path`

**Purpose:**  
Used to convert each page in a PDF to an image (e.g., PNG or JPEG), which is a necessary step before OCR can be performed on scanned or image-based documents.

**Security Consideration:**  
- `pdf2image` is an open-source Python wrapper for **Poppler**, a widely-used and transparent PDF rendering tool maintained by the open-source community.
- Does not transmit data over any network. All processing occurs locally.
- No telemetry, logging, or callbacks.

**ISO 9001 Relevance:**  
Facilitates reproducible and deterministic behavior for document processing, which is key to quality assurance and documentation integrity.

---

### 3. `import pytesseract`

**Purpose:**  
Acts as a Python wrapper for the locally installed **Tesseract OCR** engine to extract text from image-based PDFs.

**Security Consideration:**  
- Tesseract is a mature open-source OCR engine developed by Google and the open-source community.
- `pytesseract` merely interfaces with the **local installation** of `tesseract.exe`. No online activity or external communication.
- Explicit paths can be defined in the script to avoid accidental environmental leakage or uncontrolled access.

**ISO 9001 Relevance:**  
Promotes repeatable, verifiable data extraction procedures, suitable for compliance-driven document handling.

---

### 4. `from docx import Document` (i.e., `python-docx`)

**Purpose:**  
Creates and writes to Microsoft Word `.docx` files programmatically.

**Security Consideration:**  
- `python-docx` is a pure Python library that reads and writes `.docx` files using the Office Open XML standard.
- All operations are local and file-based. No internet connectivity or cloud syncing.
- Produces files in an auditable, human-readable format.

**ISO 9001 Relevance:**  
Supports quality documentation creation, version control, and traceability — key elements of any certified document workflow.

---

## General Security & Compliance Notes

- **No external APIs** are called.
- **No cloud-based dependencies** or telemetry.
- All paths (Tesseract, Poppler, Input/Output folders) are explicitly set and auditable.
- Works in **offline environments**, making it ideal for air-gapped or compliance-bound systems.

---

## Summary

All libraries used are:

- Open-source and widely vetted by developer and academic communities.
- Local-only: No data leaves the system.
- Traceable: Script behavior and outputs are consistent, deterministic, and auditable.
- Maintained: All libraries have active communities and regular updates.
- Aligned with ISO 9001 principles of process control, traceability, and risk management.
