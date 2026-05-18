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
