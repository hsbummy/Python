SELECT emp_no, sum(salary) AS SSAL FROM salaries
GROUP BY emp_no
HAVING SUM(salary) > 100000
AND emp_no = 10001;

SELECT emp_no, salary FROM salaries
WHERE salary > 70000
AND emp_no = 10001;

SELECT emp_no, ROUND(salary/12,2) AS month_s FROM salaries

SELECT emp_no, AVG(salary/12) AS SAL FROM salaries
GROUP BY emp_no
HAVING SAL >= 5000
ORDER BY emp_no ASC, SAL DESC
LIMIT 5

SELECT MAX(salary) FROM salaries

SELECT emp_no, MAX(salary), MIN(salary), MAX(salary) - MIN(salary) FROM salaries
GROUP BY emp_no

SELECT COUNT(*) FROM salaries

SELECT emp_no, COUNT(salary)
FROM salaries
GROUP BY emp_no
