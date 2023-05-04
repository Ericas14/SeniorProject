# This is a sample Python script.
import tkinter
from array import array
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import backend as program


def gui():
    # writing code needs to
    # create the main window of
    # the application creating
    # main window object named root
    global root
    root = Tk()

    # giving title to the main window
    root.title("The Automated Separation of Machine Printed and Hand-written Text")
    root.geometry("500x300")
    global topFrame
    global bottomFrame
    topFrame = Frame(root, width=500, height=150)
    topFrame.grid(row=0, column=0, sticky=W, pady=2)
    bottomFrame = Frame(root, width=500, height=150)
    bottomFrame.grid(row=1, column=0, sticky=W, pady=2)

    # Label is what output will be
    # show on the window
    label = Label(topFrame, text="Please upload one image or more.")
    b1 = Button(topFrame, text='Upload File', width=20, command=lambda: upload_file())
    label.grid(row=1, column=0, sticky=W, columnspan=3)
    b1.grid(row=2, column=0, sticky=W, pady=2)

    # calling mainloop method which is used
    # when your application is ready to run
    # and it tells the code to keep displaying
    root.mainloop()


def upload_file():
    global filenames
    global topFrame
    global bottomFrame
    categories = {}
    f_types = [('Images', '*.jpg *.jpeg *.png')]
    filenames = filedialog.askopenfilename(multiple=True, filetypes=f_types)
    categories = program.load_files(filenames)
    file = Label(root, text=filenames)
    label1 = Label(topFrame, text="Image")
    label2 = Label(topFrame, text="Verdict")
    label1.grid(row=3, column=0, sticky=W, pady=2)
    label2.grid(row=3, column=1, sticky=W, pady=2)

    row = 4
    for key, value in categories.items():
        file = Label(topFrame, text=key)
        label3 = Label(topFrame, text=value)
        file.grid(row=row, column=0, sticky=W, pady=2)
        label3.grid(row=row, column=1, sticky=W, pady=2)
        row += 1
    images = []
    column = 0
    for file in filenames:
        openImage = Image.open(file)
        openImage = openImage.resize((300,300), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(openImage)
        label = Label(bottomFrame, image=image1)
        label2 = Label(bottomFrame, text=file)
        label.image = image1
        label.grid(row=row, column=column, sticky=W, pady=2)
        label2.grid(row=row+1, column=column, sticky=W, pady=2)
        column += 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
