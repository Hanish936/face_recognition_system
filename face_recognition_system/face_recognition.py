from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from student import Student
import os
from train import Train
import cv2
import mysql.connector
from time import strftime
from datetime import datetime
from cv2 import numpy
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')

        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35, "bold"),bg="white",fg="Green")
        title_lbl.place(x=0, y=0,width=1430,height=45)
        
        img_top = Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Attendence.jpeg")
        img_top=img_top.resize((450,400),Image.LANCZOS)    
        self.photoimg_top = ImageTk.PhotoImage(img_top)  

        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=450, height=400)

        img_bottom = Image.open(r"college_images\FaceDetector.jpeg")
        img_bottom=img_bottom.resize((550,400),Image.NEAREST)    
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)  

        f_lbl = tk.Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=550, height=400)

        #button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18, "bold"),bg="brown",fg="white")
        b1_1.place(x=165, y=325,width=200,height=40)
#attendence
    def mark_attendence(self,i,r,n,d):
        with open("Hanish.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

        ############ face recognize########
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="hanish", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id = " + str(id))
                n = my_cursor.fetchone()

                if n is not None:
                    n = "+".join(n)
                else:
                    n = "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id = " + str(id))
                r = my_cursor.fetchone()

                if r is not None:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id = " + str(id))
                d = my_cursor.fetchone()

                if d is not None:
                    d = "+".join(d)
                else:
                    d = "Unknown"
                    
                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = " + str(id))
                i = my_cursor.fetchone()

                if i is not None:
                    i = "+".join(i)
                else:
                    i = "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"NAME:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]

                return coord

    
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Welcome To Face Recognition',img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition(root)
    root.mainloop()