from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from casedetails import case_details





class find_the_case:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x770+0+0")
        self.root.title("FIND THE CASE")
        img=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\ss.webp")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        flbl=Label(self.root,image=self.photoimg)
        flbl.place(x=0,y=0,width=500,height=130)
        
        img2=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\Untitled.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img2)

        flbl=Label(self.root,image=self.photoimg1)
        flbl.place(x=500,y=0,width=500,height=130)
        
        img1=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\case.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img1)

        flbl=Label(self.root,image=self.photoimg2)
        flbl.place(x=1000,y=0,width=550,height=130)
        
        img4=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\detect.jpeg")
        img4=img4.resize((1500,770),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bgd=Label(self.root,image=self.photoimg4)
        bgd.place(x=0,y=130,width=1500,height=770)

        title_lbl=Label(bgd,text="FIND THE CASE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)
        #case details
        img5=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\me2.webp")
        img5=img5.resize((400,270),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bgd,image=self.photoimg5,command=self.sandhani,cursor='HAND2')
        b1.place(x=100,y=100,width=220,height=220)
        
        b_11=Button(bgd,text="CASE DETAILS",command=self.sandhani,cursor='HAND2',font=("times new roman",17,"bold"),bg="BLACK",fg="red")
        b_11.place(x=100,y=300,width=220,height=40)

        #contact details

        img6=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\CONTACT.png")
        img6=img6.resize((300,270),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bgd,image=self.photoimg6,cursor='HAND2')
        b2.place(x=500,y=100,width=220,height=220)
        
        b_12=Button(bgd,text="CONTACT",cursor='HAND2',font=("times new roman",17,"bold"),bg="BLACK",fg="red")
        b_12.place(x=500,y=300,width=220,height=40)

        #FACE RECOGNIZATION
        
        img7=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\super-recognizer-test.webp")
        img7=img7.resize((300,270),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        

        b2=Button(bgd,image=self.photoimg7,cursor='HAND2')
        b2.place(x=900,y=100,width=220,height=220)
        
        b_13=Button(bgd,text="RECOGNIZE",cursor='HAND2',font=("times new roman",17,"bold"),bg="BLACK",fg="red")
        b_13.place(x=900,y=300,width=220,height=40)

        #recently visited places

        
        img8=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\images.jpeg")
        img8=img8.resize((300,270),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b2=Button(bgd,image=self.photoimg8,cursor='HAND2')
        b2.place(x=1200,y=100,width=220,height=220)
        
        b_14=Button(bgd,text="RECENTLY VISITED ",cursor='HAND2',font=("times new roman",15,"bold"),bg="BLACK",fg="red")
        b_14.place(x=1200,y=300,width=220,height=40)

        
        #social media

        
        img9=Image.open("C:\\Users\\SANDHANI\\Desktop\\PROJECT\\vapasa\\images\\media.jpg")
        img9=img9.resize((300,270),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b2=Button(bgd,image=self.photoimg9,cursor='HAND2')
        b2.place(x=100,y=360,width=220,height=220)
        
        b_14=Button(bgd,text="SOCIAL MEDIA ",cursor='HAND2',font=("times new roman",17,"bold"),bg="BLACK",fg="red")
        b_14.place(x=100,y=545,width=220,height=40)
        
    
   
        
    
    

    def sandhani(self):
        self.new_window=Toplevel(self.root)
        self.chinni=case_details(self.new_window)




        
if __name__ =="__main__":
    root=Tk()
    obj=find_the_case(root)
    root.mainloop()



