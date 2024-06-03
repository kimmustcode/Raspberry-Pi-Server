from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io
from e621 import E621
import random
from tkinter import messagebox as mb 
import time

class dURLImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_Data = u.read()
        maxwidth = 1080
        maxheight = 1920 
        im = Image.open(io.BytesIO(raw_Data))
        height, width = im.size

        print(height, width)
        ratio = min(maxwidth/width, maxheight/height)
        print(ratio)
        print(height*ratio, width*ratio)

        
        image = im.resize((int(height * ratio), int(width * ratio)))
        self.image = ImageTk.PhotoImage(image)
    
    def get(self):
        return self.image
    

class imageDisplay:
    def __init__(self, url):
        self.root = Tk()

        maxwidth = 1080
        maxheight = 1920 

        # Set window settings 
        self.root.wm_title("Frame")
        self.root.geometry("1920x1080")
        self.root.configure(bg='black')
        self.root.attributes('-fullscreen',True)

        self.pic = dURLImage(url).get()
        self.picLabel = Label(self.root, image=self.pic) 
        self.picLabel.grid(column=5,row=5)
        self.picLabel.place(x=maxheight/2, y=maxwidth/2, anchor=CENTER)

        self.root.mainloop()
        self.root.destroy()

imageDisplay('https://static1.e621.net/data/30/e4/30e4864022b28369c8adb4e9c7924a4d.png')
