

    while True:
        command = input("\nEnter your command: ").lower()

        if command == '1':
            name = input('Enter your name:')
            address = input('Enter your address:')
            phone = input('Enter your phone (10-digits): ')
            email = input('Enter your email:')
            birthday = datetime.strptime(input('Enter your birthday in YYYY-MM-DD:'), "%Y-%m-%d")
            assistant.add_contact(name, address, phone, email, birthday)
        elif command == '2':
            search_query = input("Enter name or email to search: ")
            results = assistant.search_contacts(search_query)
            if results:
                print("Search Results:")
                for result in results:
                    print(result.name, "|", result.address, "|", result.phone, "|", result.email, "|", result.birthday, "|")
            else:
                print("No contacts found.")
        elif command == '3':
            # Add note
            text = input("Enter note text: ")
            tags = input("Enter tags (comma-separated): ").split(',')
            assistant.add_note(text, tags)
        elif command == '4':
            # Search notes
            search_query = input("Enter note search query: ")
            results = assistant.search_notes(search_query)
            if results:
                print("Search Results:")
                for result in results:
                    print(result.tags, "|", result.text)
            else:
                print("No notes found.")
        elif command == '5':
            # Edit contact
            contact_name = input("Enter contact name: ")
            field = input("Enter field to edit: ")
            new_value = input("Enter new value: ")
            assistant.edit_contact(contact_name, field, new_value)
        elif command == '6':
            # Delete contact
            contact_name = input("Enter contact name: ")
            assistant.delete_contact(contact_name)
        elif command == '7':
            # Edit note
            old_text = input("Enter existing note text: ")
            new_text = input("Enter new note text: ")
            new_tags = input("Enter new tags (comma-separated): ").split(',')
            assistant.edit_note(old_text, new_text, new_tags)
        elif command == '8':
            # Delete note
            text = input("Enter note text: ")
            assistant.delete_note(text)
        elif command == '9':
            # Save data
            filename = input("Enter filename to save data: ")
            assistant.save_data(filename)
        elif command == '10':
            # Load data
            filename = input("Enter filename to load data: ")
            assistant.load_data(filename)
        elif command == '11':
            # Search contacts with upcoming birthdays
            days = int(input("Enter the number of days to check for upcoming birthdays: "))
            assistant.search_contacts_birthday(days)
        elif command in ['end', 'close', 'exit']:
            break
        else:
            print("Invalid command. Please try again.")





#             Інструкція для роботи з нашим ботом:

    # Додавання контакту:
# Введіть 1 для додавання нового контакту.
# Введіть інформацію про контакт, таку як ім'я, адресу, номер телефону, email та дату народження.
    # Пошук контакту:
# Введіть 2 для пошуку контакту за ім'ям або email.
# Введіть запит для пошуку.
# Додавання нотатки:
    # Введіть 3 для додавання нової нотатки.
# Введіть текст нотатки та теги (розділені комами).
# Пошук нотатки:
    # Введіть 4 для пошуку нотатки за текстом чи тегами.
# Введіть запит для пошуку.
# Редагування контакту:
    # Введіть 5 для редагування існуючого контакту.
# Введіть ім'я контакту, поле для редагування та нове значення.
# Видалення контакту:
    # Введіть 6 для видалення існуючого контакту.
# Введіть ім'я контакту для видалення.
# Редагування нотатки:
    # Введіть 7 для редагування існуючої нотатки.
# Введіть старий текст нотатки, новий текст та нові теги.
# Видалення нотатки:
    # Введіть 8 для видалення існуючої нотатки.
# Введіть текст нотатки для видалення.
# Збереження даних:
    # Введіть 9 для збереження даних у файл.
# Введіть ім'я файлу, у який ви хочете зберегти дані.
# Завантаження даних:
    # Введіть 10 для завантаження даних з файлу.
# Введіть ім'я файлу, з якого ви хочете завантажити дані.
# Пошук контактів з найближчими днями народження:
    # Введіть 11 для пошуку контактів з народженнями, які відбудуться через певну кількість днів.
# Введіть кількість днів для пошуку.
    # Завершення роботи:
# Введіть end, close або exit для завершення роботи з ботом.