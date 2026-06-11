import sqlite3


def run_sql_script():
    # Підключаємося до файлу бази даних. Файла немає, він створиться
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()

    print("Виконання SQL-скрипту")

    # Читаємо файл
    with open("task1.sql", "r", encoding="utf-8") as f:
        sql_script = f.read()

    # executeScript виконує кілька SQL-команд, розділених знаком ";"
    try:
        cursor.executescript(sql_script)
        conn.commit()
        print("SQL-скрипт успішно виконано!")
    except sqlite3.Error as e:
        print(f"Помилка при виконанні SQL: {e}")

    # Перевіримо фінальний результат у таблиці
    print("\nФінальний вміст таблиці 'staff'")
    try:
        cursor.execute("SELECT * FROM staff;")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Ім'я: {row[1]} {row[2]}, Посада: {row[3]}, Зарплата: {row[4]}")
    except sqlite3.Error as e:
        print(f"Не вдалося прочитати таблицю: {e}")

    # Закриваємо з'єднання
    conn.close()


if __name__ == "__main__":
    run_sql_script()