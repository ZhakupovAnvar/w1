from tkinter import *

window = Tk()
window.geometry('300x450')
window.title("Nuriman loh")
txt=Entry(window, width=30)
txt.grid(column=0, row=0)
def clicked():
    txt.configure(text="1")
btn=Button(window, text="1", command=clicked)
btn.grid(column=0, row=1 )
window.mainloop()