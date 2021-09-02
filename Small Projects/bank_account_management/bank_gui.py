from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('Bank')
root.iconbitmap('bank.ico')
root.geometry('500x400+200+200')

# ========================================= global variable ==========================================================

user = list()
other_user = list()
value = 0.0

# ========================= creating a database table =================================================================

# conn = sqlite3.connect('bank_data.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE accounts (
#         name text,
#         ph integer,
#         password text,
#         cash float
#         )''')
# conn.commit()
# conn.close()

# ========================= root window label, frame, entry, buttons ==================================================

l_wel = Label(root, text='WELCOME TO MY BANK', font=('Times New Roman', 25, 'bold'))
l_wel.pack(pady=50)
f = LabelFrame(root, bd=2, padx=15, pady=15)
f.pack()

l_ph = Label(f, text='Phone')
l_ph.grid(row=0, column=0, sticky=W, padx=10, pady=5)
l_pass = Label(f, text='Password')
l_pass.grid(row=1, column=0, sticky=W, padx=10, pady=5)
e_ph = Entry(f, width=30)
e_ph.grid(row=0, column=1, sticky=E, padx=10, pady=5, columnspan=4)
e_pass = Entry(f, width=30)
e_pass.grid(row=1, column=1, sticky=E, padx=10, pady=5, columnspan=4)
e_pass.config(show='*')


# ========================= root window functions =====================================================================

def open_reg_window():
    reg = Tk()
    reg.title('Registration')
    reg.geometry('285x160+300+200')
    reg.iconbitmap('bank.ico')

    # register window label, frame, entry, buttons
    l_name_reg = Label(reg, text='Name')
    l_name_reg.grid(row=0, column=0, sticky=W, padx=10, pady=5)
    l_ph_reg = Label(reg, text='Phone')
    l_ph_reg.grid(row=1, column=0, sticky=W, padx=10, pady=5)
    l_pass_reg = Label(reg, text='Password')
    l_pass_reg.grid(row=2, column=0, sticky=W, padx=10, pady=5)
    e_name_reg = Entry(reg, width=30)
    e_name_reg.grid(row=0, column=1, sticky=E, padx=10, pady=5, columnspan=4)
    e_ph_reg = Entry(reg, width=30)
    e_ph_reg.grid(row=1, column=1, sticky=E, padx=10, pady=5, columnspan=4)
    e_pass_reg = Entry(reg, width=30)
    e_pass_reg.grid(row=2, column=1, sticky=E, padx=10, pady=5, columnspan=4)

    e_cash_reg = 0

    def register():
        conn = sqlite3.connect('bank_data.db')
        c = conn.cursor()
        c.execute('''INSERT INTO accounts VALUES (:name, :ph, :password, :cash)''',
                  {
                      'name': e_name_reg.get(),
                      'ph': e_ph_reg.get(),
                      'password': e_pass_reg.get(),
                      'cash': e_cash_reg
                  })
        conn.commit()
        conn.close()

        # message
        messagebox.showinfo('Registration', 'Account has been successfully created.')
        reg.destroy()
        return

    b_register_reg = Button(reg, text='Register', command=register)
    b_register_reg.grid(row=3, column=1, pady=20, ipadx=15)


def login_success():
    global user
    conn = sqlite3.connect('bank_data.db')
    c = conn.cursor()
    c.execute('SELECT *, oid FROM accounts')
    records = c.fetchall()
    print(records)
    for record in records:
        if e_ph.get() == str(record[1]) and e_pass.get() == str(record[2]):
            user = list(record)
            print('USER : ', user)
            return True


def login_window():
    global user
    if login_success():
        root.destroy()
        # new login window
        log = Tk()
        log.title(f'Login Successful ({user[0]})')
        log.geometry('400x400+300+200')
        log.iconbitmap('bank.ico')
        # two frames
        f1 = LabelFrame(log, bd=2, padx=15, pady=15, text='Account Information')
        f1.pack(fill=BOTH, padx=20, pady=10)
        f2 = LabelFrame(log, bd=2, padx=15, pady=15, text='Options')
        f2.pack(fill=BOTH, padx=20, pady=10)

        def show_bal():  # function to show latest balance
            l_bal = Label(f1, text=f"Balance = $ {user[3]}")
            l_bal.grid(row=0, column=0, sticky=W)

        show_bal()

        def amount_window(para):
            global user
            amt_win = Tk()
            amt_win.title('')
            amt_win.iconbitmap('bank.ico')
            # show amount label and entry
            l_amt = Label(amt_win, text=f"Amount", padx=10, pady=5)
            l_amt.grid(row=0, column=0, sticky=W)
            e_amt = Entry(amt_win, width=30)
            e_amt.grid(row=0, column=1, sticky=E, padx=10, pady=5, columnspan=4)

            def update_cash(option):
                global value, user
                value = e_amt.get()
                if option == 'w':
                    user[3] = user[3] - float(value)
                elif option == 'd':
                    user[3] = user[3] + float(value)

                # update database
                conn = sqlite3.connect('bank_data.db')
                c = conn.cursor()
                c.execute('''UPDATE accounts SET
                    cash = :amt
                    WHERE oid = :oid''',
                          {'amt': user[3],
                           'oid': user[4]
                           })
                conn.commit()
                conn.close()

                # update the bal label
                show_bal()
                amt_win.destroy()
                return

            b_submit = Button(amt_win, text='SUBMIT', command=lambda: update_cash(para), width=15)
            b_submit.grid(row=3, column=1, padx=10, pady=5)
            return

        b_withdraw = Button(f2, text='Withdraw Money', width=15, command=lambda: amount_window('w'))
        b_withdraw.grid(row=2, column=0, pady=10, padx=10, ipadx=15)

        b_deposit = Button(f2, text='Deposit Money', width=15, command=lambda: amount_window('d'))
        b_deposit.grid(row=2, column=1, pady=10, padx=10, ipadx=15)

        # transfer money:
        def get_user_data():
            global e_ph2, other_user, value
            conn = sqlite3.connect('bank_data.db')
            c = conn.cursor()
            c.execute('SELECT *, oid FROM accounts')
            records = c.fetchall()
            for record in records:
                if e_ph2.get() == str(record[1]):
                    other_user = list(record)
                    print('OTHER USER : ', other_user)

        def transfer_window():
            global e_ph2, e_amt2, value
            trans = Tk()
            trans.title('Transfer')
            trans.iconbitmap('bank.ico')

            def transfer():
                global e_amt2, value
                get_user_data()
                value = e_amt2.get()
                user[3] = user[3] - float(value)
                other_user[3] = other_user[3] + float(value)
                # update database
                conn = sqlite3.connect('bank_data.db')
                c = conn.cursor()
                c.execute('''UPDATE accounts SET
                                    cash = :amt
                                    WHERE oid = :oid''',
                          {'amt': user[3],
                           'oid': user[4]
                           })
                conn.commit()
                c.execute('''UPDATE accounts SET
                                                cash = :amt
                                                WHERE oid = :oid''',
                          {'amt': other_user[3],
                           'oid': other_user[4]
                           })
                conn.commit()
                conn.close()
                print('OTHER: ', other_user)
                show_bal()
                trans.destroy()
                return

            # show amount label and entry
            l_ph2 = Label(trans, text=f"Phone", padx=10, pady=5)
            l_ph2.grid(row=0, column=0, sticky=W)
            e_ph2 = Entry(trans, width=30)
            e_ph2.grid(row=0, column=1, sticky=E, padx=10, pady=5, columnspan=4)
            l_amt2 = Label(trans, text=f"Amount", padx=10, pady=5)
            l_amt2.grid(row=1, column=0, sticky=W)
            e_amt2 = Entry(trans, width=30)
            e_amt2.grid(row=1, column=1, sticky=E, padx=10, pady=5, columnspan=4)

            b_submit2 = Button(trans, text='SUBMIT', command=transfer, width=15)
            b_submit2.grid(row=2, column=1, padx=10, pady=5)
            return

        b_transfer = Button(f2, text='Transfer Money', width=15, command=transfer_window)
        b_transfer.grid(row=3, column=0, pady=10, padx=10, ipadx=15)

        # update account info
        def open_update_window():
            upd = Tk()
            upd.title('Update Information')
            upd.geometry('285x160+300+200')
            upd.iconbitmap('bank.ico')

            # upd window label, frame, entry, buttons
            l_name_upd = Label(upd, text='Name')
            l_name_upd.grid(row=0, column=0, sticky=W, padx=10, pady=5)
            l_ph_upd = Label(upd, text='Phone')
            l_ph_upd.grid(row=1, column=0, sticky=W, padx=10, pady=5)
            l_pass_upd = Label(upd, text='Password')
            l_pass_upd.grid(row=2, column=0, sticky=W, padx=10, pady=5)
            e_name_upd = Entry(upd, width=30)
            e_name_upd.grid(row=0, column=1, sticky=E, padx=10, pady=5, columnspan=4)
            e_ph_upd = Entry(upd, width=30)
            e_ph_upd.grid(row=1, column=1, sticky=E, padx=10, pady=5, columnspan=4)
            e_pass_upd = Entry(upd, width=30)
            e_pass_upd.grid(row=2, column=1, sticky=E, padx=10, pady=5, columnspan=4)

            e_name_upd.insert(0, user[0])
            e_ph_upd.insert(0, user[1])
            e_pass_upd.insert(0, user[2])

            def update_submission():
                conn = sqlite3.connect('bank_data.db')
                c = conn.cursor()
                c.execute('''UPDATE accounts SET
                                                    name = :name,
                                                    ph = :ph,
                                                    password = :password                                                                                                        
                                                    WHERE oid = :oid''',
                          {'name': e_name_upd.get(),
                           'ph': e_ph_upd.get(),
                           'password': e_pass_upd.get(),
                           'oid': user[4]
                           })
                conn.commit()
                conn.close()
                upd.destroy()
                log.destroy()
                return

            b_sub_upd = Button(upd, text='Submit', command=update_submission)
            b_sub_upd.grid(row=3, column=1, pady=20, ipadx=15)

        b_update = Button(f2, text='Update Account Info', width=15, command=open_update_window)
        b_update.grid(row=3, column=1, pady=10, padx=10, ipadx=15)

        # delete account
        def delete():
            conn = sqlite3.connect('bank_data.db')
            c = conn.cursor()
            c.execute('''DELETE FROM accounts WHERE oid = :oid''', {'oid': user[4]})
            conn.commit()
            conn.close()

        def delete_account():
            ans = messagebox.askokcancel('Confirmation', 'Press OK to permanently delete your account.')
            if ans:
                delete()
                messagebox.showinfo('', 'account Deleted successfully')
                log.destroy()
            else:
                messagebox.showinfo('', 'cancelled')


        b_update = Button(f2, text='Delete Account', width=15, command=delete_account)
        b_update.grid(row=4, column=1, pady=10, padx=10, ipadx=15)

        b_logout = Button(f2, text='Log out', width=15)
        b_logout.grid(row=4, column=0, pady=10, padx=10, ipadx=15)

    else:
        messagebox.showwarning('Warning', 'Wrong Details. Try again.')
    return


# ========================= root buttons ==============================================================================

b_login = Button(f, text='Login', command=login_window)
b_login.grid(row=2, column=1, pady=30, ipadx=15)
b_register = Button(f, text='Register', command=open_reg_window)
b_register.grid(row=2, column=2, pady=30, ipadx=15)

root.mainloop()
