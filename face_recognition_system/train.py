from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train")

        title_lbl=Label(self.root,text="Train DataSet",font=("times new roman",35, "bold"),bg="white",fg="Green")
        title_lbl.place(x=0, y=0,width=1300,height=45)

        img_top=Image.open(r"college_images\Stanford.jpeg")
        img_top=img_top.resize((1250,200),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_1b1=Label(self.root,image=self.photoimg_top)
        f_1b1.place(x=0,y=45,width=1250,height=200)   

    

        img_bottom=Image.open(r"college_images\Background.jpeg")
        img_bottom=img_bottom.resize((1400,350),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_1b1=Label(self.root,image=self.photoimg_bottom)
        f_1b1.place(x=0,y=320,width=1400,height=350)   

        
        #button
        b1_1=Button(self.root,text="Train data",cursor="hand2",command=self.train_classifier,font=("times new roman",30, "bold"),bg="brown",fg="white")
        b1_1.place(x=0, y=248,width=1400,height=70)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')       #gray scale img
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


    #     ####classifiers#####
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","training Dataset completed")

    
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
