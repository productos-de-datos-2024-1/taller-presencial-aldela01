#This script is intended to create the datalake
#It must be executed from the src/1_datalake directory

# Importing required libraries
import os
import pkg_resources

# Defining the path to the datalake structure file
STRUCTURE_FILE ='datalake_structure.txt'

def get_datalake_dirs():
    '''Returns the datalake directories stored in the file datalake_structure.txt'''

    # Checking if the file exists
    if not pkg_resources.resource_exists(__name__, STRUCTURE_FILE):
        raise FileNotFoundError(f"File {STRUCTURE_FILE} not found")
    
    with pkg_resources.resource_stream(__name__, STRUCTURE_FILE) as f:
        # Reading the file
        dirs = f.readlines()
        dirs = [dir.strip() for dir in dirs]
    return dirs

def create_datalake(dirs):
    '''Creates the datalake in the main directory'''

    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)
            #print(f"Created directory {path}")

def main():
    '''Orchestrates the creation of the datalake'''

    # Getting the directories
    dirs = get_datalake_dirs()
    # Creating the datalake
    create_datalake(dirs)

if __name__ == '__main__':
    main()

