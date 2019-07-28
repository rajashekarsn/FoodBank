from tkinter import *
import sqlite3
import tkinter.ttk as ttk
from tkinter import Text

root = Tk()
root.title("Guelph Student - Food Bank")

fpData = ttk.Treeview(height=10, columns=('Student ID','Name','Email','FP Claimed','FP Available'))
fpData.grid(row=10, column=0, columnspan=5)

scrollBar = Scrollbar(root, orient="vertical",command=fpData.yview)
scrollBar.grid(row=10, column=6, sticky="NSE")
fpData.configure(yscrollcommand=scrollBar.set)


fpData.heading('#0',text="Student ID")
fpData.heading('#1',text="Name")
fpData.heading('#2',text="Email")
fpData.heading('#3',text="FP Claimed")
fpData.heading('#4',text="FP Available")
fpData.heading('#5',text="Date")
# ----------------db setup ------------------------
conn = sqlite3.connect('foodbank.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS "students"
                        ("studentID"	INTEGER,
                        "name"	TEXT,"emailID"	TEXT,
                        "adultDependents"	INTEGER,
                        "childrenDependents" INTEGER,
                        "eligibleFoodPoints"	INTEGER)""")
# # alter a table, add new column
# c.execute("""ALTER TABLE table_name
#             ADD column_name Type""")


# c.execute('''SELECT * FROM students''')
# print(c.fetchone())

# ----------------db setup -------

studentID = StringVar()
studentName = StringVar()
universityEmailID = StringVar()
dependentsAdults = IntVar()
dependentsChildren = IntVar()
foodPoints = IntVar()
Val1 = IntVar()

Label(root,text="Student ID:").grid(row=0,sticky= W)
Entry(root,textvar=studentID).grid(row=0,column=1)

Label(root,text="Name:").grid(row=1, sticky = W)
Entry(root,textvar=studentName).grid(row=1,column=1)

Label(root,text="University Email:").grid(row=2, sticky = W)
Entry(root,textvar=universityEmailID).grid(row=2,column=1)

Label(root,text="@uoguelph.ca").grid(row=2,column=2, sticky = W)

Label(root,text="Adults:").grid(row=3, sticky = W)
Entry(root, textvar=dependentsAdults).grid(row=3,column=1)

Label(root,text="Children:").grid(row=4, sticky = W)
Entry(root, textvar=dependentsChildren).grid(row=4,column=1)

Label(root,text="Food Points:").grid(row=6, sticky = W)
Entry(root,textvar=foodPoints).grid(row=6,column=1)


def calcfoodpoints():
    foodVal = (dependentsAdults.get() + dependentsChildren.get())*30
    foodPoints.set(foodVal)

# pickedfp = 0
# def fpConsumed():
#     actualfp = actualfp - pickedfp

def insert():
    student_data = [(studentID.get(),
                    studentName.get(),
                    universityEmailID.get(),
                    dependentsAdults.get(),
                    dependentsChildren.get(),
                    foodPoints.get())]

    # c.execute("INSERT INTO students (studentID, name, emailID, adultDependents, childrenDependents, eligibleFoodPoints) VALUES (?,?,?,?,?,?)",studentData)
    c.executemany("INSERT INTO students VALUES (?,?,?,?,?,?)",student_data)
    conn.commit()
    conn.close()

but1=Button(root,text='Calculate Food Points', command=calcfoodpoints,font=('none 10 bold')).grid(row=5, column=1)

but2=Button(root,text='Submit',command=insert,font=('none 13 bold')).grid(row=9, sticky = E)


# -----Menu------------------
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
# fileMenu.add_command(label="Add Student", command = insert)
# subMenu.add_command(label="Food Points", command = addPoints())
# subMenu.add_command(label="Exit", command = quitApp())

# editMenu = Menu(menu)
# menu.add_cascade(label="Food Points",menu=editMenu)
# editMenu.add_command(label="Add Student", command = addStudent())


if __name__ == '__main__':
    root.mainloop()
