#Importing tkinter
from tkinter import *
from tkinter import messagebox

#Tkinter code 
window=Tk()
window.title('Login page')
window.geometry('700x700+300+200')
window.configure(bg="white")
window.resizable(False,False)

#Placing image in replit
img = PhotoImage(file="3188353.png") 

#adjusting image and background color
Label(window,image=img,bg='white').place(x=220,y=30)





#Looping tkinter code
window.mainloop()

