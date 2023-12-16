from datetime import datetime, timedelta
import pickle

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

class BotAssist:
    def __init__(self):
        self.contacts = []
        self.notes = []

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

    def validate_email(self, email):
        return '@' in email and '.' in email.split('@')[-1]

    def add_contact(self, name, address, phone, email, birthday):
        if not self.validate_phone(phone):
            print("Invalid phone number format. Please enter a 10-digit number.")
            return

        if not self.validate_email(email):
            print("Invalid email format. Please enter a valid email address.")
            return

        contact = Contact(name, address, phone, email, birthday)
        self.contacts.append(contact)
        print("Contact added successfully.")
        
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




    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower():
                results.append(contact)
        return results
    

        
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

        

    def remove_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name == contact_name:
                self.contacts.remove(contact)
                break  # Завершуємо цикл, якщо знайшли контакт

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact_name.lower() in contact.name.lower():
                self.contacts.remove(contact)
        return f'{contact_name} removed'

    def add_note(self, text, tags):
        # Добавить заметку, теги
        pass

    def search_notes(self, query):
        # Поиск в заметках
        pass

    def edit_note(self, old_text, new_text, new_tags):
        # Редактор заметки
        pass

    def delete_note(self, text):
        # Удалить заметку
        pass

    def save_data(self, filename):
        # Сохранение книги
        pass

    def load_data(self, filename):
        # Загрузка книги
        pass

def main():
   assistant =  BotAssist()

   while True:
       #print(f"\nHello, your Python assistent.\nI can do many different useful things to make your life easier. \nFirst, select the command you want to implement:")
       command = input("\nEnter your command: ").lower()
    
       if command == '1':
          name = input('Enter your name:')
          address = input('Enter your adress:')
          phone = input('Enter your phone (10-digits) : ')
          email = input('Enter your email:')
          birthday = input('Enter your birthday in YYYY-MM-DD:')
          assistant.add_contact(name, address, phone, email, birthday)
       elif command == '2':
          search_query = input("Enter first name or last name: ")

          results = assistant.search_contacts(search_query)
          if results:
             print("Search Results:")
             for result in results:
                 print(result.name, "|", result.address, "|", result.phone, "|", result.email, "|", result.birthday, "|")
          else:
           print("No contacts found.")

       elif command == '3':
          contact_name = input('Enter the contact name you want to delete:')
          print(assistant.delete_contact(contact_name))
          
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
          
          
        

       elif command in ['end', 'close', 'exit']:
          break
       else:
          print("Invalid, Try Again:")
           
           
if __name__ == "__main__":
    main()
