# 🧠 Smart Resume Screener

Smart Resume Screener is an intelligent Python-based application designed to automate the initial screening of resumes against a given job description. It extracts keywords from the job description and compares them with the content of uploaded resumes to generate a relevance score.

## 🚀 Features

- 🔍 **Resume Scanning**: Scans and processes `.pdf` and `.docx` resume formats.
- 📄 **Job Description Matching**: Matches resume content with the provided job description.
- 📊 **Score Calculation**: Calculates and displays a match score for each resume.
- 🖥️ **Simple CLI-based Interface** (can be extended to GUI or Web).
- 📁 **Supports Multiple File Types**.

## 📂 Project Structure
SmartResumeScreener/
├── app.py # Main runner script
├── screener.py # Core logic for parsing and scoring
├── resume.pdf # Sample resume
├── Job Description.txt # Sample job description
├── jd.txt # Parsed job description text
├── author # Optional metadata file
└── README.md # Project documentation


## 🛠️ Requirements

- Python 3.7+
- `python-docx`
- `lxml`
- `PyPDF2`

Install dependencies:
```bash
pip install -r requirements.txt

 How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/Sanjana-17-tech/SmartResumeScreener.git
cd SmartResumeScreener
Run the application:

bash
Copy code
python app.py
Follow the prompts to upload a resume and job description.

🧪 Sample Output
Copy code
Resume matched 78% with the job description.
Recommendation: Proceed to next interview round.


