from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql




class mg_check_blance:
    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('900x550+350+100')

        self.account_no = StringVar()
        self.update_amount= IntVar()

        #*************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=900, height=50)

        # **********************MAIN FRAME***********************
        main_frame = Frame(self.top, bd=4,bg='#8B008B', relief=RIDGE)
        main_frame.place(x=0, y=100, width=900, height=450)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA CHECK BALANCE ", font=("time new roman", 10, "bold"),bg='#7B68EE', fg="black",
                          bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=900, height=50)

        # *********************** Account Entry *********************
        lbl_account_no = Label(main_frame, text="Account No :", font=("time new roman", 14, "bold"),bg='#8B008B', padx=10, pady=10)
        lbl_account_no.grid(row=0, column=0, sticky=W)

        entry_account_no = ttk.Entry(main_frame, width=30, textvariable=self.account_no,font=("time new roman", 14, "bold"))
        entry_account_no.grid(row=0, column=1)



        # ******************** Main Frame  Button **********************

        button_submit = Button(main_frame, text=" Submit ", font=("arial", 10, "bold"), bg="#000080", fg="white",
                                    padx=40, pady=1, command=self.show)
        button_submit.place(x=530, y=10)

        button_back = Button(main_frame, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="white",
                                    padx=40, pady=1, command=self.top.destroy)
        button_back.place(x=40, y=390)



        # **********************Data FRAME ***********************
        data_frame = Frame(main_frame, bd=5, relief=RIDGE,)
        data_frame.place(x=0, y=80, width=892, height=250)

        #********************** scroll barr ****************************
        scorll_y = ttk.Scrollbar(data_frame, orient=VERTICAL)

        self.cust_details=ttk.Treeview(data_frame,columns=("1", "2", "3", "4"),yscrollcommand=scorll_y.set,selectmode="browse")

        scorll_y.pack(side=RIGHT, fill=Y)

        scorll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("1", text="Account No")
        self.cust_details.heading("2", text="Fist Name")
        self.cust_details.heading("3", text="Last Name")
        self.cust_details.heading("4", text="Amount")

        self.cust_details["show"]="headings"

        self.cust_details.pack(fill=BOTH, expand=1)

    # ******************** data fetches ***********************
    def show(self):
        if self.account_no.get() == "" :
            messagebox.showerror("Error","Fields are required",parent=self.top)
        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from bank where Account_No=%s") % (self.account_no.get()))
                store = cur.fetchone()
                data_st=[]
                for i in store:
                    data_st.append(i)
                self.cust_details.insert("", END, values=(data_st[0],data_st[1],data_st[2],data_st[9]))


                db.commit()

                db.close()
                messagebox.showinfo("Success", "Customer has been Account_No Right", parent=self.top)
            except Exception as es:
                messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)


if __name__ == '__main__':
    top=Tk()
    obj=mg_check_blance(top)

    top.mainloop()