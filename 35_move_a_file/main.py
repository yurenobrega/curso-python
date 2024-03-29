import os

source = "C:\\Workspace\\repositorios\\curso-python\\35_move_a_file\\folder"
destination = "C:\\temp\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError as e:
    print(source + f" was not found: {e}" )