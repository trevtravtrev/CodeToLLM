import os

# Target directories
TARGET_DIRECTORY1 = r"C:\Users\trevo\OneDrive\Documents\GitHub\MarketingAI-frontend"
TARGET_DIRECTORY2 = r"C:\Users\trevo\OneDrive\Documents\GitHub\MarketingAI-backend"

OUTPUT_FILEPATH = r"C:\Users\trevo\OneDrive\Desktop"

# Output file names based on directory names
output_file1 = os.path.join(OUTPUT_FILEPATH, os.path.basename(TARGET_DIRECTORY1) + ".txt")
output_file2 = os.path.join(OUTPUT_FILEPATH, os.path.basename(TARGET_DIRECTORY2) + ".txt")

# List of files and directories to ignore
IGNORE_LIST = [
    '__pycache__',
    '.pyc',
    'node_modules',
    '.svelte-kit',
    'package-lock.json',
    '.venv'
]


def should_ignore(file_path):
    for pattern in IGNORE_LIST:
        if pattern in file_path:
            return True
    return False


def is_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read()
        return True
    except (UnicodeDecodeError, IOError):
        return False


def collect_code_files(directory, output_file):
    print(f"Collecting code files from directory: {directory}")
    print(f"Writing to output file: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            # Filter out directories to ignore
            dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]

            for file in files:
                file_path = os.path.join(root, file)
                if should_ignore(file_path):
                    print(f"Skipping ignored file: {file_path}")
                    continue

                print(f"Processing file: {file_path}")
                if is_text_file(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(f"Filename: {file_path}\n")
                            outfile.write(infile.read())
                            outfile.write("\n\n")
                    except Exception as e:
                        print(f"Skipping file {file_path} due to error: {e}")
                else:
                    print(f"Skipping non-text file: {file_path}")


if __name__ == '__main__':
    collect_code_files(TARGET_DIRECTORY1, output_file1)
    collect_code_files(TARGET_DIRECTORY2, output_file2)
