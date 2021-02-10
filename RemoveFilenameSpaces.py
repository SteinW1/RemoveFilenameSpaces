import datetime
import pathlib
from pathlib import Path

ignored_directories = ['AppData', 'Downloads', '.vscode']
fileExtensionsToCheck = ['.py', '.cpp', '.txt']

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

def checkFile(file_name):
    for character in file_name.name:
        if character.isspace():
            return True

class LogFile:
    def __init__(self, file):
        self.logFile = file
    
    def writelog(self, text, timestamp=True):
        log = open(self.logFile, 'at')
        log.write(f'[{datetime.datetime.now()}] {text}\n') if timestamp else log.write(f'{text} \n')
        log.close()

def main(current_directory, changelog, ignored_directories, fileExtensionsToCheck):
    if checkIfIgnored(current_directory):
        try:
            for file in current_directory.iterdir():
                if file.is_dir():
                    main(file, changelog, ignored_directories, fileExtensionsToCheck)
                else:
                    if getFileExtension(file.name) in fileExtensionsToCheck:
                        if checkFile(file):
                            changelog.writelog(f'\'{file.name}\' changed to \'{file.name}\' at {file}')
        except:
            pass

if __name__ == "__main__":
    changelog = LogFile('NameChangeLog.txt')
    main(Path.home(), changelog, ignored_directories, fileExtensionsToCheck)