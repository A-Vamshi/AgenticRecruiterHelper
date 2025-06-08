import os
import fitz

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def getResumeInfo(files, num_resumes=50):
    pdfInfos = []
    count = 0
    for file in files:
        if count < num_resumes:
            text = extract_text_from_pdf(file)
            pdfInfos.append({
                "id": count,
                "text": text
            })   
        else:
            break
        count += 1
    return pdfInfos