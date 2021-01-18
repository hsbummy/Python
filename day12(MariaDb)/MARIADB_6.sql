SHOW TABLES;

DESC employees;

SELECT * FROM employees WHERE emp_no > 10005 
AND hire_date in ('1990-01-01', '1991-01-26') 
AND gender in ('M')
AND first_name LIKE '%a%'
ORDER BY hire_date;

SELECT * FROM employees
WHERE hire_date BETWEEN '1990-01-01' AND '1990-12-31'
AND gender IN ('F')
ORDER BY birth_date DESC;


SELECT DISTINCT(gender) FROM employees;

SELECT * FROM employees LIMIT 5;

SELECT * FROM employees
WHERE gender IN ('M')
ORDER BY hire_date, birth_date 
LIMIT 0,2;