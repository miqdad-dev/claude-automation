import urllib.request
import zipfile
import os

def download_file(url):
    filename = url.split("/")[-1]
    urllib.request.urlretrieve(url, filename)
    return filename

def extract_file(filename):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall()

def count_lines():
    total_lines = 0
    for filename in os.listdir():
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                for line in file:
                    total_lines += 1
    return total_lines

def main():
    url = input("Enter the URL of a zipped file: ")
    filename = download_file(url)
    extract_file(filename)
    total_lines = count_lines()
    print(f"Total number of lines in all .txt files: {total_lines}")

if __name__ == "__main__":
    main()