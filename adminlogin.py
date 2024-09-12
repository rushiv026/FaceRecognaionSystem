from tkinter  import *
from tkinter import  ttk
from PIL import Image,ImageTk
from studentform import Student
from teacherform import Teacher
class Admin:
    def __init__(self,root1):
        self.root1=root1
        self.root1.geometry("1290x790+0+0")#0 means  x,y axes
        self.root1.configure(bg='yellow')
        self.root1.title("Face Recognition System")
        self.text=Text
        frame=Frame(root1,bg="navy",borderwidth=6,relief=SUNKEN)
        frame.pack(side=TOP,fill="x")
        l=Label(frame,text="Admin Login Pannel",font="Monospace 50 bold",bg="navy",fg="red")
        l.pack(pady=20)

        # Student1=Image.open("./photos/stud.png")
        # resized_studentimage1= Student1.resize((320,320), Image.ADAPTIVE)
        # self.studnetphoto1=ImageTk.PhotoImage(resized_studentimage1)
        # b1_student1=Button(image=self.studnetphoto1,command=self.myname,cursor="hand2",border=8,bg="black")
        # b1_student1.place(x=150,y=200,width=320,height=320)
        # b2_student1=Button(root1,text="Student Attendance",command=self.myname,cursor="hand2",border=8,bg="black",fg="white")
        # b2_student1.place(x=150,y=520,width=320,height=50)

        

        # teacher_image1=Image.open("./photos/tech.jpeg")
        # resize_teacherimage1=teacher_image1.resize((320,320),Image.ADAPTIVE)
        # self.teacherphoto1=ImageTk.PhotoImage(resize_teacherimage1)
        # teacher_b1=Button(image=self.teacherphoto1,cursor="hand2",border=8,bg="black")
        # teacher_b1.place(x=650,y=200,width=320,height=320)
        # teacher_b2=Button(root1,text="Teacher Attendance",cursor="hand2",border=8,bg="black",fg="white")
        # teacher_b2.place(x=650,y=520,width=320,height=50)
        
        # frame1=Frame(root1,bg="navy",borderwidth=6,relief=SUNKEN)
        # frame1.place(x=0,y=30,width=1200,height=700)
        frame_2=Frame(root1,bg="cyan",borderwidth=8,relief=SUNKEN,highlightbackground="blue")
        frame_2.place(x=0,y=130,width=1290,height=900)
        
        Student1=Image.open("./photos/stud.png")
        resized_studentimage1= Student1.resize((320,320), Image.ADAPTIVE)
        self.studnetphoto1=ImageTk.PhotoImage(resized_studentimage1)
        
        frame_21=Frame(frame_2,borderwidth=8,relief=SUNKEN,highlightbackground="blue")
        frame_21.place(x=200,y=150,width=320,height=320)
        l=Label(frame_21,image=self.studnetphoto1)
        l.place(x=0,y=0,width=320,height=320)
        b2_student1=Button(frame_2,text="Student Attendance",command=self.myname,cursor="hand2",border=8,bg="black",fg="white")
        b2_student1.place(x=200,y=470,width=320,height=50)

        teacher_image1=Image.open("./photos/tech.jpeg")
        resize_teacherimage1=teacher_image1.resize((320,320),Image.ADAPTIVE)
        self.teacherphoto1=ImageTk.PhotoImage(resize_teacherimage1)
        frame_2=Frame(frame_2,borderwidth=8,relief=SUNKEN,highlightbackground="blue")
        frame_2.place(x=750,y=150,width=320,height=320)
        l2=Label(frame_2,image=self.teacherphoto1)
        l2.place(x=0,y=0,width=320,height=320)
        teacher_b2=Button(root1,text="Teacher Attendance",command=self.myname2,cursor="hand2",border=8,bg="black",fg="white")
        teacher_b2.place(x=757,y=607,width=320,height=50)
        


        # l1=Label(frame,text="Admin Login Pannel",font="Monospace 50 bold",bg="navy",fg="red")
        # l1.pack(pady=20)
    def myname(self):
         self.new_window2=Toplevel(self.root1)
         self.admin22=Student(self.new_window2)
    def myname2(self):
         self.new_window3=Toplevel(self.root1)
         self.admin23=Teacher(self.new_window3)
    def exit(self):
        root1.destroy()
         

if __name__=="__main__":    
    root1=Tk()
    obj1=Admin(root1)
    root1.mainloop()
  #  root1.destroy()