from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
import csv
import datetime



class mg_deposit:
    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('900x700+350+50')

        #************************* Varable *****************************
        self.account_no = StringVar()
        self.update_amount= StringVar()

        # ************************** Date ************************************
        self.date = datetime.datetime.now()
        self.date_varable = self.date.date()
        self.date_update = self.date_varable.strftime('%d/%m/%G')

        #*************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=900, height=50)

        # **********************MAIN FRAME***********************
        main_frame = Frame(self.top, bd=4,bg='#8B008B', relief=RIDGE)
        main_frame.place(x=0, y=100, width=900, height=600)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA DEPOSIT AMOUNT", font=("time new roman", 10, "bold"),bg='#BA55D3', fg="black",bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=900, height=50)

        # *********************** Account Entry *********************
        lbl_accunt_no = Label(main_frame, text="Account No :", font=("time new roman", 14, "bold"),bg='#8B008B', padx=10, pady=10)
        lbl_accunt_no.grid(row=0, column=0, sticky=W)

        entry_account_no = ttk.Entry(main_frame, width=30, textvariable=self.account_no,font=("time new roman", 14, "bold"))
        entry_account_no.grid(row=0, column=1)

        lbl_mony = Label(main_frame, text="Deposit Amount :", font=("time new roman", 14, "bold"),bg='#8B008B', padx=10, pady=10)
        lbl_mony.place(x=5,y=450)

        entry_mony = ttk.Entry(main_frame, width=30, textvariable=self.update_amount,font=("time new roman", 14, "bold"))
        entry_mony.place(x=200,y=460)

        # ******************** Main Frame  Button **********************

        button_check_details = Button(main_frame, text=" Check details ", font=("arial", 10, "bold"), bg="#000080", fg="white",
                                    padx=40, pady=1, command=self.show)
        button_check_details.place(x=530, y=10)

        button_submit = Button(main_frame, text=" Submit ", font=("arial", 10, "bold"), bg="#000080", fg="white",
                                    padx=40, pady=1, command=self.update)
        button_submit.place(x=570, y=460)

        button_submit = Button(main_frame, text=" Back ", font=("arial", 10, "bold"), bg="Black", fg="white",
                               padx=40, pady=1,command=self.top.destroy)
        button_submit.place(x=30, y=530)

        # **********************Data FRAME ***********************
        data_frame = Frame(main_frame, bd=5, relief=RIDGE)
        data_frame.place(x=0, y=80, width=892, height=300)

        #********************** scroll barr ****************************
        scorll_y = ttk.Scrollbar(data_frame, orient=VERTICAL)

        self.cust_details=ttk.Treeview(data_frame,columns=("1", "2", "3"),yscrollcommand=scorll_y.set,selectmode="browse")

        scorll_y.pack(side=RIGHT, fill=Y)

        scorll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("1", text="Account No")
        self.cust_details.heading("2", text="Frist Name")
        self.cust_details.heading("3", text="Last Name")


        self.cust_details["show"]="headings"

        self.cust_details.pack(fill=BOTH, expand=1)

    # ******************** data fetches ***********************
    def show(self):
        if self.account_no.get() == "" :
            messagebox.showerror("Error","Fields are Account_No",parent=self.top)
        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from bank where Account_No=%s") % (self.account_no.get()))
                store = cur.fetchone()

                ch_data=[]
                for i in store:
                    ch_data.append(i)

                self.cust_details.insert("", END, values=(ch_data[0],ch_data[1],ch_data[2]))

                db.commit()
                db.close()


                messagebox.showinfo("Success", "Customer has been Account_No Right", parent=self.top)
            except Exception as es:
                messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)

    # ******************** sql conaction  ***********************
    def update(self):

        if self.update_amount.get() == "" or self.account_no.get() == "":
            messagebox.showerror("Error","Fields are required",parent=self.top)
        else:
            self.update_amount_int = int(self.update_amount.get())
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("update bank set Amount=Amount +%s where Account_No=%s") % (self.update_amount_int,self.account_no.get()))
                cur.execute(("select *from bank where Account_No=%s") % (self.account_no.get()))
                store = cur.fetchone()
                man_data_st = []
                for i in store:
                    man_data_st.append(i)

                db.commit()
                db.close()

                # ******************** csv data read  ***********************
                with open("I:/Code Run/Pycham/Bank/rkd.csv", "a", newline="") as fobj:
                    obj = csv.writer(fobj)
                    a=self.account_no.get()
                    b=self.update_amount_int
                    c=""
                    d=man_data_st[9]
                    z = [a, b, c,d,self.date_update]
                    obj.writerow(z)


                messagebox.showinfo("Success", "Customer has been Deposit Money", parent=self.top)
            except Exception as es:
                messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)


if __name__ == '__main__':
    top=Tk()
    obj=mg_deposit(top)

    top.mainloop()