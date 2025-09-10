#!/usr/bin/env python3
"""
File Organizer - Organize files by extension into subdirectories
"""

import os
import shutil
import argparse
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime


class FileOrganizer:
    def __init__(self, base_directory, dry_run=False):
        self.base_directory = Path(base_directory)
        self.dry_run = dry_run
        self.history = []
        
        # File type mappings
        self.file_categories = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
            'videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp']
        }
    
    def get_category(self, file_extension):
        """Get category for file extension."""
        for category, extensions in self.file_categories.items():
            if file_extension.lower() in extensions:
                return category
        return 'others'
    
    def scan_directory(self):
        """Scan directory and categorize files."""
        files_by_category = defaultdict(list)
        
        for file_path in self.base_directory.iterdir():
            if file_path.is_file():
                category = self.get_category(file_path.suffix)
                files_by_category[category].append(file_path)
        
        return dict(files_by_category)
    
    def organize_files(self, files_by_category):
        """Organize files into subdirectories."""
        operations = []
        
        for category, files in files_by_category.items():
            if not files:
                continue
                
            # Create category directory
            category_dir = self.base_directory / category
            
            if not self.dry_run:
                category_dir.mkdir(exist_ok=True)
            
            print(f"\nProcessing {category} ({len(files)} files):")
            
            for file_path in files:
                destination = category_dir / file_path.name
                
                if self.dry_run:
                    print(f"  [DRY RUN] Would move: {file_path.name} -> {category}/")
                else:
                    try:
                        shutil.move(str(file_path), str(destination))
                        print(f"  Moved: {file_path.name} -> {category}/")
                        
                        operations.append({
                            'operation': 'move',
                            'source': str(file_path),
                            'destination': str(destination),
                            'timestamp': datetime.now().isoformat()
                        })
                    except Exception as e:
                        print(f"  Error moving {file_path.name}: {e}")
        
        if not self.dry_run:
            self.save_history(operations)
        
        return operations
    
    def save_history(self, operations):
        """Save operation history for undo functionality."""
        history_file = self.base_directory / '.organizer_history.json'
        
        try:
            if history_file.exists():
                with open(history_file, 'r') as f:
                    history = json.load(f)
            else:
                history = []
            
            history.extend(operations)
            
            with open(history_file, 'w') as f:
                json.dump(history, f, indent=2)
                
        except Exception as e:
            print(f"Warning: Could not save history: {e}")
    
    def undo_last_operation(self):
        """Undo the last organization operation."""
        history_file = self.base_directory / '.organizer_history.json'
        
        if not history_file.exists():
            print("No history found - nothing to undo.")
            return
        
        try:
            with open(history_file, 'r') as f:
                history = json.load(f)
            
            if not history:
                print("No operations to undo.")
                return
            
            # Get the last batch of operations (same timestamp)
            last_timestamp = history[-1]['timestamp']
            last_operations = [op for op in history if op['timestamp'] == last_timestamp]
            
            print(f"Undoing {len(last_operations)} operations...")
            
            for operation in reversed(last_operations):
                if operation['operation'] == 'move':
                    try:
                        shutil.move(operation['destination'], operation['source'])
                        print(f"  Restored: {Path(operation['destination']).name}")
                    except Exception as e:
                        print(f"  Error restoring {Path(operation['destination']).name}: {e}")
            
            # Remove undone operations from history
            remaining_history = [op for op in history if op['timestamp'] != last_timestamp]
            
            with open(history_file, 'w') as f:
                json.dump(remaining_history, f, indent=2)
                
        except Exception as e:
            print(f"Error during undo: {e}")
    
    def show_preview(self):
        """Show what would be organized."""
        files_by_category = self.scan_directory()
        
        print(f"\nScanning directory: {self.base_directory}")
        print(f"Found {sum(len(files) for files in files_by_category.values())} files")
        print("\nPreview of organization:")
        
        for category, files in files_by_category.items():
            if files:
                print(f"\n{category.upper()} ({len(files)} files):")
                for file_path in files[:5]:  # Show first 5 files
                    print(f"  - {file_path.name}")
                if len(files) > 5:
                    print(f"  ... and {len(files) - 5} more files")
        
        return files_by_category


def main():
    parser = argparse.ArgumentParser(description='Organize files by extension')
    parser.add_argument('--directory', '-d', default='.', help='Directory to organize')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without moving files')
    parser.add_argument('--undo', action='store_true', help='Undo last organization')
    parser.add_argument('--preview', action='store_true', help='Show preview of what would be organized')
    
    args = parser.parse_args()
    
    organizer = FileOrganizer(args.directory, dry_run=args.dry_run)
    
    if args.undo:
        organizer.undo_last_operation()
    elif args.preview:
        organizer.show_preview()
    else:
        files_by_category = organizer.show_preview()
        
        if not args.dry_run:
            confirm = input("\nProceed with organization? (y/N): ")
            if confirm.lower() != 'y':
                print("Organization cancelled.")
                return
        
        organizer.organize_files(files_by_category)
        
        if args.dry_run:
            print("\n[DRY RUN] No files were actually moved.")
        else:
            print("\nOrganization complete! Use --undo to reverse if needed.")


if __name__ == "__main__":
    main()
