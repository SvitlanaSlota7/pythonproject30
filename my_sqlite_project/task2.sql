-- 1. Запит для відображення імен та прізвищ із використанням псевдонімів
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

-- 2. Запит для отримання унікальних ID департаментів
SELECT DISTINCT department_id
FROM employees;

-- 3. Запит для отримання всіх даних про працівників, відсортованих за ім'ям у зворотному алфавітному порядку
SELECT * FROM employees
ORDER BY first_name DESC;

-- 4. Запит для отримання імені, прізвища, зарплати та PF (який становить 12% від зарплати)
SELECT first_name, last_name, salary, (salary * 0.12) AS PF
FROM employees;

-- 5. Запит для отримання максимальної та мінімальної зарплати серед усіх працівників
SELECT MAX(salary) AS "Maximum Salary", MIN(salary) AS "Minimum Salary"
FROM employees;

-- 6. Запит для отримання місячної зарплати кожного працівника (округленої до 2 знаків після коми)
-- Примітка: зазвичай у поле salary в базах типу HR записують річний дохід, тому ділимо на 12.
SELECT first_name, last_name, ROUND(salary / 12.0, 2) AS "Monthly Salary"
FROM employees;