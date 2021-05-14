from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
import tkinter.scrolledtext as st
import os
import csv
import json
import base64
import sqlite3
import shutil
import subprocess
import win32crypt
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
#___________________________________________________________________________________________________________
def DD1():
                r=Tk()
                r.config(bg="#f5e04b")
                r1=Label(r,font=('Monotype',20),text='''"""
This Programs composes of more than 200 lines but none of them is copied from any website
or any video. Every Copyright is respected.
                                                                  Acknowledgement
                                                                        GOOGLE

                                                                                                                               Thanking You
                                                                                                                                Shubhashis Mondal

''',bg="#fdf88e").grid(row=1,column=1)
#_______________________________________________sign in page_____________________________________________________
def get(login_screen,username_login_entry,password__login_entry,password__login_entry1):  
    username_sign_entry=username_login_entry.get()
    signin_password=password__login_entry.get()
    signin_password1=password__login_entry1.get()
    if username_sign_entry!='' or signin_password!='' or signin_password1!='' :
        if signin_password==signin_password1:
            fields = ['USERNAME', 'PASSWORD']
            rows = [[username_sign_entry,signin_password]]
            filename = "doc/up.csv"
            with open(filename, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)
                csvwriter.writerows(rows)

            tkinter.messagebox.showinfo("username and password", 'username  :'+username_sign_entry+'\n'+'password  :'+signin_password)
       
    else:
        tkinter.messagebox.showinfo("Error", "please try again")
    login_screen.destroy()
    print([username_sign_entry,signin_password,signin_password1])
def signinPage():
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen)
    username_login_entry.pack()
    Label(login_screen, text="Password").pack()
    password__login_entry = Entry(login_screen)
    password__login_entry.pack()
    Label(login_screen, text="Renter Password").pack()
    password__login_entry1 = Entry(login_screen)
    password__login_entry1.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Sign in", width=10, height=1,command=lambda:get(login_screen,username_login_entry,password__login_entry,password__login_entry1)).pack()
    login_screen.mainloop()
#________________________________________________________________________________________________________________
def g(x):
    try:
        x.destroy()
    except:
        pass
    global counter ,label
    s=Tk()
    s.geometry("6000x6000")
#________________________________________________background pic________________________________________________________________
    global logo,logo_final
    logo = PhotoImage(file="doc/bg.png")
    logo_final= Label(s,image=logo,bg='#FFFFFF',fg = "Blue").place(x=0,y=0)
#_____________________________________entry boxes and log in button and about button________________________________________________________________
    e1=Entry(s,bd=10,font = ('arial', 16, 'bold'),width=30,bg='#bc946b',insertwidth = 5)
    e1.place(x=600,y=250)
    e2=Entry(s,bd=10,font = ('arial', 16, 'bold'),width=30,bg='#bc946b',insertwidth = 5,show="*")
    e2.place(x=600,y=400)
    Button(s, padx = 8, pady = 16, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10,activebackground="green", text = "Log in", bg = '#42f1ff', command = lambda:ho(e1,e2,s)).place(x=550,y=550)
    Button(s, padx = 8, pady = 16, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10,activeforeground="green" ,text = "ABOUT", bg = '#42f1ff', command = lambda:DD1()).place(x=1350,y=100)
    Button(s, padx = 8, pady = 16, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10,activebackground="green", text = "Sign in", bg = '#42f1ff',command=lambda:signinPage()).place(x=750,y=550)
#______________________________________time_______________________________________________________________
    t=datetime.now()
    date=t.date()
    counter=t.time().isoformat(timespec='seconds')
    label =Label(s, text="",bg='#f8d305', fg="black", font="Verdana 20") 
    label.place(x=1366,y=0)
    label1 =Label(s, text="TIME",bg='#f8d305', fg="black", font="Verdana 20 bold") 
    label1.place(x=1282,y=0)
    label2 =Label(s, text="DATE",bg='#f8d305', fg="black", font="Verdana 20 bold") 
    label2.place(x=1280,y=38)
    label3 =Label(s, text=date,bg='#f8d305', fg="black", font="Verdana 20") 
    label3.place(x=1366,y=38)
    label.after(1000, count)
    s.mainloop()
def count():
    global counter 
    display=str(counter)
    label['text']=" "+display+"   "
    label.after(1000, count)
    t=datetime.now()
    counter =t.time().isoformat(timespec='seconds')
#______________________________________________wifi____________________________________________________________
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
wl=[]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    wl.append([i+'         ',results])
def wifi():
    win = Tk()
    win.title("wifi password")
    Label(win,text = "wifi password",font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0,row = 0)
    text_area = st.ScrolledText(win,width = 50,height = 20,font = ("Times New Roman",15))
    text_area.grid(column = 0, pady = 50, padx = 50)
    text_area.insert(INSERT,'[USERNAME]                         [PASSWORD]'+'\n'+'______________________________________\n')
    for i in wl:
        text_area.insert(INSERT,str(i)+'\n')
    text_area.configure(state ='disabled')
    win.mainloop()
##################################################chrome###################################################
l=[]
def my_chrome_datetime(time_in_mseconds):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=time_in_mseconds)
def encryption_key():
    localState_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(localState_path, "r", encoding="utf-8") as file:
        local_state_file = file.read()
        local_state_file = json.loads(local_state_file)
    ASE_key = base64.b64decode(local_state_file["os_crypt"]["encrypted_key"])[5:]
    return win32crypt.CryptUnprotectData(ASE_key, None, None, None, 0)[1]
def decrypt_password(enc_password, key):
    try:
        init_vector = enc_password[3:15]
        enc_password = enc_password[15:]
        cipher = AES.new(key, AES.MODE_GCM, init_vector)
        return cipher.decrypt(enc_password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords(logged in with Social Account)"
password_db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "Default", "Login Data")    
shutil.copyfile(password_db_path,"my_chrome_data.db")
db = sqlite3.connect("my_chrome_data.db")
cursor = db.cursor()
cursor.execute("SELECT origin_url, username_value, password_value, date_created FROM logins")
encp_key = encryption_key()
for row in cursor.fetchall():
    site_url = row[0]
    username = row[1]
    password = decrypt_password(row[2], encp_key)
    date_created = row[3]
    l.append([site_url,username,password,str(my_chrome_datetime(date_created))])       
cursor.close()
db.close()
os.remove("my_chrome_data.db")
def cm():
    win = Tk()
    win.title("chrome password")
    Label(win,text = "chrome password",font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0,row = 0)
    text_area = st.ScrolledText(win,width = 100,height = 20,font = ("Times New Roman",15))
    text_area.grid(column = 0, pady = 50, padx = 50)
    for i in l:
        text_area.insert(INSERT,'Address : '+str(i[0])+'\n'+'User ID : '+str(i[1])+'\n'+'Password : '+str(i[2])+'\n'+'Date & Time : '+str(i[3])+'\n'+'---------------------------------------------------------------------------------------------\n')
    text_area.configure(state ='disabled')
    win.mainloop()
###############################################################################################################
def h(s):
    try:
        s.destroy()
    except:
        pass
    global counter,label,phot,phtof
    r=Tk()
    r.geometry('6000x6000')
    phot=PhotoImage(file='doc/321.png')
    photf=Label(r,image=phot).place(x=0,y=0)
    tt=datetime.now()
    date=tt.date()
    counter=tt.time().isoformat(timespec='seconds')
    label=Label(r, text="",bg='#f8d305', fg="black", font="Verdana 20") 
    label.place(x=682,y=0)
    label1=Label(r, text="TIME",bg='#f8d305', fg="black", font="Verdana 20 bold") 
    label1.place(x=600,y=0)
    label2 =Label(r, text="DATE : ",bg='#f8d305', fg="black", font="Verdana 20 bold") 
    label2.place(x=590,y=38)
    label3 =Label(r, text=date,bg='#f8d305', fg="black", font="Verdana 20") 
    label3.place(x=700,y=38)
    label.after(1000, count)
    Button(r, fg = "black", font = ('arial', 14, 'bold'), width = 18,activebackground="green", text = "CHROME PASSWORD", bg = '#42f1ff', command =  lambda:cm()).place(x=1315,y=80)
    Button(r, fg = "black", font = ('arial', 16, 'bold'), width = 15,activebackground="green", text = "WIFI PASSWORD", bg = '#42f1ff', command = lambda:wifi()).place(x=1320,y=122)   
    Button(r, fg = "black", font = ('arial', 16, 'bold'), width = 10,activebackground="green", text = "<<<BACK", bg = 'red', command =lambda:g(r)).place(x=0,y=0)
    r.mainloop()
def ho(e1,e2,s):
    filename = "doc/up.csv"
    rows = []
    with open(filename, 'r') as csvfile:
    	csvreader = csv.reader(csvfile)
    	for row in csvreader:
    		rows.append(row)
    print (rows)
    if [e1.get(),e2.get()] in rows:
        h(s)
    else:
        showinfo("Failed","PLEASE TRY AGAIN AND FILL UP CORRECTLY") 
g(2)





    
    
    
