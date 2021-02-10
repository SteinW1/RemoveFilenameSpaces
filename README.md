# RemoveFilenameSpaces
A program for finding and replacing spaces in file names so they are easier to work with in the terminal.

This program works by iterating through all files in user's home directory.
Each file is checked to see if it is a proper file type to be renamed and then the file's name is checked for spaces.
When an eligible file is found the user is prompted for confirmation before the file is renamed.
The script also creates and appends to a log file that can be reviewed when issues arise from renaming files.
