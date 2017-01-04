#Python Ver: 3.4.1
#
#Author:  Glenda A. Najem  along with 
#***Guidance from Tech Academy Portland***
#
#Purpose: Create a User Interface Script - Easier and Versatile for user.
#
#Tested OS:  This code was written and tested to work with windows 10.

#
# 

import shutil
import os
os.chdir('C:\\')
import datetime 
from datetime import timedelta
import time


import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, askopenfile, askdirectory


toplevel = Tk()
toplevel.withdraw()

class MainClass():    
  def __init__(self,master):
      frame = Frame(master)
      frame.pack()
      #self.srcDir(self) = s
      #self.dstDir(self) = d
      
      Label(root, text = "Daily File Check & or xTransfer").pack()

      self.s = StringVar()	
      dirButton_s = Button(root, text = 'Browse source Folder', 
      width=24,height=2, command = self.askSrcDir_src)
      dirButton_s.pack()

      self.d = StringVar()      
      dirButton_d = Button(root, text = 'Browse destination Folder', 
      width=24,height=2, command = self.askDstDir_dst)
      dirButton_d.pack()
       
      dirButton3 = Button(root, text = 'Check and Move Files', 
      width=24,height=2, command = self.CheckFiles)
      dirButton3.pack()

  #Choose Source folder 
  def askSrcDir_src(self):
    def askDirectory_src():
      dirSrcnam = filedialog.askdirectory()
      if dirSrcnam:
        self.s.set(dirSrcnam)
        return self.s.get()
    askDirectory_src()      
    print('Source:', self.s.get()) 
                     
  #Choose Destination folder
  def askDstDir_dst(self):  
    def askDirectory_dst():
        dirDstnam = filedialog.askdirectory()
        if dirDstnam:
          self.d.set(dirDstnam)
          return self.d.get()     
    askDirectory_dst()
    print ('Destination:', self.d.get())

               
  # CheckFiles function.     
  def CheckFiles(self):
      src = ###
      dst = ###
      print(src)
      print(dst)
      for fname in os.listdir(src):
          if fname.endswith('.txt'):
             src_fname = os.path.join(src,fname) # Use this module to create working absolute path
             dst_fname = os.path.join(dst, fname) # Use this module to create working absolute path
             mtime = (os.path.getmtime(src_fname)) # file creation/modification date
             timeDiff = time.time() - mtime #Difference from time of file creation or modification until current time
             _24hrsAgo = time.time() - (24 *60 *60) #Epoc time for a 24hr period is 86400 seconds
             last24hrs = time.time() - _24hrsAgo #Seconds that have occured within the last 24 hr period
             if timeDiff < last24hrs: #Seconds that have passed since file creation or modification from last 24 hrs
                shutil.move(src_fname,dst)
                print("( {} ) moved to: {}".format(fname, dst))
              # print("\nProcess completed.\nThere are no more qualifying files."
                     # "\nPlease check back at a later time.\nGoodbye!")
                         
                            
if __name__ == '__main__':
    root = Tk()
    mcl = MainClass(root)
    root.mainloop()
                 
      
