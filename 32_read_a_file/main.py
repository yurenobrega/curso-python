path = "C:\\Workspace\\repositorios\\curso-python\\32_read_a_file\\test.txt"

try:
    with open(path) as file: print(file.read())
except FileNotFoundError:
    print("That file was not found")
