from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

    #first image
        img=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Stanford.jpeg")
        img=img.resize((700,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=700,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Stanford.jpeg")
        img1=img1.resize((700,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_1b1=Label(self.root,image=self.photoimg1)
        f_1b1.place(x=700,y=0,width=700,height=130)
        
        
        img3=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Background.jpeg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lb1=Label(bg_img,text="Attendence MANAGEMENT SYSTEM",font=("times new roman",32,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1400,height=45)
        
        
        main_frame=Frame(bg_img,bd=2,bg="White")
        main_frame.place(x=7,y=55,width=1250,height=600)
        
        #Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=440)
        
        img_left=Image.open(r"C:\Users\sonal\OneDrive\Desktop\face_recognition_system\college_images\Stanford.jpeg")
        img_left=img_left.resize((590,100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_1b1=Label(Left_frame,image=self.photoimg_left)
        f_1b1.place(x=5,y=0,width=590,height=100)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=115,width=570,height=250)
        
        #labels
        #attendence Id
        attendenceId_label=Label(left_inside_frame,text='Attendence Id:',font=("times new roman",10,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=7,pady=3,sticky=W)
        
        attendenceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",10,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=7,pady=3,sticky=W)
        
        #Name
        rolllabel=Label(left_inside_frame,text='Roll:',font=("times new roman",10,"bold"),bg="white")
        rolllabel.grid(row=0,column=2,padx=7,pady=3,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",10,"bold"))
        atten_roll.grid(row=0,column=3,padx=7,pady=3,sticky=W)
        
        #date
        nameLabel=Label(left_inside_frame,text="Name",font=("times new roman",10,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",10,"bold"))
        atten_name.grid(row=1,column=1,pady=8)
        
        #Department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",10,"bold"),bg="white")
        depLabel.grid(row=1,column=2)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font="comicsansns 10 bold")
        atten_dep.grid(row=1,column=3,pady=8)
        
        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 10 bold")
        timeLabel.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font="comicsansns 10 bold")
        atten_time.grid(row=2,column=1,pady=8)
        
        #Date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 10 bold")
        dateLabel.grid(row=2,column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font="comicsansns 10 bold")
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendence
        attendenceLabel=Label(left_inside_frame,text="Attendence Status",bg="white",font="comicsansns 10 bold")
        attendenceLabel.grid(row=3,column=0)
        

        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 10 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=560,height=30)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=36,font=("times new roman",7,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=36,font=("times new roman",7,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        
        
        reset_btn=Button(btn_frame,text="Reset",width=36,command=self.reset_data,font=("times new roman",7,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        #Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Attendence Details",font=("comicsansns 10 bold"))
        Right_frame.place(x=620,y=10,width=600,height=430)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=580,height=400)
        
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendaceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)
        
        self.AttendaceReportTable.heading("id",text="Attendance ID")
        self.AttendaceReportTable.heading("roll",text="Roll")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="Department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendance",text="Attendance")
        
        self.AttendaceReportTable["show"]="headings"
       
        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("roll",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("attendance",width=100)        
        self.AttendaceReportTable.pack(fill=BOTH,expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())   
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
   
   #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","no Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
        
    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        

if __name__== "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()