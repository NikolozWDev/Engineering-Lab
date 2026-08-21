import os
import json
import csv
import pickle
from pathlib import Path

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def append_file(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(file_path, data, fieldnames=None):
    if not data:
        return
    
    if fieldnames is None:
        fieldnames = list(data[0].keys())
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_pickle(file_path, data):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def get_file_info(file_path):
    path = Path(file_path)
    if not path.exists():
        return None
    
    stat = path.stat()
    return {
        'name': path.name,
        'extension': path.suffix,
        'size': stat.st_size,
        'created': stat.st_ctime,
        'modified': stat.st_mtime,
        'is_file': path.is_file(),
        'is_dir': path.is_dir()
    }

def ensure_directory(directory_path):
    Path(directory_path).mkdir(parents=True, exist_ok=True)

def list_files(directory_path, extension=None):
    path = Path(directory_path)
    if not path.exists():
        return []
    
    if extension:
        return [str(f) for f in path.glob(f"*.{extension}")]
    return [str(f) for f in path.iterdir() if f.is_file()]

def copy_file(src, dst):
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    Path(src).copy2(dst)

def move_file(src, dst):
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    Path(src).rename(dst)

def delete_file(file_path):
    path = Path(file_path)
    if path.exists():
        path.unlink()
        return True
    return False

if __name__ == "__main__":
    test_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
    
    write_json("test.json", test_data)
    write_csv("test.csv", test_data)
    save_pickle("test.pkl", test_data)
