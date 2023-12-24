from tkinter import *
from PIL import ImageTk, Image
from Manager_Login import Manager
from User_Login import User

class Main:
    def __init__(self,top):

        self.top = top
        self.top.title('BANK')
        self.top.geometry('800x600+400+100')
        self.top.resizable(False, False)

        # *********************** Title ***************************************
        self.tile_name = Label(self.top, text="RKD BANK OF INDIA", font=("time new roman", 30, "bold"), bg="lightcoral",fg="black", bd=4, relief=RIDGE)
        self.tile_name.place(x=0, y=0, width=800, height=50)

        #************************** Main Frame *******************************
        self.main_frame=Frame(self.top,bd=4,bg="#BE5A83",relief=RIDGE)
        self.main_frame.place(x=0,y=50,width=800,height=550)



        #*************************** Image ***********************************
        self.path = "I:/Code Run/Pycham/Bank/adminLogin1.png"
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.im1 = Label(self.main_frame, image=self.img)
        self.im1.place(x=150,y=100)

        self.path2 = "I:/Code Run/Pycham/Bank/customer.png"
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        self.im12 = Label(self.main_frame, image=self.img2)
        self.im12.place(x=400, y=100,height=160,width=200)

        #*********************** Button *************************************
        self.manager_button=Button(self.main_frame, text="MANAGER", font=("arial",15,"bold"), bg="#FFABAB", fg="#89375F",activebackground="#804674", command=self.login_manager)
        self.manager_button.place(x=150,y=300,height=50,width=200)

        self.user_button=Button(self.main_frame,text="USER",font=("arial",15,"bold"),bg="#FFABAB",fg="#89375F",activebackground="#804674",command=self.login_us)
        self.user_button.place(x=400,y=300,height=50,width=200)

    # ******************************** New window ***************************
    def login_manager(self):
        self.new_windeo = Toplevel(self.top)
        self.app = Manager(self.new_windeo)


    def login_us(self):
        self.new_windeo = Toplevel(self.top)
        self.app = User(self.new_windeo)




if __name__ == '__main__':
    top=Tk()
    obj=Main(top)


    top.mainloop()

