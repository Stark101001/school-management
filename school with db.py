from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt

window = Tk()
window.geometry("600x400+500+120")
window.resizable(0, 0)
window.title("School")
window.iconbitmap('sc.ico.ico')
f55 = None


# ========================DATA BASE MANAGEMENT=============================
# ========================DATA BASE MANAGEMENT=============================

def Insert_value():
    if Rno.get() and Name.get() and Phy.get() and Che.get() and Maths.get() != "":
        db = sqlite3.connect('school.db')
        cur0 = db.cursor()
        command0 = "insert into ins VALUES('" + Rno.get() + "','" + Name.get() + "','" + Phy.get() + "','" + Che.get() + "','" + Maths.get() + "') "
        cur0.execute(command0)
        db.commit()
        messagebox.showinfo("Info..", 'Data Insertion Successfull')

        Rno.set("")
        Name.set("")
        Phy.set("")
        Che.set("")
        Maths.set("")
        Show_data_1(f55)
    else:
        messagebox.showerror("Error", "All Field's Are Required")


def Reg_1():
    if reg_e1.get() and reg_e3.get() and reg_e2.get() != "":
        db = sqlite3.connect('school.db')
        cur1 = db.cursor()
        command1 = "insert into regis VALUES('" + reg_e1.get() + "','" + reg_e2.get() + "','" + reg_e3.get() + "') "
        cur1.execute(command1)
        db.commit()
        messagebox.showinfo("Info..", 'Registration Successfull')
        reg_e1.set("")
        reg_e2.set("")
        reg_e3.set("")
    else:
        messagebox.showerror("Error", "All Field's Are Required")


def Log_1():
    db = sqlite3.connect('school.db')
    cur2 = db.cursor()
    command2 = "select * from regis where UNAME='" + log_e1.get() + "' AND UPASS='" + log_e2.get() + "'"
    ld = cur2.execute(command2)
    for up in ld:
        My_menu()
        log_e1.set("")
        log_e2.set("")
        break
    else:
        messagebox.askretrycancel("Title", 'Incorrect Username or Password')
    db.commit()


# ========================DATA BASE MANAGEMENT=============================
# ========================DATA BASE MANAGEMENT=============================

# ========================FRONT End DESIGN=================================
# ========================FRONT End DESIGN=================================
reg_e1 = StringVar()
reg_e2 = StringVar()
reg_e3 = StringVar()


def Registration():
    f1_reg = Frame(bg='lightblue')
    f1_reg.place(x=0, y=0, width=600, height=400)

    l4_reg = Label(f1_reg, text='Registration Page', fg='red', font=("arial", 25, 'bold'), bg='lightblue')
    l4_reg.place(x=180, y=50)

    l1_reg = Label(f1_reg, text='Enter Name', bg='lightblue', font=("arial", 12))
    l1_reg.place(x=190, y=125)

    l2_reg = Label(f1_reg, text='Enter Pass', bg='lightblue', font=("arial", 12))
    l2_reg.place(x=190, y=180)

    l3_reg = Label(f1_reg, text='Enter C.N', bg='lightblue', font=("arial", 12))
    l3_reg.place(x=190, y=235)

    e1_reg = Entry(f1_reg, textvariable=reg_e1)
    e1_reg.place(x=300, y=125)

    e2_reg = Entry(f1_reg, show='*', textvariable=reg_e2)
    e2_reg.place(x=300, y=180)

    e3_reg = Entry(f1_reg, textvariable=reg_e3)
    e3_reg.place(x=300, y=235)

    b1_reg = Button(f1_reg, text='Back', bg='yellow', command=Home, width=7)
    b1_reg.place(x=0, y=0)

    b2_reg = Button(f1_reg, text='Register', bg='#09F2ED', width=10, height=2, command=Reg_1)
    b2_reg.place(x=280, y=280)

    b3_reg = Button(f1_reg, text="Home", fg='black', bg='#0C4DF2', width=10, height=2, command=Home)
    b3_reg.place(x=7, y=354)

    b4_reg = Button(f1_reg, text="Login", bg='#0C4DF2', width=10, height=2, command=Login)
    b4_reg.place(x=515, y=354)


log_e1 = StringVar()
log_e2 = StringVar()


# =================================LOGIN=====================================
def Login():
    f2_login = Frame(bg='lightblue')
    f2_login.place(x=0, y=0, width=600, height=400)

    l3_login = Label(f2_login, text='Login Page', font=("arial", 30, 'bold'), bg='lightblue', fg='red')
    l3_login.place(x=200, y=30)

    l1_login = Label(f2_login, text='Enter Name', bg='lightblue', font=("arial", 12))
    l1_login.place(x=190, y=125)

    l2_login = Label(f2_login, text='Enter Pass', bg='lightblue', font=("arial", 12))
    l2_login.place(x=190, y=180)

    e1_login = Entry(f2_login, textvariable=log_e1)
    e1_login.place(x=300, y=125)

    e2_login = Entry(f2_login, show='*', textvariable=log_e2)
    e2_login.place(x=300, y=180)

    b2_login = Button(f2_login, text="Login", bg='green', fg='yellow', width=10, height=2, command=Log_1)
    b2_login.place(x=290, y=230)

    b3_login = Button(f2_login, text='Back', bg='grey', fg='white', command=Home, width=7)
    b3_login.place(x=0, y=0)

    b4_login = Button(f2_login, text="Registration", bg='#0C4DF2', width=10, height=2, command=Registration)
    b4_login.place(x=515, y=354)

    b5_login = Button(f2_login, text="Home", bg='#0C4DF2', width=10, height=2, command=Home)
    b5_login.place(x=7, y=354)


# ====================================================================
def Logout():
    Log = messagebox.askyesno("Logout", "You Want To Logout?")
    if Log == 1:
        Home()
    else:
        pass


def My_menu():
    n = ttk.Notebook()
    n.place(x=0, y=0, width=600, height=400)
    b1_my_menu = Button(n, text='Logout', width=9, command=Logout, bg="grey")
    b1_my_menu.place(x=530, y=-2)

    # Menu bar command
    Insert_data(n)
    Show_data(n)
    Search_data(n)
    Update_data(n)
    Delete_data(n)
    Graph_data(n)


# ^^^^^^^^^^^^^^^^^^

# =============================Insert Data=============================
Rno = StringVar()
Name = StringVar()
Phy = StringVar()
Che = StringVar()
Maths = StringVar()


def Insert_data(n):
    f1_insert = Frame(bg='lightblue')
    n.add(f1_insert, text='Insert')

    l1_insert = Label(f1_insert, text='Enter RNo.', bg='lightblue', font=("arial", 12))
    l1_insert.place(x=150, y=50)

    l1_insert = Label(f1_insert, text='Enter Name', bg='lightblue', font=("arial", 12))
    l1_insert.place(x=150, y=100)

    l1_insert = Label(f1_insert, text='Phy.Marks', bg='lightblue', font=("arial", 12))
    l1_insert.place(x=150, y=150)

    l1_insert = Label(f1_insert, text='Che.Marks', bg='lightblue', font=("arial", 12))
    l1_insert.place(x=150, y=200)

    l1_insert = Label(f1_insert, text='Maths.Marks', bg='lightblue', font=("arial", 12))
    l1_insert.place(x=150, y=250)

    e1_insert = Entry(f1_insert, textvariable=Rno)
    e1_insert.place(x=250, y=50)

    e2_insert = Entry(f1_insert, textvariable=Name)
    e2_insert.place(x=250, y=100)

    e3_insert = Entry(f1_insert, textvariable=Phy)
    e3_insert.place(x=250, y=150)

    e4_insert = Entry(f1_insert, textvariable=Che)
    e4_insert.place(x=250, y=200)

    e5_insert = Entry(f1_insert, textvariable=Maths)
    e5_insert.place(x=250, y=250)

    b1_insert = Button(f1_insert, text="Insert", width=12, height=2, command=Insert_value)
    b1_insert.place(x=230, y=295)

    bu = Button(f1_insert, text="back", command=Login, width=10)
    bu.place(x=0, y=340)


# ==========================Show Data==============================
def Show_data(n):
    f1_show = Frame(bg='pink')
    n.add(f1_show, text='Show All')
    global f55
    f55 = f1_show
    Show_data_1(f1_show)


def Show_data_1(f1_show):
    for w in f1_show.winfo_children():
        w.destroy()
    b1_show_data = Button(f1_show, text='Refresh', command=None)
    b1_show_data.place(x=270, y=0)

    l1_Show_data = Label(f1_show, text="Roll No.", font=('arial', 13, 'bold', 'underline'), bg='pink')
    l1_Show_data.place(x=20, y=30)

    l2_Show_data = Label(f1_show, text="Name", font=('arial', 13, 'bold', 'underline'), bg='pink')
    l2_Show_data.place(x=95, y=30)

    l3_Show_data = Label(f1_show, text="Phy Marks", font=('arial', 13, 'bold', 'underline'), bg='pink')
    l3_Show_data.place(x=230, y=30)

    l4_Show_data = Label(f1_show, text="Che Marks", font=('arial', 13, 'bold', 'underline'), bg='pink')
    l4_Show_data.place(x=360, y=30)

    l5_Show_data = Label(f1_show, text="Math Marks", font=('arial', 13, 'bold', 'underline'), bg='pink')
    l5_Show_data.place(x=500, y=30)

    data5 = sqlite3.connect('school.db')
    cur4 = data5.cursor()
    command4 = "select * from ins "
    d = cur4.execute(command4)
    x = 20
    y = 60
    for row in d:
        l0_show_data = Label(f1_show, text=row[0], font=('arial', 10, 'bold'), bg='pink')
        l0_show_data.place(x=x, y=y)

        x += 77

        l6_show_data = Label(f1_show, text=row[1], font=('arial', 10, 'bold'), bg='pink')
        l6_show_data.place(x=x, y=y)

        x += 160

        l7_show_data = Label(f1_show, text=row[2], font=('arial', 10, 'bold'), bg='pink')
        l7_show_data.place(x=x, y=y)

        x += 140

        l8_show_data = Label(f1_show, text=row[3], font=('arial', 10, 'bold'), bg='pink')
        l8_show_data.place(x=x, y=y)

        x += 140

        l9_show_data = Label(f1_show, text=row[4], font=('arial', 10, 'bold'), bg='pink')
        l9_show_data.place(x=x, y=y)

        x = 20
        y += 30


# =======================Search Data==================================
sd = StringVar()


def Search_data(n):
    f1_search = Frame(bg='cyan')
    n.add(f1_search, text='Search')
    l1_search = Label(f1_search, text='Roll No. =', bg='cyan', font=("arial", 14))
    l1_search.place(x=115, y=20)
    e1_search = Entry(f1_search, font=("", 12), textvariable=sd)
    e1_search.place(x=220, y=22)

    l5_Show_data = Label(f1_search, text="Name", font=('arial', 13, 'bold', 'underline'), bg='cyan')
    l5_Show_data.place(x=55, y=65)

    l6_Show_data = Label(f1_search, text="Phy Marks", font=('arial', 13, 'bold', 'underline'), bg='cyan')
    l6_Show_data.place(x=190, y=65)

    l7_Show_data = Label(f1_search, text="Che Marks", font=('arial', 13, 'bold', 'underline'), bg='cyan')
    l7_Show_data.place(x=320, y=65)

    l8_Show_data = Label(f1_search, text="Math Marks", font=('arial', 13, 'bold', 'underline'), bg='cyan')
    l8_Show_data.place(x=460, y=65)

    def Search_data1():

        data5 = sqlite3.connect('school.db')
        cur4 = data5.cursor()
        command4 = "select * from ins where URNO='" + sd.get() + "' "
        d = cur4.execute(command4)

        for row in d:
            l0_searchdata1 = Label(f1_search, bg='cyan', text="                  ", font=("arial", 15, 'bold'), height=50,
                                   width=600)
            l0_searchdata1.place(x=60, y=100)

            l1_searchdata1 = Label(f1_search, bg='cyan', text=row[1], font=("arial", 12))
            l1_searchdata1.place(x=53, y=100)

            l2_searchdata1 = Label(f1_search, bg='cyan', text=row[2], font=("arial", 12))
            l2_searchdata1.place(x=220, y=100)

            l3_searchdata1 = Label(f1_search, bg='cyan', text=row[3], font=("arial", 12))
            l3_searchdata1.place(x=350, y=100)

            l4_searchdata1 = Label(f1_search, bg='cyan', text=row[4], font=("arial", 12))
            l4_searchdata1.place(x=500, y=100)
            sd.set("")
            break
        else:
            l9_searchdata1 = Label(f1_search, bg='cyan', text=" ", font=("arial", 15, 'bold'), height=30, width=600)
            l9_searchdata1.place(x=0, y=100)
            sd.set("")
            messagebox.showerror("Error", "Roll No. Not Found")

        data5.commit()

    b1_search = Button(f1_search, text='Find', width=10, height=-1, command=Search_data1)
    b1_search.place(x=420, y=20)


# def Search_data1(f1_search):


# =====================Update Data===================================


def Update_data(n):
    f1_update = Frame(bg='pink')
    ud = StringVar()
    n.add(f1_update, text='Update')

    l1_update_data = Label(f1_update, text='Roll No. =', bg='pink', font=("arial", 14))
    l1_update_data.place(x=115, y=20)
    e1_update_data = Entry(f1_update, font=("", 12), textvariable=ud)
    e1_update_data.place(x=220, y=22)

    def Update_data1():
        sd1 = StringVar()
        sd2 = StringVar()
        sd3 = StringVar()
        sd4 = StringVar()

        data5 = sqlite3.connect('school.db')
        cur4 = data5.cursor()
        command4 = "select * from ins where URNO='" + ud.get() + "' "
        d = cur4.execute(command4)

        for row in d:

            l5_Update_data1 = Label(f1_update, text="Name", font=('arial', 13, 'bold', 'underline'), bg='pink')
            l5_Update_data1.place(x=55, y=65)

            l6_Update_data1 = Label(f1_update, text="Phy Marks", font=('arial', 13, 'bold', 'underline'), bg='pink')
            l6_Update_data1.place(x=190, y=65)

            l7_Update_data1 = Label(f1_update, text="Che Marks", font=('arial', 13, 'bold', 'underline'), bg='pink')
            l7_Update_data1.place(x=320, y=65)

            l8_Update_data1 = Label(f1_update, text="Math Marks", font=('arial', 13, 'bold', 'underline'), bg='pink')
            l8_Update_data1.place(x=460, y=65)

            e1_Update_data1 = Entry(f1_update, textvariable=sd1)
            e1_Update_data1.insert(0, row[1])
            e1_Update_data1.place(x=20, y=100)

            e2_Update_data1 = Entry(f1_update, textvariable=sd2)
            e2_Update_data1.insert(0, row[2])
            e2_Update_data1.place(x=170, y=100)

            e3_Update_data1 = Entry(f1_update, textvariable=sd3)
            e3_Update_data1.insert(0, row[3])
            e3_Update_data1.place(x=310, y=100)

            e4_Update_data1 = Entry(f1_update, textvariable=sd4)
            e4_Update_data1.insert(0, row[4])
            e4_Update_data1.place(x=455, y=100)

            def Update_data_2():
                data10 = sqlite3.connect('school.db')
                cur10 = data10.cursor()
                command = "UPDATE ins SET UNAME='" + sd1.get() + "' ,UPHY='" + sd2.get() + "' ,UCHE='" + sd3.get() + "' ,UMATHS='" + sd4.get() + "' WHERE URNO='" + ud.get() + "' "
                cur10.execute(command)
                data10.commit()
                Show_data_1(f55)

                messagebox.showinfo("Title", "Data Updated Successfully")

                sd1.set("")
                sd2.set("")
                sd3.set("")
                sd4.set("")

            b1_Update_data1 = Button(f1_update, text='Update', width=10, command=Update_data_2)
            b1_Update_data1.place(x=260, y=130)

            break
        else:
            messagebox.showerror("Title", "Invalid RollNo..")

    b1_Update_data = Button(f1_update, text='Search', width=10, command=Update_data1)
    b1_Update_data.place(x=445, y=20)


def Delete_data(n):
    f1_delete = Frame(bg='lightblue')
    dd = StringVar()
    n.add(f1_delete, text='Delete')

    l1_Delete_data = Label(f1_delete, text='Roll No. =', bg='lightblue', font=("arial", 14))
    l1_Delete_data.place(x=115, y=20)
    e1_Delete_data = Entry(f1_delete, font=("", 12), textvariable=dd)
    e1_Delete_data.place(x=220, y=22)

    def Delete_data_1():
        if dd.get() == "":
            messagebox.showerror("Error", "Field Are Required")
        else:
            yes = messagebox.askyesno("Delete data", "Are You Sure, You Want To Delete data")
            if yes == 1:

                data11 = sqlite3.connect('school.db')
                cur11 = data11.cursor()
                command = "DELETE FROM ins WHERE URNO='" + dd.get() + "' "
                cur11.execute(command)
                data11.commit()
                data11.close()
                Show_data_1(f55)
                messagebox.showinfo("Title", "Data deleted Successfully")
                dd.set("")
            else:
                pass

    b1_Delete_data = Button(f1_delete, text='Delete', width=10, command=Delete_data_1)
    b1_Delete_data.place(x=445, y=20)


def Graph_data(n):
    f1_graph = Frame(bg='cyan')
    n.add(f1_graph, text='Graph')
    l1_search = Label(f1_graph, text='Roll No. =', bg='cyan', font=("arial", 14))
    l1_search.place(x=115, y=20)
    e1_search = Entry(f1_graph, font=("", 12), textvariable=sd)
    e1_search.place(x=220, y=22)

    def Graph_data1():

        data5 = sqlite3.connect('school.db')
        cur4 = data5.cursor()
        command4 = "select * from ins where URNO='" + sd.get() + "' "
        d = cur4.execute(command4)

        l5_Show_data = Label(f1_graph, text="Name", font=('arial', 13, 'bold', 'underline'), bg='cyan')
        l5_Show_data.place(x=55, y=65)

        l6_Show_data = Label(f1_graph, text="Phy Marks", font=('arial', 13, 'bold', 'underline'), bg='cyan')
        l6_Show_data.place(x=190, y=65)

        l7_Show_data = Label(f1_graph, text="Che Marks", font=('arial', 13, 'bold', 'underline'), bg='cyan')
        l7_Show_data.place(x=320, y=65)

        l8_Show_data = Label(f1_graph, text="Math Marks", font=('arial', 13, 'bold', 'underline'), bg='cyan')
        l8_Show_data.place(x=460, y=65)

        for row in d:
            l0_searchdata1 = Label(f1_graph, bg='cyan', text="            ", font=("arial", 15, 'bold'), height=30,
                                   width=600)
            l0_searchdata1.place(x=100, y=100)

            l1_searchdata1 = Label(f1_graph, bg='cyan', text=row[1], font=("arial", 12))
            l1_searchdata1.place(x=53, y=100)

            l2_searchdata1 = Label(f1_graph, bg='cyan', text=row[2], font=("arial", 12))
            l2_searchdata1.place(x=220, y=100)

            l3_searchdata1 = Label(f1_graph, bg='cyan', text=row[3], font=("arial", 12))
            l3_searchdata1.place(x=350, y=100)

            l4_searchdata1 = Label(f1_graph, bg='cyan', text=row[4], font=("arial", 12))
            l4_searchdata1.place(x=500, y=100)

            l8_Graph_data = Label(f1_graph, font=('arial', 15, 'bold'), bg='cyan',
                                  text='Show Marks In Graph Visulization')
            l8_Graph_data.place(x=20, y=140)

            l9_Graph_data = Label(f1_graph, font=('', 60, 'bold'), fg="red", bg='cyan', text='↓')
            l9_Graph_data.place(x=120, y=165)

            l10_Graph_data = Label(f1_graph, font=('', 60, 'bold'), fg="red", bg='cyan', text='→')
            l10_Graph_data.place(x=260, y=200)

            def Graph_show():

                x = ['Physics', 'Chemistry', 'Maths']  # Subject
                y = [int(row[2]), int(row[3]), int(row[4])]  # Marks
                plt.title(row[1])
                plt.xlabel('Subject')
                plt.ylabel('Marks')
                plt.bar(x, y, color='red')
                plt.show()

            b2_Graph_data = Button(f1_graph, text='Show Graph', width=15, height=3, command=Graph_show)
            b2_Graph_data.place(x=90, y=280)

            # graph=ImageTk.PhotoImage(file='graph.png')
            # graph_ldl=Label(f1_graph,image=graph).pack()

            break
        else:
            l9_searchdata1 = Label(f1_graph, bg='cyan', text=" ", font=("arial", 15, 'bold'), height=30, width=600)
            l9_searchdata1.place(x=0, y=100)
            sd.set("")
            messagebox.showerror("Error", "Roll No. Not Found")

        data5.commit()

    b1_search = Button(f1_graph, text='Find', width=10, height=-1, command=Graph_data1)
    b1_search.place(x=420, y=20)


# =================================HOME======================================
def Home():
    f1_home = Frame(bg='purple')
    f1_home.place(x=0, y=0, width=600, height=400)

    b1_home = Button(f1_home, text='Login', width=14, height=3, command=Login)
    b1_home.place(x=150, y=150)

    b2_home = Button(f1_home, text='Register', width=14, height=3, command=Registration)
    b2_home.place(x=350, y=150)

    l3_home = Label(f1_home, bg='purple', fg='yellow', text='<MR.><Pawan><Kumar>', font=('arial', 13, 'bold'))
    l3_home.place(x=400, y=370)

    l2_home = Label(f1_home, height=4, bg='yellow')
    l2_home.pack(fill=X)

    l1_home = Label(f1_home, text='SCHOOL MANAGEMENT', fg='red', font=('monaco', 30, 'bold'), bg='yellow')
    l1_home.place(x=90, y=15)


Home()
# ========================FRONT End DESIGN================================
# ========================FRONT End DESIGN================================

# ==============Delete empty files from database=========================
# ==============Delete empty files from database=========================
data = sqlite3.connect('school.db')
cur3 = data.cursor()
command3 = "delete from ins WHERE URNO=' ' "
cur3.execute(command3)
data.commit()
# ==============Delete empty files from database==========================
# ==============Delete empty files from database==========================

# ==============Delete empty files from database=========================
# ==============Delete empty files from database=========================
data = sqlite3.connect('school.db')
cur3 = data.cursor()
command3 = "delete from regis WHERE UNAME='ggi' "
cur3.execute(command3)
data.commit()
# ==============Delete empty files from database==========================
# ==============Delete empty files from database==========================


window.mainloop()










