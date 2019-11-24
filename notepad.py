from tkinter import Menu
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import os

#  initialize tkinter
pad = tk.Tk()
note = ScrolledText(pad)
note.place(relwidth=1, relheight=1)
#  window title
pad.title("Python Notepad")


#  menu bar
menu = Menu(pad)
pad.config(menu=menu)
#  sub menus
fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
infoMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Info", menu=infoMenu)


def new():
    note.delete(1.0, "end")


def open_file():
    file = filedialog.askopenfile()
    file_content = file.read()
    note.delete(1.0, "end")
    note.insert(1.0, file_content)
    pad.title("Python Notepad" + "\\" + os.path.abspath(os.path.basename(str(file).replace("mode='r' encoding='cp1252'>", ""))))


def save_as():
    save_content = note.get("1.0", tk.END)
    file_type = [("All files", "*.*"),
                 ("Python files", "*.py"),
                 ("Text Document", "*.txt")
                 ]
    save = filedialog.asksaveasfile(filetypes=file_type, defaultextension=file_type)
    save.write(save_content)


#  commands under "File" menu
fileMenu.add_command(label="New", command=new)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save as", command=save_as)
fileMenu.add_command(label="Exit", command=exit)


def project_info():
    tk.messagebox.showinfo("About the project", "Python Notepad was written using Python 3.6 and Tkinter library.")


def author_info():
    tk.messagebox.showinfo("About the author", "Python Notepad was written by Allexus M. Constantino."
                                               "A college student pursuing Bachleor of Science in Entertainment and Multimedia Computing")


#  commands under "Info" menu
infoMenu.add_cascade(label="About the project", command=project_info)
infoMenu.add_cascade(label="About the author", command=author_info)

#  loop the notepad
pad.mainloop()
