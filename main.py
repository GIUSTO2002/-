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

# --- ФУНКЦИИ ДЛЯ ЭТОЙ ВЕТКИ (СПИСОК И СТАТИСТИКА) ---

def show_books():
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
    print("\n--- ВАШИ КНИГИ ---")
    for b in books:
        print(f"{b['author']} - {b['title']} | Оценка: {b['rating']}")

def show_stats():
    books = load_books()
    if not books:
        print("Нет данных для статистики.")
        return
    
    # Расчет средней оценки
    avg = sum(b['rating'] for b in books) / len(books)
    print(f"\nСредняя оценка: {avg:.2f}")
    
    # Статистика по авторам
    stats = {}
    for b in books:
        stats[b['author']] = stats.get(b['author'], 0) + 1
    
    print("Книг по авторам:")
    for author, count in stats.items():
        print(f"- {author}: {count}")

def main():
    while True:
        print("\n--- МЕНЮ (Статистика) ---")
        print("1. Добавить книгу (не реализовано в этой ветке)")
        print("2. Показать все книги")
        print("3. Средняя оценка")
        print("4. Статистика по авторам")
        print("5. Удалить книгу (не реализовано в этой ветке)")
        print("6. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            print("Этот пункт будет доступен после слияния веток.")
        elif choice == '2':
            show_books() # Вызов функции списка
        elif choice == '3' or choice == '4':
            show_stats() # Вызов функции статистики
        elif choice == '6':
            print("Выход...")
            break
        else:
            print("Неверный ввод или функция недоступна в этой ветке.")

if __name__ == "__main__":
    main()
