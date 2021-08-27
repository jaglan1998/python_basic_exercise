from valid_inputs.valid_inputs import ValidInput


class Bank:
    def __init__(self):
        self.user_accounts_list = []
        self.user = []
        self.user_index = None
        self.logged_in = False
        self.other_user = []
        self.other_user_index = None

    @staticmethod
    def register(name, ph, password):
        with open('accounts.txt', 'a') as a:
            a.write(f"{name}-{ph}-{password}-0\n")
        print("Account has been created successfully.")

    def import_data(self):  # load the file, and makes lists and nested list
        self.user_accounts_list = []  # need to fresh restart with empty list
        with open('accounts.txt', 'r') as a:
            account_list = (a.read().strip()).split('\n')  # each line in file is one account separated with line
            # account_list --> [account 1, account 2, account 3, ....]
            for account in account_list:  # each account has name, ph, address, notes separated with '-'
                account_details_list = account.split('-')
                # account_details_list --> [name, ph, password, cash]
                self.user_accounts_list.append(account_details_list)
                # self.user_accounts_list --> [[[name, ph, password, cash], [name, ph, password, cash], ....]]
        return self.user_accounts_list

    def export_data(self):  # save data back into the file, for changing information
        if len(self.user) != 0:  # only if the user account have some info
            self.user_accounts_list[self.user_index] = self.user  # updating the master list with latest user info
        with open('accounts.txt', 'w') as a:
            for account in self.user_accounts_list:  # looping each account (nested list with all account details)
                a.write('-'.join(account) + '\n')  # join all account details with '-' and write them in new
        return

    def login(self, ph, password):
        found = False
        self.import_data()  # refresh the list for latest information
        for index, account in enumerate(self.user_accounts_list):  # iterate each account and return index
            if str(ph) == str(account[1]) and str(password) == str(account[2]):  # if both of these values match
                found = True
                self.user = account  # temp save details in list
                self.user_index = index  # temp save index of that particular contact
                self.logged_in = True
        if not found:
            print("Wrong details, try again.")
            self.logged_in = False
        return

    def balance_check(self):
        print(f"Your balance is ${self.user[3]}.")
        return

    def log_out(self):
        print(f"\n'{self.user[0]}' is successfully logged out.\n")
        self.user = []
        self.logged_in = False

    def deposit_money(self, amt):
        if amt > 0:
            self.user[3] = int(self.user[3]) + amt  # updating the amount
            self.user[3] = str(self.user[3])
            self.export_data()  # export the updates
            print(f'${amt} has been successfully deposited.')
        else:
            print('Invalid amount. Try again.')

    def withdraw_money(self, amt):
        if amt <= 0:
            print('Invalid amount. Try again.')
        elif amt > int(self.user[3]):  # if less than account balance
            print("Insufficient funds. Try different amount.")
        else:
            self.user[3] = int(self.user[3]) - amt
            self.user[3] = str(self.user[3])
            self.export_data()  # export the updates
            print(f"Withdraw successful. New balance is ${self.user[3]}")

    def transfer_money(self, amt, name, ph):  # receiver's info
        found = False
        if amt <= 0:
            print('Invalid amount. Try again.')
        elif amt > int(self.user[3]):  # if less than account balance
            print("Insufficient funds. Try different amount.")
        else:
            self.import_data()  # refresh the list for latest information
            for index, account in enumerate(self.user_accounts_list):  # iterate each account and return index
                if str(name) == str(account[0]) and str(ph) == str(account[1]):  # if both of these values match
                    account[3] = int(account[3]) + amt  # added to receiver's account
                    account[3] = str(account[3])
                    self.user[3] = int(self.user[3]) - amt  # minus from user's account
                    self.user[3] = str(self.user[3])
                    self.export_data()
                    found = True
                    print(f"Transfer successful. New balance is ${self.user[3]}")
            if not found:
                print("Wrong details, try again. No such account found.")
        return

    def change_user_details(self, option, new_data):
        if option == 'name':
            self.user[0] = new_data
        elif option == 'ph':
            self.user[1] = new_data
        elif option == 'password':
            self.user[2] = new_data
        else:
            print('Wrong option, choose: name, ph, password')
        self.export_data()
        return

    def delete_account(self, password):
        if password == self.user[2]:
            self.user = []  # empty the user details
            self.user_accounts_list.pop(self.user_index)  # deleting that account
            self.export_data()
        else:
            print("Wrong password. Try again.")


if __name__ == "__main__":

    b = Bank()
    v = ValidInput()

    def home():
        print("----- WELCOME TO MY BANK ------\n")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

    def login_menu():
        print("-------------------------------")
        print("1. Check your balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. Update profile")
        print("6. Delete your account")
        print("7. Log out")
        print("-------------------------------")

    def back_or_logout_menu():
        print("-------------------------------")
        print("1. Back to menu")
        print("2. Log out")
        print("-------------------------------")

    def change_details_menu():
        print("-------------------------------")
        print("1. Change name")
        print("2. Change phone number")
        print("3. Change password")
        print("-------------------------------")

    def valid_amount():
        while True:
            a = input('Amount: $')
            try:
                a = int(a)
                break
            except ValueError:
                print("Value Error. Try again.")
        return a

    def start_program():
        home()
        x = v.get_valid_digit_input(1, 3)  # return valid str options
        if x == '1':
            ph = v.get_valid_ph_no()
            password = v.get_valid_password()
            b.login(ph, password)
            if b.logged_in:

                while True:  # loop back to login menu
                    login_menu()
                    y = v.get_valid_digit_input(1, 7)
                    if y == '1':
                        b.balance_check()
                        back_or_logout_menu()
                        # ----------------- back menu/logout logic -------------------
                        z = v.get_valid_digit_input(1, 2)
                        if z == '1':
                            continue  # will return to back menu
                        elif z == '2':
                            b.log_out()  # will log out
                            start_program()  # restart the program again
                        # --------------------------------------------------------------
                    elif y == '2':
                        amt = valid_amount()  # local function to get valid amount
                        b.deposit_money(amt)
                        continue
                    elif y == '3':
                        amt = valid_amount()
                        b.withdraw_money(amt)
                        continue
                    elif y == '4':
                        amt = valid_amount()
                        name = v.get_valid_name()
                        ph = v.get_valid_ph_no()
                        b.transfer_money(amt, name, ph)
                        continue
                    elif y == '5':
                        change_details_menu()
                        z = v.get_valid_digit_input(1, 3)
                        if z == '1':
                            name = v.get_valid_name()
                            b.change_user_details('name', name)
                        elif z == '2':
                            ph = v.get_valid_ph_no()
                            b.change_user_details('ph', ph)
                        elif z == '3':
                            password = v.get_valid_password()
                            b.change_user_details('password', password)
                        continue
                    elif y == '6':
                        password = v.get_valid_password()
                        b.delete_account(password)
                        continue
                    elif y == '7':
                        b.log_out()
                        start_program()
        elif x == '2':
            name = v.get_valid_name()
            ph = v.get_valid_ph_no()
            password = v.get_valid_password()
            b.register(name, ph, password)
            start_program()  # restart program again
        elif x == '3':
            quit()


    start_program()






