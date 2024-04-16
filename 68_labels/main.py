from tkinter import *

window = Tk()
photo = PhotoImage(file='C:\\Workspace\\repositorios\\curso-python\\68_labels\\dog-poster.png')

label = Label(window,
              text="Hello World", 
              font=('Arial', 40, 'bold'), fg='#00FF00', 
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              image=photo,
              compound='bottom')
            
label.pack()
#label.place(x=100,y=100)

window.mainloop()