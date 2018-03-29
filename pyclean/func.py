import os

def find_files(directory):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            filename = os.path.join(root, basename)
            yield filename

def find_dir(directory):
    for root, dirs, files in os.walk(directory):
        for basename in dirs:
            dirname = os.path.join(root, basename)
            yield dirname

def cleanup(args):
    cwd = os.getcwd()
    print(cwd)
    for dir in find_dir(cwd):
        if dir.find('__pycache__')>0:
            print(dir)
