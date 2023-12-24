from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql




class forgot_id_us:
    def __init__(self,top):
        self.top = top
        self.top.title('BANK')
        self.top.geometry('700x565+400+100')
        self.top.resizable(False, False)

        # ********************** variable **********************
        self.account_no = StringVar()
        self.mobile_no = StringVar()

        #*************************Title*********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 25, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=700, height=50)


        # **********************MAIN FRAME***********************
        main_frame = Frame(self.top, bd=4, bg="#F73D93", relief=RIDGE)
        main_frame.place(x=0, y=100, width=698, height=465)

        # ********************** Form Frame *********************
        lbl_title = Label(self.top, text="RKD BANK OF INDIA WITHDRAWAL AMOUNT", font=("time new roman", 10, "bold"), bg='#A91079',fg="#070A52",bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=50, width=698, height=50)

        # **********************Data FRAME ***********************
        self.data_frame = Frame(main_frame, bd=5, relief=RIDGE,bg='#A91079')
        self.data_frame.place(x=45, y=250, width=600, height=100)



        # *********************** Account Entry *********************
        lbl_account_no = Label(main_frame, text=" Account No : ", font=("time new roman", 14, "bold"),bg="#F73D93", padx=10, pady=10)
        lbl_account_no.grid(row=0, column=0, sticky=W)

        entry_account_no = ttk.Entry(main_frame, width=25, textvariable=self.account_no,font=("time new roman", 14, "bold"))
        entry_account_no.grid(row=0, column=1)

        lbl_mobile_no = Label(main_frame, text=" Mobile No : ", font=("time new roman", 14, "bold"),bg="#F73D93", padx=10, pady=10)
        lbl_mobile_no.grid(row=1, column=0, sticky=W)

        entry_mobile_no = ttk.Entry(main_frame, width=25, textvariable=self.mobile_no,font=("time new roman", 14, "bold"))
        entry_mobile_no.grid(row=1, column=1)



        # ******************** Main Frame  Button **********************

        button_submit = Button(main_frame, text=" Submit ", font=("arial", 10, "bold"), bg="black", fg="gold",padx=40, pady=1,command=self.id_us)
        button_submit.place(x=180, y=130)


        button_back = Button(self.top, text=" Back ", font=("arial", 10, "bold"), bg="black", fg="gold",padx=40, pady=1, command=self.top.destroy)
        button_back.place(x=40, y=510)

        # ******************** data fetches ***********************

    def id_us(self):

        if self.account_no.get() == "":
            messagebox.showerror("Error", "Fields are Empty Column", parent=self.top)
        else:
            try:
                db = sql.connect(host='localhost', user='root', passwd='12345', db='bank')
                cur = db.cursor()
                cur.execute(("select *from app where Account_No=%s") % (self.account_no.get()))
                store = cur.fetchone()
                store_data=[]
                for i in store:
                    store_data.append(i)

                self.account_n=str(store_data[0])
                self.mobile_n=str(store_data[3])

                if self.account_n == self.account_no.get() and self.mobile_n == self.mobile_no.get():
                    messagebox.showinfo("Success", "Successful", parent=self.top)
                    # ************************* password Lable ********************
                    self.user_id_lb = Label(self.data_frame, text="User id : ", font=("time new roman", 14, "bold"))
                    self.user_id_lb.place(x=200, y=35)

                    self.user_id_fath = Label(self.data_frame, text=store_data[4], font=("time new roman", 14, "bold"))
                    self.user_id_fath.place(x=280, y=35)

                else:
                    messagebox.showerror("Error", "Wrong Mobile Numer ", parent=self.top)


                db.commit()
                db.close()


            except Exception as es:
                messagebox.showerror("Error",f"wrong Account No:{str(es)}",parent=self.top)


if __name__ == '__main__':
    top=Tk()
    obj=forgot_id_us(top)

    top.mainloop()