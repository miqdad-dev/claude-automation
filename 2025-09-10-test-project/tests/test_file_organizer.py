#!/usr/bin/env python3
"""
Tests for File Organizer
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from file_organizer import FileOrganizer


class TestFileOrganizer(unittest.TestCase):
    
    def setUp(self):
        """Set up test directory with sample files."""
        self.test_dir = tempfile.mkdtemp()
        self.test_path = Path(self.test_dir)
        
        # Create sample files
        test_files = [
            'photo.jpg', 'document.pdf', 'video.mp4', 'song.mp3',
            'archive.zip', 'script.py', 'unknown.xyz'
        ]
        
        for filename in test_files:
            (self.test_path / filename).touch()
        
        self.organizer = FileOrganizer(self.test_path, dry_run=True)
    
    def tearDown(self):
        """Clean up test directory."""
        shutil.rmtree(self.test_dir)
    
    def test_get_category(self):
        """Test file categorization."""
        self.assertEqual(self.organizer.get_category('.jpg'), 'images')
        self.assertEqual(self.organizer.get_category('.pdf'), 'documents')
        self.assertEqual(self.organizer.get_category('.mp4'), 'videos')
        self.assertEqual(self.organizer.get_category('.mp3'), 'audio')
        self.assertEqual(self.organizer.get_category('.zip'), 'archives')
        self.assertEqual(self.organizer.get_category('.py'), 'code')
        self.assertEqual(self.organizer.get_category('.xyz'), 'others')
    
    def test_scan_directory(self):
        """Test directory scanning."""
        files_by_category = self.organizer.scan_directory()
        
        self.assertIn('images', files_by_category)
        self.assertIn('documents', files_by_category)
        self.assertIn('videos', files_by_category)
        self.assertIn('audio', files_by_category)
        self.assertIn('archives', files_by_category)
        self.assertIn('code', files_by_category)
        self.assertIn('others', files_by_category)
        
        # Check specific files are categorized correctly
        image_files = [f.name for f in files_by_category['images']]
        self.assertIn('photo.jpg', image_files)
    
    def test_dry_run(self):
        """Test dry run doesn't move files."""
        files_by_category = self.organizer.scan_directory()
        operations = self.organizer.organize_files(files_by_category)
        
        # In dry run, no operations should be recorded
        self.assertEqual(len(operations), 0)
        
        # Original files should still exist
        self.assertTrue((self.test_path / 'photo.jpg').exists())
        self.assertTrue((self.test_path / 'document.pdf').exists())
    
    def test_actual_organization(self):
        """Test actual file organization."""
        organizer = FileOrganizer(self.test_path, dry_run=False)
        files_by_category = organizer.scan_directory()
        operations = organizer.organize_files(files_by_category)
        
        # Check that directories were created
        self.assertTrue((self.test_path / 'images').exists())
        self.assertTrue((self.test_path / 'documents').exists())
        
        # Check that files were moved
        self.assertTrue((self.test_path / 'images' / 'photo.jpg').exists())
        self.assertTrue((self.test_path / 'documents' / 'document.pdf').exists())
        
        # Check that original files don't exist in root
        self.assertFalse((self.test_path / 'photo.jpg').exists())
        self.assertFalse((self.test_path / 'document.pdf').exists())
    
    def test_case_insensitive_extensions(self):
        """Test that file extensions are handled case-insensitively."""
        (self.test_path / 'IMAGE.JPG').touch()
        
        files_by_category = self.organizer.scan_directory()
        
        # Should categorize uppercase extension correctly
        image_files = [f.name for f in files_by_category['images']]
        self.assertIn('IMAGE.JPG', image_files)


if __name__ == '__main__':
    unittest.main()
