
import json
from datetime import datetime

def log_injection(original, renamed, file_type, confidence='1.0', model_used='gpt-sim', assisted_by='gpt_file_classifier'):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "original": original,
        "renamed": renamed,
        "type": file_type,
        "confidence": confidence,
        "model_used": model_used,
        "assisted_by": assisted_by
    }
    with open("injector_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
