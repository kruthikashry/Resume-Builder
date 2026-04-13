# Resume Builder with Python (Flask)

This is a Python Flask-based resume builder web application that allows users to:
- Enter personal, educational, and professional details
- Preview the resume in real-time
- Export the resume as a PDF (handled client-side via html2canvas + jsPDF)
- Save resume data to JSON format on the server

## Tech Stack

- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Backend:** Python (Flask)
- **PDF Export:** jsPDF (client-side)

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

Then open your browser to `http://127.0.0.1:5000/`