from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql




class mg_check_deatils:
    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('1100x685+250+50')

        self.account_no = StringVar()

        # *********************** Title ***************************************
        self.tile_name = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        self.tile_name.place(x=0, y=0, width=1100, height=50)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA FORGOT ID", font=("time new roman", 11, "bold"),
                          bg='#A91079', fg="#070A52", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=1100, height=50)

        # **********************MAIN FRAME 2***********************
        main_frame2 = Frame(self.top, bd=4,bg='#FF00FF', relief=RIDGE)
        main_frame2.place(x=0, y=100, width=1100, height=585)

        # *********************** Account Entry *********************
        lbl_acc2_no = Label(main_frame2, text="Account No :", font=("time new roman", 14, "bold"),bg='#FF00FF', padx=10, pady=10)
        lbl_acc2_no.grid(row=0, column=0, sticky=W)

        entry_account_no = ttk.Entry(main_frame2, width=30, textvariable=self.account_no,font=("time new roman", 14, "bold"))
        entry_account_no.grid(row=0, column=1)

        # ******************** Main Frame 2 Button **********************
        button_submit = Button(main_frame2, text=" Submit ", font=("arial", 10, "bold"), bg="#000080", fg="white",
                                    padx=40, pady=1,command=self.show_data)
        button_submit.place(x=530, y=10)

        button_back = Button(main_frame2, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="white",padx=40, pady=1,command=self.top.destroy)
        button_back.place(x=30, y=525)

        # ********************* Show data table ************************
        data_frame = Frame(main_frame2, bd=5, relief=RIDGE)
        data_frame.place(x=0, y=80, width=1092, height=400)

        # ********************** scroll barr ****************************

        scorll_x = ttk.Scrollbar(data_frame, orient=HORIZONTAL)
        scorll_y = ttk.Scrollbar(data_frame, orient=VERTICAL)

        self.cust_details = ttk.Treeview(data_frame, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"),
                                         xscrollcommand=scorll_x.set, yscrollcommand=scorll_y.set, selectmode="browse")

        scorll_x.pack(side=BOTTOM, fill=X)
        scorll_y.pack(side=RIGHT, fill=Y)

        scorll_x.config(command=self.cust_details.xview)
        scorll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("1", text="Account No")
        self.cust_details.heading("2", text="Frist Name")
        self.cust_details.heading("3", text="Last Name")
        self.cust_details.heading("4", text="Father Name")
        self.cust_details.heading("5", text="Mother Name")
        self.cust_details.heading("6", text="Aadhar Number")
        self.cust_details.heading("7", text="Mobile Number")
        self.cust_details.heading("8", text="Gender")
        self.cust_details.heading("9", text="County")
        self.cust_details.heading("10", text="Amount")

        self.cust_details["show"] = "headings"

        self.cust_details.column("1", width=100)
        self.cust_details.column("2", width=100)
        self.cust_details.column("3", width=100)
        self.cust_details.column("4", width=100)
        self.cust_details.column("5", width=100)
        self.cust_details.column("6", width=100)
        self.cust_details.column("7", width=100)
        self.cust_details.column("8", width=100)
        self.cust_details.column("9", width=100)
        self.cust_details.column("10", width=100)

        self.cust_details.pack(fill=BOTH, expand=1)


    #******************** data fetches ***********************
    def show_data(self):

        if self.account_no.get() == "" :
            messagebox.showerror("Error", " Empty the account_no", parent=self.top)
        else:
            try:
                #*********************** sql data output ***********************************
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from bank where Account_No=%s") % (self.account_no.get()))
                store = cur.fetchone()
                man_data_st = []
                for i in store:
                    man_data_st.append(i)

                self.cust_details.insert("", END, values=(man_data_st[0],man_data_st[1],man_data_st[2],man_data_st[3],man_data_st[4],man_data_st[5],man_data_st[6],man_data_st[7],man_data_st[8],man_data_st[9]))

                db.commit()
                db.close()


                messagebox.showinfo("Success", "Customer has been Account_No Right", parent=self.top)
            except Exception as es:
                messagebox.showerror("Error", f"Some thing went wrong:{str(es)}", parent=self.top)


if __name__ == '__main__':
    top=Tk()
    obj=mg_check_deatils(top)


    top.mainloop()
