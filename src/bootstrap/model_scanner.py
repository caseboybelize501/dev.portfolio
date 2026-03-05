import os
import hashlib
from pathlib import Path

def scan_models(paths) -> list:
    """
    Walk paths and calculate SHA256 for all model files
    """
    models = []
    
    for path in paths:
        if not os.path.exists(path):
            continue
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(('.pt', '.bin', '.model', '.weights')):
                    file_path = os.path.join(root, file)
                    try:
                        sha256_hash = calculate_sha256(file_path)
                        models.append({
                            "path": file_path,
                            "sha256": sha256_hash,
                            "size": os.path.getsize(file_path)
                        })
                    except Exception as e:
                        print(f"Error scanning {file_path}: {e}")
    
    return models

def calculate_sha256(file_path) -> str:
    """
    Calculate SHA256 hash of a file
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()