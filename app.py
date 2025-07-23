import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
import docx
import PyPDF2

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# ---------- Text Extraction Helpers ----------
def extract_text(file):
    file_type = file.name.split('.')[-1].lower()

    if file_type == 'txt':
        return file.read().decode('utf-8')

    elif file_type == 'pdf':
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif file_type == 'docx':
        doc = docx.Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])

    else:
        return "Unsupported file type"

# ---------- Cleaner ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return [w for w in words if w not in stop_words]

# ---------- Streamlit UI ----------
def main():
    st.title("Smart Resume Screener (Multi-File Format)")

    jd_file = st.file_uploader("Upload Job Description (any file)", type=None)
    resume_file = st.file_uploader("Upload Resume (any file)", type=None)

    if jd_file and resume_file:
        jd_text = extract_text(jd_file)
        resume_text = extract_text(resume_file)

        if jd_text == "Unsupported file type" or resume_text == "Unsupported file type":
            st.error("Please upload TXT, PDF, or DOCX files only.")
            return

        jd_words = clean_text(jd_text)
        resume_words = clean_text(resume_text)

        jd_word_set = set(jd_words)
        resume_word_set = set(resume_words)

        matched_keywords = jd_word_set.intersection(resume_word_set)
        missing_keywords = jd_word_set.difference(resume_word_set)
        match_score = (len(matched_keywords) / len(jd_word_set)) * 100 if jd_word_set else 0

        st.subheader(f"Resume Match Score: {match_score:.2f}%")
        st.success(f"Matched Keywords ({len(matched_keywords)}):")
        st.write(", ".join(sorted(matched_keywords)))
        st.warning(f"Missing Keywords ({len(missing_keywords)}):")
        st.write(", ".join(sorted(missing_keywords)))

if __name__ == "__main__":
    main()
