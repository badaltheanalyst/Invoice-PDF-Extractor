{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3ce36e51-dd22-44b8-ae36-763525d3d38a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pdfplumber in c:\\users\\rathr\\anaconda3\\lib\\site-packages (0.11.7)\n",
      "Requirement already satisfied: pdfminer.six==20250506 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfplumber) (20250506)\n",
      "Requirement already satisfied: Pillow>=9.1 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfplumber) (11.1.0)\n",
      "Requirement already satisfied: pypdfium2>=4.18.0 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfplumber) (4.30.0)\n",
      "Requirement already satisfied: charset-normalizer>=2.0.0 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfminer.six==20250506->pdfplumber) (3.3.2)\n",
      "Requirement already satisfied: cryptography>=36.0.0 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfminer.six==20250506->pdfplumber) (44.0.1)\n",
      "Requirement already satisfied: cffi>=1.12 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from cryptography>=36.0.0->pdfminer.six==20250506->pdfplumber) (1.17.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six==20250506->pdfplumber) (2.21)\n"
     ]
    }
   ],
   "source": [
    "!pip install pdfplumber"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "876320a8-f6db-49ff-83a3-1bb2b9df70a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pdfplumber in c:\\users\\rathr\\anaconda3\\lib\\site-packages (0.11.7)\n",
      "Requirement already satisfied: pandas in c:\\users\\rathr\\anaconda3\\lib\\site-packages (2.2.3)\n",
      "Requirement already satisfied: openpyxl in c:\\users\\rathr\\anaconda3\\lib\\site-packages (3.1.5)\n",
      "Requirement already satisfied: pdfminer.six==20250506 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfplumber) (20250506)\n",
      "Requirement already satisfied: Pillow>=9.1 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfplumber) (11.1.0)\n",
      "Requirement already satisfied: pypdfium2>=4.18.0 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfplumber) (4.30.0)\n",
      "Requirement already satisfied: charset-normalizer>=2.0.0 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfminer.six==20250506->pdfplumber) (3.3.2)\n",
      "Requirement already satisfied: cryptography>=36.0.0 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pdfminer.six==20250506->pdfplumber) (44.0.1)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pandas) (2.1.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: et-xmlfile in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from openpyxl) (1.1.0)\n",
      "Requirement already satisfied: cffi>=1.12 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from cryptography>=36.0.0->pdfminer.six==20250506->pdfplumber) (1.17.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six==20250506->pdfplumber) (2.21)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\rathr\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pdfplumber pandas openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7457ff15-6b05-461f-972a-3a20f4e32b80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DONE! SAVED 379 plot numbers to: E:\\PDF TO EXCEL\\Urban\\A&B Updeted New_Dhrangadhra Nagarpalika.xlsx\n",
      "DONE! SAVED 230 plot numbers to: E:\\PDF TO EXCEL\\Urban\\A&B Updeted New_Surendranagar UDA.xlsx\n",
      "DONE! SAVED 410 plot numbers to: E:\\PDF TO EXCEL\\Urban\\C&D New__Chotila Nagarpalika.xlsx\n",
      "DONE! SAVED 879 plot numbers to: E:\\PDF TO EXCEL\\Urban\\C&D New__Limbdi Nagarpalika.xlsx\n",
      "DONE! SAVED 581 plot numbers to: E:\\PDF TO EXCEL\\Urban\\C&D New__Thangadh Nagarpalika.xlsx\n",
      "DONE! SAVED 627 plot numbers to: E:\\PDF TO EXCEL\\Urban\\CD Updeted_Patdi.xlsx\n",
      "DONE! SAVED 153 plot numbers to: E:\\PDF TO EXCEL\\Urban\\TP_Schem A & B_Surendranagar TPS NO 01.xlsx\n",
      "DONE! SAVED 96 plot numbers to: E:\\PDF TO EXCEL\\Urban\\TP_Schem A & B_Surendranagar TPS NO 02.xlsx\n",
      "DONE! SAVED 223 plot numbers to: E:\\PDF TO EXCEL\\Urban\\TP_Schem A & B_Wadhwan TPS NO 01.xlsx\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import re\n",
    "import pdfplumber\n",
    "import pandas as pd\n",
    "\n",
    "# ==========================================\n",
    "\n",
    "# CONFIGURATION\n",
    "\n",
    "# ==========================================\n",
    "\n",
    "PDF_FOLDER = r\"E:\\PDF TO EXCEL\\Urban\"\n",
    "OUTPUT_FOLDER = r\"E:\\APR_excel_output_file\"\n",
    "\n",
    "os.makedirs(OUTPUT_FOLDER, exist_ok=True)\n",
    "\n",
    "# ==========================================\n",
    "\n",
    "# HELPER FUNCTIONS\n",
    "\n",
    "# ==========================================\n",
    "\n",
    "def clean_survey_number(token):\n",
    "\"\"\"\n",
    "Clean and standardize survey numbers.\n",
    "\n",
    "```\n",
    "Examples:\n",
    "    0012      -> 12\n",
    "    0012/003  -> 12/3\n",
    "    0         -> None\n",
    "\"\"\"\n",
    "\n",
    "if token == \"0\":\n",
    "    return None\n",
    "\n",
    "try:\n",
    "    if \"/\" in token:\n",
    "        first, second = token.split(\"/\")\n",
    "        return f\"{int(first)}/{int(second)}\"\n",
    "\n",
    "    return str(int(token))\n",
    "\n",
    "except ValueError:\n",
    "    return None\n",
    "```\n",
    "\n",
    "def extract_survey_numbers(pdf_path):\n",
    "\"\"\"\n",
    "Extract survey numbers from a PDF file.\n",
    "\"\"\"\n",
    "\n",
    "```\n",
    "try:\n",
    "    with pdfplumber.open(pdf_path) as pdf:\n",
    "        pages = [page.extract_text() or \"\" for page in pdf.pages]\n",
    "\n",
    "    full_text = \"\\n\".join(pages)\n",
    "\n",
    "    matches = re.findall(r\"\\b\\d+(?:/\\d+)?\\b\", full_text)\n",
    "\n",
    "    cleaned_numbers = []\n",
    "\n",
    "    for item in matches:\n",
    "        cleaned = clean_survey_number(item)\n",
    "\n",
    "        if cleaned:\n",
    "            cleaned_numbers.append(cleaned)\n",
    "\n",
    "    unique_numbers = sorted(\n",
    "        set(cleaned_numbers),\n",
    "        key=lambda x: (int(x.split(\"/\")[0]), x)\n",
    "    )\n",
    "\n",
    "    return unique_numbers\n",
    "\n",
    "except Exception as error:\n",
    "    print(f\"Error processing {pdf_path}\")\n",
    "    print(error)\n",
    "    return []\n",
    "```\n",
    "\n",
    "def save_to_excel(data, output_path):\n",
    "\"\"\"\n",
    "Save extracted survey numbers to Excel.\n",
    "\"\"\"\n",
    "\n",
    "```\n",
    "df = pd.DataFrame({\n",
    "    \"INDEX NO.\": range(1, len(data) + 1),\n",
    "    \"CITY SURVEY NO.\": data\n",
    "})\n",
    "\n",
    "df.to_excel(output_path, index=False)\n",
    "```\n",
    "\n",
    "# ==========================================\n",
    "\n",
    "# MAIN PROCESS\n",
    "\n",
    "# ==========================================\n",
    "\n",
    "def main():\n",
    "\n",
    "```\n",
    "pdf_files = [\n",
    "    file for file in os.listdir(PDF_FOLDER)\n",
    "    if file.lower().endswith(\".pdf\")\n",
    "]\n",
    "\n",
    "print(f\"\\nFound {len(pdf_files)} PDF files\\n\")\n",
    "\n",
    "for file in pdf_files:\n",
    "\n",
    "    pdf_path = os.path.join(PDF_FOLDER, file)\n",
    "\n",
    "    base_name = os.path.splitext(file)[0]\n",
    "\n",
    "    output_excel = os.path.join(\n",
    "        OUTPUT_FOLDER,\n",
    "        f\"{base_name}.xlsx\"\n",
    "    )\n",
    "\n",
    "    survey_numbers = extract_survey_numbers(pdf_path)\n",
    "\n",
    "    save_to_excel(\n",
    "        survey_numbers,\n",
    "        output_excel\n",
    "    )\n",
    "\n",
    "    print(\n",
    "        f\"SUCCESS | {file} | \"\n",
    "        f\"{len(survey_numbers)} records exported\"\n",
    "    )\n",
    "\n",
    "print(\"\\nProcessing Completed Successfully\")\n",
    "```\n",
    "if **name** == \"**main**\":\n",
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "71b9cbd9-30c0-4b81-9581-832791442ec6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\rathr\\anaconda3\\Lib\\site-packages\\pdfplumber\\__init__.py\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0cb90f19-4be5-413a-97da-a165f8bba3e2",
   "metadata": {},
   "outputs": [],
   "source": [
    " "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
