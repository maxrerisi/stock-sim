import os

os.system("pip freeze > requirements.txt")
os.system("git add .")
os.system(f'git commit -m "{input("Commit Message > ")}"')
os.system("git push -u origin main")
