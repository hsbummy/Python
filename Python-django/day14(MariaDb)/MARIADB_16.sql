SELECT * FROM dept;
SELECT * FROM title;
SELECT * FROM emp;

UPDATE emp SET deptno = NULL WHERE empno='1001';

SELECT e.*,d.deptname,d.deptloc FROM emp e INNER JOIN dept d
ON e.deptno = d.deptno;

SELECT e.*, e.empname, d.deptname, t.titlename 
FROM emp e 
INNER JOIN dept d 
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno;

SELECT e.*, d.deptname, d.deptloc FROM emp e
LEFT OUTER JOIN dept d
ON e.deptno =d.deptno
UNION
SELECT e.*, d.deptname, d.deptloc FROM emp e
RIGHT OUTER JOIN dept d
ON e.deptno =d.deptno;

# 1. 2000년 이후 입사한 사원들의 정보를 출력, 사번, 이름, 타이틀, 부서, 지역
SELECT * FROM emp;
SELECT * FROM dept;
SELECT * FROM title;

SELECT emp.empno,emp.empname,title.titlename, dept.deptname,dept.deptloc  FROM emp 
LEFT OUTER JOIN dept
ON emp.deptno = dept.deptno
JOIN title
ON title.titleno = emp.titleno
WHERE YEAR(hdate) > 1999

# 2. 부서 이름 별 월급의 평균을 구하시오 단, 평균이 3000이상인 부서만 출력

SELECT dept.deptname, AVG(emp.salary)
FROM emp
JOIN dept
ON emp.deptno = dept.deptno
GROUP BY dept.deptname
HAVING AVG(emp.salary) >= 3000


# 3. 경기 지역ㅇ의 직원들의 평균 연봉을 구하시오

SELECT dept.deptloc, AVG(emp.salary) FROM emp
JOIN dept
ON emp.deptno=dept.deptno
WHERE dept.deptloc='경기'
GROUP BY deptloc

# 4. 홍영자 직원과 같은 부서 직원들의 근무 월수를 구하시오

SELECT emp.empname, dept.deptname, PERIOD_DIFF(DATE_FORMAT(NOW(),'%Y-%m'),DATE_FORMAT(hdate,'%Y%m'))
FROM emp
JOIN dept
ON emp.deptno = dept.deptno
WHERE emp.deptno = (SELECT deptno FROM emp WHERE emp.empname='하이');

# 5. 입사 년수가 가장 많은 직원 순으로 정렬 하여 순위를 정한다. 이름, 부서명, 직위 ,년수
SELECT RANK() OVER(ORDER BY emp.hdate) , emp.empname, dept.deptname, title.titlename,
YEAR(NOW())- YEAR(emp.hdate) AS 'subyear'
FROM emp
LEFT OUTER JOIN dept
ON emp.deptno = dept.deptno
JOIN title
ON emp.titleno = title.titleno;
