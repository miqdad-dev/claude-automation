import argparse
import os

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

def main():
    parser = argparse.ArgumentParser(description='List files with specific extension in a directory.')
    parser.add_argument('-d', '--directory', help='Directory to be scanned')
    parser.add_argument('-e', '--extension', help='File extension to be listed')

    args = parser.parse_args()

    if args.directory and args.extension:
        files = list_files(args.directory, args.extension)
        for file in files:
            print(file)
    else:
        print('Both directory and extension are required.')

if __name__ == '__main__':
    main()