-- 1. Початкова таблиця працівників
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT
);

-- 2. Перейменування таблиці
ALTER TABLE employees RENAME TO staff;

-- 3. Додавання нової колонки до переіменованої таблиці
ALTER TABLE staff ADD COLUMN salary REAL;

-- 4. Вставка  кількох рядків із даними
INSERT INTO staff (first_name, last_name, position, salary)
VALUES ('John', 'Doe', 'Python Developer', 2500.00);

INSERT INTO staff (first_name, last_name, position, salary)
VALUES ('Jane', 'Smith', 'QA Engineer', 2000.00);

INSERT INTO staff (first_name, last_name, position, salary)
VALUES ('Alex', 'Jones', 'DevOps Engineer', 3000.00);

-- 5. Оновлення даних, піднімемо зарплату John Doe
UPDATE staff
SET salary = 2800.00
WHERE first_name = 'John' AND last_name = 'Doe';

-- 6. Видалення рядка  QA Engineer
DELETE FROM staff
WHERE position = 'QA Engineer';