import os
import subprocess

def main():
    # Prompt the user for a commit message
    commit_message = input("Enter your commit message: ")

    # Define the commands to run
    commands = [
        "git add .",
        "git reset venv",  # Exclude the venv directory
        f'git commit -m "{commit_message}"',
        "git push"
    ]

    # Execute the commands
    for command in commands:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Command failed: {command}")
            break

if __name__ == "__main__":
    main()