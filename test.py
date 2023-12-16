class BotAssist:
    def __init__(self):
        self.contacts = []
        self.notes = []
        self.notes_index = {}

    def add_tags_to_note(self, text, new_tags):
            for note in self.notes:
                if note.text.lower() == text.lower():
                    note.tags.extend(new_tags)
                    print("Tags added to the note successfully.")
                    return
            print("Note not found.")


    def search_notes_by_tags(self, tags):
        results = []
        for tag in tags:
            tag_lower = tag.lower()
            if tag_lower in self.notes_index:
                results.extend(self.notes_index[tag_lower])
        return results