from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql




class forgot_password_us:
    def __init__(self,top):

        self.top = top
        self.top.title('BANK')
        self.top.geometry('800x515+400+100')
        self.top.resizable(False, False)

        # ********************** variable **********************
        self.password = StringVar()
        self.confrom_password = StringVar()

        self.user_id = StringVar()



        #*************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=800, height=50)


        # **********************MAIN FRAME***********************
        main_frame = Frame(self.top, bd=4,bg='#46C2CB', relief=RIDGE)
        main_frame.place(x=0, y=100, width=798, height=415)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA WITHDRAWAL AMOUNT", font=("time new roman", 10, "bold"),bg="#A3C7D6", fg="#A91079",
                          bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=798, height=50)

        # **********************Data FRAME ***********************
        self.data_frame = Frame(main_frame, bd=5, relief=RIDGE,bg='#46C2CB')
        self.data_frame.place(x=0, y=0, width=791, height=300)

        # ************************* password Lable ********************
        self.lbl_acc2_no = Label(self.data_frame, text="User Id :", font=("time new roman", 14, "bold"),bg='#46C2CB', padx=10, pady=10)
        self.lbl_acc2_no.grid(row=0, column=0, sticky=W)

        self.admin = Label(self.data_frame, text="Password : ", font=("time new roman", 14, "bold"),bg='#46C2CB')
        self.admin.grid(row=1, column=0, sticky=W)

        self.admin = Label(self.data_frame, text="Confirm Password : ", font=("time new roman", 14, "bold"),bg='#46C2CB',padx=0, pady=10)
        self.admin.grid(row=2, column=0, sticky=W)

        # *********************** Entry *********************


        self.entry_user_id = ttk.Entry(self.data_frame, width=30, textvariable=self.user_id,font=("time new roman", 14, "bold"))
        self.entry_user_id.grid(row=0, column=1)

        self.password_e = ttk.Entry(self.data_frame, width=30, textvariable=self.password, font=("time new roman", 14, "bold"))
        self.password_e.grid(row=1, column=1)

        self.entry_password = ttk.Entry(self.data_frame, width=30, textvariable=self.confrom_password,font=("time new roman", 14, "bold"))
        self.entry_password.grid(row=2, column=1)



        # ******************** Main Frame  Button **********************

        button_submit = Button(self.data_frame, text=" Submit ", font=("arial", 10, "bold"), bg="#E7AB79", fg="black",padx=40, pady=1,command=self.password_us)
        button_submit.place(x=280, y=200)


        button_back = Button(self.top, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="white",padx=40, pady=1, command=self.top.destroy)
        button_back.place(x=50, y=460)


    def password_us(self):
        if self.password.get() == "" or self.confrom_password.get() == "" or self.user_id.get() == "":
            messagebox.showerror("Error", "Fields are required", parent=self.top)
        else:
            if self.password.get() == self.confrom_password.get() :
                try:
                    db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                    cur = db.cursor()
                    cur.execute(("select *from app where User_Id='%s'") % (self.user_id.get()))
                    store = cur.fetchone()
                    store_data = []
                    for i in store:
                        store_data.append(i)
                    self.id=store_data[4]

                    db.commit()
                    db.close()

                    if self.id == self.user_id.get():
                        print(1)
                        db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                        cur = db.cursor()
                        cur.execute(("update app set Password = %s where User_Id='%s'") % (self.password.get(), self.user_id.get()))
                        db.commit()
                        db.close()
                        messagebox.showinfo("Success", "successful Change", parent=self.top)
                    else:
                        messagebox.showerror("Error", "User Id Rong", parent=self.top)
                except Exception as es:
                    messagebox.showerror("Error", f"Some thing went wrong:{str(es)}", parent=self.top)
            else:
                messagebox.showerror("Error", "No Match Password", parent=self.top)


if __name__ == '__main__':
    top=Tk()
    obj=forgot_password_us(top)

    top.mainloop()