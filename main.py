class BotAssist:
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
        
    def remove_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name == contact_name:
                self.contacts.remove(contact)
                break  # Завершуємо цикл, якщо знайшли контакт
            
            
    def search_contacts_birthday(self, days):
        upcoming_birthday_contacts = []
        today = datetime.now()

        for contact in self.contacts:
            birthday_date = datetime.strptime(contact.birthday, '%Y-%m-%d')
            days_until_birthday = (birthday_date - today).days

            if 0 < days_until_birthday <= days:
                upcoming_birthday_contacts.append(contact)

        if upcoming_birthday_contacts:
            print("Contacts with upcoming birthdays:")
            for contact in upcoming_birthday_contacts:
                print(contact.name, "|", contact.address, "|", contact.phone, "|", contact.email, "|", contact.birthday, "|")
        else:
            print("No contacts with upcoming birthdays.")



        

