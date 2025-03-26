from feature_extraction.pe_parser import extract_pe_features
from feature_extraction.pdf_parser import parse_pdfid_output
from feature_extraction.script_parser import extract_script_features
from feature_extraction.office_parser import extract_office_features
from ml_models.static_classifier import train_static_models
from dynamic_analysis.behavior_to_image import behavior_to_image

def detect_file_type(file_path):
    if file_path.endswith(('.exe', '.dll', '.sys')):
        return "exe"
    elif file_path.endswith('.pdf'):
        return "pdf"
    elif file_path.endswith(('.py', '.js', '.vbs')):
        return "script"
    elif file_path.endswith(('.docx', '.xlsx', '.pptx')):
        return "office"
    return "unknown"

def extract_features(file_path, file_type):
    if file_type == "exe":
        return extract_pe_features(file_path)
    elif file_type == "pdf":
        return parse_pdfid_output(file_path)
    elif file_type == "script":
        return extract_script_features(file_path)
    elif file_type == "office":
        return extract_office_features(file_path)
    return {}

# Example Usage
file_path = "sample.exe"
file_type = detect_file_type(file_path)
features = extract_features(file_path, file_type)
print(f"Features for {file_type}: {features}")
