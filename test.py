class BotAssist:
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