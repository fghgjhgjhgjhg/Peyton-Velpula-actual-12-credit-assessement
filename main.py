from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login page')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file="https://www.pngegg.com/en/png-ncacu")
Label(root,image=img,bg='yellow').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='red')
frame.place(x=480,y=70)


root.mainloop()
