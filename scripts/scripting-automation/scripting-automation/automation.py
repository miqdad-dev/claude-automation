import os
import requests
import zipfile
import io

def download_and_extract(url, directory):
    filename = url.split("/")[-1]

    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(os.path.join(directory, filename)):
        print(f"Downloading {filename}")
        response = requests.get(url)
        file = zipfile.ZipFile(io.BytesIO(response.content))
        file.extractall(directory)
    else:
        print(f"{filename} already exists")

def main():
    url = input("Enter the URL of the zip file: ")
    directory = input("Enter the directory to save the file: ")
    download_and_extract(url, directory)

if __name__ == "__main__":
    main()