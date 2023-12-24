from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
from manager_paramtion import mg_parmation
from forgot_manager_id import forgot_id_mg
from forgot_manager_password import forgot_password_mg






class Manager:
    def __init__(self,top):
        self.top=top
        self.top.title("BANK")
        self.top.geometry('900x650+300+50')
        self.top.resizable(False, False)

        # ********************** variable **********************
        self.manager_id_get = StringVar()
        self.manager_password_get = StringVar()

        #******************** Title ********************
        self.tile=Label(self.top,text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"),  bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        self.tile.place(x=0, y=0, width=900, height=50)

        #******************* Frame ************************
        self.frame = Frame(self.top,bd=4,bg="#FF5F9E",relief=RIDGE)
        self.frame.place(x=0,y=50,width=900,height=599)

        #******************* Image *************************
        self.path = "I:/Code Run/Pycham/Bank/user1.png"
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.im1 = Label(self.frame, image=self.img)
        self.im1.place(x=450,y=280,height=30,width=30)

        self.path1 = "I:/Code Run/Pycham/Bank/lock1.png"
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        self.im11 = Label(self.frame, image=self.img1)
        self.im11.place(x=450,y=340,height=30,width=30)

        self.path2 = "I:/Code Run/Pycham/Bank/adminLogin1.png"
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        self.im12 = Label(self.frame, image=self.img2)
        self.im12.place(x=100, y=160,height=200,width=200)

        self.path3 = "I:/Code Run/Pycham/Bank/download.jpeg"
        self.img3 = ImageTk.PhotoImage(Image.open(self.path3))
        self.im13 = Label(self.frame, image=self.img3)
        self.im13.place(x=500, y=50,width=200,height=180)

        #**************** Entry column *********************
        self.id_et=ttk.Entry(self.frame,width=20,textvariable=self.manager_id_get, font=("time new roman", 14, "bold"))
        self.id_et.place(x=500,y=280)

        self.password_et = ttk.Entry(self.frame, width=20, textvariable=self.manager_password_get, font=("time new roman", 14, "bold"), show='*')
        self.password_et.place(x=500, y=340)

        #****************** Button **************************
        self.login_bt=Button(self.frame,text=" Login ",font=("arial",10,"bold"),bg="#C060A1",fg="#790252",command=self.login)
        self.login_bt.place(x=630,y=400,width=100,height=30)

        self.back_bt = Button(self.frame, text=" Back ", font=("arial", 15, "bold"), bg="black", fg="white",command=self.top.destroy)
        self.back_bt.place(x=50, y=500, width=100, height=40)

        self.forget_id_bt = Button(self.frame, text=" Forgot User Id ", font=("arial", 10, "bold"), bg="#C060A1",fg="#790252",command=self.forgot_id)
        self.forget_id_bt.place(x=450, y=470, width=125, height=20)

        self.forget_password_bt = Button(self.frame, text=" Forgot Password", font=("arial", 10, "bold"), bg="#C060A1",fg="#790252",command=self.forgot_password)
        self.forget_password_bt.place(x=600, y=470, width=140, height=20)

        #************************* Admain Lable ********************
        self.admin_lb=Label(self.frame,text="Admin Login",font=("time new roman", 14, "bold"),padx=40,pady=10)
        self.admin_lb.place(x=100,y=60)

        # ******************** data fetches ***********************
    def login(self):
        if self.manager_id_get.get() == "" or self.manager_password_get.get() == "":
            messagebox.showerror("Error", "Fields are Empty Column", parent=self.top)

        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from manager where User_Id='%s'") % (self.manager_id_get.get()))
                store_data = []
                store = cur.fetchone()
                for i in store:
                    store_data.append(i)
                self.id_fetch = store_data[0]
                self.password_fetch = store_data[1]


                db.commit()
                db.close()

                if self.manager_id_get.get() == self.id_fetch and self.manager_password_get.get() == self.password_fetch:
                    messagebox.showinfo("Successful", "Successful Login Admin", parent=self.top)
                    self.new_window = Toplevel(self.top)
                    self.app = mg_parmation(self.new_window)

                else:
                    messagebox.showerror("Error", " Password Wrong", parent=self.top)

            except Exception as es:
                messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)

    # ******************************** New window ***************************
    def forgot_id(self):
        self.new_window = Toplevel(self.top)
        self.app = forgot_id_mg(self.new_window)


    def forgot_password(self):
        self.new_window = Toplevel(self.top)
        self.app = forgot_password_mg(self.new_window)



if __name__ == '__main__':
    top=Tk()
    object=Manager(top)
    top.mainloop()


