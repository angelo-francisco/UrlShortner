from tkinter import *
from api import shortener
import customtkinter as ctk
window = ctk.CTk()
window.title('urlShortener')
window.geometry('300x150')

def createUrl():
    global label3
    result = shortener(entry.get())
    label3 = ctk.CTkLabel(window, text='Result: '+result).pack()
    window.update()


label1 = ctk.CTkLabel(window, text='').pack()
label2 = ctk.CTkLabel(window, text='Write the url that you wanna turn to short').place(x=30, y=0)
entry = ctk.CTkEntry(window, width=200)
entry.pack()
ctk.CTkLabel(window, text='').pack()
btn = ctk.CTkButton(window, text='Enviar', command=createUrl).pack()



window.mainloop()