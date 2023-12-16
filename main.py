class BotAssist:
    def search_contacts_birthday(self, days):
        upcoming_birthday_contacts = []
        today = datetime.now()

        for contact in self.contacts:
            birthday_date = datetime(today.year, *map(int, contact.birthday.split('-')[1:]))
            days_until_birthday = (birthday_date - today).days

            if 0 < days_until_birthday <= days:
                upcoming_birthday_contacts.append(contact)

        if upcoming_birthday_contacts:
            print("Contacts with upcoming birthdays:")
            for contact in upcoming_birthday_contacts:
                print(contact.name, "|", contact.address, "|", contact.phone, "|", contact.email, "|", contact.birthday, "|")
        else:
            print("No contacts with upcoming birthdays.")

    def edit_contact(self, old_contact_name, new_name, new_address, new_phone, new_email, new_birthday):
        contact_replaced = False
        for contact in self.contacts:
            if contact.name == old_contact_name:
                contact.name = new_name
                contact.address = new_address
                contact.phone = new_phone
                contact.email = new_email
                contact.birthday = new_birthday
                contact_replaced = True
                break

        if not contact_replaced:
            raise ValueError('Даного контакту не існує')
def main():
   assistant =  BotAssist()

while True:
    
    elif command == '4':
        old_contact_name = input('Enter the contact old name you want to edit: ')
        new_name = input('Enter the new name: ')
        new_address = input('Enter the new address: ')
        new_phone = input('Enter the new phone: ')
        new_email = input('Enter the new email: ')
        new_birthday = input('Enter the new birthday in YYYY-MM-DD: ')

        assistant.edit_contact(old_contact_name, new_name, new_address, new_phone, new_email, new_birthday)
        print(f'Contact {old_contact_name} successfully edited.')

    elif command == '5':
        day_to_birthday = int(input("Enter the number of days until the birthday: "))
        assistant.search_contacts_birthday(day_to_birthday)
