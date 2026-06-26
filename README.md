# File-organizer-automation


# 📂 Automatic File Organizer

A Python automation script that organizes files into folders based on their file extensions.

## Features
- Automatically creates folders by file type.
- Moves files into their respective folders.
- Uses Python's `os` and `shutil` modules.

## Technologies
- Python 3
- os
- shutil

## How to Run
1. Update the `pathfolder` variable with your folder path.
2. Run:

```bash
python temp.py
python fileorg.py
```

## Example
Before:
```
Downloads/
├── file.pdf
├── image.jpg
├── notes.txt
```

After:
```
Downloads/
├── pdf/
├── jpg/
└── txt/
```
