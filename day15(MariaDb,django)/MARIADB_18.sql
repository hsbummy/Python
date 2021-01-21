SELECT * FROM emp

# 1. 사원 정보를 조회한다. 사원의 모든 정보와 사원의 manager 이름까지 조회한다.

SELECT * FROM emp;

SELECT e.*, e1.empname AS 'manager 이름' FROM emp e
LEFT OUTER JOIN emp e1
ON e.manager = e1.empno

 


# 2. 사원 정보를 조회한다. 사원의 모든 정보와 사원의 manager 이름까지 조회한다. 추가적으로 사원의 부서와 타이틀 정보까지 조회한다.

SELECT * FROM emp;

SELECT e.*,dept.deptname,title.titlename, e1.empname AS 'manager 이름' FROM emp e
LEFT OUTER JOIN emp e1
ON e.manager = e1.empno
LEFT OUTER JOIN dept
ON e.deptno = dept.deptno
LEFT OUTER JOIN title
ON e.titleno = title.titleno;


# 트리거 

INSERT INTO orderTbl,,,,
UPDATE prodTbl SET ,,,,,