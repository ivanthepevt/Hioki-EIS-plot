from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, Text
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import sys
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

root = Tk()
root.title("EIS plot vjp pro")
frm = ttk.Frame(root, padding=20)
frm.grid()

filelist = ["Choose a .csv file", "Choose a .csv file", "Choose a .csv file", "Choose a .csv file",
            "Choose a .csv file", "Choose a .csv file", "Choose a .csv file", "Choose a .csv file",
            "Choose a .csv file", "Choose a .csv file", "Stop right there", "Too much data",
            "One more and error", "Noooooooooo"]

En1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
namae = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
poloto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

fig, ax = plt.subplots()  # create a fig


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


def select_file(plc):
    global roww
    filetypes = (
        ('Measured data', '*.csv'),
        ('All files', '*.*')
    )

    filelist[plc] = fd.askopenfilename(
        title='Choose a file',
        initialdir='/',
        filetypes=filetypes)

    En1[plc].insert(END, filelist[plc].split("/")[-1].split(".")[0])
    namae[plc] = En1[plc].get()

    if (plc == roww):
        roww = roww + 1
        ttk.Label(frm, text="Plot " + str(roww) + "   ").grid(column=0, row=roww + a)  # Labels, all column 0
        ttk.Button(frm, text=filelist[roww], command=lambda: select_file(roww)).grid(column=1,
                                                                                     row=roww + a)  # Filedialog, all column 1
        ttk.Label(frm, text="Name: ").grid(column=2, row=roww + a)
        En1[roww] = ttk.Entry(frm)
        En1[roww].grid(column=3, row=roww + a)
    #print(plc, roww)

def export():
    polotoo = []
    # Dump line to re-get all the names
    for k in range(roww - 1):
        namae[k + 1] = En1[k + 1].get()
    # print(En1)
    # print(filelist)
    # print(namae)
    # print(mode.get())
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        if (namae[i - 1] != i):
            # print(i)
            plotzz(i - 1)
            # check for rows that filled
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        if (poloto[i - 1] != i):
            polotoo.append(poloto[i - 1])
            # append names for legends
    # make the plot
    plt.title(Title.get())
    plt.xlabel(Zthuc.get())
    plt.ylabel(Zao.get())
    ax.legend(handles=polotoo)
    plt.show()


def plotzz(fileindex):
    reader = np.loadtxt(open(filelist[fileindex], "rb"), delimiter=",", skiprows=1)
    data = [[reader[j][i] for j in range(len(reader))] for i in range(len(reader[0]))]
    #print(data)
    zreal = data[2]
    zimag = data[3]
    if (mode.get() == " Z' vs -Z''"):
        for i in range(len(zimag)):
            zimag[i] = -zimag[i]
    poloto[fileindex] = ax.scatter(zreal, zimag, label=namae[fileindex])  # Plot some data on the axes.


# Row 1
ttk.Label(frm, text="").grid(column=0, row=0)

Title = ttk.Entry(frm)
Title.grid(column=0, row=1)
Title.insert(END, "Title here")

ttk.Label(frm, text="Plotting mode:").grid(column=0, row=2)

mode = ttk.Combobox(frm)
mode['values'] = (" Z' vs Z''", " Z' vs -Z''")
mode.grid(column=1, row=2)
mode.current(1)

ttk.Label(frm, text="x - axis: ").grid(column=0, row=3)
Zthuc = ttk.Entry(frm)
Zthuc.grid(column=1, row=3)
Zthuc.insert(END, "Z' (Ω)")

ttk.Label(frm, text="y - axis: ").grid(column=0, row=4)
Zao = ttk.Entry(frm)
Zao.grid(column=1, row=4)
Zao.insert(END, "-Z'' (Ω)")

# A row to separate
a = 5
ttk.Label(frm, text="_______________").grid(column=0, row=a)
# Rows later
roww = 1
ttk.Label(frm, text="Plot " + str(roww) + "   ").grid(column=0, row=roww + a)  # Labels, all column 0
ttk.Button(frm, text=filelist[roww], command=lambda: select_file(roww)).grid(column=1,
                                                                             row=roww + a)  # Filedialog, all column 1
# put a lamda so that the button will not self activate
ttk.Label(frm, text="Name: ").grid(column=2, row=roww + a)
En1[roww] = ttk.Entry(frm)
En1[roww].grid(column=3, row=roww + a)

ttk.Label(frm, text=" ").grid(column=0, row=48)
ttk.Label(frm, text=" ").grid(column=0, row=49)
ttk.Button(frm, text="Plot", command=export).grid(column=0, row=50)

root.mainloop()
