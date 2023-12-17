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
        # 
        pass

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower():
                results.append(contact)
        return results

        

    def edit_contact(self, contact_name, field, new_value):
        # Редактор контакта
        pass

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
          print(assistant.delete_contact(contact_name))

       elif command == '7': # команда для запису тегів до нотатків
            title = input('Enter title')
            new_tags = input('Enter tags:').split(',')
            assistant.add_tags_to_note(title, new_tags)

       elif command == '8': # команда для пошуку нотатків за тегами (відсортованих)
        tags = input('Введіть теги для пошуку (розділені комою):').split(',')
        results = assistant.search_notes_by_tags(tags)
        if results:
            for result in results:
                print(result.title, "|", result.text, "|", result.tags)
        else:
            print("Not faund.")

       elif command in ['end', 'close', 'exit']:
          break
       else:
          print("Invalid, Try Again:")
           
           
if __name__ == "__main__":
    main()

     