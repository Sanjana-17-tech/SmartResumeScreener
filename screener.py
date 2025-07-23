import PyPDF2
import re
import nltk
nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def extract_keywords(text):
    words = nltk.word_tokenize(text.lower())
    words = [re.sub(r'\W+', '', word) for word in words if word.isalpha()]
    return set(words)

def match_score(resume_keywords, jd_keywords):
    matched = resume_keywords.intersection(jd_keywords)
    score = (len(matched) / len(jd_keywords)) * 100
    return score, matched

# === Load Files ===
resume_text = extract_text_from_pdf('resume.pdf')
with open('jd.txt', 'r', encoding='utf-8') as file:
    jd_text = file.read()

# === Extract Keywords ===
resume_keywords = extract_keywords(resume_text)
jd_keywords = extract_keywords(jd_text)

# === Match Score ===
score, matched_keywords = match_score(resume_keywords, jd_keywords)

print(f"\nResume Match Score: {score:.2f}%")
print("Matched Keywords:", ", ".join(matched_keywords))
