from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
class Traindata:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("Train Data")
        b=Button(root,text="train data Teacher",command=self.train_data,width=18,font=("times new roman",20,"bold"),bg="black",fg="white")
        b.pack()

        b = Button(root, text="Train Data Student", command=self.train_data2, cursor="hand2", border=8, bg="black", fg="white")
        b.place(x=350, y=500, width=200, height=40)
    def train_data(self):
        data_dir=("imgdata")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
             


            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("trainng",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("trainnerdata.xml")
        cv2.destroyAllWindows()
        messagebox.INFO("result","data train successfully")

    def train_data2(self):
        data_dir=("studentphoto")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
             


            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("trainng",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("trainnerdata_student.xml")
        cv2.destroyAllWindows()
        messagebox.INFO("result","data train successfully")




if __name__=="__main__":
    root=Tk()
    obj1=Traindata(root)
    root.mainloop()

