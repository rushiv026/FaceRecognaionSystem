from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
from adminlogin import Admin

class Login1:
    def __init__(self,login):
        self.login=login
        self.login.geometry("1290x790+0+0")#0 means  x,y axes
        self.login.configure(bg="white")
        self.login.title("Face Recognition System")
        frame=Frame(login,width=250,height=350,bg='white',highlightbackground="blue", highlightthickness=2)
        frame.place(x=580,y=100,width=500,height=500)
        f=Frame(login,width=380,height=380,bg="black")
        f.place(x=60,y=100)
        adminphoto=Image.open("./photos/admin.jpeg")
        admin_image_resize=adminphoto.resize((380,380),Image.ADAPTIVE)
        self.admin=ImageTk.PhotoImage(admin_image_resize)
        l1=Label(f,image=self.admin)
        l1.place(x=0,y=0,width=380,height=380)
        

        heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',50,'bold'))
        heading.place(x=130,y=15)
        b1=Button(frame,text='sign in',bg='#57a1f8',fg='white',border=1,command=self.signin,font=('Microsoft YaHei UI Light',14,'bold'))
        b1.place(x=110,y=310,width=260,height=30)
        # admin_b2=Button(root,text="Admin Login",command=self.adminform,cursor="hand2",border=8,bg="black",fg="white")
        label=Label(frame,text="Don't have account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=75,y=570)

        # sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',)
        # sign_up.place(x=200,y=570)

        

       
        self.user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        self.user.insert(0,'Username')
        self.user.place(x=100,y=180)
        self.user.bind('<FocusIn>',self.on_enter)
        self.user.bind('<FocusOut>',self.on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=95,y=207)

        self.code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        self.code.place(x=100,y=250)
        self.code.insert(0,'Password')
        self.code.bind('<FocusIn>',self.on_enter1)
        self.code.bind('<FocusOut>',self.on_leave1)
        Frame(frame,width=295,height=2,bg='black').place(x=95,y=277)

    def signin(self):
      username=self.user.get()
      password=self.code.get()
    
      if username=="Admin" and password=="1234":
         self.new_window=Toplevel(self.login)
         self.admin22=Admin(self.new_window)
       
      elif username!='Admin' and password!='1234':
          messagebox.showerror("Invalid","Invalid Username and Password",parent=self.login)
      elif password!='1234':
          messagebox.showerror("Invalid","Invalid Password",parent=self.login)
      elif username!='Admin':
          messagebox.showerror("Invalid","Invalid Username",parent=self.login)
    def on_enter(self):
        (self.user).delete(0,'end')
        print("10")
    def on_leave(self):
        name=(self.user).get()
        if name=="":
            (self.user).insert(0,"Username")

    def on_enter1(self):
        (self.code).delete(0,'end')

    def on_leave1(self):
        name=(self.code).get()
        if name=="":
            (self.code).insert(0,"Password")
    


if __name__=="__main__":
    login=Tk()
    obj=Login1(login)
    login.mainloop()
