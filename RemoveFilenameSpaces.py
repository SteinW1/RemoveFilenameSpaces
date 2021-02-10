import datetime
import pathlib
from pathlib import Path

ignored_directories = ['AppData', 'Downloads', '.vscode']
extensions_to_check = ['.py', '.cpp', '.txt']

class ChangeName():
    def __init__(self, logFile):
        self.logFile = logFile
    
    def replaceSpaces(self, file_name):
        new_name = ''
        for character in file_name.name:
            new_name += '_' if character.isspace() else character
        return new_name

    def commitNameChange(self, file_name, new_name):
        file_name.rename(f'{file_name.parent}/{new_name}')
        print(f'\'{file_name.name}\' renamed to \'{new_name}\' at {file_name.parent}')

    def promptUser(self, file_name, new_name):
        print(f'\nFile found at {file_name}')
        response = input(f'(Y/N) Would you like to change the name \'{file_name.name}\' to \'{new_name}\'?')
        return True if response.upper() == 'Y' else False

    def namechange(self, file_name):
        new_name = self.replaceSpaces(file_name)
        if self.promptUser(file_name, new_name):
            self.commitNameChange(file_name, new_name)
            if self.logFile != None:
                self.logFile.writelog(f'\'{file_name.name}\' changed to \'{new_name}\' at {file_name}')

class LogFile:
    def __init__(self, logfile):
        self.logFile = logfile
    
    def writelog(self, text, timestamp=True):
        log = open(self.logFile, 'at')
        log.write(f'[{datetime.datetime.now()}] {text}\n') if timestamp else log.write(f'{text} \n')
        log.close()

def getFileExtension(file_name):
    return pathlib.Path(file_name).suffix

def checkIfIgnored(current_directory):
    for i in ignored_directories:
        if i == current_directory.name:
            return False
    return True

def checkFile(file_name):
    for character in file_name.name:
        if character.isspace():
            return True

def main(current_directory, filenamechange, ignored_directories, extensions_to_check):
    if checkIfIgnored(current_directory):
        try:
            for _file in current_directory.iterdir():
                if _file.is_dir():
                    main(_file, filenamechange, ignored_directories, extensions_to_check)
                else:
                    if getFileExtension(_file.name) in extensions_to_check:
                        if checkFile(_file):
                            filenamechange.namechange(_file)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    print('Searching files...')
    changelog = LogFile('NameChangeLog.txt')
    filenamechange = ChangeName(changelog)
    main(Path.home(), filenamechange, ignored_directories, extensions_to_check)
    input('Couldn\'t find any more files. Press a key to exit.')