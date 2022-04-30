import textwrap
from tkinter import *
from tkinter.ttk import *
import numpy as np
import star_gazer
from functools import partial
class GUI:
    def __init__(self,menuitem,id):
        self.win=Tk()
        self.win.geometry("780x580")
        self.win.resizable(False, False)
        self.menuitem=menuitem
        self.id=id
        self.textframebodytext="This database is a subset of the data in three major catalogs:the Hipparcos Catalog,the Yale Bright Star Catalog (5th Edition), and the Gliese Catalog of Nearby Stars (3rd Edition). "
        self.mainframeheight=400
        self.mainframewidth=600
        self.row=list(range(18))+list(range(18))
        self.col=[0]*18+[3]*18
        self.variable = StringVar()
        self.variable.set(0) # default value
        self.mainframe=LabelFrame(self.win,text="Info",height=self.mainframeheight,width=self.mainframewidth)
        self.mainframe.grid(column=1,row=1)
        self.mainframe.grid_propagate(0)
        self.textframe=LabelFrame(self.win, height=100,width=400)
        self.textframe.grid(column=0,row=0,columnspan=2)
        self.textframetitle=Label(self.textframe,text="Star Catalogue")
        self.textframetitle.place(relx=.5, rely=.2,anchor= CENTER)
        self.textframebody=Label(self.textframe,text=self.textframebodytext,wraplength=350)
        self.textframebody.place(relx=.5, rely=.7,anchor= CENTER)
        self.padx=70
        self.pady=40
        self.attribute=[Label(self.mainframe,text=str(x),wraplength=500, justify= LEFT).grid(row =r, column =c,sticky='ew',padx= self.padx) for x,r,c in zip(self.menuitem[0],self.row,self.col)] 
        self.values=[Label(self.mainframe,text=str(x),wraplength=500, justify= LEFT).grid(row =r, column =c+1,sticky='ew') for x,r,c in zip(self.menuitem[0].values(),self.row,self.col)] 

        self.selectbox=LabelFrame(self.win,text="All stars")
        self.selectbox.grid(column=0,row=1)
        self.listbox = Listbox(self.selectbox,listvariable=StringVar(value=self.id),height=20,selectmode='extended')
        self.listbox.grid(column=0,row=0,sticky='nwes')
        
        self.scrollbar = Scrollbar(self.selectbox,orient='vertical',command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.grid(column=1,row=0,sticky='ns')
        # self.button_1= Button(self.win, text ="Hello",command=partial(self.UpdateMainFrame,1)).grid(row=1,column=1)
        # self.Options = OptionMenu(self.win, self.variable, *self.id,command=self.UpdateMainFrame).grid(row=3,column=3)
        self.listbox.bind('<<ListboxSelect>>', self.UpdateMainFrame)



    def UpdateMainFrame(self,event):
        self.choice=int(list(self.listbox.curselection())[0])
        self.mainframe.grid_forget()
        self.mainframe=LabelFrame(self.win,text="Info",height=self.mainframeheight,width=self.mainframewidth)
        self.mainframe.grid(column=1,row=1)
        self.mainframe.grid_propagate(0)
        self.attribute=[Label(self.mainframe,text=str(x),wraplength=500, justify= LEFT).grid(row =r, column =c,sticky='ew',padx= self.padx) for x,r,c in zip(self.menuitem[self.choice],self.row,self.col)] 
        self.values=[Label(self.mainframe,text=str(x),wraplength=500, justify= LEFT).grid(row =r, column =c+1,sticky='ew') for x,r,c in zip(self.menuitem[self.choice].values(),self.row,self.col)] 


    def run(self):
        self.win.mainloop()

Stars=star_gazer.Group(r'C:\Users\prav\All_Projects\Other\Star_gazer\hygdata_v3.csv\hygdata_v3.csv')   
Mystars=Stars.data()


        

Mywindow=GUI(Stars.data(list(range(len(Mystars)))),list(range(len(Mystars))))
Mywindow.run()