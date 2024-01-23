from termcolor import colored

class Contacts:
    def __init__(self, name, family, number, email, country, city, address):
        self.name = name
        self.family = family
        self.number = number
        self.email = email
        self.country = country
        self.city = city
        self.address = address

    def fullname(self):
        return f"{self.name} {self.family}"

def get_valid_name():
    while True:
        try:
            name = str(input(colored("Enter a name for your contact: ", "magenta")))
            if not name:
                print(colored("Please fill out the name field.", "red"))
                continue
            else:
                return name
        except ValueError:
            print(colored("Invalid input! Please enter a name.", "red"))

def get_valid_number():
    while True:
        try:
            number = input(colored("Enter contact number: ", "magenta"))
            if number.isdigit() and len(number) == 11:
                return int(number)
            else:
                print(colored("Invalid phone number! Please enter a valid 11-digit phone number.", "red"))
        except ValueError:
            print(colored("Invalid input! Please enter a number.", "red"))
            
def view_all_contacts():
    if not contact_list:
        print(colored("No contact available!" , "red"),
        colored("\nPlease add a contact first.\n", "red"))
    else:
        for Contact in contact_list:
            print(colored(f"↓ YOUR CONTACTS LIST CONTAINS ↓\n" , "red"))
            print(colored(f"Contact Name: {Contact.fullname()}\n", "green"),
            colored(f"Contact Number: +98{Contact.number}\n", "green"),
            colored(f"Contact Country: {Contact.country}\n", "green"),
            colored(f"Contact City: {Contact.city}\n", "green"),
            colored(f"Contact Address: {Contact.address}\n", "green"))

print(colored("Welcome To Contacts!" , "green"))

contact_list = []

while True:
    user_choice = input(colored("For help menu type 'help'. \n If you know the commands enter it here: " , "cyan")).lower()
    if user_choice == "help":
        print(colored("If you want to create a new contact type" , "cyan") , colored("New\n" , "red"))
        print(colored("If you want to delete a contact type" , "cyan") , colored("Delete 'contact_name'\n" , "red"))
        print(colored("If you want to edit a contact type" , "cyan") , colored("Edit\n" , "red"))
        print(colored("If you want to view all contacts type" , "cyan") , colored("View\n" , "red"))
        print(colored("If you want to quit the app type" , "cyan") , colored("Quit\n" , "red"))

    elif user_choice == "quit":
        print(colored("Goodbye :)\nHope To See You Soon!" , "magenta"))
        break

    elif user_choice == "new":

        while True:
            name_inp = get_valid_name().capitalize()
            family_inp = str(input(colored("Enter the family for your contact: " , "magenta"))).capitalize()
            number_inp = get_valid_number()
            email_inp = str(input(colored("Enter contact email (IF NEEDED): " , "magenta")))
            country_inp = str(input(colored("Enter contact country (IF NEEDED): " , "magenta"))).capitalize()
            city_inp = str(input(colored("Enter contact city (IF NEEDED): " , "magenta"))).capitalize()
            address_inp = str(input(colored("Enter contact address (IF NEEDED): " , "magenta")))

            if not family_inp:
                family_inp = "No Family"

            if not email_inp:
                email_inp = "No Email"

            if not country_inp:
                country_inp = "No Country"

            if not city_inp:
                city_inp = "No City"

            if not address_inp:
                address_inp = "No Address"

            contact_info = Contacts(name_inp, family_inp, number_inp, email_inp, country_inp, city_inp, address_inp)
            contact_list.append(contact_info)

            print(colored(f"Contact Name: {contact_info.fullname()}\n", "green"),
                colored(f"Contact Number: +98{contact_info.number}\n", "green"),
                colored(f"Contact Email: {contact_info.email}\n", "green"),
                colored(f"Contact Country: {contact_info.country}\n", "green"),
                colored(f"Contact City: {contact_info.city}\n", "green"),
                colored(f"Contact Address: {contact_info.address}\n", "green"))

            new_contact = str(input(colored("Do you want to make another Contact? (y/n): ", "cyan")))
            if new_contact.lower() != "y":
                print(colored("You are back in the menu!." , "green"))
                break

    elif user_choice == "view":
        view_all_contacts()
                
    elif user_choice == "edit":
        
        while True:
            if not contact_list:
                print(colored("There is no contact to edit.\n" , "red"))
                break
            view_all_contacts()
            select_contact = str(input(colored("Enter the name of the contact you want to EDIT: ", "magenta")))
            contact_exists = False

            for Contacts in contact_list:
                if select_contact.lower() in Contacts.name.lower():
                    contact_exists = True
                    selected_contact = contact_list.index(Contacts)
                    break

            if not contact_exists:
                print(colored("This contact does not exist.", "red"))
                continue
            
            else:
                print(colored("Please choose what you want to edit in this contact.", "magenta"))
                print(colored("1. Name\n 2. PhoneNumber\n 3. Country\n 4. City\n 5. Address", "red"))
                edit_choice = int(input(colored("What's your choice? : ", "cyan")))
                
                if edit_choice == 1:
                    new_first_name = str(input(colored("\nEnter a new Firstname: ", "yellow"))).capitalize()
                    
                    while new_first_name == "":
                        new_first_name = str(input(colored("Error!\nPlease enter a name: ", "red"))).capitalize()
                    
                    new_last_name = str(input(colored("\nEnter a new Lastname: ", "yellow"))).capitalize()
                    
                    if not new_last_name:
                        new_last_name = "No Family"
                        
                    contact_list[selected_contact].name = new_first_name
                    contact_list[selected_contact].family = new_last_name
                    print(colored("Name updated successfully!", "green"))
                    view_all_contacts()
                    
                    cont_editing = str(input(colored("Do you want to continue editing? (y/n)" , "magenta"))).lower()
                    if cont_editing != "y":
                        break
                    
                elif edit_choice == 2:
                    new_number = int(input(colored("\nEnter a new Phonenumber: ", "yellow")))
                    
                    while not new_number:
                        new_number = int(input(colored("Error!\nPlease enter a Phonenumber: ", "red")))
                        
                    contact_list[selected_contact].number = new_number
                    print(colored("Phonenumber updated successfully!", "green"))
                    view_all_contacts()
                    
                    cont_editing = str(input(colored("Do you want to continue editing? (y/n)" , "magenta"))).lower()
                    if cont_editing != "y":
                        break
                    
                elif edit_choice == 3:
                    new_country = str(input(colored("\nEnter a new Country: ", "yellow"))).capitalize()
                                        
                    while not new_country:
                        new_country = str(input(colored("Error!\nPlease enter a Country: ", "red"))).capitalize()
                        
                    contact_list[selected_contact].country = new_country
                    print(colored("Country updated successfully!", "green"))
                    view_all_contacts()
                    
                    cont_editing = str(input(colored("Do you want to continue editing? (y/n)" , "magenta"))).lower()
                    if cont_editing != "y":
                        break
                    
                elif edit_choice == 4:
                    new_city = str(input(colored("\nEnter a new City: ", "yellow"))).capitalize()
                    
                    while not new_city:
                        new_city = str(input(colored("Error!\nPlease enter a City: ", "red"))).capitalize()
                    
                    contact_list[selected_contact].city = new_city
                    print(colored("City updated successfully!", "green"))
                    view_all_contacts()
                    
                    cont_editing = str(input(colored("Do you want to continue editing? (y/n)" , "magenta"))).lower()
                    if cont_editing != "y":
                        break
                    
                elif edit_choice == 5:
                    new_address = str(input(colored("\nEnter a new Address: ", "yellow")))
                    
                    while not new_address:
                        new_address = str(input(colored("Error!\nPlease enter a Address: ", "red")))
                        
                    contact_list[selected_contact].address = new_address
                    print(colored("Address updated successfully!", "green"))
                    view_all_contacts()
                    
                    cont_editing = str(input(colored("Do you want to continue editing? (y/n)" , "magenta"))).lower()
                    if cont_editing != "y":
                        break
                    
    elif user_choice == "delete":
        while True:
            if not contact_list:
                print(colored("There is no contact to delete.\n", "red"))
                break
            
            view_all_contacts()
            select_contact = str(input(colored("Enter the name of the contact you want to DELETE: ", "magenta")))
            contact_exists = False
            
            for contact in contact_list:
                if select_contact.lower() in contact.name.lower():
                    contact_exists = True
                    contact_list.remove(contact)
                    print(colored("Contact deleted successfully!", "green"))
                    break
            
            if not contact_exists:
                print(colored("This contact does not exist.", "red"))
                continue

            if not contact_list:
                break

            view_all_contacts()
            cont_del = str(input(colored("Do you want to continue deleting? (y/n)", "magenta"))).lower()
            if cont_del != "y":
                break
