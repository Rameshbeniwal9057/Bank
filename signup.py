from tkinter import *
from tkinter import ttk
import pymysql as sql
from tkinter import messagebox

class App:
    def __init__(self,top):
        self.top=top
        self.top.title("BANK")
        self.top.geometry('900x600+300+100')
        self.top.resizable(False, False)

        # ********************** variable **********************
        self.fist_name=StringVar()
        self.last_name = StringVar()
        self.mobile_no = StringVar()
        self.account_no = StringVar()
        self.password_n = StringVar()
        self.password_cn = StringVar()
        self.user_id = StringVar()

        # *************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=900, height=50)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA SIGNUP", font=("time new roman", 10, "bold"),
                          bg='#BA55D3', fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=900, height=50)

        # ******************* Frame ************************
        self.frame = Frame(self.top, bd=4,bg='#1E90FF', relief=RIDGE, )
        self.frame.place(x=0, y=100, width=900, height=500)

        # First Name
        lbl_name = Label(self.frame, text="First Name :", font=("time new roman", 14, "bold"),bg='#1E90FF', padx=40, pady=10)
        lbl_name.grid(row=0, column=0, sticky=W)

        entry_f_name = ttk.Entry(self.frame, width=30, textvariable=self.fist_name, font=("time new roman", 14, "bold"))
        entry_f_name.grid(row=0, column=1)

        # Last Name
        lbl_name = Label(self.frame, text="Last Name :", font=("time new roman", 14, "bold"),bg='#1E90FF', padx=40, pady=10)
        lbl_name.grid(row=1, column=0, sticky=W)

        entry_name = ttk.Entry(self.frame, width=30, textvariable=self.last_name, font=("time new roman", 14, "bold"))
        entry_name.grid(row=1, column=1)

        # Mobile No
        lbl_name = Label(self.frame, text="Mobile Number :", font=("time new roman", 14, "bold"),bg='#1E90FF', padx=40, pady=10)
        lbl_name.grid(row=2, column=0, sticky=W)

        entry_name = ttk.Entry(self.frame, width=30, textvariable=self.mobile_no, font=("time new roman", 14, "bold"))
        entry_name.grid(row=2, column=1)

        # Account No
        lbl_name = Label(self.frame, text="Account NO :", font=("time new roman", 14, "bold"),bg='#1E90FF', padx=40, pady=10)
        lbl_name.grid(row=3, column=0, sticky=W)

        entry_name51 = ttk.Entry(self.frame, width=30, textvariable=self.account_no, font=("arial", 14, "bold"))
        entry_name51.grid(row=3, column=1)

        # user id
        lbl_id = Label(self.frame, text="User Id :", font=("time new roman", 14, "bold"),bg='#1E90FF', padx=40, pady=10)
        lbl_id.grid(row=4, column=0, sticky=W)

        entry_name51 = ttk.Entry(self.frame, width=30, textvariable=self.user_id, font=("arial", 14, "bold"))
        entry_name51.grid(row=4, column=1)

        # password
        lbl_name_am = Label(self.frame, text="Password :", font=("time new roman", 14, "bold"),bg='#1E90FF', padx=40, pady=10)
        lbl_name_am.grid(row=5, column=0, sticky=W)

        entry_name_am = ttk.Entry(self.frame, width=30, textvariable=self.password_n, font=("arial", 14, "bold"))
        entry_name_am.grid(row=5, column=1)

        lbl_name_am = Label(self.frame, text="Confirm  Password :", font=("time new roman", 14, "bold"),bg='#1E90FF', padx=40, pady=10)
        lbl_name_am.grid(row=6, column=0, sticky=W)

        entry_name_am = ttk.Entry(self.frame, width=30, textvariable=self.password_cn, font=("arial", 14, "bold"))
        entry_name_am.grid(row=6, column=1)

        # ******************** Button **********************
        button_submit = Button(self.frame, text=" Submit ", font=("arial", 15, "bold"), bg="#32CD32", fg="black",command=self.app)
        button_submit.place(x=300, y=350, width=150, height=50)

        button_back = Button(self.frame, text=" Back ", font=("arial", 15, "bold"), bg="black", fg="white",command=self.top.destroy)
        button_back.place(x=30, y=450, width=150, height=35)

    #******************************************* data insert ******************************************************

    def app(self):
        if self.fist_name.get() == "" or self.last_name.get() == "" or self.mobile_no.get() == "" or self.account_no.get() == "" or self.password_n.get() == "" or self.password_cn.get() == "" :
            messagebox.showerror("Error", "Fields are Empty Column", parent=self.top)
        else:
            if self.password_n.get() == self.password_cn.get():
                try:
                    db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                    cur = db.cursor()
                    cur.execute(("select *from bank where Account_No=%s") % (self.account_no.get()))
                    store = cur.fetchone()
                    man_data_st = []
                    for i in store:
                        man_data_st.append(i)

                    self.account_no_fath=str(man_data_st[0])
                    self.fist_name_fath=str(man_data_st[1])
                    self.last_name_fath=str(man_data_st[2])
                    self.mobile_no_fath=str(man_data_st[6])

                    db.commit()

                    db.close()

                    if self.account_no_fath == self.account_no.get() and self.mobile_no_fath == self.mobile_no.get() and self.fist_name_fath == self.fist_name.get() and self.last_name_fath == self.last_name.get():
                        db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                        cur = db.cursor()

                        cur.execute("insert into app values(%s,%s,%s,%s,%s,%s)", (self.account_no.get(),self.fist_name.get(),self.last_name.get(),self.mobile_no.get(),self.user_id.get(),self.password_n.get()))
                        db.commit()

                        db.close()
                        messagebox.showinfo("Success", "Successful", parent=self.top)
                    else:
                        messagebox.showerror("Error", "Enter your account details", parent=self.top)


                except Exception as es:
                    messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)
            else:
                messagebox.showerror("Error", "No mach password", parent=self.top)




if __name__ == '__main__':
    top=Tk()
    obj=App(top)


    top.mainloop()