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


# --- ФУНКЦИЯ ДЛЯ ЭТОЙ ВЕТКИ (УДАЛЕНИЕ) ---

def delete_book():
    title = input("Введите название книги для удаления: ")
    books = load_books()
    
    # Создаем новый список без книги с указанным названием
    new_books = [b for b in books if b['title'].lower() != title.lower()]
    
    if len(books) == len(new_books):
        print("Книга не найдена.")
    else:
        save_books(new_books)
        print(f"Книга '{title}' успешно удалена.")

def main():
    while True:
        print("\n--- МЕНЮ (Удаление) ---")
        print("1. Добавить книгу (в разработке)")
        print("2. Показать все книги (в разработке)")
        print("3. Средняя оценка (в разработке)")
        print("4. Статистика по авторам (в разработке)")

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
        

        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            print("Эта функция находится в другой ветке. Используйте пункт 5 или 6.")
        elif choice == '5':
            delete_book() # Вызов функции удаления
        elif choice == '6':
            print("Выход...")

        if choice == '1':
            pass 
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            print("Выход из программы.")

            break
        else:
            print("Неверный ввод!")

if __name__ == "__main__":
    main()
