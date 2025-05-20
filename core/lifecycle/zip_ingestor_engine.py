
import zipfile
import os
from file_classifier import classify_file
from rename_manager import suggest_rename
from injector_logger import log_injection

def process_zip(zip_path):
    temp_extract_path = "temp_extracted_runtime"
    os.makedirs(temp_extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_extract_path)

    injected_files = []
    for root, dirs, files in os.walk(temp_extract_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_type = classify_file(full_path)
            new_name = suggest_rename(file, file_type)
            log_injection(file, new_name, file_type)
            injected_files.append({
                "original": file,
                "renamed": new_name,
                "type": file_type
            })
    return injected_files
