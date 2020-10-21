import os
from tkinter import *
import socket
import calendar

try:
    import imdb
except ImportError:
    os.system("pip install IMDbPY")

def run():
    command = str(ci.get())
    if command == "exit":
        root.destroy()
    elif command == "info":
        lbl['text'] = """Hello, this is a cmd making of SKAN Industry.
    SKAN Copyright 2020-2021
    Version:1.1"""
    elif command == "help":
        lbl['text'] = """exit------close the app
    info------show some info about the app
    note------open a new note window
    help------show all the app commands
    my ip------show your ip address
    my hostname------show your hostname
    calendar------open a calendar
    clear------clean the cmd
    st page------go to start page
    light------light mode color
    dark------dark mode color"""  
    elif command == "note":
        lbl['text'] = "You open a new note window"
        note = Tk()
        note.title("Note")
        note.geometry("400x20")
        en = Entry(note, width=400)
        en.grid(row=0,column=0)
        en.config(bg="yellow")
        note.mainloop()
    elif command == "my ip":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        lbl['text'] = f"IP address: {ip_address}"
    elif command == "my hostname":
        myhostname = socket.gethostname()
        lbl['text'] = f"Hostname: {myhostname}"
    elif command == "calendar":
        def calendardef():
            year = int(year_entry.get())
            month = int(month_entry.get())
            my_calendar = calendar.month(year,month)
            lbl1['text'] = f"{my_calendar}"
        mycalendar = Tk()
        mycalendar.title("calendar")
        mycalendar.config(bg="lightgreen")
        year_entry = Entry(mycalendar)
        year_entry.grid(row=0,column=0)
        year_entry.config(bg="lightblue")
        month_entry = Entry(mycalendar)
        month_entry.grid(row=1,column=0)
        month_entry.config(bg="lightblue")
        btn1 = Button(mycalendar,text="FIND",command=calendardef)
        btn1.grid(row=1,column=1)
        btn1.config(bg="lightblue")
        lbl1 = Label(mycalendar, text="", height=10, width=30)
        lbl1.grid(row=3,column=0)
        lbl1.config(bg="lightgreen")
        mycalendar.mainloop()
    elif command == "clear":
        lbl['text'] = "Input a new command"
    elif command == "st page":
        lbl['text'] = f"""Welcome {myhostname2}!
    Type help to see all the commands
    Type info for more information
    SKAN copyright 2020-2021"""
    elif command == "skan":
        lbl['text'] = f"Hello, {myhostname2}!!!"
    elif command == "light":
        root.config(bg="white")
        ci.config(bg="white")
        btn.config(bg='white',fg='black')
        lbl.config(bg='white',fg='black')
    elif command == "dark":
        root.config(bg="black")
        ci.config(bg="white")
        btn.config(bg='black',fg='white')
        lbl.config(bg='black',fg='white')
    elif command == "":
        lbl['text'] = "Please,input a command first."
    else:
        lbl['text'] = "Sorry but i can't find this command."
    
def exit_():
    root.destroy() 

myhostname2 = socket.gethostname()

root = Tk()
root.geometry("520x350")
root.title("SKAN CMD")
root.config(bg='black')
root.maxsize(width=520, height=350)
root.minsize(width=520, height=350)
root.iconbitmap(r'C:\Users\agela\Downloads\code_xJ9_icon.ico')

mymenu = Menu(root)
m1 = Menu(mymenu, tearoff=0)
m1.add_command(label="exit", command=exit_)
mymenu.add_cascade(label="tools", menu=m1)
root.config(menu=mymenu)

ci = Entry(root, width=80)
ci.grid(row=9,column=0)
ci.config(bg='white')

btn = Button(root, text="RUN", command=run)
btn.grid(row=9,column=1)
btn.config(bg='black', fg='white')

lbl = Label(root, text=f"""Welcome {myhostname2}!
Type help to see all the commands
Type info for more information
SKAN copyright 2020-2021""", height=20, width=60)
lbl.grid(row=0,column=0)
lbl.config(bg='black', fg='white')

root.mainloop()