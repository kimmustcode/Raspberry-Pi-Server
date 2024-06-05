from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io
import os
import sys
import time

if os.environ.get('DISPLAY', '') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')

class dURLImage:
    def __init__(self, url):

        req = urllib.request.Request(
            url,
            data=None,
            headers = {'User-Agent': 'Mozilla/0.5 (Windows; U; Windows NT 6.3; Win64; x64) Gecko/20100101 Firefox/69.5'}
        )

        with urllib.request.urlopen(url) as u:
            raw_Data = u.read()
        maxwidth = self.root.winfo_screenwidth()
        maxheight = self.root.winfo_screenheight() 
        im = Image.open(io.BytesIO(raw_Data))
        height, width = im.size

      
        ratio = min(maxwidth/width, maxheight/height)
        
        image = im.resize((int(height * ratio), int(width * ratio)))
        self.image = ImageTk.PhotoImage(image)
    
    def get(self):
        return self.image
    

class imageDisplay:
    def __init__(self, url):
        self.root = Tk()

        maxwidth = self.root.winfo_screenwidth()
        maxheight = self.root.winfo_screenheight() 
        geo = str(maxwidth) + 'x' + str(maxheight) 

        # Set window settings 
        self.root.wm_title("Frame")
        self.root.geometry(geo)
        self.root.configure(bg='black')

        self.pic = dURLImage(url).get()
        self.picLabel = Label(self.root, image=self.pic) 
        self.picLabel.grid(column=5,row=5)
        self.picLabel.place(x=maxheight/2, y=maxwidth/2, anchor=CENTER)
        
        self.picLabel.pack()
        self.root.update_idletasks()
        self.root.after(100, self.root.overrideredirect(1))
        self.root.after(100, self.root.wm_attributes('-fullscreen',True))


        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.picLabel.focus_set()
        self.root.mainloop()

    def closeWindow(self):
        self.root.quit()

imageDisplay('https://static1.e621.net/data/30/e4/30e4864022b28369c8adb4e9c7924a4d.png')
