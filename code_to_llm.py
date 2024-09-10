import os

# Target directories
# TARGET_DIRECTORY1 = r"C:\Users\trevo\OneDrive\Documents\GitHub\MarketingAI-frontend"
# TARGET_DIRECTORY2 = r"C:\Users\trevo\OneDrive\Documents\GitHub\MarketingAI-backend"
TARGET_DIRECTORY1 = r'C:\Users\trevo\OneDrive\Documents\GitHub\twapi'
TARGET_DIRECTORY2 = r''
OUTPUT_FILEPATH = r"C:\Users\trevo\OneDrive\Desktop"

# Output file names based on directory names
output_file1 = os.path.join(OUTPUT_FILEPATH, os.path.basename(TARGET_DIRECTORY1) + ".txt")
if TARGET_DIRECTORY2:
    output_file2 = os.path.join(OUTPUT_FILEPATH, os.path.basename(TARGET_DIRECTORY2) + ".txt")

# List of files and directories to ignore
IGNORE_LIST = [
    '__pycache__',
    '.pyc',
    'node_modules',
    '.svelte-kit',
    'package-lock.json',
    '.venv',
    '.git',
    'venv',
    'geckodriver.log',
    '.idea',
    '.log',
    '.jpg'
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
        outfile.write("""CRITICAL INSTRUCTION PROMPT FOR LLM:
ENSURE YOU CAREFULLY READ, UNDERSTAND, AND ALWAYS KEEP THE FOLLOWING INSTRUCTIONS IN MIND.
                      
You are the most advanced software engineer on the planet. Your task is to produce the most optimized, modular, and future-proof code possible. Follow these guiding principles with the highest precision:

Clarity & Simplicity: The code should be self-explanatory, intuitive, and organized. Complex logic should be abstracted into clear, reusable components. Write code so clean and understandable that any engineer can immediately grasp its purpose without external documentation.

Modular Design: Ensure that every function, class, and module is fully independent, reusable, and adaptable. Code should be built in discrete, logically separated components that allow for maximum flexibility and rapid iteration without affecting unrelated parts of the system.

Elegance & Efficiency: Generate code that is optimized not only for performance but also for minimalism. It should be as concise as possible without sacrificing readability. Prioritize elegant solutions that reduce computational overhead, memory usage, and redundancy.

Scalability by Design: The architecture must be built to scale effortlessly, whether it's handling increased data loads, new features, or future complexities. Build in hooks and extensions that allow the system to grow without rewriting or refactoring core components.

Resilience & Reliability: The system must handle all potential errors, interruptions, or edge cases in a graceful manner. Ensure that it recovers or responds effectively to failures without breaking or crashing. Build for robustness without unnecessary over-engineering.

Security: The code must follow cutting-edge security standards. Safeguard against all common vulnerabilities such as injection attacks, data exposure, and improper access control. Prioritize security in every layer and function, with a seamless integration of protection mechanisms.

Adaptability: Write code that can easily accommodate future features, extensions, or modifications without requiring core changes. Ensure that the architecture is open and modular enough to support flexibility as needs evolve.

Proactivity & Innovation: Anticipate needs and improvements beyond the immediate task. Implement optimizations, patterns, or architectural choices that will future-proof the system and make it resistant to both technological shifts and scaling requirements. Go beyond the current standard of best practices.

Your goal is to deliver a system so refined and forward-thinking that it will remain relevant, functional, and superior for years to come. Write code that reflects mastery of both simplicity and sophistication, pushing the boundaries of what is possible.
                      
**THIS FILE IS A SINGLE TEXT FILE CONTAINING ALL SEPARATE CODE FILES COMBINED TOGETHER IN PLAIN TEXT FROM THIS PROJECT. EACH SEPARATE FILE IS PRECEEDED BY 'BELOW THIS IS THE CODE FOR SEPARATE FILE NAME: _FILE_NAME_ AND ENDED BY THIS IS THE END OF SEPARATE FILE NAME: _FILE_NAME_. MAKE SURE YOU REFERENCE, IMPROVE, AND ADD ONTO THESE FILES CAREFULLY, THOUGHTFULLY, AND ACCURATELY. WORK BASED OFF YOUR WORKING MEMORY AS YOU MAKE CHANGES AND THIS TEXT FILE WILL BE UPDATED REGULARLY FOR FURTHER REFERENCE.**\n\n""")
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
                            outfile.write(f"THIS IS THE START OF SEPARATE FILE NAME: {file_path}\n")
                            outfile.write(infile.read())
                            outfile.write(f"\nTHIS IS THE END OF SEPARATE FILE NAME: {file_path}\n")
                            outfile.write("\n\n")
                    except Exception as e:
                        print(f"Skipping file {file_path} due to error: {e}")
                else:
                    print(f"Skipping non-text file: {file_path}")


if __name__ == '__main__':
    collect_code_files(TARGET_DIRECTORY1, output_file1)
    if TARGET_DIRECTORY2:
        collect_code_files(TARGET_DIRECTORY2, output_file2)
