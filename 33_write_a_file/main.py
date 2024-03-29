path = "C:\\Workspace\\repositorios\\curso-python\\33_write_a_file\\test.txt"

text = "Have a nice day! See ya"

with open(path, 'a') as file:
    file.write(text)