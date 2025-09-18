# backend.py

import easyocr
from PIL import Image
import numpy as np

# Initialize EasyOCR once
reader = easyocr.Reader(['en'])

# Reference ranges for example lab tests
REFERENCE_RANGES = {
    "WBC": (4000, 11000),           # /µL
    "RBC": (4.5, 5.9),              # million/µL
    "Hemoglobin": (13, 17),         # g/dL
}

# User-friendly explanations
EXPLANATIONS = {
    "WBC": "Your white blood cells are {} than normal. This often happens when your body is fighting an infection.",
    "RBC": "Your red blood cell count is {}. This affects oxygen transport in your body.",
    "Hemoglobin": "Your blood has {} oxygen-carrying protein, which can make you feel {}.",
}

def extract_text_from_image(uploaded_file):
    """
    Extract text from uploaded image using EasyOCR
    """
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    results = reader.readtext(img_array)
    text = " ".join([res[1] for res in results])
    return text

def parse_lab_values(text: str):
    """
    Parse lab values from OCR text.
    Expects format like 'WBC: 12500 /µL' or 'Hemoglobin: 10.5 g/dL'
    """
    lab_results = {}
    lines = text.splitlines()
    for line in lines:
        for test in REFERENCE_RANGES.keys():
            if test.lower() in line.lower():
                # Extract numeric values from the line
                numbers = [float(s.replace(',', '')) for s in line.split() if s.replace(',', '').replace('.', '').isdigit()]
                if numbers:
                    lab_results[test] = numbers[0]
    return lab_results

def interpret_lab_values(lab_results):
    """
    Compare lab results to reference ranges and classify as Low/Normal/High.
    Returns a dictionary with status and user-friendly explanation.
    """
    interpreted = {}
    for test, value in lab_results.items():
        low, high = REFERENCE_RANGES[test]
        if value < low:
            status = "Low"
            extra = "low"
            feeling = "tired"
        elif value > high:
            status = "High"
            extra = "higher"
            feeling = "weak or other symptoms"
        else:
            status = "Normal"
            extra = "in the healthy range"
            feeling = "fine"
        # Create readable explanation
        explanation = EXPLANATIONS[test].format(extra, feeling)
        interpreted[test] = {"status": status, "explanation": explanation}
    return interpreted

# Optional test if running backend.py directly
if __name__ == "__main__":
    sample_text = "WBC: 12500 /µL\nRBC: 5.0 million/µL\nHemoglobin: 10.5 g/dL"
    lab_vals = parse_lab_values(sample_text)
    interpreted = interpret_lab_values(lab_vals)
    for test, info in interpreted.items():
        print(f"{test}: {info['status']} → {info['explanation']}")
