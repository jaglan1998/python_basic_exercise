import string


class ContactsBook:
    def __init__(self):
        self.contact_list = []  # list of all contacts, contain nested list with all contact details
        self.found_contact = []  # temp dump for found contact
        self.found_contact_index = None  # temp dump for found contact index, to delete or change

    @staticmethod
    def valid_name():  # gets valid name
        while True:  # keep on looping until we get valid name
            name = input("Name: ")
            temp = name.replace(' ', '')  # just mix first and last name
            if len(temp) == 0:  # if we decide to pass the name
                break
            elif len(temp) > 20:
                print("Name must be under 20 characters.")
                continue
            elif len(set(temp)-set(string.ascii_letters)) == 0:  # if the letters are english alphabets only
                break
            else:
                print("Wrong input. Try again.")
                continue
        return name

    @staticmethod
    def valid_phone():
        while True:  # loops until we get valid phone
            phone = input("Phone: ")
            try:  # trying to get the integral value
                if len(phone) != 0:  # just to pass empty phone number
                    ph = int(phone)
            except ValueError:
                print('Integral values only.')
                continue
            if len(phone) == 10 or len(phone) == 0:
                break
            print('Phone must be of 10 digits. Try again.')
            continue
        return phone

    @staticmethod
    def add_contact(name, phone, address=None, notes=None):  # append all contacts into contacts.txt
        with open('contacts.txt', 'a') as cb:
            cb.write(f"{name}-{phone}-{address}-{notes}\n")

    def generate_list(self):  # load the file, and makes lists and nested list
        self.contact_list = []  # need to fresh restart with empty list
        with open('contacts.txt', 'r') as cb:
            contact_list = (cb.read().strip()).split('\n')  # each line in file is one contact separated with line
            for contact in contact_list:  # each line in file has contact details separated with '-'
                contact_details_list = contact.split('-')  # nested list with contact details (name, phone, ad, notes)
                self.contact_list.append(contact_details_list)  # appending one nested list (one contact) after second.
        return self.contact_list

    def save_data(self):  # save data back into the file, for changing information
        with open('contacts.txt', 'w') as cb:
            for contact in self.contact_list:  # looping each contact (nested list with all contact details)
                cb.write('-'.join(contact) + '\n')  # join all contact details with '-' and write that in new line

    def show_contact_list(self):  # show complete list of contacts
        print('-----------------------------------------------')
        self.generate_list()  # refresh list
        for contact in self.contact_list:  # iterating each contact
            print(f"Name: {contact[0]}")
            print(f"Phone: {contact[1]}")
            print(f"Address: {contact[2]}")
            print(f"Notes: {contact[3]}")
            print('-----------------------------------------------')

    def find_contacts(self, name, phone):
        found = False  # just to know if we found or not found
        self.generate_list()  # refresh the list for latest information
        print('-----------------------------------------------')
        for index, contact in enumerate(self.contact_list):  # iterate each contact and return index
            if name == contact[0] or phone == contact[1]:  # if any of these values match
                found = True
                self.found_contact = contact  # temp save details in list
                self.found_contact_index = index  # temp save index of that particular contact
                print(f"Name: {contact[0]}")
                print(f"Phone: {contact[1]}")
                print(f"Address: {contact[2]}")
                print(f"Notes: {contact[3]}")
                print('-----------------------------------------------')
        if not found:
            print("No contact found.")
            print('-----------------------------------------------')

    def edit_contact(self, name, phone, address=None, notes=None):
        self.generate_list()  # again refresh
        self.found_contact[0] = name  # replacing the items in found contact list
        self.found_contact[1] = phone
        self.found_contact[2] = address
        self.found_contact[3] = notes
        self.contact_list[self.found_contact_index] = self.found_contact  # replacing the new contact in contact list
        self.save_data()  # save the changed contact list into file
        print("Contact has been successfully edited.")

    def delete_contact(self):
        self.generate_list()  # refresh again
        self.contact_list.pop(self.found_contact_index)  # delete the found/selected contact
        self.save_data()  # save info into the file
        print("Contact has been successfully deleted.")


c = ContactsBook()
while True:
    print('-----------------------------------------------')
    print("1. See complete contact list.")
    print("2. Find a contact.")
    print("3. Add contact.")

    x = input("")
    while x not in ['1', '2', '3']:
        x = input("Wrong input. Try again.")

    if x == '1':
        c.show_contact_list()
        x = input("Press enter to back.....")
        while x != '':
            x = input("Press enter to go back.....")
        continue

    elif x == '2':
        name = c.valid_name()
        phone = c.valid_phone()
        c.find_contacts(name, phone)

        print('1. Edit.')
        print('2. Delete.')
        print('3. Main menu.')
        print('4. Quit.')
        x = input("")
        while x not in ['1', '2', '3', '4']:
            x = input("Wrong input. Try again.")
        print('-----------------------------------------------')

        if x == '1':
            new_name = c.valid_name()
            new_phone = c.valid_phone()
            new_address = input("Address: ")
            new_notes = input("Notes: ")
            c.edit_contact(new_name, new_phone, new_address, new_notes)
            print('-----------------------------------------------')

        elif x == '2':
            c.delete_contact()
            x = input("")
            while x not in ['1', '2', '3']:
                x = input("Wrong input. Try again.")
        elif x == '3':
            continue

        elif x == '4':
            break

    elif x == '3':
        name = c.valid_name()
        phone = c.valid_phone()
        address = input("Address: ")
        notes = input("Notes: ")
        c.add_contact(name, phone, address, notes)
        print('-----------------------------------------------')
        x = input("Press enter to back.....")
        while x != '':
            x = input("Press enter to go back.....")
        continue

input("Press any key to exit......")