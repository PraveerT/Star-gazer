from http.client import IM_USED
import textwrap
from tkinter import *
from tkinter.ttk import *
import numpy as np
import star_gazer
from functools import partial
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import math

class GUI:
    def __init__(self,data,constellations):
        self.win=Tk()
        self.win.wm_title("Star Gazer")
        self.constellations=constellations
        self.constellations_keys=list(constellations.keys())
        #image
        self.tempimage=Image.open(r"C:\Users\prav\All_Projects\Other\Star_gazer\Images\Star_logo.png")
        self.finalimage=self.tempimage.resize((round(self.tempimage.size[0]*0.07),round(self.tempimage.size[1]*0.07)))
        self.image = ImageTk.PhotoImage(self.finalimage)
        #geomery
        self.win.geometry("780x580")
        self.win.resizable(False, False)
        self.mainframeheight=406
        self.mainframewidth=600
        self.row=list(range(18))+list(range(18))
        self.col=[0]*18+[3]*18
        self.padx=70
        self.pady=40
        #data for stars
        self.data=data
        #text entries and text frame
        self.textframebodytext="This database is a subset of the data in three major catalogs:the Hipparcos Catalog,the Yale Bright Star Catalog (5th Edition), and the Gliese Catalog of Nearby Stars (3rd Edition). "
        self.textframe=LabelFrame(self.win, height=100,width=700)
        self.textframe.grid(column=0,row=0,columnspan=2)
        self.textframetitle=Label(self.textframe,text="Star Catalogue")
        self.textframetitle.place(relx=.5, rely=.2,anchor= CENTER)
        self.textframebody=Label(self.textframe,text=self.textframebodytext,wraplength=350)
        self.textframebody.place(relx=.5, rely=.6,anchor= CENTER)
        self.textframebody=Label(self.textframe,image=self.image)
        self.textframebody.place(relx=0.01, rely=0)
        #Mainframe
        self.mainframe=LabelFrame(self.win,text="Info",height=self.mainframeheight,width=self.mainframewidth)
        self.mainframe.grid(column=1,row=1)
        self.mainframe.grid_propagate(0)
        
        self.selectbox=LabelFrame(self.win,text="All stars")
        self.selectbox.grid(column=0,row=1)
        
        self.listbox = Listbox(self.selectbox,listvariable=StringVar(value=list(self.data.keys())),height=24,selectmode='extended')
        self.listbox.grid(column=0,row=0,sticky='nwes')
        
        self.scrollbar = Scrollbar(self.selectbox,orient='vertical',command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.grid(column=1,row=0,sticky='ns')
        #Option
        self.OptionVar= StringVar()
        # self.button_1= Button(self.win, text ="Hello",command=partial(self.UpdateMainFrame,1)).grid(row=1,column=1)
        self.Options = OptionMenu(self.win, self.OptionVar,"Constellation", *self.constellations_keys,command=self.UpdateScrollbar).grid(row=3,column=0,pady=15)
        self.listbox.bind('<<ListboxSelect>>', self.UpdateMainFrame)
        #button
        self.buttonspace=LabelFrame(self.win)
        self.buttonspace.grid(row=3,column=1)
        self.button1 = Button(self.buttonspace,text ='Show',command = self.button1action).grid(row=0,column=0)
        self.button2 = Button(self.buttonspace,text ='Abs Mag vs Lum',command = self.button2action).grid(row=0,column=1)

        self.listbox.select_set(0)
        self.UpdateMainFrame(self.listbox.curselection())
   

    def UpdateScrollbar(self,event):
        self.listbox = Listbox(self.selectbox,listvariable=StringVar(value=(self.constellations[str(self.OptionVar.get())])),height=24,selectmode='extended')
        self.scrollbar = Scrollbar(self.selectbox,orient='vertical',command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.grid(column=1,row=0,sticky='ns')
        self.listbox.grid(column=0,row=0,sticky='nwes')
        self.listbox.bind('<<ListboxSelect>>', self.UpdateMainFrame)

    def UpdateMainFrame(self,event):
        
        self.choice=int(self.listbox.get(int(list(self.listbox.curselection())[0])))
        self.attribute=[Label(self.mainframe,text=(str(x)).capitalize()+":",wraplength=500, justify= LEFT, font=('Helvetica', 8, 'bold')).grid(row =r, column =c,sticky='ew',padx= self.padx) for x,r,c in zip(self.data[self.choice].keys(),self.row,self.col)] 
        self.values=[Label(self.mainframe,text=str(x),wraplength=500, justify= LEFT).grid(row =r, column =c+1,sticky='ew') for x,r,c in zip(self.data[self.choice].values(),self.row,self.col)] 
    
    def button1action(self):
        novi = Toplevel()
        canvas = Canvas(novi, width = 600, height = 600)
        canvas.pack(expand = YES, fill = BOTH)
        file =Image.open("C:\\Users\\prav\\All_Projects\Other\\Star_gazer\\Images\\constellation_images\\%s.gif"%self.OptionVar.get())
        finalimage=file.resize((600,600))
        gif1 = ImageTk.PhotoImage(finalimage)
        canvas.create_image((0,0), image = gif1, anchor = NW)
        #assigned the gif1 to the canvas object
        canvas.gif1 = gif1

    def button2action(self):
        stardataAmag=[list(self.data[star].values())[13] for star in (self.constellations[str(self.OptionVar.get())])]
        stardatalum=[(list(self.data[star].values())[32]) for star in (self.constellations[str(self.OptionVar.get())])]
        
        fig, ax = plt.subplots()
        ax.plot(stardataAmag, stardatalum,'x')

        ax.set(xlabel='AMag', ylabel='Lum',
            title='Abs Mag vs luminosity')
        ax.grid()

        fig.savefig("test.png")
        plt.show()

    def run(self):
        self.win.mainloop()

Stars=star_gazer.Group(r'C:\Users\prav\All_Projects\Other\Star_gazer\hygdata_v3.csv\hygdata_v3.csv')   
Mywindow=GUI(Stars.stardict,Stars.categoriescon)

Mywindow.run()
