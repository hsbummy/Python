SELECT emp_no, ADDDATE(hire_date,INTERVAL 31 DAY),
DATEDIFF(NOW(),hire_date),
PERIOD_DIFF(DATE_FORMAT(NOW(), '%Y%m',hire_date),DATE_FORMAT(hire_date,'%Y%m')),
YEAR(hire_date),MONTH(hire_date),DAY(hire_date)
FROM employees;

SELECT YEAR(hire_date),
AVG(PERIOD_DIFF(DATE_FORMAT(NOW(), '%Y%m'),DATE_FORMAT(hire_date,'%Y%m')))
FROM employees
GROUP BY YEAR(hire_date);