import os
import shutil
from datetime import datetime

def organize_files_by_extension(directory_path):
    if not os.path.exists(directory_path):
        return
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1] if '.' in filename else 'no_extension'
            folder_path = os.path.join(directory_path, ext)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, filename))

def cleanup_old_files(directory_path, days=30):
    if not os.path.exists(directory_path):
        return []
    
    deleted_files = []
    cutoff_time = datetime.now().timestamp() - (days * 86400)
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            file_mtime = os.path.getmtime(file_path)
            
            if file_mtime < cutoff_time:
                os.remove(file_path)
                deleted_files.append(filename)
    
    return deleted_files

def batch_rename(directory_path, prefix="", suffix=""):
    if not os.path.exists(directory_path):
        return
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{name}{suffix}{ext}"
            new_path = os.path.join(directory_path, new_name)
            os.rename(file_path, new_path)

if __name__ == "__main__":
    test_dir = "test_folder"
    os.makedirs(test_dir, exist_ok=True)
    
    for i in range(5):
        with open(os.path.join(test_dir, f"file_{i}.txt"), 'w') as f:
            f.write(f"Test content {i}")
        with open(os.path.join(test_dir, f"image_{i}.png"), 'w') as f:
            f.write(f"Image {i}")
    
    organize_files_by_extension(test_dir)
    batch_rename(test_dir, prefix="renamed_")
    cleanup_old_files(test_dir, days=30)
