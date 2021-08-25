""" this file can be used to get valid inputs, e.g
1. valid names (include only alphabets, need to be => 3 chars <=20, can have spaces)
2. valid phone (only integral vales == 10 digits)
3. valid strong passwords (at least 8 chars < 20, mix upper lower and numbers, special chars)
4. valid emails
5. valid digit options i.e. 1, 2, 3,
6. valid press enter key..
"""
import string


class ValidInput:
    def __init__(self):
        self.INPUT = None
        self.email_domains = []
        with open('all_email_provider_domains.txt', 'r') as f:
            self.email_domains = (f.read()).split('\n')

    def is_valid_name(self):
        temp = self.INPUT.replace(' ', '')  # mix first and last name if any
        if temp == '-':  # just in case don't want to provide any name
            return True, 'No name provided'
        elif 20 >= len(temp) >= 3:
            if len(set(temp) - set(string.ascii_letters)) == 0:  # if the letters are english alphabets only
                return True, 'Valid english alphabet'
            return False, 'Not a valid english alphabet'
        else:
            return False, 'Name must be => 3 or <= 20 characters.'

    def get_valid_name(self):
        self.INPUT = input("Name: ")
        self.is_valid_name()
        while not self.is_valid_name()[0]:
            print(self.is_valid_name()[1])
            self.INPUT = input("Name: ")
            self.is_valid_name()
        return self.INPUT

    def is_valid_ph_no(self):
        try:
            self.INPUT = int(self.INPUT)
        except ValueError:
            return False, 'Integral value only. Try again'
        if len(str(self.INPUT)) != 10:
            return False, 'Phone number must be of 10 digits. Try again'
        else:
            return True, 'Valid phone number'

    def get_valid_ph_no(self):
        self.INPUT = input("Phone: ")
        self.is_valid_ph_no()
        while not self.is_valid_ph_no()[0]:
            print(self.is_valid_ph_no()[1])
            self.INPUT = input("Phone: ")
            self.is_valid_ph_no()
        return self.INPUT

    def is_valid_password(self):
        if len(set(string.ascii_lowercase).intersection(set(self.INPUT))) == 0:
            return False, 'Need at least one lowercase letter. Try again'
        elif len(set(string.ascii_uppercase).intersection(set(self.INPUT))) == 0:
            return False, 'Need at least one uppercase letter. Try again'
        elif len(set(string.punctuation).intersection(set(self.INPUT))) == 0:
            return False, 'Need at least one special character letter. Try again'
        elif len(set(string.digits).intersection(set(self.INPUT))) == 0:
            return False, 'Need at least one integral number character letter. Try again'
        elif len(self.INPUT) < 8 or len(self.INPUT) > 20:
            return False, 'Need to be in between 8 to 20 characters. Try again'
        return True, 'Valid strong password'

    def get_valid_password(self):
        self.INPUT = input("Password: ")
        self.is_valid_password()
        while not self.is_valid_password()[0]:
            print(self.is_valid_password()[1])
            self.INPUT = input("Password: ")
            self.is_valid_password()
        return self.INPUT

    # def is_valid_email(self):
    #     if '@' not in self.INPUT:
    #         return False, 'Not a valid email. Missing @. Try again'
    #     e = self.INPUT.split('@')
    #     prefix = e[0]
    #     domain = e[1]
    #     if domain not in self.email_domains:
    #         return False, 'Not a valid email domain. Try again'
    #     elif len(prefix) > 20:
    #         return False, 'Email prefix should be less than 20 character. Try again'
    #     return True, 'Valid email'
    #
    # def get_valid_email(self):
    #     self.INPUT = input("Email: ")
    #     self.is_valid_email()
    #     while not self.is_valid_email()[0]:
    #         print(self.is_valid_email()[1])
    #         self.INPUT = input("Email: ")
    #         self.is_valid_email()
    #     return self.INPUT

    def get_valid_digit_input(self, start, end):
        self.INPUT = input("Select option: ")
        options = [str(i) for i in range(start, end + 1)]
        while self.INPUT not in options:
            self.INPUT = input("*** Wrong input. Select option again: ")
        return self.INPUT

    def valid_press_enter(self):
        self.INPUT = input("Press enter to back.....")
        while self.INPUT != '':
            self.INPUT = input("Wrong input. Just press enter.")
        return True
