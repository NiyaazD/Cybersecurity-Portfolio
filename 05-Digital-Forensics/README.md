# Digital Forensics Metadata Extractor

## Overview

The **Digital Forensics Metadata Extractor** is a Python-based command-line tool developed as part of my Cyber Security Bootcamp.

The purpose of the tool is to collect and display filesystem metadata associated with a specified file. This type of information can be useful during an initial digital forensic examination when an investigator needs to establish basic information about a file and its timestamps, location, size, and permissions.

The tool uses Python's built-in libraries to inspect filesystem attributes without modifying the target file.

---

## Objectives

The project was developed to demonstrate practical knowledge of:

- Filesystem metadata collection
- File properties and timestamps
- File permissions
- Python filesystem operations
- Basic digital forensic analysis
- Handling files supplied by a user
- Presenting forensic information in a readable format

---

## Features

The tool accepts a file path from the user and extracts the following information:

| Metadata | Description |
|---|---|
| File Name | Name of the target file |
| File Path | Absolute location of the file |
| File Extension | Extension associated with the file |
| File Size | Size of the file in bytes |
| Creation Time | Filesystem creation/change timestamp |
| Last Modified | Time the file was last modified |
| Last Accessed | Time the file was last accessed |
| Readable | Whether the current user can read the file |
| Writable | Whether the current user can modify the file |
| Executable | Whether the current user can execute the file |

If the specified file does not exist, the program returns an appropriate error message instead of attempting to process it.

---

## Technologies Used

- **Python 3**
- `os`
- `time`
- `pprint`

All libraries used by the application are part of Python's standard library, so no external packages are required.

---

## How the Tool Works

The application follows a simple forensic collection process:

```text
User provides file path
        ↓
Program checks whether file exists
        ↓
Filesystem statistics are collected
        ↓
Metadata is organised into a dictionary
        ↓
Metadata is displayed to the investigator
```

The program uses:

```python
os.stat(file_path)
```

to retrieve filesystem information associated with the target file.

It also uses:

```python
os.path
```

to determine information such as the filename, absolute path, and file extension.

---

## Usage

Navigate to the project directory and run:

```bash
python forensics.py
```

The program will prompt:

```text
Enter the path of the file:
```

Provide the path to the file you want to examine.

For example:

```text
08-015_Digital Forensics.pdf
```

---

## Example

Example input:

```text
Enter the path of the file: 08-015_Digital Forensics.pdf
```

Example output:

```text
Extracted Metadata
---------------------------------------------

{'File Extension': '.pdf',
 'File Name': '08-015_Digital Forensics.pdf',
 'File Path': '...',
 'File Size (bytes)': 358013,
 'Creation Time': '...',
 'Last Modified': '...',
 'Last Accessed': '...',
 'Readable': True,
 'Writable': True,
 'Executable': True}
```

The exact timestamps and file path will depend on the system where the program is executed.

---

## Digital Forensics Relevance

Filesystem metadata can provide useful information during a digital forensic investigation.

For example, timestamps can assist an investigator when constructing a preliminary timeline of file activity. File permissions can also provide information about whether a user or process may have had permission to access, modify, or execute a file.

However, filesystem timestamps should **not automatically be treated as definitive evidence of when an event occurred**. They can be affected by operating-system behaviour, file transfers, copying, metadata changes, and other factors.

This project therefore represents a **basic metadata collection tool**, rather than a complete forensic investigation platform.

---

## Error Handling

Before attempting to collect metadata, the program checks whether the specified file exists:

```python
if not os.path.exists(file_path):
    return {"Error": "File not found."}
```

This prevents the program from attempting to retrieve filesystem information from a nonexistent file.

---

## Skills Demonstrated

### Python

- Functions
- Dictionaries
- User input
- Conditional statements
- Standard library modules
- File and path handling

### Digital Forensics

- Filesystem metadata collection
- File timestamp analysis
- File permission analysis
- Basic forensic information gathering

### Security

- Understanding the value of filesystem metadata
- Establishing preliminary file information
- Understanding limitations of filesystem timestamps
- Collecting information without modifying the target file

---

## Project Structure

```text
05-Digital-Forensics/
│
├── forensics.py
└── README.md
```

---

## Limitations

This tool focuses on basic filesystem metadata and does not currently extract specialised metadata contained within files.

For example, it does not currently extract:

- EXIF information from images
- PDF document metadata
- Microsoft Office document properties
- File hashes
- Deleted-file information
- NTFS-specific forensic artefacts
- Browser artefacts
- Operating-system event logs

These would require additional forensic techniques and/or specialised libraries.

---

## Future Improvements

Potential enhancements include:

1. **File hashing**

   Add MD5, SHA-1, and SHA-256 hash generation to help verify file integrity.

2. **Directory analysis**

   Allow investigators to analyse multiple files within a directory.

3. **Recursive scanning**

   Search subdirectories automatically.

4. **Report generation**

   Export collected metadata to CSV or JSON for further analysis.

5. **Additional metadata**

   Add support for EXIF, PDF, and Office document metadata.

6. **Forensic timeline**

   Convert file timestamps into a structured timeline for investigation.

---

## Learning Outcomes

This project provided practical experience in applying Python to a digital forensics scenario.

It demonstrated how filesystem information can be programmatically collected and presented for analysis, while also highlighting the importance of understanding the limitations and reliability of metadata when conducting forensic investigations.

---

## Author

**Niyaaz Dawjee**

Cyber Security Bootcamp Portfolio