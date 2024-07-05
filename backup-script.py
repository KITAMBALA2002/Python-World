#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

def backup_files(src_dir, backup_dir):
    # Get current date for unique backup folder name
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d")
    backup_subdir = os.path.join(backup_dir, f"backup_{timestamp}")

    try:
        # Create backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Create subdirectory for this backup
        os.makedirs(backup_subdir)

        # Copy files
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dest_path = os.path.join(backup_subdir, item)
            
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)
        
        print(f"Backup successful: {backup_subdir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source_directory = "/home/verde/Desktop/Computer-Health-Check/PROJECTS"
    backup_directory = "/home/verde/Desktop/BACKUP" 

    backup_files(source_directory, backup_directory)

    #0 0 * * * /path/to/python /path/to/your/backup_script.py


