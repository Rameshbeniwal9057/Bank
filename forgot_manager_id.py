from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql as sql

class forgot_id_mg:
    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('700x565+450+100')
        self.top.resizable(False, False)

        # ********************** variable **********************

        self.mg_id = StringVar()
        self.mobile_no = StringVar()

        #*************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=700, height=50)


        # **********************MAIN FRAME***********************
        main_frame = Frame(self.top, bd=4,bg="#F73D93", relief=RIDGE)
        main_frame.place(x=0, y=100, width=698, height=465)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA FORGOT ID", font=("time new roman", 11, "bold"),bg='#A91079',fg="#070A52",bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=698, height=50)

        # **********************Data FRAME ***********************
        self.data_frame = Frame(main_frame, bd=5, relief=RIDGE,bg='#A91079')
        self.data_frame.place(x=45, y=250, width=600, height=100)



        # *********************** Account Entry *********************
        lbl_email = Label(main_frame, text=" Email Id : ", font=("time new roman", 14, "bold"), bg="#F73D93",
                               padx=10, pady=10)
        lbl_email.grid(row=0, column=0, sticky=W)

        entry_email_et = ttk.Entry(main_frame, width=25, textvariable=self.mg_id,
                                     font=("time new roman", 14, "bold"))
        entry_email_et.grid(row=0, column=1)

        lbl_mobile_no = Label(main_frame, text=" Mobile No : ", font=("time new roman", 14, "bold"), bg="#F73D93",
                              padx=10, pady=10)
        lbl_mobile_no.grid(row=1, column=0, sticky=W)

        entry_mobile_no = ttk.Entry(main_frame, width=25, textvariable=self.mobile_no,
                                    font=("time new roman", 14, "bold"))
        entry_mobile_no.grid(row=1, column=1)



        # ******************** Main Frame  Button **********************

        button_submit = Button(main_frame, text=" Submit ", font=("arial", 10, "bold"), bg="#576CBC", fg="#3A1078",activebackground="#4E31AA",padx=40, pady=1,command=self.show)
        button_submit.place(x=180, y=130)

        button_back = Button(self.top, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="white",padx=40, pady=1, command=self.top.destroy)
        button_back.place(x=50, y=510)

        # ******************** data fetches ***********************

    def show(self):
        if self.mg_id.get() == "":
            messagebox.showerror("Error", "Fields are Empty Column", parent=self.top)
        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from manager where Email='%s'") % (self.mg_id.get()))
                store = cur.fetchone()
                sore_data=[]
                for i in store:
                    sore_data.append(i)

                self.email=str(sore_data[3])
                self.mobile=str(sore_data[2])

                if self.email == self.mg_id.get() and self.mobile == self.mobile_no.get():
                    messagebox.showinfo("Success", "Successful", parent=self.top)

                    # ************************* id Lable ********************
                    self.admin = Label(self.data_frame, text="User id : ", font=("time new roman", 14, "bold"))
                    self.admin.place(x=200, y=35)

                    self.admin = Label(self.data_frame, text=sore_data[0], font=("time new roman", 14, "bold"))
                    self.admin.place(x=280, y=35)

                else:
                    messagebox.showerror("Error", "Wrong Mobile Number ", parent=self.top)


                db.commit()
                db.close()


            except Exception as es:
                messagebox.showerror("Error",f"Account_No wrong:{str(es)}",parent=self.top)


if __name__ == '__main__':
    top=Tk()
    obj=forgot_id_mg(top)

    top.mainloop()