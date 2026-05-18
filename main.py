import json
import os

def load_books():
    if not os.path.exists('books.json'):
        return []
    with open('books.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_books(books):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

# --- НОВАЯ ФУНКЦИЯ ДЛЯ ЭТОЙ ВЕТКИ ---
def add_book():
    author = input("Автор: ")
    title = input("Название: ")
    
    try:
        rating = int(input("Оценка (1-5): "))
        if not (1 <= rating <= 5):
            print("Ошибка: Оценка должна быть от 1 до 5")
            return
    except ValueError:
        print("Ошибка: Введите число")
        return

    date = input("Дата прочтения: ")
    books = load_books()
    
    # Проверка на дубликаты
    if any(b['title'].lower() == title.lower() and b['author'].lower() == author.lower() for b in books):
        print("Ошибка: Такая книга уже существует!")
        return

    books.append({"author": author, "title": title, "rating": rating, "date": date})
    save_books(books)
    print("Книга добавлена!")

def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Средняя оценка")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_book() # <--- ЗДЕСЬ МЫ ВЫЗЫВАЕМ ФУНКЦИЮ
        elif choice == '6':
            print("Выход...")
            break
        else:
            print("Этот пункт пока не реализован в этой ветке или введен неверный номер.")

if __name__ == "__main__":
    main()
