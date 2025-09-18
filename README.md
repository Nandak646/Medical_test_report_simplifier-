# Medical_test_report_simplifier-

💉 Medical Test Report Simplifier – Flow Sequence


🖼️ User Uploads Report
User uploads a medical/lab report image (PNG/JPG) via the front-end (app_image3.py).

📤 Backend Receives Image
Image is sent to the backend (backend1.py) for processing.

🔍 OCR (Text Extraction)
Backend uses EasyOCR to extract text from the uploaded report.

📝 Parse Extracted Text

Identify lab test names (e.g., WBC, Hemoglobin)

Extract test values (numerical results)


📊 Compare With Reference Ranges

Check each value:

✅ Normal

⚠️ Low

❌ High


✍️ Generate Summary

Create short sentences for each test, e.g., “Your WBC count is high.”

🗣️ Simplify for User

Convert medical jargon into easy-to-understand language.

📄 Display Final Report

Show the simplified report back to the user on the front-end.


🛠️ Requirements

Python ≥ 3.8 🐍

Libraries:

easyocr 🔍 – for text extraction

Pillow 🖼️ – for image handling

numpy ➕ – for numerical operations

pandas 📊 – for structured data manipulation

torch 🔥 – for underlying deep learning models in OCR

Optional: streamlit 💻 – for web interface


Hardware:

CPU or GPU (GPU recommended for faster OCR)

🚀 Optional Future Enhancements

🔔 Alerts for abnormal results

🗂️ Store history of reports

📤 Export report (PDF/CSV)

☁️ Cloud-based OCR for scalability
