# Scripting Automation

This script automates the process of downloading and extracting zip files from a given URL. It can be used in any situation where there's a need to automate file downloads and extraction. This script checks whether a file already exists, download it if not, and then extract its content.

## How it works

The script uses Python's `requests` and `zipfile` libraries to handle the downloading and extraction of the zip files. It checks whether a file already exists in the given directory and skips downloading if it does. It then extracts the file into the same directory.

## How to run

1. Clone the repository.
2. Navigate to the root folder.
3. Run `python automation.py`

## Example usage