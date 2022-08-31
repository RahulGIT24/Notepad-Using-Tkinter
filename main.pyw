
#! Author - Rahul
#! Date - 30-08-2022
#! Project - GUI Notepad

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

if __name__ == "__main__":
    root = Tk()
    root.geometry("700x400")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("icon.ico")

# * Adding Text Area
    textarea = Text(root, font="lucida 13")
    textarea.pack(fill=BOTH, expand=True)
    file = None

# * Creating a menu bar
menubar = Menu(root)


def newFile():
    global file
    root.title("Untitled Notepad")
    file = None
    textarea.delete(1.0, END)

# * Opening an external File


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, 'r')
        textarea.insert(1.0, f.read())
        f.close()

# * Saving a file


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
            ("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            #! Save as a new File
            f = open(file, 'w')
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        #! Save the File
        f = open(file, 'w')
        f.write(textarea.get(1.0, END))
        f.close()


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


def about():
    messagebox.showinfo("About Notepad", "This is simple notepad")


#! filemenu starts
filemenu = Menu(menubar, tearoff=0)

# * To open a new file
filemenu.add_command(label="New", command=newFile)

# * To open an already existing file
filemenu.add_command(label="Open", command=openFile)

# * To save the current file
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_separator()

# * Exit
filemenu.add_command(label='Exit', command=exit)
menubar.add_cascade(label='File', menu=filemenu)
#! file menu ends

#! Edit menu Starts
Edit = Menu(menubar, tearoff=0)

# * To give a feature of cut copy and paste
Edit.add_command(label='Cut', command=cut)
Edit.add_command(label='Copy', command=copy)
Edit.add_command(label='Paste', command=paste)

menubar.add_cascade(label="Edit", menu=Edit)
#! Edit menu ends

#! Help menu starts
helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="About Notepad", command=about)
menubar.add_cascade(label="Help", menu=helpMenu)

root.config(menu=menubar)

#! Adding Scrool bar
scrollbar = Scrollbar(textarea)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)

root.mainloop()
