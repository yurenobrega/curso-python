from tkinter import * 

window = Tk() 
window.geometry("420x420")
window.title("First GUI program")

icon = PhotoImage(file='C:\\Workspace\\repositorios\\curso-python\\67_GUI\\image.png')
window.iconphoto(True, icon)
window.config(background="#3794ad")

window.mainloop()