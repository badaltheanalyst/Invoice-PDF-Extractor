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

![Invoice](screenshots/input_invoice.png)

### Script Execution

![Execution](screenshots/script_execution.png)

### Excel Output

![Output](screenshots/excel_output.png)

## About Me

I enjoy building automation solutions that reduce repetitive manual work and turn unstructured documents into useful business data.
