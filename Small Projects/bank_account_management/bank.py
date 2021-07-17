import os


class Bank:
    def __init__(self):
        self.user_details = []  # store temp data in list to access it anytime during login or register
        self.other_user_details = []
        self.logged_in = False  # is logger logged in ? False right now
        self.transfer_valid = False  # is transfer valid ? right info, ph, name etc.
        self.cash = 0  # starting balance is zero.
        self.name = ''  # can be used to store name of the person sometime

    def register(self, name, ph, password):  # we need these 3 parameters which we can pass on with user input.
        cash = self.cash  # in line 19, we want to add cash details in user details of customer
        valid_details = True
        if len(str(ph)) < 10:  # 10 digit ph no.
            print("Wrong Input. Try again")
            valid_details = False
        if len(str(password)) < 5 or len(str(password)) > 20:
            print("Please enter a valid password between 5-10 characters.")
            valid_details = False
        if valid_details is True:
            print("Account has been created.")
            self.user_details = [name, ph, password, cash]  # now all this information is stored in user_details list
            with open(f"{name}.txt", 'w') as f:  # write a txt file with 'name'
                for details in self.user_details:  # looping through user_details list to write each element
                    f.write(str(details) + '\n')  # with \n
        return

    def login(self, name, ph, password):
        with open(f"{name}.txt", 'r') as f:
            details = f.read()  # read file in string
            self.user_details = details.split("\n")  # braking down details string with \n to store into list
            if str(ph) in self.user_details:  # name is already confirmed, checking ph
                if str(password) in self.user_details:  # check password if it exists in user_details
                    self.logged_in = True
            if self.logged_in is True:
                print(f"User '{name}' logged in successfully.")
                self.cash = int(self.user_details[3])  # show the int cash from user_details
                self.name = name  # store the name is init function
        return

    def balance_check(self):
        balance = self.cash  # will show the cash stored while login into init
        print("Your balance is $", balance)
        return

    def log_out(self):
        print(f"'{self.name}' is successfully logged out.")  # login --> store 'name' into init function
        self.logged_in = False
        return

    def deposit_money(self, amount):  # amount parameter will be asked as a user input
        if amount > 0:  # we want amount more than 0
            self.cash = self.cash + amount  # the temp value in self.cash will change
            print(f"Deposit successful. New balance is '${self.cash}'")

            # now we want to add this change to data file

            with open(f"{self.name}.txt", 'r') as f:  # first read the data file
                details = f.read()
                self.user_details = details.split("\n")  # download the data
            with open(f"{self.name}.txt", 'w') as f:  # write the same data but now slightly edited
                f.write(details.replace(self.user_details[3], str(self.cash)))  # upload the data with cash replaced
        else:
            print("Invalid amount. Amount must be > 0")
        return

    def withdraw_money(self, amount):
        if self.cash > amount:
            self.cash = self.cash - amount
            print(f"Withdraw successful. New balance is '${self.cash}'")
            with open(f"{self.name}.txt", 'r') as f:
                details = f.read()
                self.user_details = details.split("\n")
            with open(f"{self.name}.txt", 'w') as f:
                f.write(details.replace(str(self.user_details[3]), str(self.cash)))
        else:
            print("Insufficient funds. Try different amount.")
        return

    def transfer_money(self, amount, name, ph):  # receiver's info
        if self.cash > amount > 0:  # valid amount
            with open(f"{name}.txt", "r") as f:
                rec_details = f.read()  # read other user's file
                self.other_user_details = rec_details.split("\n")  # upload data in other_user_details list
                if str(ph) in self.other_user_details:  # match the ph
                    self.transfer_valid = True
                else:
                    print("Wrong name/number. Try again")
        else:
            print("Enter the right amount. Try again")

        if self.transfer_valid:
            total_cash_on_rec = int(self.other_user_details[3]) + amount
            left_cash_on_sender = self.cash - amount
            with open(f"{name}.txt", "w") as f:  # write data in rec file
                # updating the amount with replace function, replace('old', 'new')
                f.write(rec_details.replace(str(self.other_user_details[3]), str(total_cash_on_rec)))

            with open(f"{self.name}.txt", "r") as f:  # read data from user file
                sender_details = f.read()
                self.user_details = sender_details.split("\n")   # upload data in user_details list

            with open(f"{self.name}.txt", "w") as f:  # write data on user file
                # updating the amount with replace function, replace('old', 'new')
                f.write(sender_details.replace(str(self.user_details[3]), str(left_cash_on_sender)))

            print("Amount Transferred Successfully to", name, "-", ph)
            print("Balance left $", left_cash_on_sender)
            self.cash = left_cash_on_sender
        return

    def change_password(self, password):
        if len(str(password)) < 5 or len(str(password)) > 20:
            print("Please enter a valid password between 5-10 characters.")
        else:
            self.user_details[2] = password
            with open(f"{self.name}.txt", 'w') as f:
                for details in self.user_details:
                    f.write(str(details) + '\n')
            print("Password changed successfully")
        return

    def change_ph(self, ph):
        if len(str(ph)) < 10:  # 10 digit ph no.
            print("Wrong Input. Try again")
        else:
            self.user_details[1] = ph
            with open(f"{self.name}.txt", 'w') as f:
                for details in self.user_details:
                    f.write(str(details) + '\n')
            print("Phone number changed successfully")
        return

    def delete_account(self, password):
        if password in self.user_details:
            os.remove(f"{name}.txt")
            print("Account deleted successfully")
        else:
            print("Enter the correct password.")





if __name__ == "__main__":
    bank_object = Bank()
    print("Welcome to my bank.")
    while True:
        print("1. Login")
        print("2. Register")
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            name = input("Name: ")
            ph = input("Phone number: ")
            password = input("Password: ")
            bank_object.login(name, ph, password)
            while bank_object.logged_in is True:
                print("1. Check your balance")
                print("2. Deposit money")
                print("3. Withdraw money")
                print("4. Transfer money")
                print("5. Update profile")
                print("6. Delete your account")
                print("7. Log out")
                login_input = int(input())
                if login_input == 1:
                    bank_object.balance_check()
                    print("1. Back to menu")
                    print("2. Log out")
                    input_b_check = int(input())
                    if input_b_check == 1:
                        continue
                    elif input_b_check == 2:
                        bank_object.log_out()
                        break
                elif login_input == 2:
                    amount = int(input("Enter the amount: $"))
                    bank_object.deposit_money(amount)
                    print("1. Back to menu")
                    print("2. Log out")
                    input_b_check = int(input())
                    if input_b_check == 1:
                        continue
                    elif input_b_check == 2:
                        bank_object.log_out()
                        break
                elif login_input == 3:
                    amount = int(input("Enter the amount: $"))
                    bank_object.withdraw_money(amount)
                    print("1. Back to menu")
                    print("2. Log out")
                    input_b_check = int(input())
                    if input_b_check == 1:
                        continue
                    elif input_b_check == 2:
                        bank_object.log_out()
                        break

                elif login_input == 4:
                    amount = int(input("Enter the amount: $"))
                    name = input("Name: ")
                    ph = input("Phone number: ")
                    bank_object.transfer_money(amount, name, ph)
                    print("1. Back to menu")
                    print("2. Log out")
                    input_b_check = int(input())
                    if input_b_check == 1:
                        continue
                    elif input_b_check == 2:
                        bank_object.log_out()
                        break

                elif login_input == 5:
                    print("1. Change password")
                    print("2. Change phone number")
                    press = int(input())
                    if press == 1:
                        password = input("Enter new password: ")
                        bank_object.change_password(password)
                        print("1. Back to menu")
                        print("2. Log out")
                        input_b_check = int(input())
                        if input_b_check == 1:
                            continue
                        elif input_b_check == 2:
                            bank_object.log_out()
                            break
                    elif press == 2:
                        ph = input("Enter new phone number: ")
                        bank_object.change_ph(ph)
                        print("1. Back to menu")
                        print("2. Log out")
                        input_b_check = int(input())
                        if input_b_check == 1:
                            continue
                        elif input_b_check == 2:
                            bank_object.log_out()
                            break

                elif login_input == 6:
                    press = input("Please confirm Y/N: ").upper()
                    if press == 'Y':
                        password = input("Enter your password to completely delete you account: ")
                        bank_object.delete_account(password)
                        bank_object.logged_in = False
                        break
                    elif press == 'N':
                        continue

                elif login_input == 7:
                    bank_object.log_out()
                    break


        elif user_input == 2:
            name = input("Name: ")
            ph = input("Phone number: ")
            password = input("Password: ")
            bank_object.register(name, ph, password)
            continue







