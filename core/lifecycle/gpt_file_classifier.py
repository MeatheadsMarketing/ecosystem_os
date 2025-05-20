
import hashlib

classification_cache = {}

def gpt_classify_file(filename, content):
    cache_key = hashlib.sha1((filename + content[:500]).encode()).hexdigest()
    if cache_key in classification_cache:
        return classification_cache[cache_key]

    if filename.endswith(".sh") and ("streamlit" in content or "exec" in content):
        result = "bootstrap_script"
    elif filename.endswith(".py") and ("streamlit" in content or "_viewer" in filename):
        result = "tab_ui"
    elif "setting" in content or filename.endswith(".json"):
        result = "config"
    else:
        result = "unknown"

    classification_cache[cache_key] = result
    return result
