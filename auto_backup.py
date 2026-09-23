import os
import shutil
from datetime import datetime

def run_backup(source_dir, base_dest_dir):
    if not os.path.exists(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        return

    # Create the destination folder name using current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = f"backup_{timestamp}"
    final_destination = os.path.join(base_dest_dir, backup_folder_name)

    try:
        # Copy the entire directory tree
        shutil.copytree(source_dir, final_destination)
        print(f"Backup successfully created at: {final_destination}")
    except Exception as e:
        print(f"An error occurred during the backup process: {e}")

if __name__ == "__main__":
    # Change these paths to fit your system requirements
    SOURCE_PATH = r"C:\MyProject\Data"
    DESTINATION_PATH = r"D:\Backups"
    
    run_backup(SOURCE_PATH, DESTINATION_PATH)
