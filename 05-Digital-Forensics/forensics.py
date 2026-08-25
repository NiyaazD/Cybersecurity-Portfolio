import os
import time
from pprint import pprint


def extract_metadata(file_path):
    """Extract metadata from a file."""

    if not os.path.exists(file_path):
        return {"Error": "File not found."}

    stats = os.stat(file_path)

    metadata = {
        "File Name": os.path.basename(file_path),
        "File Path": os.path.abspath(file_path),
        "File Extension": os.path.splitext(file_path)[1],
        "File Size (bytes)": stats.st_size,
        "Creation Time": time.ctime(stats.st_ctime),
        "Last Modified": time.ctime(stats.st_mtime),
        "Last Accessed": time.ctime(stats.st_atime),
        "Readable": os.access(file_path, os.R_OK),
        "Writable": os.access(file_path, os.W_OK),
        "Executable": os.access(file_path, os.X_OK)
    }

    return metadata


def main():
    print("=" * 45)
    print("      DIGITAL FORENSICS METADATA TOOL")
    print("=" * 45)

    file_path = input("Enter the path of the file: ")

    metadata = extract_metadata(file_path)

    print("\nExtracted Metadata")
    print("-" * 45)
    pprint(metadata)


if __name__ == "__main__":
    main()