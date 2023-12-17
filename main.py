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
    def __init__(self, text):
        self.text = text
        self.tags = []

class BotAssist:
    def __init__(self):
        self.contacts = []
        self.notes = {}
        self.tags = {}

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

        

    def edit_contact(self, old_contact_name, new_contact_name):
        contact_replaced = False
        for contact in self.contacts:
            if contact.name == old_contact_name:
                contact.name = new_contact_name  # Update the name directly
                contact_replaced = True
                break  # Завершуємо цикл, якщо знайшли контакт
        if contact_replaced:
            return f'Contact {old_contact_name} successfully edited to {new_contact_name}.'
        else:
            raise ValueError('Даного контакту не існує')

    def delete_contact(self, contact_name):

        for contact in self.contacts:
            if contact_name.lower() in contact.name.lower():
                self.contacts.remove(contact)
                print(f'{contact_name} removed')
            else:
                print("Contact not found")
      

    def add_note(self, note_name, note_text):
        if note_name in self.notes:  # Перевірка, чи назва нотатки вже існує
            choice = input(f"Note '{note_name}' already exists. Do you want to edit it? enter yes or no: ").lower()
            if choice == 'yes':
                self.edit_note(note_name, note_text)  # Виклик методу для редагування нотатки
            else:
                print("Note creation aborted.")
        else:
            self.notes[note_name] = Note(note_text)  # Створення нової нотатки в словнику notes
            print(f"Note '{note_name}' created successfully.")

    def search_notes(self, note_name):
        if not self.notes:  # Перевірка, чи словник notes пустий
            print("Notes not found. Please create a note using command '6'.")
        elif note_name in self.notes:  # Пошук нотатки за вказаною назвою
            print(f"Note '{note_name}': {self.notes[note_name].text}")
        else:
            print(f"Note '{note_name}' does not exist.")

    def edit_note(self, note_name, new_text):
        if note_name in self.notes:  # Перевірка, чи існує нотатка з вказаною назвою
            self.notes[note_name].text = new_text  # Зміна тексту нотатки
            print(f"Edited note '{note_name}' successfully.")
        else:
            print(f"Note '{note_name}' does not exist. Cannot edit.")

    def delete_note(self, note_name):
        if not self.notes:  # Перевірка, чи словник notes пустий
            print("No notes found. Please create a note using command '6'.")
        elif note_name in self.notes:  # Перевірка, чи існує нотатка з вказаною назвою
            print(f"Note '{note_name}': {self.notes[note_name].text}")
            choice = input(f"Are you sure you want to delete note '{note_name}'? (1 - Yes, 2 - No): ")
            if choice == '1':
                del self.notes[note_name]  # Видалення нотатки за вказаною назвою
                print(f"Note '{note_name}' deleted successfully.")
            else:
                print("Deletion aborted.")
        else:
            print(f"Note '{note_name}' does not exist.")

    def add_tags_to_note(self, title, new_tags):
        if title in self.notes:
            self.notes[title].tags.extend(new_tags)
            for tag in new_tags:
                if tag in self.tags:
                    self.tags[tag].append(title)
                else:
                    self.tags[tag] = [title]
            print("Ok")
        else:
            print("Not found.")

    def search_notes_by_tags(self, tags):
        results = []
        for tag in tags:
            if tag in self.tags:
                results.extend([self.notes[title] for title in self.tags[tag]])
        sorted_results = sorted(results, key=lambda x: x.title)
        return sorted_results

    def save_data(self, filename):
        # Сохранение книги
        pass

    def load_data(self, filename):
        # Загрузка книги
        pass

def main():
   assistant =  BotAssist()

   while True:
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
          if contact_name =='':
              print ("No contacts found.")
          else:
              assistant.delete_contact(contact_name)

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
        
       elif command == '6':
            note_name = input("Enter note name: ")
            note_text = input("Enter note text: ")
            assistant.add_note(note_name, note_text)  # Виклик методу для створення нотатки

       elif command == '7':
            note_name = input("Enter note name to search: ")
            assistant.search_notes(note_name)  # Виклик методу для пошуку нотатки

       elif command == '8':
            edit_or_delete = input("Enter 'edit' to edit a note or 'delete' to delete a note: ").lower()

            if edit_or_delete == 'edit':
                note_name = input("Enter note name to edit: ")
                new_text = input("Enter new text for the note: ")
                assistant.edit_note(note_name, new_text)  # Виклик методу для редагування нотатки
            elif edit_or_delete == 'delete':
                note_name = input("Enter note name to delete: ")
                assistant.delete_note(note_name)  # Виклик методу для видалення нотатки
            else:
                print("Invalid command. Please enter 'edit' or 'delete'.")
    

       elif command == '9': # команда для запису тегів до нотатків
            title = input('Enter title:')
            new_tags = input('Enter tags:').split(',')
            assistant.add_tags_to_note(title, new_tags)

       elif command == '10': # команда для пошуку нотатків за тегами (відсортованих)
            tags = input('Введіть теги для пошуку (розділені комою):').split(',')
            results = assistant.search_notes_by_tags(tags)
            if results:
                for result in results:
                    print(result.title, "|", result.text, "|", result.tags)
            else:
                print("Not found.")

       elif command in ['end', 'close', 'exit']:
          break
       else:
          print("Invalid, Try Again:")
           
           
if __name__ == "__main__":
    main()
