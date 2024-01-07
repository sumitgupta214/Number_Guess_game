import time
from tkinter import *


root = Tk()
root.geometry("900x850")
root.title("ATM MACHINE")
root.configure(bg="black")

Tops = Frame(root,bg="white",width=800,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,bg="black",width=300,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,bg="black",width=400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lbl1 = Label(Tops,font=('aria',30,'bold'),text="ATM MACHINE",fg="Powder Blue",bg="black",bd=10,anchor='w')
lbl1.grid(row=0,column=0)
lbl2 = Label(Tops,font=('aria',20,'bold'),text=localtime,fg="Powder Blue",bg="black",bd=10,anchor='w')
lbl2.grid(row=1,column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
acca = " "

def bank():
    global acca
    accno = ["0092","27833","78364"]
    account =number.get()
    if account in accno:
        label.config(text="Rgistered User")
        bank = {
            "0092":10000,
            "27833":20000,
            "78364" : 30000
        }
        balance = bank[account]
        acca = balance
    else:
        label.config(text="Non Registered user")


def deposit():
    global acca
    amo = float(amount.get())
    bal = acca+amo
    label3.config(text=("Net Balance:",str(bal)))

def withdraw():
    global acca
    wd = float(withd.get())
    if acca>wd:
        acca-=wd
        label4.config(text=("Net balance :",str(acca)))
    else:
        label4.config(text="Insufficient Balance")

def bal():
    global acca
    label5.config(text=("Net balance : ",str(acca)))

def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")



#---------------------------GUI Interface-----------------------#

lbl = Label(f1,font=('aria',16,'bold'),fg="Powder Blue",bg="black",bd=10,anchor='w',text="Enter the account Number :")
lbl.grid(row=0,column=3)
text = Entry(f1,font=('aria',16,'bold'),fg="black",bg="Powder Blue",bd=6,textvariable=number)
text.grid(row=0,column=4)

label = Label(f1,font=('aria',16,'bold'),fg="Powder Blue",bg="black",bd=10,anchor='w')
label.grid(row=1,column=4)
btnsubmit = Button(f2,padx=16,pady=4,bd=10,fg="black",font=('aria',16,'bold'),width=7,text="SUBMIT",bg="Powder Blue",command=bank)
btnsubmit.grid(row=0,column=4)




lbl = Label(f1,font=('aria',16,'bold'),text="Enter the amount to be deposited :",fg="Powder Blue",bg="black",bd=10,anchor='w')
lbl.grid(row=4,column=3)
text = Entry(f1,font=('aria',16,'bold'),fg="black",bg="Powder Blue",bd=6,textvariable=amount,insertwidth=4,justify="right")
text.grid(row=4,column=4)
label3 = Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label3.grid(row=5,column=4)
btndeposit = Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="DEPOSIT",bg="Powder Blue",command=deposit)
btndeposit.grid(row=4,column=4)



lbl = Label(f1,font=('aria',16,'bold'),text="Enter the amount to be Withdrawn :",fg="Powder Blue",bg="black",bd=10,anchor='w')
lbl.grid(row=8,column=3)
text = Entry(f1,font=('aria',16,'bold'),fg="black",bg="Powder Blue",bd=6,textvariable=withd,insertwidth=4)
text.grid(row=8,column=4)



label4 = Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label4.grid(row=9,column=4)
label5 = Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label5.grid(row=10,column=4)


btnwithdraw = Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="Withdraw",bg="Powder Blue",command=withdraw)
btnwithdraw.grid(row=8,column=4)
btnbal = Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="BALANCE",bg="Powder Blue",command=bal)
btnbal.grid(row=10,column=4)
btnreset = Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="RESET",bg="Powder Blue",command=reset)
btnreset.grid(row=11,column=4)
btnexit = Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="EXIT",bg="Powder Blue",command=exit)
btnexit.grid(row=12,column=4)

root.mainloop()
