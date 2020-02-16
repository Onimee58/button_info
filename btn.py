# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:56:29 2020

@author: Saif
"""

from tkinter import *
import numpy as np
import os


global stdnt_1
name_file = open("name.txt", 'r')
stdnt = name_file.readlines()
bttn = [1, 1, 1, 1, 1]
buttonClick = bttn


for i in range(len(stdnt)-1):
    stdnt[i] = stdnt[i][:-1]

class Window(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.window_1(std_num = 4)
        
    def window_1(self,std_num): 
        self.master.title("Student Info")
        self.pack(fill = BOTH, expand = 1)
        bttn[0] = Button(self, text = stdnt[0] , command = self.buttonClick_0)
        bttn[0].place(x=0, y=0+0*30)
        bttn[1] = Button(self, text = stdnt[1] , command = self.buttonClick_1)
        bttn[1].place(x=0, y=0+1*30)
        bttn[2] = Button(self, text = stdnt[2] , command = self.buttonClick_2)
        bttn[2].place(x=0, y=0+2*30)
        bttn[3] = Button(self, text = stdnt[3] , command = self.buttonClick_3)
        bttn[3].place(x=0, y=0+3*30)
        bttn[4] = Button(self, text = stdnt[4] , command = self.buttonClick_4)
        bttn[4].place(x=0, y=0+4*30)

    def buttonClick_0(self):
        name = stdnt[0] + ".txt"
        info = open(name, 'r')
        final_info = info.readlines()
        #print(final_info)
        os.startfile(name)
        
    def buttonClick_1(self):
        name = stdnt[1] + ".txt"
        info = open(name, 'r')
        final_info = info.readlines()
        #print(final_info)
        os.startfile(name)
        
    def buttonClick_2(self):
        name = stdnt[2] + ".txt"
        info = open(name, 'r')
        final_info = info.readlines()
        #print(final_info)
        os.startfile(name)
        
    def buttonClick_3(self):
        name = stdnt[3] + ".txt"
        info = open(name, 'r')
        final_info = info.readlines()
       #print(final_info)
        os.startfile(name)
        
    def buttonClick_4(self):
        name = stdnt[4] + ".txt"
        info = open(name, 'r')
        final_info = info.readlines()
        #print(final_info)
        os.startfile(name)

def start():
    root = Tk()
    root.geometry("500x500")
    app = Window(root)
    root.mainloop()




if __name__ == "__main__":
    start()