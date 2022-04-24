import os,glob,time,sys,keyboard
from pathlib import Path
import tkinter as tk
from numpy import load
from functools import partial
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget
import star_gazer

from PIL import Image, ImageTk

def read(choice,variable):
    choice=variable
    print (choice)

class gui:
    def __init__(self):
        
        # Create an instance of TKinter Window or frame
        
        self.window = tk.Tk()
    def menu(self):
        variable = tk.StringVar()
        variable.set("Stars") # default value
        w = tk.OptionMenu(self.window, variable, *self.staridlist,command=partial(read,variable))
        w.grid(row=19,column=0)
        
    def run(self,data):

        self.data=data
        self.staridlist=[self.data[x]["id"] for x in range(len(self.data))]
        

        
        row=list(range(18))+list(range(18))
        col=[0]*18+[3]*18
        
        self.menu()
        

        [tk.Label(text=str(x),wraplength=500, justify= tk.LEFT).grid(row =r, column =c) for x,r,c in zip(self.data[0],row,col)] 
        [tk.Label(text=str(x),wraplength=500, justify= tk.LEFT).grid(row =r, column =c+1) for x,r,c in zip(self.data[0].values(),row,col)] 
        self.window.mainloop()


        
    
Stars=star_gazer.Group(r'C:\Users\prav\All_Projects\Other\Star_gazer\hygdata_v3.csv\hygdata_v3.csv')   
Stars.data([2,3])

instance=gui()
instance.run(Stars.data(list(range(100))))