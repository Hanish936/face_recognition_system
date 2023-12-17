from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')

        title_lbl=Label(self.root,text="Help",font=("times new roman",35, "bold"),bg="white",fg="Blue")
        title_lbl.place(x=0, y=0,width=1400,height=45)

        img_top = Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\helpdesk1.jpeg")
        img_top=img_top.resize((1400,650),Image.LANCZOS)    
        self.photoimg_top = ImageTk.PhotoImage(img_top)  

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1400, height=720)

        dev_label=Label(f_lbl,text="Email:Hanishchauhan02@gmail.com",font=("times new roman",20,"bold"))
        dev_label.place(x=500,y=220,)






if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()