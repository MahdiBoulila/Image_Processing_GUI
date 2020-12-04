### Image Processing GUI
#
# Made by: Sarah Foley and Mahdi Boulila
#
# Python Code for GUI

# Importing Packages
import tkinter as tk
from tkinter import ttk
from script import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
import time

def Upload_Global():
    """ Uploads a global image to be treated, saves the path of the image in a json file.
    """
    path = filedialog.askopenfilename()
    # For debugging purposes, this will print out the file directory
    # in the terminal
    print('Selected Global Image:', path)
    image = Image.open(path)
    img = ImageTk.PhotoImage(image)
    panel.configure(image=img)
    panel.image = img
    with open('path1.json', 'w') as fp:
        fp.write(path)

def Upload_Cropped():
    """ Uploads a cropped image to be treated, saves the path of the image in a json file
    """
    path = filedialog.askopenfilename()
    # For debugging purposes, this will print out the file directory
    # in the terminal
    print()
    print('Selected Cropped Image:', path)
    with open('path2.json', 'w') as fp:
        fp.write(path)

def Execute():
    """ Reads two json files and execute the algorithm
    """
    with open('path1.json', 'r') as fp1, open("path2.json") as fp2 :
        path1 = fp1.readline()
        path2 = fp2.readline()
        finder(path1,path2)
        path = 'result.png'
        image = Image.open(path)
        img = ImageTk.PhotoImage(image)
        panel.configure(image=img)
        panel.image = img

def Help():
    """ pops the help window
    """
    tk.messagebox.showinfo(title='Help Message', message='First, check first if the dimensions of the Global Image is bigger than the Cropped Image. Second, Upload the Global Image first, then the Cropped Image. Then press Execute. The order of the steps is very important.')

window = tk.Tk()
window.title("Image Processing GUI")
window.geometry("650x500+10+10")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)


# Creating frames
fr_buttons = tk.Frame(window)
img_button = tk.Frame(window)

# Creating the buttons
btn_open = tk.Button(fr_buttons, text="Open Global Img...", width = 12, command = Upload_Global)
btn_open2 = tk.Button(fr_buttons, text="Open Searched Img..." , command = Upload_Cropped)
btn_run = tk.Button(fr_buttons, text="Execute", command = Execute)
btn_help = tk.Button(fr_buttons, text="Help", command = Help)

# Creating Labels
lbl_help = tk.Label(fr_buttons,text= 'If stuck, press Help button')

# Layout of the buttons
btn_open.grid(row=0, column=0, sticky="news", padx=(30,10), pady = 5)
btn_open2.grid(row=1, column=0, sticky="news", padx=(30,10))
btn_run.grid(row=2, column=0, sticky="news", padx=(30,10), pady = 5)
btn_help.grid(row=3, column=0, sticky="news", padx=(30,10))
lbl_help.grid(row=4,column=0, sticky='s' , padx=(30,10))

# Layout of the labels

# Display Default Image
path = "sample.png"
image = Image.open(path)
image = image.resize((450, 490), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
panel = tk.Label(image = img)

# Layout of the frames
fr_buttons.grid(row=0, column=0, sticky="nsew")
panel.grid(row=0, column=1, sticky="new")

window.mainloop()