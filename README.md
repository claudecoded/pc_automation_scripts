# Automation Scripts Repository

A collection of useful automation scripts written in **Python** and **Windows Batch** to streamline daily PC tasks. These tools handle system cleanup, automatic file backups, files automatic deletor and batch file renaming.

<img width="654" height="392" alt="ezgif-58f5f62280705fe9" src="https://github.com/user-attachments/assets/403c8dfa-06eb-4b33-93e2-f271301e82c5" />

## 🚀 Features

*   **Temporary Files Cleanup:** A lightweight Windows Batch script that removes hidden temporary files and prefetch clutter to free up disk space.
*   **Automatic Folder Backup:** A Python script that creates secure, timestamped backups of your project directories.
*   **Batch File Renamer:** A Python utility to systematically rename multi-file assets using clean, sequential numbering.

---

## 🛠️ Getting Started

### Prerequisites
*   **Windows OS** (required for the cleanup script).
*   **Python 3.x** installed on your system (required for backup and renaming scripts).

### Repository Structure
```text
├── clean_temp_files.bat   # Windows temporary files cleanup script
├── auto_backup.py        # Python automated backup tool
├── batch_renamer.py       # Python sequential file renamer
└── README.md              # Repository documentation
```

---

## 📖 Usage Guide

### 1. Temporary Files Cleanup
Run this script to wipe out Windows cache files (`Temp`, `%Temp%`, and `Prefetch`).
*   **File:** `clean_temp_files.bat`
*   **How to run:** Right-click the file and select **Run as Administrator** to ensure it has permissions to clean system directories.

### 2. Automatic Folder Backup
Creates a compressed-style copy of a specific folder inside a backup directory, appended with the precise date and time.
*   **File:** `auto_backup.py`
*   **Configuration:** Open the script and modify the configuration paths at the bottom:
    ```python
    SOURCE_PATH = r"C:\YourProject\Data"
    DESTINATION_PATH = r"D:\YourBackups"
    ```
*   **How to run:** 
    ```bash
    python auto_backup.py
    ```

### 3. Batch File Renamer
Quickly reorganizes messy file folders by converting names like `IMG_9482.png` into clean formats like `final_project_001.png`.
*   **File:** `batch_renamer.py`
*   **Configuration:** Adjust your target directory and desired prefix name before executing:
    ```python
    TARGET_DIRECTORY = r"C:\YourProject\Images"
    BASE_NAME = "your_custom_prefix"
    ```
*   **How to run:**
    ```bash
    python batch_renamer.py
    ```

---

## ⚙️ Automation Tip (Windows Task Scheduler)
You can set the backup or cleanup scripts to run automatically every day at a specific time:
1. Open **Task Scheduler** in Windows.
2. Click **Create Basic Task** and set your trigger (e.g., Daily).
3. Under **Action**, select *Start a program*.
4. Point it to your `.bat` file or a batch file executing your Python script.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
