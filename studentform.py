from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1290x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='black')
        frame=Frame(root,bg="navy",borderwidth=6,relief=SUNKEN)
        frame.place(x=0,y=0,width=1265,height=120)
        frame.pack(fill="x")
#"student_id","student_name","e_mail","gender","phone_no","parent_no","dob","address","photo","department","course","semester","year"
        self.var_student_id=StringVar()
        self.var_student_name=StringVar()
        self.var_e_mail=StringVar()
        # self.var_gender=StringVar()
        self.var_phone_no=StringVar()
        self.var_parent_no=StringVar()
        self.var_bod=StringVar()
        self.var_address=StringVar()
        self.var_photo=StringVar()
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.var_year=StringVar()


        l=Label(frame,text="Student Details",font="Monospace 50 bold",bg="navy",fg="red")
        l.pack(pady=20)
        frame_2=Frame(root,bg="cyan",borderwidth=8,relief=SUNKEN,highlightbackground="blue")
        frame_2.place(x=0,y=138,width=1285,height=900)
        # frame_2.pack(fill="x")
        l_frame=LabelFrame(frame_2,bd=5,bg="white",relief="ridge",text="Student Details",font=("times new roman",12,"bold"))
        l_frame.place(x=10,y=7,width=615,height=580)


        c_frame=LabelFrame(l_frame,bd=5,bg="white",relief="ridge",text="Student Info",font=("times new roman",12,"bold"))
        c_frame.place(x=5,y=10,width=590,height=260)

        studid=Label(c_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studid.grid(row=0,column=0,padx=10)

        studid_entry=ttk.Entry(c_frame,textvariable=self.var_student_id,width=20,font=("times new roman",12,"bold"))
        studid_entry.grid(row=0,column=1,padx=10,sticky=W)


        studname=Label(c_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studname.grid(row=1,column=0,padx=10)

        studename_entry=ttk.Entry(c_frame,textvariable=self.var_student_name,width=20,font=("times new roman",12,"bold"))
        studename_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        email=Label(c_frame,text="E-Mail:",font=("times new roman",12,"bold"),bg="white")
        email.grid(row=2,column=0,padx=10)

        email_entry=ttk.Entry(c_frame,textvariable=self.var_e_mail,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=10)

        gender=Label(c_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender.grid(row=4,column=0)

        # gen=ttk.Radiobutton(c_frame,text="Male")
        # gen.grid(row=3,column=1,padx=10,pady=10)W

        # gender_entry=ttk.Entry(c_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=4,column=1,padx=10,pady=10)
        self.var_gender1=StringVar()
        rd1=ttk.Radiobutton(c_frame,text="Male",variable=self.var_gender1,value="Male")
        rd1.grid(row=4,column=1)
        rd2=ttk.Radiobutton(c_frame,text="Female",variable=self.var_gender1,value="Female")
        rd2.grid(row=4,column=3)
        

        add=Label(c_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        add.grid(row=3,column=0,padx=10)

        add_entry=ttk.Entry(c_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=3,column=1,padx=10,pady=10)


        phone_no=Label(c_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_no.grid(row=0,column=3,padx=5)

        phone_no_entry=ttk.Entry(c_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=0,column=4,padx=10,pady=10)

        phone_no1=Label(c_frame,text="Parent No:",font=("times new roman",12,"bold"),bg="white")
        phone_no1.grid(row=1,column=3,padx=5)

        phone_no1_entry=ttk.Entry(c_frame,textvariable=self.var_parent_no,width=20,font=("times new roman",12,"bold"))
        phone_no1_entry.grid(row=1,column=4,padx=10,pady=10)

        dob=Label(c_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob.grid(row=2,column=3,padx=5)

        dob_entry=ttk.Entry(c_frame,textvariable=self.var_bod,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=4,padx=10,pady=10)

        # photo=Button(c_frame,text="Take Photo",font=("times new roman",8,"bold"),bg="black",fg="white")
        # photo.grid(row=3,column=3,padx=10,pady=10)
        
        rd1=ttk.Radiobutton(c_frame,text="take photo",variable=self.var_photo,value="yes")
        rd1.grid(row=3,column=3)
        rd2=ttk.Radiobutton(c_frame,text="No photo",variable=self.var_photo,value="no")
        rd2.grid(row=3,column=4)

        photosample=Button(c_frame,text="photo collect",command=self.generate,font=("times new roman",12,"bold"),bg="black",fg="white")
        photosample.grid(row=5,column=0,pady=10)

        c1_frame=LabelFrame(l_frame,bd=5,bg="white",relief="ridge",text="Current Course Details",font=("times new roman",12,"bold"))
        c1_frame.place(x=5,y=270,width=590,height=130)

        dept=Label(c1_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dept.grid(row=0,column=0,padx=10)

        dept_combobox=ttk.Combobox(c1_frame,textvariable=self.var_department,font=("times new roman",12,"bold"),state="   readonly")
        dept_combobox["values"]=("Select Department","Computer Science","Physic","Chemistry","Biology","Zoology","Mathamatics","Statistics")
        dept_combobox.current(0)
        dept_combobox.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        course=Label(c1_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course.grid(row=0,column=2,padx=10)

        course_combobox=ttk.Combobox(c1_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="   readonly")
        course_combobox["values"]=("Select Course","Bsc CS","Bsc Plane","Msc CS","Msc CHEM","Msc BIO","Msc ZOO","Msc MATH","Msc STAT")
        course_combobox.current(0)
        course_combobox.grid(row=0,column=3,sticky=W)

        semester=Label(c1_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester.grid(row=1,column=0,padx=10)

        semester_combobox=ttk.Combobox(c1_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combobox["values"]=("Select Semester","Semester-I","Semester-II","Semester-III","Semester-IV","Semester-V","Semester-VI",)
        semester_combobox.current(0)
        semester_combobox.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        year=Label(c1_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year.grid(row=1,column=2,padx=10)

        year_combobox=ttk.Combobox(c1_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="   readonly")
        year_combobox["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
        year_combobox.current(0)
        year_combobox.grid(row=1,column=3,sticky=W)

        
        r_frame=LabelFrame(frame_2,bd=5,bg="white",relief="ridge",text="Student Details",font=("times new roman",12,"bold"))
        r_frame.place(x=628,y=7,width=615,height=580)


        button_frame=LabelFrame(l_frame,bd=5,bg="white",relief="ridge",text="Current Course Details",font=("times new roman",12,"bold"))
        button_frame.place(x=5,y=410,width=590,height=130)

        save_button=Button(button_frame,text="Save",command=self.data_feach,width=18,font=("times new roman",20,"bold"),bg="black",fg="white")
        save_button.place(x=5,y=15,width=145,height=40)

        update_button=Button(button_frame,text="Update",command=self.update_details,width=18,font=("times new roman",20,"bold"),bg="black",fg="white")
        update_button.place(x=150,y=15,width=140,height=40)
        
        delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",20,"bold"),bg="black",fg="white")
        delete_button.place(x=290,y=15,width=140,height=40)

        reset_button=Button(button_frame,text="Reset",command=self.reset,width=18,font=("times new roman",20,"bold"),bg="black",fg="white")
        reset_button.place(x=430,y=15,width=140,height=40)


        rc_frame=LabelFrame(r_frame,bd=5,bg="white",relief="ridge",text="Search Student",font=("times new roman",12,"bold"))
        rc_frame.place(x=5,y=10,width=590,height=120)

        searchbutton=Button(rc_frame,text="Search By:",font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
        searchbutton.grid(row=0,column=0,padx=10)


        searchby=ttk.Combobox(rc_frame,font=("times new roman",12,"bold"),state="readonly")
        searchby["values"]=("Select","Student Id","Phone No")
        searchby.current(0)
        searchby.grid(row=0,column=1,padx=10,sticky=W)

        searchentry=ttk.Entry(rc_frame,textvariable=self.var_student_id,width=20,font=("times new roman",12,"bold"))
        searchentry.grid(row=0,column=2,padx=10,sticky=W)

        search=Button(rc_frame,text="Show All",command=self.search,font=("times new roman",12,"bold"),bg="black",fg="white")
        search.grid(row=1,column=0,pady=10)

        clear=Button(rc_frame,text="Clear",font=("times new roman",12,"bold"),bg="black",fg="white")
        clear.grid(row=1,column=1)


        rc1_frame=Frame(r_frame,bd=5,bg="white",relief="ridge")
        rc1_frame.place(x=5,y=130,width=590,height=425  )
        scroll_x=ttk.Scrollbar(rc1_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(rc1_frame,orient=VERTICAL)
      
        #table Database
        self.student_table=ttk.Treeview(rc1_frame,columns=("student_id","student_name","e_mail","address","gender","phone_no","parent_no","dob","department","course","semester","year","photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side="bottom",fill=X)
        scroll_y.pack(side="right",fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("student_id",text="Student Id")
        self.student_table.heading("student_name",text="Student Name")
        self.student_table.heading("e_mail",text="E-Mail")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone_no",text="Phone No")
        self.student_table.heading("parent_no",text="Parent No")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo")
        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("year",text="Year")
        self.student_table["show"]="headings"

        self.student_table.column("student_name",width=140)
        self.student_table.column("student_id",width=140)
        self.student_table.column("e_mail",width=140)
        self.student_table.column("gender",width=140)
        self.student_table.column("phone_no",width=140)
        self.student_table.column("parent_no",width=140)
        self.student_table.column("dob",width=140)
        self.student_table.column("address",width=140)
        self.student_table.column("photo",width=140)
        self.student_table.column("department",width=140)
        self.student_table.column("course",width=140)
        self.student_table.column("semester",width=140)
        self.student_table.column("year",width=140)
    
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.data_fill)
        self.show_data()
    def data_feach(self):
        
        if self.var_student_name.get()=="":
            messagebox.showerror("Invalid","fill all fields",parent=self.root)
        else:
                try:
                    connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
                    print(connection)
                    my_curse=connection.cursor()
                  
                    my_curse.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_student_id.get(),self.var_student_name.get(),self.var_e_mail.get(),self.var_address.get(),self.var_gender1.get(),self.var_phone_no.get(),self.var_parent_no.get(),self.var_bod.get(),self.var_department.get(),self.var_course.get(),self.var_semester.get(),self.var_year.get(),self.var_photo.get()))
                    connection.commit()
                    self.show_data()
                    connection.close()
                    print(my_curse)
                    messagebox.showinfo("sucess","student details added successfully",parent=self.root)
                except Exception as e:
                    
                     messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)

    def show_data(self):
         try:
              connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
              my_curse=connection.cursor()
              my_curse.execute("select * from student")
              #store all data in temp vairable
              d=my_curse.fetchall()
              if len(d)!=0:
                   self.student_table.delete(*self.student_table.get_children())
                   for i in d:
                        self.student_table.insert("",END,values=i)
                        connection.commit()
                   connection.close()
         except Exception as e:
              print(e)
    def data_fill(self,event=""):
            select_i=self.student_table.focus()
            content=self.student_table.item(select_i)
            data=content["values"]  

            self.var_student_id.set(data[0])
            self.var_student_name.set(data[1])
            self.var_e_mail.set(data[2])
            self.var_address.set(data[3])
            self.var_gender1.set(data[4])
            self.var_phone_no.set(data[5])
            self.var_parent_no.set(data[6])
            self.var_bod.set(data[7])
            self.var_department.set(data[8])
            self.var_course.set(data[9])
            self.var_semester.set(data[10])
            self.var_year.set(data[11])
            self.var_photo.set(data[12])

    def update_details(self):
         try:
              
              #update=messagebox.showinfo("update","due you want Upadate Deatail",parent=self.root)
              connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
              my_cousor=connection.cursor()
              my_cousor.execute("update student set student_name=%s,email=%s,address=%s,gender=%s,phone_no=%s,parent_no=%s,dob=%s,dept=%s,course=%s,semester=%s,year=%s,photo=%s where student_id=%s",(self.var_student_name.get(),self.var_e_mail.get(),self.var_address.get(),self.var_gender1.get(),self.var_phone_no.get(),self.var_parent_no.get(),self.var_bod.get(),self.var_department.get(),self.var_course.get(),self.var_semester.get(),self.var_year.get(),self.var_photo.get(),self.var_student_id.get()))
              messagebox.showinfo("sucess","update sucessfully",parent=self.root) 
              connection.commit()
              self.show_data()
              connection.close()
             
               
         except Exception as e:
              messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)                
     

    def delete_data(self):
         if self.var_student_id.get()=="":
              messagebox.showerror("error","student id must be require",parent=self.root)
         else:
              try:
                   messagebox.showinfo("confirm","due you want delete")
                   connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
                   my_cursor=connection.cursor()
                   a=("delete from student where student_id=%s")
                   b=(self.var_student_id.get(),)
                   my_cursor.execute(a,b)
                   connection.commit()
                   self.show_data()
                   connection.close()
              
              except Exception as e:
                   messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)

    def reset(self):
         self.var_student_id.set("")
         self.var_student_name.set("")
         self.var_e_mail.set("")
         self.var_address.set("")
         self.var_gender1.set("")
         self.var_phone_no.set("")
         self.var_parent_no.set("")
         self.var_bod.set("")
         self.var_department.set("")
         self.var_course.set("")
         self.var_semester.set("")
         self.var_year.set("")
         self.var_photo.set("")

    def generate(self):
         print("hell")
         if self.var_student_id.get()=="" or self.var_student_name.get()=="":
              messagebox.showerror("error","Must be Fill all Fields")
         else:
              print("rushi")
              try:
                   connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
                   my_cousor=connection.cursor()
                   my_cousor.execute("select * from student")
                   result=my_cousor.fetchall()
                   id=self.var_student_id.get()
                   name=self.var_student_name.get()
                   my_cousor.execute("update student set student_name=%s,email=%s,address=%s,gender=%s,phone_no=%s,parent_no=%s,dob=%s,dept=%s,course=%s,semester=%s,year=%s,photo=%s where student_id=%s",(self.var_student_name.get(),self.var_e_mail.get(),self.var_address.get(),self.var_gender1.get(),self.var_phone_no.get(),self.var_parent_no.get(),self.var_bod.get(),self.var_department.get(),self.var_course.get(),self.var_semester.get(),self.var_year.get(),self.var_photo.get(),self.var_student_id.get()))
                   connection.commit()
                   self.show_data()
                   self.reset()
                   connection.close() 
               
                    
              

        
                   face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                   cap = cv2.VideoCapture(0)
                   if not cap.isOpened():
                     print("Error: Could not open camera.")
                     exit()
                   sample_count=0
                   while True:
                         ret, frame = cap.read()
                         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
                         for (x, y, w, h) in faces:
                              cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                              sample_count += 1
                              filepath="studentphoto/"+name+"."+str(id)+"."+str(sample_count)+".jpg"
                              cv2.imwrite(filepath,gray[y:y+h, x:x+w])
                              print(f"Collected {sample_count} face samples")
                              if sample_count >= 100:
                                   break
                         cv2.imshow('Camera', frame)
                         if cv2.waitKey(1) & 0xFF == ord('q') or sample_count >= 100:
                              break
                   cap.release()
                   cv2.destroyAllWindows()
                   messagebox.showinfo("massege","generated face complete")

                  
              except Exception as e:
                   messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)
    def search(self):
         try:
              connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
              my_curse=connection.cursor()
              my_curse.execute("select * from student where student_id=%s",(self.var_student_id.get()))
              connection.commit()
              self.data_feach()
              connection.close()
         except Exception as e:
              print(e)
                        

    

         


if __name__=="__main__":
    root=Tk()
    obj1=Student(root)
    root.mainloop()


