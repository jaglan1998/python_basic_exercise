from valid_inputs.valid_inputs import ValidInput  # import specific class


class ContactsBook:
    def __init__(self):
        self.contact_list = []  # list of all contacts, contain nested list with all contact details
        self.found_contact = []  # temp dump for found contact
        self.found_contact_index = None  # temp dump for found contact index, to delete or change

    @staticmethod
    def add_contact(name, phone, address=None, notes=None):  # append all contacts into contacts.txt
        with open('contacts.txt', 'a') as cb:
            cb.write(f"{name}-{phone}-{address}-{notes}\n")

    def import_data(self):  # load the file, and makes lists and nested list
        self.contact_list = []  # need to fresh restart with empty list
        with open('contacts.txt', 'r') as cb:
            contact_list = (cb.read().strip()).split('\n')  # each line in file is one contact separated with line
            # contact_list --> [contact 1, contact 2, contact 3, ....]
            for contact in contact_list:  # each contact has name, ph, address, notes separated with '-'
                contact_details_list = contact.split('-')
                # contact_details_list --> [name, phone, address, notes]
                self.contact_list.append(contact_details_list)
                # self.contact_list --> [[[name, phone, address, notes], [name, phone, address, notes], ....]]
        return self.contact_list

    def export_data(self):  # save data back into the file, for changing information
        with open('contacts.txt', 'w') as cb:
            for contact in self.contact_list:  # looping each contact (nested list with all contact details)
                cb.write('-'.join(contact) + '\n')  # join all contact details with '-' and write them in new line

    def show_contact_list(self):  # show complete list of contacts
        print('------------- CONTACT LIST --------------------')
        self.import_data()  # refresh list
        for contact in self.contact_list:  # iterating each contact
            print(f"Name: {contact[0]}")
            print(f"Phone: {contact[1]}")
            print(f"Address: {contact[2]}")
            print(f"Notes: {contact[3]}")
            print('-----------------------------------------------')

    def find_contacts(self, name, phone):
        found = False  # just to know if we found or not found
        self.import_data()  # refresh the list for latest information
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
        self.import_data()  # again refresh
        self.found_contact[0] = name  # replacing the items in found contact list
        self.found_contact[1] = phone
        self.found_contact[2] = address
        self.found_contact[3] = notes
        self.contact_list[self.found_contact_index] = self.found_contact  # replacing the new contact in contact list
        self.export_data()  # save the changed contact list into file
        print("Contact has been successfully edited.")

    def delete_contact(self):
        self.import_data()  # refresh again
        self.contact_list.pop(self.found_contact_index)  # delete the found/selected contact
        self.export_data()  # save info into the file
        print("Contact has been successfully deleted.")


# ---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    def main_menu():
        print('---------------- MAIN MENU ---------------------')
        print("1. See complete contact list.")
        print("2. Find a contact.")
        print("3. Add contact.")
        print("4. Quit.")


    def find_contacts_menu():
        print('-----------------------------------------------')
        print('1. Edit.')
        print('2. Delete.')
        print('3. Main menu.')
        print('4. Quit.')
        print('-----------------------------------------------')

    def start_program():
        c = ContactsBook()  # creating a class instance
        v = ValidInput()  # class instance

        while True:
            main_menu()  # 3 options available
            x = v.get_valid_digit_input(1, 4)  # select valid

            if x == '1':  # option to see
                c.show_contact_list()  # complete contact list
                e = v.valid_press_enter()  # asking for press enter to return to main menu
                if e:  # if user press enter
                    continue  # program start again from main menu

            elif x == '2':  # find contact
                name = v.get_valid_name()
                ph = v.get_valid_ph_no()
                c.find_contacts(name, ph)  # find contact logic
                find_contacts_menu()  # showing menu, 4 options available
                y = v.get_valid_digit_input(1, 4)
                if y == '1':  # option to edit contact
                    print("**** ENTER NEW DETAILS ****")
                    name = v.get_valid_name()
                    ph = str(v.get_valid_ph_no())  # gets int, need str
                    ad = input("Address: ")
                    notes = input("Notes: ")
                    c.edit_contact(name, ph, ad, notes)
                elif y == '2':  # delete option
                    c.delete_contact()
                elif y == '3':  # return to main menu
                    continue
                elif y == '4':  # quit the program
                    break

            elif x == '3':  # option to new contact
                print("**** ENTER CONTACT DETAILS ****")
                name = v.get_valid_name()
                ph = v.get_valid_ph_no()
                ad = input("Address: ")
                notes = input("Notes: ")
                c.add_contact(name, ph, ad, notes)
                continue

            elif x == '4':  # quit
                break
        return

    start_program()
    input("Press any key to exit.....")
