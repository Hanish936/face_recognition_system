import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from time import strftime
from datetime import datetime
from face_recognition import Face_Recognition
from attendence import Attendence
from help import Help
import tkinter
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #first image
        img=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Stanford.jpeg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=500,height=130)
        #second image
        img1=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Stanford.jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_1b1=Label(self.root,image=self.photoimg1)
        f_1b1.place(x=500,y=0,width=500,height=130)
        #third image
        img2=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Stanford.jpeg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_1b1=Label(self.root,image=self.photoimg2)
        f_1b1.place(x=1000,y=0,width=500,height=130)
        #background image
        img3=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Background.jpeg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",32,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1400,height=45)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lb1,font=('times new roman',14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        #student button
        img4=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Student.png")
        img4=img4.resize((150,150),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2")
        b1_1.place(x=150,y=250,width=150,height=40)
        
        #Detect face Button
        img5=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\FaceDetector.jpeg")
        img5=img5.resize((150,150),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data)
        b1_1.place(x=400,y=250,width=150,height=40)
        
        
        #Attendence face Button
        img6=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Attendence.jpeg")
        img6=img6.resize((150,150),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=650,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data)
        b1_1.place(x=650,y=250,width=150,height=40)
        
        #Help Desk
        img7=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Helpdesk.jpeg")
        img7=img7.resize((150,150),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=900,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data)
        b1_1.place(x=900,y=250,width=150,height=40)
        
        #Train face Button
        img8=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Traindata.jpeg")
        img8=img8.resize((150,150),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=275,y=300,width=150,height=150)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data)
        b1_1.place(x=275,y=450,width=150,height=40)
        
        #photos face Button
        img9=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\photos.jpeg")
        img9=img9.resize((150,150),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=525,y=300,width=150,height=150)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img)
        b1_1.place(x=525,y=450,width=150,height=40)
        
        
        
        #Exit Button
        img11=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Exit.jpeg")
        img11=img11.resize((150,150),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=775,y=300,width=150,height=150)
        
        b1_1=Button(bg_img,text="Exit ",cursor="hand2",command=self.iExit)
        b1_1.place(x=775,y=450,width=150,height=40)
            
    def open_img(self):
        os.startfile("data")
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)   
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)   
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition ","Do you want to exit ")
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        
if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
