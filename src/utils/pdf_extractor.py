import os
import fitz
from dotenv import load_dotenv
load_dotenv()

cv_folder = os.getenv("RESUME_FOLDER_PATH")
cv_data = {}

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text

for cv_file in os.listdir(cv_folder):
    if cv_file.endswith(".pdf"):
        cv_path = os.path.join(cv_folder, cv_file)
        text = extract_text_from_pdf(cv_path)
        cv_data[cv_file] = text

print(len(list(cv_data.keys())))