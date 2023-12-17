#Для реалізації мого коду використав скелет Антона

class Note:
    def __init__(self, text):
        self.text = text
        
class BotAssist:
    def __init__(self):
        self.contacts = []  
        self.notes = {}  # Словник для зберігання нотаток (ключ - назва, значення - нотатка)

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

def main():
    assistant = BotAssist()  

    while True:  # Основний цикл програми
        command = input("\nEnter your command: ").lower()  # Запит користувача на введення команди

        if command == '6':
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

if __name__ == "__main__":
    main()  
