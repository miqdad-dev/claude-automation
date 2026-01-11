import main
import os
import zipfile

def test_download_file():
    url = "https://example.com/myfile.zip"
    filename = main.download_file(url)
    assert filename == "myfile.zip"

def test_extract_file():
    filename = "myfile.zip"
    main.extract_file(filename)
    assert os.path.exists("mytextfile.txt")

def test_count_lines():
    total_lines = main.count_lines()
    assert total_lines == 10