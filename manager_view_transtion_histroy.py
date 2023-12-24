from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv



class mg_traction:
    def __init__(self,top):

        self.top = top
        self.top.title('BANK')
        self.top.geometry('900x600+350+100')

        self.account_no= StringVar()

        #*************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=900, height=50)

        # **********************MAIN FRAME***********************
        main_frame = Frame(self.top, bd=4,bg='#00FFFF', relief=RIDGE)
        main_frame.place(x=0, y=100, width=900, height=500)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="Customer View Transaction History",bg='#C71585', font=("time new roman", 10, "bold"), fg="black",
                          bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=900, height=50)

        # *********************** Account Entry *********************
        lbl_account_no = Label(main_frame, text="Account No :", font=("time new roman", 14, "bold"),bg='#00FFFF', padx=10, pady=10)
        lbl_account_no.grid(row=0, column=0, sticky=W)

        entry_account_no = ttk.Entry(main_frame, width=30, textvariable=self.account_no,font=("time new roman", 14, "bold"))
        entry_account_no.grid(row=0, column=1)



        # ******************** Main Frame  Button **********************

        button_submit = Button(main_frame, text=" Submit ", font=("arial", 10, "bold"), bg="#DA70D6", fg="black",
                                    padx=40, pady=1, command=self.show)
        button_submit.place(x=530, y=10)

        button_back = Button(main_frame, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="white",
                               padx=40, pady=1, command=self.top.destroy)
        button_back.place(x=30, y=440)



        # **********************Data FRAME ***********************
        data_frame = Frame(main_frame, bd=5, relief=RIDGE)
        data_frame.place(x=0, y=80, width=892, height=300)

        #********************** scroll barr ****************************
        scorll_y = ttk.Scrollbar(data_frame, orient=VERTICAL)

        self.cust_details=ttk.Treeview(data_frame,columns=("1", "2", "3", "4", "5"),yscrollcommand=scorll_y.set,selectmode="browse")

        scorll_y.pack(side=RIGHT, fill=Y)

        scorll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("1", text="Account No")
        self.cust_details.heading("2", text="Deposit")
        self.cust_details.heading("3", text="Withdraw")
        self.cust_details.heading("4", text="Total Amount")
        self.cust_details.heading("5", text="Date")

        self.cust_details["show"]="headings"

        self.cust_details.column("1", width=10)
        self.cust_details.column("2", width=10)
        self.cust_details.column("3", width=10)
        self.cust_details.column("4", width=10)
        self.cust_details.column("5", width=10)

        self.cust_details.pack(fill=BOTH, expand=1)

    # ******************** csv data read  ***********************
    def show(self):
        if self.account_no.get() == "" :
            messagebox.showerror("Error","Fields are required",parent=self.top)
        else:
            try:
                with open("I:/Code Run/Pycham/Bank/rkd.csv", "r") as fobj:
                    obj = csv.reader(fobj)
                    for i in obj:
                        if i[0] == str(self.account_no.get()):

                            self.cust_details.insert("", END, values=(i))

                messagebox.showinfo("Success", "customer has been Account_No Right", parent=self.top)
            except Exception as es:
                messagebox.showerror("Error",f"Some thing went wrong:{str(es)}",parent=self.top)




if __name__ == '__main__':
    top=Tk()
    obj=mg_traction(top)

    top.mainloop()