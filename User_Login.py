from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
import csv
from forgot_user_password import forgot_password_us
from forgot_user_id import forgot_id_us
from signup import App
import datetime


user_account_no=[]

class User:
    def __init__(self,top):
        self.top=top
        self.top.title("BANK")
        self.top.geometry('900x650+300+50')
        self.top.config(bg="blue")
        self.top.resizable(False, False)

        # ********************** variable **********************
        self.user_id_get = StringVar()
        self.user_password_get = StringVar()

        #******************** Title ********************
        self.tile=Label(self.top,text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"),  bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        self.tile.place(x=0, y=0, width=900, height=50)

        #******************* Frame ************************
        self.frame = Frame(self.top, bd=4, bg="#FF5F9E", relief=RIDGE)
        self.frame.place(x=0, y=50, width=900, height=599)

        #******************* Image *************************
        self.path = "I:/Code Run/Pycham/Bank/user1.png"
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.im1 = Label(self.frame, image=self.img)
        self.im1.place(x=450,y=280,height=30,width=30)

        self.path1 = "I:/Code Run/Pycham/Bank/lock1.png"
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        self.im11 = Label(self.frame, image=self.img1)
        self.im11.place(x=450,y=340,height=30,width=30)

        self.path2 = "I:/Code Run/Pycham/Bank/customer.png"
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        self.im12 = Label(self.frame, image=self.img2)
        self.im12.place(x=100, y=160,height=200,width=200)

        self.path3 = "I:/Code Run/Pycham/Bank/download.jpeg"
        self.img3 = ImageTk.PhotoImage(Image.open(self.path3))
        self.im13 = Label(self.frame, image=self.img3)
        self.im13.place(x=500, y=50,width=200,height=180)

        #**************** Entry column *********************
        self.id_et=ttk.Entry(self.frame,width=20,font=("time new roman", 14, "bold"),textvariable=self.user_id_get)
        self.id_et.place(x=500,y=280)

        self.password_et = ttk.Entry(self.frame, width=20, font=("time new roman", 14, "bold"), textvariable=self.user_password_get, show='*')
        self.password_et.place(x=500, y=340)

        #****************** Button **************************
        self.login_bt=Button(self.frame,text=" Login ",font=("arial",10,"bold"),bg="#C060A1",fg="black",command=self.login_us)
        self.login_bt.place(x=630,y=400,width=100,height=30)

        self.back_bt = Button(self.frame, text=" Back ", font=("arial", 15, "bold"), bg="black", fg="white",command=self.top.destroy)
        self.back_bt.place(x=50, y=500, width=100, height=40)


        self.forgot_password_bt = Button(self.frame, text=" Forgot Password", font=("arial", 10, "bold"), bg="#C060A1",fg="black",command=self.user_password_new)
        self.forgot_password_bt.place(x=600, y=470, width=140, height=20)

        self.forgot_id_bt = Button(self.frame, text=" Forgot Id", font=("arial", 10, "bold"), bg="#C060A1",fg="black",command=self.user_id_new)
        self.forgot_id_bt.place(x=610, y=520, width=120, height=20)

        self.sign_bt = Button(self.frame, text=" Sign Up", font=("arial", 10, "bold"), bg="#C060A1",fg="black",command=self.sign_up)
        self.sign_bt.place(x=450, y=470, width=110, height=20)

        #************************* user Lable ********************
        self.admin=Label(self.frame,text="User Login",font=("time new roman", 14, "bold"),padx=40,pady=10)
        self.admin.place(x=100,y=60)


    def login_us(self):
        if self.user_id_get.get() == "" or self.user_password_get.get() == "":
            messagebox.showerror("Error", "Fields are Empty Column", parent=self.top)
        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from app where User_Id='%s'") % (self.user_id_get.get()))
                store_data = []
                store = cur.fetchone()
                for i in store:
                    store_data.append(i)
                self.user_id = str(store_data[4])
                self.user_password = store_data[5]
                self.account_no=store_data[0]
                user_account_no.append(self.account_no)


                db.commit()
                db.close()

                if self.user_id_get.get() == self.user_id and self.user_password_get.get() == self.user_password:
                    messagebox.showinfo("Successful", "Successful Login Admin", parent=self.top)
                    self.new_window = Toplevel(self.top)
                    self.app = user_prmation(self.new_window)

                else:
                    messagebox.showerror("Error", " Password Wrong", parent=self.top)

            except Exception as es:
                messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)

    # ******************************** New window ***************************
    def user_id_new(self):
        self.new_window = Toplevel(self.top)
        self.app = forgot_id_us(self.new_window)


    def user_password_new(self):
        self.new_window = Toplevel(self.top)
        self.app = forgot_password_us(self.new_window)

    def sign_up(self):
        self.new_window = Toplevel(self.top)
        self.app = App(self.new_window)



class user_prmation:
    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('800x550+350+50')
        self.top.resizable(False, False)
        self.top.configure(bg='#E9A178')


        # *********************** Title ***************************************
        self.tile_name = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"),bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        self.tile_name.place(x=0, y=0, width=800, height=50)

        #************************** Main Frame *******************************
        self.main_frame=Frame(self.top,bd=4,relief=RIDGE,bg='#7149C6')
        self.main_frame.place(x=0,y=50,width=800,height=420)

        # ****************** Button **************************
        self.balance_ch_bt = Button(self.main_frame, text=" Balance Check ", font=("arial", 20, "bold"), width=16, bg="#19A7CE",fg="gold",command=self.blance_check)
        self.balance_ch_bt.place(x=250,y=70)

        self.withdraw_bt = Button(self.main_frame, text=" Withdraw ", font=("arial", 20, "bold"), width=16, bg="#19A7CE",fg="gold",command=self.withdraw)
        self.withdraw_bt.place(x=250,y=170)

        self.transaction_bt = Button(self.main_frame, text="Transaction History", font=("arial", 20, "bold"), bg="#19A7CE",fg="gold",command=self.transaction)
        self.transaction_bt.place(x=250,y=270)

        self.back_bt = Button(self.top, text=" Back ", font=("arial", 20, "bold"), bg="black",fg="white",command=self.top.destroy)
        self.back_bt.place(x=20, y=490,width=120,height=40)

        #******************************** New window ***************************

    def blance_check(self):
        self.new_window=Toplevel(self.top)
        self.app=blance(self.new_window)

    # ************************* Withdraw window open *************************
    def withdraw(self):
        self.new_window = Toplevel(self.top)
        self.app = withdrawal(self.new_window)
    #
    # ************************* view history window open *************************
    def transaction(self):
        self.new_window = Toplevel(self.top)
        self.app = view_traction(self.new_window)


class blance:

    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('500x400+500+100')
        self.top.resizable(False, False)
        self.top.configure(bg='#0F6292')

        # *********************** Title ***************************************
        self.tile_name = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        self.tile_name.place(x=0, y=0, width=500, height=50)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA AMOUNT CHECK", font=("time new roman", 10, "bold"),bg='#865DFF',
                          fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=500, height=50)

        #************************** Main Frame *******************************
        self.main_frame=Frame(self.top,bd=4,bg='#AD7BE9',relief=RIDGE)
        self.main_frame.place(x=0,y=100,width=500,height=228)

        #************************** fetch amount *****************************

        db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
        cur = db.cursor()
        self.account_num = user_account_no[0]
        cur.execute(("select *from bank where Account_No=%s") % (self.account_num))
        store = cur.fetchone()
        data_st = []
        for i in store:
            data_st.append(i)

        # ************************* Lable ***************************************
        self.lbl_mony = Label(self.main_frame, text="Available Amount :", font=("time new roman", 14, "bold"),bg='#AD7BE9', padx=10,
                              pady=10)
        self.lbl_mony.place(x=5, y=80)

        self.lbl_mony_so = Label(self.main_frame, text=data_st[9], font=("time new roman", 14, "bold"),bg='#AD7BE9', padx=10,
                                 pady=10)
        self.lbl_mony_so.place(x=200, y=80)

        db.commit()

        db.close()

        #*********************** Button *************************************
        self.back_button=Button(self.top, text="Back", font=("arial",15,"bold"), bg="black", fg="gold", command=self.top.destroy)
        self.back_button.place(x=10,y=360,height=25,width=120)

class view_traction:
    def __init__(self, top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('800x470+400+100')
        self.top.resizable(False, False)
        self.top.configure(bg='#913175')

        # *************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=800, height=50)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="Customer View Transaction History", font=("time new roman", 10, "bold"),bg='#F2921D',
                              fg="#326273", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=800, height=50)

        # ******************** Button **********************
        button_back = Button(self.top, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="white",padx=40, pady=1, command=self.top.destroy)
        button_back.place(x=10, y=400)

        # **********************Data FRAME ***********************
        data_frame = Frame(self.top, bd=5, relief=RIDGE)
        data_frame.place(x=0, y=100, width=799, height=280)

        # ********************** scroll barr ****************************
        scorll_y = ttk.Scrollbar(data_frame, orient=VERTICAL)

        self.cust_details = ttk.Treeview(data_frame, columns=("1", "2", "3", "4", "5"), yscrollcommand=scorll_y.set,
                                             selectmode="browse")

        scorll_y.pack(side=RIGHT, fill=Y)

        scorll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("1", text="Account No")
        self.cust_details.heading("2", text="Deposit")
        self.cust_details.heading("3", text="Withdraw")
        self.cust_details.heading("4", text="Total Amount")
        self.cust_details.heading("5", text="Date")

        self.cust_details["show"] = "headings"

        self.cust_details.column("1", width=10)
        self.cust_details.column("2", width=10)
        self.cust_details.column("3", width=10)
        self.cust_details.column("4", width=10)
        self.cust_details.column("5", width=10)

        self.cust_details.pack(fill=BOTH, expand=1)
        self.account_numb=user_account_no[0]

        #****************** factch ***************************
        with open("I:/Code Run/Pycham/Bank/rkd.csv", "r") as fobj:
            obj = csv.reader(fobj)
            for i in obj:
                if i[0] == str(self.account_numb):
                    self.cust_details.insert("", END, values=(i))


class withdrawal:
    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('800x465+350+50')
        self.top.resizable(False, False)
        self.top.configure(bg='#ADA2FF')

        #********************** varable ************************
        self.us_account=user_account_no[0]
        self.update_amount_get= StringVar()

        # ************************** Date ************************************
        self.date = datetime.datetime.now()
        self.date_varable = self.date.date()
        self.date_update = self.date_varable.strftime('%d/%m/%G')

        #*************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=800, height=50)

        # **********************MAIN FRAME***********************
        main_frame = Frame(self.top, bd=4,bg='#CB1C8D', relief=RIDGE)
        main_frame.place(x=0, y=100, width=800, height=369)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA WITHDRAWAL AMOUNT", font=("time new roman", 10, "bold"), fg="black",
                          bd=4,bg='#326273', relief=RIDGE)
        lbl_title.place(x=0, y=50, width=800, height=50)

        # *********************** Account Entry *********************

        lbl_mony = Label(main_frame, text="Deposit Amount :",bg='#CB1C8D', font=("time new roman", 14, "bold"), padx=10, pady=10)
        lbl_mony.grid(row=0, column=0, sticky=W)

        entry_mony = ttk.Entry(main_frame, width=25, textvariable=self.update_amount_get,font=("time new roman", 14, "bold"))
        entry_mony.grid(row=0, column=1)

        # ******************** Main Frame  Button **********************

        button_submit = Button(main_frame, text=" Submit ", font=("arial", 10, "bold"), bg="#863A6F", fg="black",
                                    padx=40, pady=1, command=self.update)
        button_submit.place(x=530, y=10)

        button_back = Button(main_frame, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="white",
                                    padx=40, pady=1, command=self.top.destroy)
        button_back.place(x=10, y=320)

        # **********************Data FRAME ***********************
        data_frame = Frame(main_frame, bd=5, relief=RIDGE)
        data_frame.place(x=0, y=80, width=792, height=180)

        #********************** scroll barr ****************************
        scorll_y = ttk.Scrollbar(data_frame, orient=VERTICAL)

        self.cust_details=ttk.Treeview(data_frame,columns=("1", "2", "3", "4"),yscrollcommand=scorll_y.set,selectmode="browse")

        scorll_y.pack(side=RIGHT, fill=Y)

        scorll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("1", text="Account No")
        self.cust_details.heading("2", text="First Name")
        self.cust_details.heading("3", text="Last Name")
        self.cust_details.heading("4", text="Total Amount")


        self.cust_details["show"]="headings"

        self.cust_details.pack(fill=BOTH, expand=1)


    def update(self):
        if self.update_amount_get.get() == "" :
            messagebox.showerror("Error","Fields are required",parent=self.top)
        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from bank where Account_No=%s") % (self.us_account))
                store = cur.fetchone()

                with_data = []
                for i in store:
                    with_data.append(i)

                Enter_your_Account_No=with_data[9]
                self.update_amount_get_int = int(self.update_amount_get.get())

                if Enter_your_Account_No >= self.update_amount_get_int:
                    self.amounu_update = self.update_amount_get.get()
                    cur.execute(("update bank set Amount=Amount -%s where Account_No=%s") % (self.update_amount_get_int,self.us_account))

                    cur.execute(("select *from bank where Account_No=%s") % (self.us_account))
                    store = cur.fetchone()
                    store_data = []
                    for i in store:
                        store_data.append(i)
                    self.cust_details.insert("", END, values=(store_data[0], store_data[1], store_data[2],store_data[9]))

                    db.commit()
                    db.close()

                    # ******************** csv data read  ***********************
                    with open("I:/Code Run/Pycham/Bank/rkd.csv", "a", newline="") as fobj:
                        obj = csv.writer(fobj)
                        a = self.us_account
                        b = ""
                        c = self.update_amount_get.get()
                        d = store_data[9]
                        z = [a, b, c, d, self.date_update]
                        obj.writerow(z)

                    messagebox.showinfo("Success", "Withdraw money", parent=self.top)
                else:
                    messagebox.showerror("Error", "no amount", parent=self.top)

            except Exception as es:
                messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)



if __name__ == '__main__':
    top=Tk()
    object=User(top)


    top.mainloop()

