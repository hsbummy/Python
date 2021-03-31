SELECT LEFT(UPPER(first_name),3), LPAD(last_name,10,'#'),
SUBSTR(last_name,2,3) 
FROM employees;
SELECT LEFT(UPPER(first_name),3), LPAD(last_name,10,'#'),
last_name
FROM employees;