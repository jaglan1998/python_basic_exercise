import os  # used to remove file


class Bank:
    def __init__(self):
        self.user_details_list = []  # store data while register, login and other functions
        self.other_user_details = []  # store other user's data while transferring money
        self.logged_in = False  # is logger logged in ? False right now
        self.transfer_valid = False  # is transfer valid ? right info, ph, name etc.
        self.cash = 0  # starting balance is zero.
        self.name = ''  # store name of user while login, register and other functions

    def register(self, name, ph, password):  # we need these 3 parameters which we can pass on with user input.
        cash = self.cash  # in line 24, we want to add cash details in user details of customer
        valid_details = True
        if len(str(ph)) != 10:
            print("Incorrect input. Phone number must be of 10 digits and only in integers.")
            valid_details = False
        if len(str(password)) < 5 or len(str(password)) > 20:
            print("Please enter a valid password between 5-10 characters.")
            valid_details = False
        if valid_details is True:
            print("\nAccount has been created.\n")
            self.user_details_list = [name, str(ph), password, cash]  # information is stored in user_details_list
            with open(f"{name}.txt", 'w') as f:  # write a txt file with 'name'
                for details in self.user_details_list:  # looping through user_details_list list to write each element
                    f.write(str(details) + '\n')  # with \n

    def login(self, name, ph, password):
        try:
            with open(f"{name}.txt", 'r') as f:
                details = f.read()  # read file in string
                self.user_details_list = details.split("\n")  # braking down details string with \n to store into list
            if str(ph) in self.user_details_list:  # name is already confirmed, checking ph
                if str(password) in self.user_details_list:  # check password if it exists in user_details_list
                    self.logged_in = True
                else:
                    print("Incorrect password. Try again.")
            else:
                print("Incorrect phone number. Try again.")

            if self.logged_in is True:
                print(f"\nUser '{name}' logged in successfully.\n")
                self.cash = int(self.user_details_list[3])  # show the int cash from user_details_list
                self.name = name  # store the name is init function
        except FileNotFoundError:
            print("Wrong details. File not found. Try again")
        return

    def balance_check(self):
        balance = self.cash  # will show the cash stored while login into init
        print(f"\nYour balance is ${balance}.\n")
        return

    def log_out(self):
        print(f"\n'{self.name}' is successfully logged out.\n")  # login --> store 'name' into init function
        self.logged_in = False

    def deposit_money(self, amount):  # amount parameter will be asked as a user input
        try:
            if amount > 0:  # we want amount more than 0
                self.cash = self.cash + amount  # the temp value in self.cash will change
                print(f"\nDeposit successful. New balance is '${self.cash}'\n")
                # now we want to add this change to data file
                with open(f"{self.name}.txt", 'r') as f:  # first read the data file
                    details = f.read()
                    self.user_details_list = details.split("\n")  # download the data
                with open(f"{self.name}.txt", 'w') as f:  # write the same data but now slightly edited
                    f.write(details.replace(self.user_details_list[3], str(self.cash)))  # upload cash replaced data
            else:
                print("Invalid amount. Amount must be > 0")
        except FileNotFoundError:
            print("Wrong details. File not found. Try again")

    def withdraw_money(self, amount):
        try:
            if self.cash > amount:
                self.cash = self.cash - amount
                print(f"\nWithdraw successful. New balance is '${self.cash}'\n")
                with open(f"{self.name}.txt", 'r') as f:
                    details = f.read()
                    self.user_details_list = details.split("\n")

                with open(f"{self.name}.txt", 'w') as f:
                    f.write(details.replace(str(self.user_details_list[3]), str(self.cash)))
            else:
                print("Insufficient funds. Try different amount.")
        except FileNotFoundError:
            print("Wrong details. File not found. Try again")

    def transfer_money(self, amount, name, ph):  # receiver's info
        try:
            if self.cash >= amount > 0:  # valid amount
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
                    self.user_details_list = sender_details.split("\n")  # upload data in user_details_list list

                with open(f"{self.name}.txt", "w") as f:  # write data on user file
                    # updating the amount with replace function, replace('old', 'new')
                    f.write(sender_details.replace(str(self.user_details_list[3]), str(left_cash_on_sender)))

                print(f"\nAmount Transferred Successfully to {name} - {ph}")
                print(f"Balance left ${left_cash_on_sender}\n")
                self.cash = left_cash_on_sender
        except FileNotFoundError:
            print("Wrong details. File not found. Try again")

    def change_password(self, password):
        try:
            if len(str(password)) < 5 or len(str(password)) > 20:
                print("Please enter a valid password between 5-10 characters.")
            else:
                self.user_details_list[2] = password
                with open(f"{self.name}.txt", 'w') as f:
                    for details in self.user_details_list:
                        f.write(str(details) + '\n')
                print("\nPassword changed successfully\n")
        except FileNotFoundError:
            print("Wrong details. File not found. Try again")

    def change_ph(self, ph):
        try:
            if len(str(ph)) != 10:  # 10 digit ph no.
                print("Wrong Input. Try again")
            else:
                self.user_details_list[1] = str(ph)
                with open(f"{self.name}.txt", 'w') as f:
                    for details in self.user_details_list:
                        f.write(str(details) + '\n')
                print("\nPhone number changed successfully\n")
        except FileNotFoundError:
            print("Wrong details. File not found. Try again")

    def delete_account(self, password):
        if password in self.user_details_list:
            os.remove(f"{name}.txt")
            print("\nAccount deleted successfully\n")
        else:
            print("Enter the correct password.")

    @staticmethod
    def valid_ph():
        global ph
        while True:  # valid ph
            try:
                ph = int(input("Phone number: "))
                if len(str(ph)) != 10:
                    print("Phone number must be of 10 digits.")
                    continue
                else:
                    break
            except ValueError:
                print("ValueError. Try again.")
                continue
        return ph

    @staticmethod
    def valid_password():
        password = input("Password: ")
        while len(password) < 5:
            print("Password must be of minimum 5 characters.")
            password = input("Password: ")
        return password

    @staticmethod
    def valid_amount():
        global amount
        while True:
            try:
                amount = int(input("Enter the amount: $"))
                if amount <= 0:
                    print("Amount must be > 0")
                    continue
                else:
                    break
            except ValueError:
                print("Value Error. Try again")
                continue
        return amount


if __name__ == "__main__":
    bank_object = Bank()  # creating a object for class bank
    print("-------------------------------")
    print("Welcome to my bank.")
    print("-------------------------------")

    while True:  # this is to trigger back to homepage once we logout
        print("-------------------------------")
        print("1. Login")
        print("2. Register")
        print("-------------------------------")
        try:  # this is for handling error, FileNotFound, ValueError or EOF errors.
            user_input = input("Enter your choice: ")
            while user_input not in ['1', '2']:  # input must be 1 or 2 or it will keep asking
                print("Choose from only 1 or 2.")
                user_input = input("Enter your choice: ")
            print("-------------------------------")

            if user_input == '1':  # login
                name = input("Name: ")
                ph = bank_object.valid_ph()
                password = bank_object.valid_password()
                bank_object.login(name, ph, password)

                while bank_object.logged_in is True:
                    print("-------------------------------")
                    print("1. Check your balance")
                    print("2. Deposit money")
                    print("3. Withdraw money")
                    print("4. Transfer money")
                    print("5. Update profile")
                    print("6. Delete your account")
                    print("7. Log out")
                    print("-------------------------------")

                    user_input = input()
                    while user_input not in ['1', '2', '3', '4', '5', '6', '7']:
                        print("Wrong input. Try again.")
                        user_input = input()
                    print("-------------------------------")

                    if user_input == '1':
                        bank_object.balance_check()  # check balance

                        # back menu logic and log out option
                        print("-------------------------------")
                        print("1. Back to menu")
                        print("2. Log out")
                        print("-------------------------------")
                        user_input = input()
                        while user_input not in ['1', '2']:
                            print("Wrong input. Try again.")
                            user_input = input()
                        print("-------------------------------")
                        if user_input == '1':
                            continue
                        elif user_input == '2':
                            bank_object.log_out()
                            break

                    elif user_input == '2':  # deposit money
                        amount = bank_object.valid_amount()
                        bank_object.deposit_money(amount)

                        # back menu logic and log out option
                        print("-------------------------------")
                        print("1. Back to menu")
                        print("2. Log out")
                        print("-------------------------------")
                        user_input = input()
                        while user_input not in ['1', '2']:
                            print("Wrong input. Try again.")
                            user_input = input()

                        if user_input == '1':
                            continue
                        elif user_input == '2':
                            bank_object.log_out()
                            break

                    elif user_input == '3':  # withdraw money
                        amount = bank_object.valid_amount()
                        bank_object.withdraw_money(amount)

                        # back menu logic and log out option
                        print("-------------------------------")
                        print("1. Back to menu")
                        print("2. Log out")
                        print("-------------------------------")
                        user_input = input()
                        while user_input not in ['1', '2']:
                            print("Wrong input. Try again.")
                            user_input = input()
                        if user_input == '1':
                            continue
                        elif user_input == '2':
                            bank_object.log_out()
                            break

                    elif user_input == '4':  # transfer money
                        amount = bank_object.valid_amount()
                        name = input("Transfer money to (Name): ")
                        ph = bank_object.valid_ph()
                        bank_object.transfer_money(amount, name, ph)

                        # back menu logic and log out option
                        print("-------------------------------")
                        print("1. Back to menu")
                        print("2. Log out")
                        print("-------------------------------")
                        user_input = input()
                        while user_input not in ['1', '2']:
                            print("Wrong input. Try again.")
                            user_input = input()
                        if user_input == '1':
                            continue
                        elif user_input == '2':
                            bank_object.log_out()
                            break

                    elif user_input == '5':  # change details

                        print("1. Change password")
                        print("2. Change phone number")
                        print("-------------------------------")
                        # valid input
                        user_input = input()
                        while user_input not in ['1', '2']:
                            print("Wrong input. Try again.")
                            user_input = input()
                        # change password
                        if user_input == '1':
                            password = bank_object.valid_password()
                            bank_object.change_password(password)

                            # back menu logic and log out option
                            print("-------------------------------")
                            print("1. Back to menu")
                            print("2. Log out")
                            print("-------------------------------")
                            user_input = input()
                            while user_input not in ['1', '2']:
                                print("Wrong input. Try again.")
                                user_input = input()
                            if user_input == '1':
                                continue
                            elif user_input == '2':
                                bank_object.log_out()
                                break
                        # change ph
                        elif user_input == '2':
                            ph = bank_object.valid_ph()
                            bank_object.change_ph(ph)

                            # back menu logic and log out option
                            print("-------------------------------")
                            print("1. Back to menu")
                            print("2. Log out")
                            print("-------------------------------")
                            user_input = input()
                            while user_input not in ['1', '2']:
                                print("Wrong input. Try again.")
                                user_input = input()
                            if user_input == '1':
                                continue
                            elif user_input == '2':
                                bank_object.log_out()
                                break

                    elif user_input == '6':
                        user_input = input("Please confirm Y/N: ").upper()
                        while user_input not in ['Y', 'N']:
                            print("Wrong input. Try again.")
                            user_input = input("Please confirm Y/N: ").upper()

                        if user_input == 'Y':
                            password = bank_object.valid_password()
                            bank_object.delete_account(password)
                            bank_object.logged_in = False
                            break

                        elif user_input == 'N':
                            continue

                    elif user_input == '7':
                        bank_object.log_out()
                        break

            elif user_input == '2':
                name = input("Name: ")
                ph = bank_object.valid_ph()
                password = bank_object.valid_password()
                bank_object.register(name, ph, password)
                continue

        except ValueError:
            print("\nFix me\n")
        except EOFError:
            print("\nFix me\n")
        except FileNotFoundError:
            print("\nFix me\n")