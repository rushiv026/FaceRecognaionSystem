import cv2
import mysql.connector
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button

class Face:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='black')

        Student = Image.open("./photos/student.jpg")
        resized_studentimage = Student.resize((650, 700), Image.ADAPTIVE)
        self.studentphoto = ImageTk.PhotoImage(resized_studentimage)
        f = Label(self.root, image=self.studentphoto)
        f.place(x=0, y=55, width=650, height=700)

        Student1 = Image.open("./photos/image2.jpg")
        resized_studentimage1 = Student1.resize((650, 700), Image.ADAPTIVE)
        self.studentphoto1 = ImageTk.PhotoImage(resized_studentimage1)
        f1 = Label(self.root, image=self.studentphoto1)
        f1.place(x=650, y=55, width=650, height=700)

        b = Button(f1, text="Face Recognition", command=self.face_recognition, cursor="hand2", border=8, bg="black", fg="white")
        b.place(x=350, y=500, width=200, height=40)

    def face_recognition(self):
        def draw(img, classifier, scalefactor, minneighbors, color, text, clf):
            greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            feature = classifier.detectMultiScale(greyimg, scalefactor, minneighbors)
            cordinate = []
            for (x, y, w, h) in feature:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(greyimg[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                connection=mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition_system")
                my_curse = connection.cursor()
                my_curse.execute("SELECT teacher_name FROM teacher WHERE teacher_id=" + str(id))
                feach = my_curse.fetchone()
                feach = "+".join(feach)

                my_curse.execute("SELECT department FROM teacher WHERE teacher_id=" + str(id))
                feach1 = my_curse.fetchone()
                feach1 = "+".join(feach1)
                    
                if confidence > 77:
                    cv2.putText(img, f"Name: {feach}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                    cv2.putText(img, f"Department: {feach1}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                cordinate = [x, y, w, h]
            return cordinate

        def recognize(img, clf, facecascade):
            cordinate = draw(img, facecascade, 1.1, 10, (255, 25, 255), "face", clf)
            return img

        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("trainnerdata.xml")
        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img1 = recognize(img, clf, face_classifier)
            cv2.imshow("Welcome Teachers", img1)
            if cv2.waitKey(1) == 13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face(root)
    root.mainloop()
