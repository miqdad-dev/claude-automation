# Test Project - Simple File Organizer

## What it does
A command-line tool that organizes files in a directory by their extensions into subdirectories.

## How it works
- Scans a target directory for files
- Groups files by extension
- Creates subdirectories for each extension
- Moves files to appropriate subdirectories

## How to run
```bash
python src/file_organizer.py --directory /path/to/organize
python src/file_organizer.py --directory . --dry-run  # Test mode
```

## Example usage
```bash
# Organize current directory
python src/file_organizer.py --directory .

# Organize with dry run to see what would happen
python src/file_organizer.py --directory ./downloads --dry-run
```

## Architecture & tradeoffs
- Simple CLI interface using argparse
- File operations with proper error handling
- Dry-run mode for safety
- Configurable file type mappings
- Preserves original timestamps and permissions

## Features
- Recursive directory scanning
- Configurable file type categories
- Undo functionality via history tracking
- Progress reporting for large directories
