from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
class Teacher:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1290x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='black')
        frame=Frame(root,bg="navy",borderwidth=6,relief=SUNKEN)
        frame.place(x=0,y=0,width=1265,height=120)
        frame.pack(fill="x")
#"student_id","student_name","e_mail","gender","phone_no","parent_no","dob","address","photo","department","course","semester","year"
        self.var_teacher_id=StringVar()
        self.var_teacher_name=StringVar()
        self.var_e_mail=StringVar()
        self.var_gender=StringVar()
        self.var_account=StringVar()
        self.var_phone_no=StringVar()
        self.var_bod=StringVar()
        self.var_address=StringVar()
        self.var_photo=StringVar()
        self.var_department=StringVar()
        self.var_quali=StringVar()


        l=Label(frame,text="Teacher Details",font="Monospace 50 bold",bg="navy",fg="red")
        l.pack(pady=20)
        frame_2=Frame(root,bg="cyan",borderwidth=8,relief=SUNKEN,highlightbackground="blue")
        frame_2.place(x=0,y=138,width=1285,height=900)
        # frame_2.pack(fill="x")
        l_frame=LabelFrame(frame_2,bd=5,bg="white",relief="ridge",text="Teacher Details",font=("times new roman",12,"bold"))
        l_frame.place(x=10,y=7,width=615,height=580)

        studid=Label(l_frame,text="Teacher Id:",font=("times new roman",12,"bold"),bg="white")
        studid.grid(row=0,column=0,padx=10)

        studid_entry=ttk.Entry(l_frame,textvariable=self.var_teacher_id,width=20,font=("times new roman",12,"bold"))
        studid_entry.grid(row=0,column=1,padx=10,sticky=W)


        studname=Label(l_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        studname.grid(row=1,column=0,padx=10)

        studename_entry=ttk.Entry(l_frame,textvariable=self.var_teacher_name,width=20,font=("times new roman",12,"bold"))
        studename_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        email=Label(l_frame,text="E-Mail:",font=("times new roman",12,"bold"),bg="white")
        email.grid(row=2,column=0,padx=10)

        email_entry=ttk.Entry(l_frame,textvariable=self.var_e_mail,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=10)
        
        ac_no=Label(l_frame,text="Account No:",font=("times new roman",12,"bold"),bg="white")
        ac_no.grid(row=3,column=0,padx=5)

        ac_no_entry=ttk.Entry(l_frame,textvariable=self.var_account,width=20,font=("times new roman",12,"bold"))
        ac_no_entry.grid(row=3,column=1,padx=10,pady=10)

        gender=Label(l_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender.grid(row=4,column=0)

        # gen=ttk.Radiobutton(c_frame,text="Male")
        # gen.grid(row=3,column=1,padx=10,pady=10)W

        # gender_entry=ttk.Entry(c_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=4,column=1,padx=10,pady=10)
       
        rd1=ttk.Radiobutton(l_frame,text="Male",variable=self.var_gender,value="Male")
        rd1.grid(row=4,column=1)
        rd2=ttk.Radiobutton(l_frame,text="Female",variable=self.var_gender,value="Female")
        rd2.grid(row=4,column=2)
        

        add=Label(l_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        add.grid(row=5,column=0,padx=10)

        add_entry=ttk.Entry(l_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=5,column=1,padx=10,pady=10)


        phone_no=Label(l_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_no.grid(row=6,column=0,padx=5)

        phone_no_entry=ttk.Entry(l_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=6,column=1,padx=10,pady=10)

        
        dob=Label(l_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob.grid(row=7,column=0,padx=5)

        dob_entry=ttk.Entry(l_frame,textvariable=self.var_bod,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=7,column=1,padx=10,pady=10)

        # photo=Button(c_frame,text="Take Photo",font=("times new roman",8,"bold"),bg="black",fg="white")
        # photo.grid(row=3,column=3,padx=10,pady=10)
        photo=Label(l_frame,text="Take Photo:",font=("times new roman",12,"bold"),bg="white")
        photo.grid(row=8,column=0,padx=5)
        rd1=ttk.Radiobutton(l_frame,text="yes photo",variable=self.var_photo,value="yes")
        rd1.grid(row=8,column=1)
        rd2=ttk.Radiobutton(l_frame,text="No photo",variable=self.var_photo,value="no")
        rd2.grid(row=8,column=2)

        photosample=Button(l_frame,text="photo collect",command=self.generate,font=("times new roman",12,"bold"),bg="black",fg="white")
        photosample.grid(row=8,column=3,pady=10)

        dept=Label(l_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dept.grid(row=9,column=0,padx=10)

        dept_combobox=ttk.Combobox(l_frame,textvariable=self.var_department,font=("times new roman",12,"bold"),state="   readonly")
        dept_combobox["values"]=("Select Department","Computer Science","Physic","Chemistry","Biology","Zoology","Mathamatics","Statistics")
        dept_combobox.current(0)
        dept_combobox.grid(row=9,column=1,padx=2,pady=10,sticky=W)

        quali=Label(l_frame,text="Qualification:",font=("times new roman",12,"bold"),bg="white")
        quali.grid(row=9,column=2,padx=10)

        quali_combobox=ttk.Combobox(l_frame,textvariable=self.var_quali,font=("times new roman",12,"bold"),state="   readonly")
        quali_combobox["values"]=("Select Course","Msc CS","Msc CHEM","Msc BIO","Msc ZOO","Msc MATH","Msc STAT")
        quali_combobox.current(0)
        quali_combobox.grid(row=9,column=3,sticky=W)


        
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

        
        searchby=Label(rc_frame,text="Teacher Id:",font=("times new roman",12,"bold"),bg="white")
        searchby.grid(row=0,column=0,padx=10)

        searchentry=ttk.Entry(rc_frame,textvariable=self.var_teacher_id,width=20,font=("times new roman",12,"bold"))
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
        self.teacher_table=ttk.Treeview(rc1_frame,columns=("teacher_id","teacher_name","e_mail","ac_no","gender","address","phone_no","dob","quali","department","photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side="bottom",fill=X)
        scroll_y.pack(side="right",fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table.heading("teacher_id",text="Teacher Id")
        self.teacher_table.heading("teacher_name",text="Teacher Name")
        self.teacher_table.heading("e_mail",text="E-Mail")
        self.teacher_table.heading("ac_no",text="Account No")
        self.teacher_table.heading("gender",text="Gender")
        self.teacher_table.heading("address",text="Address")
        self.teacher_table.heading("phone_no",text="Phone No")
        self.teacher_table.heading("dob",text="DOB")
        self.teacher_table.heading("quali",text="Qualification")
        self.teacher_table.heading("department",text="Department")
        self.teacher_table.heading("photo",text="Photo")
        self.teacher_table["show"]="headings"

        self.teacher_table.column("teacher_name",width=140)
        self.teacher_table.column("teacher_id",width=140)
        self.teacher_table.column("e_mail",width=140)
        self.teacher_table.column("ac_no",width=140)
        self.teacher_table.column("gender",width=140)
        self.teacher_table.column("address",width=140)
        self.teacher_table.column("phone_no",width=140)
        self.teacher_table.column("dob",width=140)
        self.teacher_table.column("quali",width=140)
        self.teacher_table.column("department",width=140)
        self.teacher_table.column("photo",width=140)
    
        self.teacher_table.pack(fill=BOTH,expand=1)
        self.teacher_table.bind("<ButtonRelease>",self.data_fill)
        self.show_data()
    def data_feach(self):
        
        if self.var_teacher_name.get()=="":
            messagebox.showerror("Invalid","fill all fields",parent=self.root)
        else:
                try:
                    connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
                    print(connection)
                    my_curse=connection.cursor()
                  
                    my_curse.execute("insert into teacher values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_teacher_id.get(),self.var_teacher_name.get(),self.var_e_mail.get(),self.var_account.get(),self.var_gender.get(),self.var_address.get(),self.var_phone_no.get(),self.var_bod.get(),self.var_quali.get(),self.var_department.get(),self.var_photo.get()))
                    connection.commit()
                    self.show_data()
                    connection.close()
                    print(my_curse)
                    messagebox.showinfo("sucess","Teacher details added successfully",parent=self.root)
                except Exception as e:
                    
                     messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)

    def show_data(self):
         try:
              connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
              my_curse=connection.cursor()
              my_curse.execute("select * from teacher")
              #store all data in temp vairable
              d=my_curse.fetchall()
              if len(d)!=0:
                   self.teacher_table.delete(*self.teacher_table.get_children())
                   for i in d:
                        self.teacher_table.insert("",END,values=i)
                        connection.commit()
                   connection.close()
         except Exception as e:
              print(e)
    def search_data(self):
         try:
              connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
              my_curse=connection.cursor()
              my_curse.execute("select * from teacher where teacher_id=%s",(self.var_teacher_id.get()))
              #store all data in temp vairable
              d=my_curse.fetchall()
              if len(d)!=0:
                   self.teacher_table.delete(*self.teacher_table.get_children())
                   for i in d:
                        self.teacher_table.insert("",END,values=i)
                        connection.commit()
                   connection.close()
         except Exception as e:
              print(e)
    def data_fill(self,event=""):
            select_i=self.teacher_table.focus()
            content=self.teacher_table.item(select_i)
            data=content["values"]  

            self.var_teacher_id.set(data[0])
            self.var_teacher_name.set(data[1])
            self.var_e_mail.set(data[2])
            self.var_account.set(data[3])
            self.var_gender.set(data[4])
            self.var_address.set(data[5])
            self.var_phone_no.set(data[6])
            self.var_bod.set(data[7])
            self.var_quali.set(data[8])
            self.var_department.set(data[9])
            self.var_photo.set(data[10])

    def update_details(self):
         try:
              
              #update=messagebox.showinfo("update","due you want Upadate Deatail",parent=self.root)
              connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
              my_cousor=connection.cursor()
              my_cousor.execute("update teacher set teacher_name=%s,e_mail=%s,ac_no=%s,gender=%s,address=%s,phone_no=%s,dob=%s,quali=%s,department=%s,photo=%s where teacher_id=%s",(self.var_teacher_name.get(),self.var_e_mail.get(),self.var_account.get(),self.var_gender.get(),self.var_address.get(),self.var_phone_no.get(),self.var_bod.get(),self.var_quali.get(),self.var_department.get(),self.var_photo.get(),self.var_teacher_id.get()))
              messagebox.showinfo("sucess","update sucessfully",parent=self.root) 
              connection.commit()
              self.show_data()
              connection.close()
             
               
         except Exception as e:
              messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)                
     

    def delete_data(self):
         if self.var_teacher_id.get()=="":
              messagebox.showerror("error","teacher id must be require",parent=self.root)
         else:
              try:
                   messagebox.showinfo("confirm","due you want delete")
                   connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
                   my_cursor=connection.cursor()
                   a=("delete from teacher where teacher_id=%s")
                   b=(self.var_teacher_id.get(),)
                   my_cursor.execute(a,b)
                   connection.commit()
                   self.show_data()
                   connection.close()
              
              except Exception as e:
                   messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)

    def reset(self):
         self.var_teacher_id.set("")
         self.var_teacher_name.set("")
         self.var_e_mail.set("")
         self.var_account.set("")
         self.var_gender.set("")
         self.var_address.set("")
         self.var_phone_no.set("")
         self.var_bod.set("")
         self.var_quali.set("select qualification")
         self.var_department.set("select department")
         self.var_photo.set("")    

#collect photo sample
    def generate(self):
         print("hell")
         if self.var_teacher_id.get()=="" or self.var_teacher_name.get()=="":
              messagebox.showerror("error","Must be Fill all Fields")
         else:
              print("rushi")
              try:
                   connection=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
                   my_cousor=connection.cursor()
                   my_cousor.execute("select * from teacher")
                   result=my_cousor.fetchall()
                   id=self.var_teacher_id.get()
                   name=self.var_teacher_name.get()
                   my_cousor.execute("update teacher set teacher_name=%s,e_mail=%s,ac_no=%s,gender=%s,address=%s,phone_no=%s,dob=%s,quali=%s,department=%s,photo=%s where teacher_id=%s",(self.var_teacher_name.get(),self.var_e_mail.get(),self.var_account.get(),self.var_gender.get(),self.var_address.get(),self.var_phone_no.get(),self.var_bod.get(),self.var_quali.get(),self.var_department.get(),self.var_photo.get(),self.var_teacher_id.get()))
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
                              filepath="imgdata/"+name+"."+str(id)+"."+str(sample_count)+".jpg"
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
              my_curse.execute("select * from teacher where teacher_id=%s",(self.var_teacher_id.get()))
              connection.commit()
              self.search_data()
              connection.close()
         except Exception as e:
              print(e)
                        

    

         


if __name__=="__main__":
    root=Tk()
    obj1=Teacher(root)
    root.mainloop()


