from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("Employee.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#7FE9DE")
root.state("zoomed")


name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

entries_frame=Frame(root,bg="#FF55BB")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("calibri",20,"bold"),bg="#454545",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

Name=Label(entries_frame,text="Name",font=("Calibri",16),bg="#454545",fg="white")
Name.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("Clabiri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

Age=Label(entries_frame,text="Age",font=("Calibri",16),bg="#454545",fg="white")
Age.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entries_frame,textvariable=age,font=("Clabiri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

Doj=Label(entries_frame,text="DOJ",font=("Calibri",16),bg="#454545",fg="white")
Doj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtDoj=Entry(entries_frame,textvariable=doj,font=("Clabiri",16),width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

Email=Label(entries_frame,text="Email",font=("Calibri",16),bg="#454545",fg="white")
Email.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail=Entry(entries_frame,textvariable=email,font=("Clabiri",16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

Gender=Label(entries_frame,text="Gender",font=("Calibri",16),bg="#454545",fg="white")
Gender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entries_frame,font=("Clabiri",16),width=28,textvariable=gender,state="readonly")
comboGender['values']=("Male", "Female")
comboGender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

Contact=Label(entries_frame,text="Contact",font=("Calibri",16),bg="#454545",fg="white")
Contact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtContact=Entry(entries_frame,textvariable=contact,font=("Clabiri",16),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

Address=Label(entries_frame,text="Address",font=("Calibri",16),bg="#454545",fg="white")
Address.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtAddress=Text(entries_frame,width=80,height=5, font=("Calibri",16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,pady=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[5])
    email.set(row[4])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])
def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get()=="" or  txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(1.0,END)=="":
               messagebox.showerror("Error in Input","Please fill all the details")
               return
    db.insert(txtName.get(), txtAge.get(), txtDoj.get(),txtEmail.get(),comboGender.get(),  txtContact.get(), txtAddress.get(1.0,END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayall()
def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get()=="" or  txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(1.0,END)=="":
               messagebox.showerror("Error in Input","Please fill all the details")
               return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(),txtEmail.get(),comboGender.get(),  txtContact.get(), txtAddress.get(1.0,END))
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    displayall()

def delete_employee():
    db.remove(row[0])
    clearAll()
    displayall()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)

btn_frame=Frame(entries_frame, bg="#454545")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd = Button(btn_frame,command=add_employee,text="Add Details", width=15,font=("Calibri",16,"bold"),bg="green",fg="white",bd=0).grid(row=0,column=0)

btnEdit=Button(btn_frame,command=update_employee,text="Update Details", width=15,font=("Calibri",16,"bold"),bg="orange",fg="white",bd=0).grid(row=0,column=1, padx=10)

btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details", width=15,font=("Calibri",16,"bold"),bg="red",fg="white",bd=0).grid(row=0,column=2, padx=10)

btnClear=Button(btn_frame,command=clearAll,text="Clear Details", width=15,font=("Calibri",16,"bold"),bg="blue",fg="white",bd=0).grid(row=0,column=3, padx=10)


tree_frame=Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=500, width=1299, height=180)
style=ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 18),rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("Calibri", 18),rowheight=50)
tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=0)
tv.heading("2", text="Name")
tv.column("2", width=5)
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="DOJ")
tv.column("4", width=5)
tv.heading("5", text="Email")
tv.column("5", width=15)
tv.heading("6", text="Gender")
tv.column("6", width=5)
tv.heading("7", text="Contact")
tv.column("7", width=5)
tv.heading("8", text="Address")
tv.column("8", width=5)
tv['show']='headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayall()
displayall()
root.mainloop()


