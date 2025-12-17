import requests

class NoteAPI:


    def __init__(self):
        self.server_url = "http://127.0.0.1:8000"
        self.notes_url = f"{self.server_url}/notes"


# Создать новую заметку
    def create_note(self, title, content):
        data = {
            "title": title,
            "content": content
        }
        return requests.post(self.notes_url, json=data)

# Получить все заметки
    def get_all_notes(self):
        return requests.get(self.notes_url)

# Получить заметку по ID
    def get_note_by_id(self, note_id):
        return requests.get(f"{self.notes_url}/{note_id}")

# Обновить заметку
    def update_note(self, note_id, title, content):
        data = {
            "title": title,
            "content": content
        }
        return requests.put(f"{self.notes_url}/{note_id}", json=data)

# Удалить заметку
    def delete_note(self, note_id):
        return requests.delete(f"{self.notes_url}/{note_id}")

# Удалить все заметки
    def clear_all_notes(self):
            for note in self.get_all_notes().json():
                self.delete_note(note["id"])



