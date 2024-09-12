from tkinter  import *
from tkinter import  ttk
from PIL import Image,ImageTk
from login1 import Login1
from Face_Recognition_teacher import Face
from Face_Recognition_student import Face_Student
class facedetection:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1290x790+0+0")#0 means  x,y axes
        self.root.configure(bg="yellow")
        self.root.title("Face Recognition System")
        self.text=Text
        frame=Frame(root,bg="navy",borderwidth=6,relief=SUNKEN)
        frame.pack(side=TOP,fill="x")
        l=Label(frame,text="Welcome Attendance System",font="Monospace 50 bold",bg="navy",fg="red")
        l.pack(pady=20)

        Student=Image.open("./photos/student.jpg")
        resized_studentimage= Student.resize((220,220), Image.ADAPTIVE)
        self.studnetphoto=ImageTk.PhotoImage(resized_studentimage)
        b1_student=Button(image=self.studnetphoto,cursor="hand2",border=8,bg="black")
        b1_student.place(x=150,y=200,width=220,height=220)
        b2_student=Button(root,text="Student Attendance",command=self.Studentdemo,cursor="hand2",border=8,bg="black",fg="white")
        b2_student.place(x=150,y=420,width=220,height=50)

        

        teacher_image=Image.open("./photos/teacher.jpeg")
        resize_teacherimage=teacher_image.resize((220,220),Image.ADAPTIVE)
        self.teacherphoto=ImageTk.PhotoImage(resize_teacherimage)
        teacher_b=Button(image=self.teacherphoto,command=self.Teacherdemo,cursor="hand2",border=8,bg="black")
        teacher_b.place(x=500,y=200,width=220,height=220)
        teacher_b2=Button(root,text="Teacher Attendance",command=self.Teacherdemo,cursor="hand2",border=8,bg="black",fg="white")
        teacher_b2.place(x=500,y=420,width=220,height=50)
        

        admin=Image.open("./photos/admin.jpeg")
        admin_image_resize=admin.resize((220,220),Image.ADAPTIVE)
        self.admin=ImageTk.PhotoImage(admin_image_resize)
        admin_button=Button(image=self.admin,command=self.adminform,cursor="hand2",border=8,bg="black")
        admin_button.place(x=850,y=200,width=220,height=220)
        admin_b2=Button(root,text="Admin Login",command=self.adminform,cursor="hand2",border=8,bg="black",fg="white")
       # admin_b2.bind("<Button>",command=lambda e:loginpage(root))
        admin_b2.place(x=850,y=420,width=220,height=50)


    def adminform(self):
        self.new_window=Toplevel(self.root)
        self.admin22=Login1(self.new_window)   
    def Teacherdemo(self):
        self.new_window1=Toplevel(self.root)
        self.teacher=Face(self.new_window1) 
    def Studentdemo(self):
        self.new_window2=Toplevel(self.root)
        self.student=Face_Student(self.new_window2) 
if __name__=="__main__":        
    root=Tk()
    obj=facedetection(root)
    root.mainloop()