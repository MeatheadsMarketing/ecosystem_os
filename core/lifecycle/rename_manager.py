
import hashlib

def suggest_rename(filename, file_type):
    base, ext = filename.rsplit('.', 1) if '.' in filename else (filename, 'bin')
    tag = hashlib.sha1(filename.encode()).hexdigest()[:6]
    return f"{file_type}_{base}_{tag}.{ext}"
