import os
import sqlite3


def run_and_print_queries():
    db_path = r"E:\PyCharm\pythonproject30\my_sqlite_project\hr.db"
    script_path = "task2.sql"

    # Перевіримо, чи файл бази даних лежить у потрібному місці
    if not os.path.exists(db_path):
        print(
            f"Помилка: Файл {db_path} не знайдено! Будь ласка, завантаж його та поклади в папку з цим скриптом."
        )
        return

    # Підключаємось до бази даних HR
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Список таблиць у відкритій базі даних: {tables}")

    # Читаємо SQL-скрипт
    with open(script_path, "r", encoding="utf-8") as f:
        sql_content = f.read()

    # Розділяємо запити за символом ";" і прибираємо порожні рядки
    queries = [q.strip() for q in sql_content.split(";") if q.strip()]

    print(f"Знайдено запитів для тестування: {len(queries)}\n")

    for index, query in enumerate(queries, 1):
        print(f"=== ТЕСТ ЗАПИТУ №{index} ===")
        print(f"SQL код:\n{query}\n")

        try:
            cursor.execute(query)

            # Отримуємо назви колонок
            titles = [description[0] for description in cursor.description]
            print(f"Результат (Колонки: {', '.join(titles)}):")

            # Беремо перші 5 рядків для демонстрації
            rows = cursor.fetchmany(5)

            for row in rows:
                print(row)

            # Якщо в таблиці більше ніж 5 рядків, попередимо про це
            remaining = cursor.fetchall()
            if remaining:
                print(f"... та ще {len(remaining)} рядків ...")

        except sqlite3.Error as e:
            print(f"Помилка при виконанні запиту №{index}: {e}")

        print("-" * 20 + "\n")

    conn.close()


if __name__ == "__main__":
    run_and_print_queries()