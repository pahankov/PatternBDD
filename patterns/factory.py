import random

class NoteFactory:

# Создание валидной заметки с рандомными данными
    @staticmethod
    def create_valid_note():
        num = random.randint(1, 10000)
        return {
            "title": f"Note {num}",
            "content": f"Content {num}"
        }

# Создание невалидной заметки с рандомными данными
    @staticmethod
    def create_invalid_note():
        num = random.randint(1, 10000)
        return {
#            "title": f"Test Note {random.randint(1, 1000)}",
             "content": f"Content {num}"
        }

