""" this file can be used to get valid inputs, e.g
1. valid names (include only alphabets, need to be => 3 chars <=20, can have spaces)
2. valid phone (only integral vales == 10 digits)
3. valid strong passwords (at least 8 chars < 20, mix upper lower and numbers, special chars)
valid """
import string


class ValidName:
    def __init__(self):
        self.INPUT = None

    def is_valid_name(self):
        temp = self.INPUT.replace(' ', '')  # mix first and last name if any
        if temp == '-':  # just in case don't want to provide any name
            return True, 'No name provided'
        elif 20 >= len(temp) >= 3:
            if len(set(temp) - set(string.ascii_letters)) == 0:  # if the letters are english alphabets only
                return True, 'True'
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




    # @staticmethod
    # def valid_name():  # gets valid name
    #     while True:  # keep on looping until we get valid name
    #         name = input("Name: ")
    #         temp = name.replace(' ', '')  # just mix first and last name
    #         if len(temp) == 0:  # if we decide to pass the name
    #             break
    #         elif len(temp) > 20:
    #             print("Name must be under 20 characters.")
    #             continue
    #         elif len(set(temp) - set(string.ascii_letters)) == 0:  # if the letters are english alphabets only
    #             break
    #         else:
    #             print("Wrong input. Try again.")
    #             continue
    #     return name
    #
    # @staticmethod
    # def valid_phone():
    #     while True:  # loops until we get valid phone
    #         phone = input("Phone: ")
    #         try:  # trying to get the integral value
    #             if len(phone) != 0:  # just to pass empty phone number
    #                 ph = int(phone)
    #         except ValueError:
    #             print('Integral values only.')
    #             continue
    #         if len(phone) == 10 or len(phone) == 0:
    #             break
    #         print('Phone must be of 10 digits. Try again.')
    #         continue
    #     return phone

n = ValidName()
print(n.get_valid_name())
