from tkinter import *
import smtplib

master=Tk()

master.title("Custom Python Email App")

#functions
def send():
    try:
        username=temp_username.get()
        password=temp_password.get()
        to=temp_receiver.get()
        subject=temp_subject.get()
        body=temp_body.get()
        if(username=="" or password=="" or to=="" or subject=="" or body==""):
            notif.config(text="All fileds requried",fg="red")
        else:
            finalMessage="Subject:{}\n\n{}".formate(subject,body)
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username,password)
            server.sendmail(username,to,finalMessage)
            notif.config(text="Email has been send to:"+to,fg="green")
    except:
        notif.config(text="Error sending email",fg="red")



def reset():
    print("reset")
    userName.delete(0,"end")
    userPass.delete(0,"end")
    subjectEntry.delete(0,"end")
    bodyEntry.delete(0,"end")
    reciverEntry.delete(0,"end")        
        


Label(master,text="Custom Email App",font=('Calibri',15)).grid(row=0,sticky=N)
Label(master,text="Use the form below to send an email",font=('Calibri',11)).grid(row=1,padx=5,sticky=W)
Label(master,text="Email",font=('Calibri',11)).grid(row=2,padx=5,sticky=W)
Label(master,text="Password",font=('Calibri',11)).grid(row=3,padx=5,sticky=W)
Label(master,text="To",font=('Calibri',11)).grid(row=4,padx=5,sticky=W)
Label(master,text="Subject",font=('Calibri',11)).grid(row=5,padx=5,sticky=W)
Label(master,text="Body",font=('Calibri',11)).grid(row=6,padx=5,sticky=W)
notif=Label(master,text="",font=('Calibri',11))
notif.grid(row=7,padx=5,sticky=S)

#storage variables
temp_username=StringVar()
temp_password=StringVar()
temp_receiver=StringVar()
temp_subject=StringVar()
temp_body=StringVar()


#
#entries
#
userName=Entry(master,textvariable=temp_username)
userName.grid(row=2,column=0)
userPass=Entry(master,show='*',textvariable=temp_password)
userPass.grid(row=3,column=0)
reciverEntry=Entry(master,textvariable=temp_receiver)
reciverEntry.grid(row=4,column=0)
subjectEntry=Entry(master,textvariable=temp_subject)
subjectEntry.grid(row=5,column=0)
bodyEntry=Entry(master,textvariable=temp_body)
bodyEntry.grid(row=6,column=0)

#
#buttons
#
Button(master,text="Send",command=send).grid(row=7,sticky=W,padx=5,pady=15)
Button(master,text="Reset",command=reset).grid(row=7,sticky=W,padx=45,pady=45)


master.mainloop()