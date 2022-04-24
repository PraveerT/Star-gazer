import os,glob,time,sys,keyboard
from pathlib import Path
import tkinter as tk
from numpy import load
from functools import partial
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget
import star_gazer

from PIL import Image, ImageTk

class gui:
    def __init__(self,data):
        # Create an instance of TKinter Window or frame
        self.data=data
        self.window = tk.Tk()
        
    def run(self):
        row=list(range(18))+list(range(18))
        col=[0]*18+[3]*18
        [tk.Label(text=str(x),wraplength=500, justify= tk.LEFT).grid(row =r, column =c) for x,r,c in zip(self.data[0],row,col)] 
        [tk.Label(text=str(x),wraplength=500, justify= tk.LEFT).grid(row =r, column =c+1) for x,r,c in zip(self.data[0].values(),row,col)] 
        self.window.mainloop()
        
    
Stars=star_gazer.Group(r'C:\Users\prav\All_Projects\Other\Star_gazer\hygdata_v3.csv\hygdata_v3.csv')   
Stars.data([2,3])

instance=gui(Stars.data([2]))
instance.run()