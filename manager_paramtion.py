from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import random
import pymysql as sql
from tkinter import messagebox
from manager_check_blence import mg_check_blance
from manager_deposit import mg_deposit
from manager_withdraw import mg_withdrow
from manager_view_transtion_histroy import mg_traction
from signup import App
from manager_check_details import mg_check_deatils
import csv
import datetime

class mg_parmation:
    def __init__(self,top):
        self.top=top
        self.top.title("BANK")
        self.top.geometry("1230x750+100+0")
        self.top.resizable(False,False)
        # self.top.configure(bg='#F2B6A0')

        #************************** Date ************************************
        self.date=datetime.datetime.now()
        self.date_varable = self.date.date()
        self.date_update = self.date_varable.strftime('%d/%m/%G')

        # ********************** random account variable **********************
        self.var_acount_no = IntVar()
        x = random.randint(10000000000, 99999999999)
        self.var_acount_no.set(int(x))

        # ********************** variable **********************
        self.account_no = StringVar()
        self.fist_name = StringVar()
        self.last_name = StringVar()
        self.father_name = StringVar()
        self.mother_name = StringVar()
        self.mobile_no = StringVar()
        self.aadhar_no = StringVar()
        self.gender = StringVar()
        self.countr = StringVar()
        self.var_amount = IntVar()

        #********************** Title ******************
        tile = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"), bg="#E76161", fg="#AFD3E2",bd=4, relief=RIDGE)
        tile.place(x=0, y=0, width=1230, height=70)

        # ******************* Frame ************************
        self.sid_frame = Frame(self.top, bd=4, relief=RIDGE)
        self.sid_frame.place(x=3, y=130, width=310, height=610)

        # ******************* create Frame ************************
        self.create_frame = Frame(self.top, bd=4, relief=RIDGE)
        self.create_frame.place(x=310, y=130, width=910, height=610)

        # ******************* Image *************************
        self.path = "I:/Code Run/Pycham/Bank/pexels-habib-904735 (5).jpg"
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.im1 = Label(self.sid_frame, image=self.img)
        self.im1.place( y=360)

        # ****************** Button **************************
        self.blance_b = Button(self.sid_frame, text=" Balance Check ", font=("arial", 20, "bold"),width=17, fg="#1D267D", bg='#FDCEDF',command=self.blance_check)
        self.blance_b.place(x=0,y=0)

        self.deposit_b = Button(self.sid_frame, text=" Deposit ", font=("arial", 20, "bold"), width=17, fg="#1D267D", bg='#FDCEDF',command=self.deposit)
        self.deposit_b.place(x=0,y=60)

        self.withdraw_b = Button(self.sid_frame, text=" Withdraw ", font=("arial", 20, "bold"),width=17, fg="#1D267D", bg='#FDCEDF',command=self.withdraw)
        self.withdraw_b.place(x=0,y=120)

        self.transction_b = Button(self.sid_frame, text="Transaction History", font=("arial", 20, "bold"),width=17, fg="#1D267D", bg='#FDCEDF',command=self.transaction)
        self.transction_b.place(x=0,y=180)

        self.account_d_b = Button(self.sid_frame, text=" Account Details ", font=("arial", 20, "bold"),width=17, fg="#1D267D", bg='#FDCEDF',command=self.details)
        self.account_d_b.place(x=0,y=240)

        self.app_b = Button(self.sid_frame, text=" R.K.D App sign Up ", font=("arial", 20, "bold"),width=17, fg="#1D267D", bg='#FDCEDF',command=self.sign_up)
        self.app_b.place(x=0,y=300)

        self.sumbit_b = Button(self.create_frame, text=" Submit ", font=("arial", 15, "bold"), bg="#1B9C85",fg="black",command=self.add_data)
        self.sumbit_b.place(x=300,y=500,width=150,height=50)

        self.clear_b = Button(self.create_frame, text=" Clear ", font=("arial", 10, "bold"), bg="#1B9C85", fg="black",command=self.clear)
        self.clear_b.place(x=700, y=550, width=150, height=30)

        self.exit_b = Button(self.create_frame, text=" Back ", font=("arial", 10, "bold"), bg="#1B9C85", fg="black",command=self.top.destroy)
        self.exit_b.place(x=15, y=560, width=150, height=30)

        # ********************** From entry ********************

        # First Name
        lbl_name = Label(self.create_frame, text="First Name :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_name.grid(row=0, column=0, sticky=W)

        entry_f_name = ttk.Entry(self.create_frame, width=30, textvariable=self.fist_name, font=("time new roman", 14, "bold"))
        entry_f_name.grid(row=0, column=1)

        # Last Name
        lbl_last_name = Label(self.create_frame, text="Last Name :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_last_name.grid(row=1, column=0, sticky=W)

        entry_last_name = ttk.Entry(self.create_frame, width=30, textvariable=self.last_name, font=("time new roman", 14, "bold"))
        entry_last_name.grid(row=1, column=1)

        # Father Name
        lbl_father_name = Label(self.create_frame, text="Father Name :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_father_name.grid(row=2, column=0, sticky=W)

        entry_father_name = ttk.Entry(self.create_frame, width=30, textvariable=self.father_name, font=("time new roman", 14, "bold"))
        entry_father_name.grid(row=2, column=1)

        # Mother Name
        lbl_mother_name = Label(self.create_frame, text="Mother Name :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_mother_name.grid(row=3, column=0, sticky=W)

        entry_mothername = ttk.Entry(self.create_frame, width=30, textvariable=self.mother_name, font=("time new roman", 14, "bold"))
        entry_mothername.grid(row=3, column=1)

        # Aadhar No
        lbl_aadhar_no = Label(self.create_frame, text="Aadhar Number :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_aadhar_no.grid(row=4, column=0, sticky=W)

        entry_aadhar_no = ttk.Entry(self.create_frame, width=30, textvariable=self.aadhar_no, font=("time new roman", 14, "bold"))
        entry_aadhar_no.grid(row=4, column=1)

        # Mobile No
        lbl_mobile_no = Label(self.create_frame, text="Mobile Number :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_mobile_no.grid(row=5, column=0, sticky=W)

        entry_mobile_no = ttk.Entry(self.create_frame, width=30, textvariable=self.mobile_no, font=("time new roman", 14, "bold"))
        entry_mobile_no.grid(row=5, column=1)

        # Gender
        lbl_gender = Label(self.create_frame, text="Gender :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_gender.grid(row=6, column=0, sticky=W)

        enter_redi_bu = Radiobutton(self.create_frame, text='Male', variable=self.gender, value='Male',
                                    font=("time new roman", 14, "bold"), padx=2, pady=5)
        enter_redi_bu.place(x=240, y=280)
        enter_redi_bu.select()
        enter_redi_bu1 = Radiobutton(self.create_frame, text='Female', value='Female', variable=self.gender,
                                     font=("time new roman", 14, "bold"), padx=2, pady=5)
        enter_redi_bu1.place(x=330, y=280)
        enter_redi_bu1.deselect()
        enter_redi_bu2 = Radiobutton(self.create_frame, text='Transgender', value='Transgender', variable=self.gender,
                                     font=("time new roman", 14, "bold"), padx=2, pady=5)
        enter_redi_bu2.place(x=450, y=280)
        enter_redi_bu2.deselect()

        # Country
        lbl_name = Label(self.create_frame, text="Country :",font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_name.grid(row=7, column=0, sticky=W)

        combo_country = ttk.Combobox(self.create_frame, textvariable=self.countr, font=("arial", 14, "bold"), width=30,
                                     state="readonly")
        combo_country["value"] = ("Select", "Afghanistan", "Aland Islands", "Aruba", "India", "Iraq")
        combo_country.current(0)
        combo_country.grid(row=7, column=1)

        # Account No
        lbl_account_no = Label(self.create_frame, text="Account NO :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_account_no.grid(row=8, column=0, sticky=W)

        entry_account_no = ttk.Entry(self.create_frame, width=30, textvariable=self.var_acount_no, font=("arial", 14, "bold"),
                                 state="readonly")
        entry_account_no.grid(row=8, column=1)

        # Amount
        lbl_amount = Label(self.create_frame, text="Amount :", font=("time new roman", 14, "bold"), padx=40, pady=10)
        lbl_amount.grid(row=9, column=0, sticky=W)

        entry_amount = ttk.Entry(self.create_frame, width=30, textvariable=self.var_amount, font=("arial", 14, "bold"))
        entry_amount.grid(row=9, column=1)

        #******************* Time and date *******************************************

        def clock():
            var = datetime.datetime.now()
            time = (var.strftime("%H : %M : %S"))
            date = (var.strftime("%d / %m / %y"))
            time_t.config(text=time)
            date_d.config(text=date)
            time_t.after(200, clock)

        time_t = Label(self.top, font=("Times_New_Roman", 20), fg="#1D267D", bg='#E76161')
        time_t.place(x=3, y=75, height=50, width=300)

        date_d = Label(self.top, font=("Times_New_Roman", 20), fg="#1D267D", bg='#E76161')
        date_d.place(x=950, y=75, height=50, width=270)
        clock()

    # ********************** sql conation data and insert ************************************
    def add_data(self):

        if self.fist_name.get() == "" or self.last_name.get() == "" or self.father_name.get() == "" or self.mother_name.get() == "" or self.aadhar_no.get() == "" or self.mobile_no.get() == "" or self.gender.get() == "" or self.countr.get() == "" and self.var_amount.get() == "":
            messagebox.showerror("Error", "Fields are Empty Column", parent=self.top)
        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute("insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_acount_no.get(),
                                                                                           self.fist_name.get(),
                                                                                           self.last_name.get(),
                                                                                           self.father_name.get(),
                                                                                           self.mother_name.get(),
                                                                                           self.aadhar_no.get(),
                                                                                           self.mobile_no.get(),
                                                                                           self.gender.get(),
                                                                                           self.countr.get(),
                                                                                           self.var_amount.get()))

                self.b=""



                db.commit()

                db.close()

                # *************************** txt file create insert data *************************
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from bank where Account_No=%s") % (self.var_acount_no.get()))
                store = cur.fetchone()
                man_data_st = []
                for i in store:
                    man_data_st.append(i)

                db.commit()
                db.close()

                with open("I:/Code Run/Pycham/Bank/rkd.csv", "a", newline="") as f:
                    obj = csv.writer(f)
                    a = man_data_st[0]
                    b = str(man_data_st[9])
                    c = ""
                    d = str(man_data_st[9])
                    z = [a, b, c, d,self.date_update]
                    obj.writerow(z)

                messagebox.showinfo("Success", "customer has been added", parent=self.top)
            except Exception as es:
                messagebox.showerror("Error", f"Some thing went wrong:{str(es)}", parent=self.top)

    #************************* balance check window open *************************
    def blance_check(self):
        self.new_windeo=Toplevel(self.top)
        self.app=mg_check_blance(self.new_windeo)

    # ************************* Deposit window open *************************
    def deposit(self):
        self.new_windeo = Toplevel(self.top)
        self.app =mg_deposit(self.new_windeo)

    # ************************* Withdraw window open *************************
    def withdraw(self):
        self.new_windeo = Toplevel(self.top)
        self.app = mg_withdrow(self.new_windeo)

    # ************************* view history window open *************************
    def transaction(self):
        self.new_windeo = Toplevel(self.top)
        self.app = mg_traction(self.new_windeo)

    # ************************* App sign up *************************
    def sign_up(self):
        self.new_windeo = Toplevel(self.top)
        self.app = App(self.new_windeo)

    # ************************* Details *************************
    def details(self):
        self.new_windeo = Toplevel(self.top)
        self.app = mg_check_deatils(self.new_windeo)

    # ************************* fill data clear *************************

    def clear(self):
        self.fist_name.set("")
        self.last_name.set("")
        self.father_name.set("")
        self.mother_name.set("")
        self.mobile_no.set("")
        self.aadhar_no.set("")
        self.var_amount.set("")
        x = random.randint(10000000000, 99999999999)
        self.var_acount_no.set(int(x))



if __name__ == '__main__':
    top=Tk()
    object=mg_parmation(top)

    top.mainloop()