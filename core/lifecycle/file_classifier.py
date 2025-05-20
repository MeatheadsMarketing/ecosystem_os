
from gpt_file_classifier import gpt_classify_file
import os

def classify_file(filepath):
    try:
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read()
        filename = os.path.basename(filepath)
        return gpt_classify_file(filename, content)
    except:
        return "unknown"
