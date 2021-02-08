import pathlib
from pathlib import Path

ignored_directories = ['AppData', 'Downloads', '.vscode']
fileExtensionsToCheck = ['.py', '.cpp']

def getFileExtension(file_name):
    return pathlib.Path(file_name).suffix

def replaceSpaces(file_name):
    new_name =''
    for character in file_name:
        new_name += '_' if i.isspace() else character
    return new_name

def checkIfIgnored(current_directory):
    for i in ignored_directories:
        if i == current_directory.name:
            return False
    return True

def iterateDirectories(current_directory, ignored_directories, fileExtensionsToCheck):
    if checkIfIgnored(current_directory):
        try:
            for file in current_directory.iterdir():
                if file.is_dir():
                    iterateDirectories(file, ignored_directories, fileExtensionsToCheck)
                else:
                    if getFileExtension(file.name) in fileExtensionsToCheck:
                        print(f'space found in name {file}') if checkFile(file) else None
        except:
            pass

def checkFile(file_name):
    for character in file_name.name:
        if character.isspace():
            return True

if __name__ == "__main__":
    iterateDirectories(Path.home(), ignored_directories, fileExtensionsToCheck)
    input("Press enter and exit")