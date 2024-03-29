import os
import shutil

path = 'C:\\Workspace\\repositorios\\curso-python\\36_delete_a_file\\folder'

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")