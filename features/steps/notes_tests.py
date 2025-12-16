from behave import given, when, then
import requests

# ========== ФУНКЦИИ ==========

# Создать валидную заметку
def create_test_valid_note_data():
    return {
        "title": "Test Note",
        "content": "Test content"
    }

# Создать невалидную заметку
def create_test_invalid_note_data():
     return {#"title": "Test Note",
            "content": "Test"}

# Отправить запрос создания
def send_test_note_data(data):
    return requests.post("http://127.0.0.1:8000/notes",
                         json=data)

# Получить все заметки
def get_all_note_data():
    return requests.get("http://127.0.0.1:8000/notes")

# ========== ШАГИ ==========

# Валидные данные
@given('валидные данные заметки')
def valid_note_data(context):
    context.note_data = create_test_valid_note_data()

# Невалидные данные
@given('невалидные данные заметки')
def invalid_note_data(context):
    context.note_data = create_test_invalid_note_data()

# Создать заметку
@when('создаю заметку')
def create_note(context):
    context.response = send_test_note_data(context.note_data)

# Получить все заметки
@when('запрашиваю все заметки')
def request_all_note_data(context):
    context.response = get_all_note_data()

# Проверить статус 200
@then('статус ответа 200')
def check_status_200(context):
    assert context.response.status_code == 200

# Проверить статус 422
@then ('статус ответа 422')
def check_status_422(context):
    assert context.response.status_code == 422

# Проверить статус 404
@then ('статус ответа 404')
def check_status_404(context):
    assert context.response.status_code == 404


# Проверить ID
@then('в ответе есть ID')
def check_id_in_response(context):
    response_data = context.response.json()
    assert "id" in response_data

# Пустой список
@then('получаю пустой список')
def get_empty_list(context):
    assert context.response.json() == []

# Непустой список
@then('получаю непустой список')
def get_non_empty_list(context):
    data = context.response.json()
    assert isinstance(data, list) and len(data) > 0

# Создание заметки
@given('в системе есть заметка')
def note_availability(context):
    data = create_test_valid_note_data()
    response = send_test_note_data(data)
    context.note_id = response.json()["id"]

# Получения заметки по ID
@when('запрашиваю заметку по её ID')
def get_note_by_valid_id(context):
    note_id = context.note_id
    context.response = requests.get(f"http://127.0.0.1:8000/notes/{note_id}")

# Запрос заметки по несуществующему ID
@when('запрашиваю заметку по несуществующему ID')
def get_note_by_invalid_id(context):
    context.response = requests.get("http://127.0.0.1:8000/notes/999999999999")

# Удаление заметки по валидному id
@when('удаляю заметку по валидному id')
def delete_note_valid_id(context):
    note_id = context.note_id
    context.response = requests.delete(f"http://127.0.0.1:8000/notes/{note_id}")

# Проверка статуса 404 после удаления
@then('при попытке получить заметку статус ответа 404')
def check_status_404_after_delete(context):
    note_id = context.note_id
    response = requests.get(f"http://127.0.0.1:8000/notes/{note_id}")
    assert response.status_code == 404

# Удаление заметки по не валидному id
@when('удаляю заметку по не валидному id')
def delete_note_invalid_id(context):
    context.response = requests.delete("http://127.0.0.1:8000/notes/999999999999999")

# Очистка всех заметок
@given('в системе нет заметок')
def delete_all_notes(context):
    notes = requests.get("http://127.0.0.1:8000/notes").json()
    for note in notes:
        requests.delete(f"http://127.0.0.1:8000/notes/{note['id']}")

# Обновление заметки по валидному ID
@when('обновляю заметку с новыми данными по валидному id')
def update_note_valid_id(context):
    note_id = context.note_id
    new_data = {
        "title": "New Title",
        "content": "New Content"
    }
    context.response = requests.put(
        f"http://127.0.0.1:8000/notes/{note_id}",
        json=new_data
    )
    context.new_note_data = new_data


# Проверка заметки после обновления
@then('заметка обновлена с новыми данными')
def check_note_new_data(context):
    note_id = context.note_id
    response = requests.get(f"http://127.0.0.1:8000/notes/{note_id}")
    data = response.json()
    assert data["title"] == "New Title"
    assert data["content"] == "New Content"

# Обновление заметки по не валидному ID
@when('обновляю заметку с новыми данными по не валидному id')
def update_note_invalid_id(context):
    new_data = {
        "title": "New Title",
        "content": "New Content"
    }
    context.response = requests.put(
        "http://127.0.0.1:8000/notes/999999999999999",
        json=new_data
    )

