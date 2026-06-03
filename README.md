<img width="1920" height="1080" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/d0e88d8d-5d38-4e46-bc7c-627dbb9cd20b" />
# Invoice Data Extraction System

This project was built to automate the process of extracting invoice information from PDF files and converting it into a structured Excel report.

Instead of manually opening invoices and typing data into spreadsheets, the script reads PDF invoices, extracts important details, and generates a clean Excel summary automatically.

## What This Project Does

- Reads PDF invoices from a folder
- Extracts invoice details automatically
- Generates an Excel report
- Processes multiple invoices in one run
- Reduces manual data entry work

## Extracted Information

The script extracts:

- Invoice Number
- Order Number
- Invoice Date
- Due Date
- Customer Name
- Subtotal
- Tax Amount
- Total Amount

## Technologies Used

- Python
- PDFPlumber
- Pandas
- OpenPyXL
- Regular Expressions (Regex)

## Project Structure

```text
Invoice-Data-Extraction-System/

├── invoices/
├── output/
├── invoice_extractor.py
├── requirements.txt
└── README.md
```

## How To Run

Install required packages:

```bash
pip install -r requirements.txt
```

Place PDF invoices inside the `invoices` folder.

Run:

```bash
python invoice_extractor.py
```

The script will generate an Excel report automatically.

## Why I Built This

Many businesses receive invoice data in PDF format and spend time manually entering information into Excel.

I built this project to automate that workflow and demonstrate practical PDF processing and data extraction skills using Python.

## Sample Output

The generated Excel report contains structured invoice information that can be used for reporting, analysis, or record keeping.

## Screenshots

### Invoice PDF
[wordpress-pdf-invoice-plugin-sample.pdf](https://github.com/user-attachments/files/28553474/wordpress-pdf-invoice-plugin-sample.pdf)

### Script Execution

<img width="1920" height="1080" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/d8f6539a-f7fc-4d64-894a-c44cacebd603" />

### Excel Output
<img width="1920" height="1080" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/2ee89d9a-4b0c-4389-8668-1af8b0ef0d65" />

## About Me

I enjoy building automation solutions that reduce repetitive manual work and turn unstructured documents into useful business data.
