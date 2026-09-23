import os

def rename_files(target_dir, new_base_name):
    if not os.path.exists(target_dir):
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    try:
        file_list = os.listdir(target_dir)
        counter = 1

        for file_name in file_list:
            old_path = os.path.join(target_dir, file_name)

            # Skip if it is a directory
            if os.path.isdir(old_path):
                continue

            # Extract the original file extension (.txt, .png, etc.)
            _, file_extension = os.path.splitext(file_name)
            
            # Format the new filename (e.g., final_project_001.png)
            new_file_name = f"{new_base_name}_{counter:03d}{file_extension}"
            new_path = os.path.join(target_dir, new_file_name)

            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} -> {new_file_name}")
            counter += 1

        print("File renaming process completed!")
    except Exception as e:
        print(f"An error occurred while renaming files: {e}")

if __name__ == "__main__":
    # Change the target folder and the base name you want to apply
    TARGET_DIRECTORY = r"C:\MyProject\Images"
    BASE_NAME = "final_project"
    
    rename_files(TARGET_DIRECTORY, BASE_NAME)
