DROP VIEW vemp

SELECT * FROM vemp

CREATE VIEW vemp
AS
SELECT e.empno, e.empname, d.deptname, t.titlename 
FROM emp e 
INNER JOIN dept d 
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno;