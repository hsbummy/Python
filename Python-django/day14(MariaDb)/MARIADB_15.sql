DROP TABLE emp;
DROP TABLE dept;
DROP TABLE title;


CREATE TABLE dept (
	deptno CHAR(2) PRIMARY KEY,
	deptname NVARCHAR(20),
	deptloc NVARCHAR(20)
);

CREATE TABLE title (
	titleno CHAR(2) PRIMARY KEY,
	titlename NVARCHAR(20)
);


CREATE TABLE emp (
	empno CHAR(4) PRIMARY KEY,
	titleno CHAR(2),
	deptno CHAR(2),
	empname NVARCHAR(10),
	manager CHAR(4),
	salary INT(5),
	hdate DATE
);

#ALTER TABLE emp
#ADD CONSTRAINT fk_title
#FOREIGN KEY (titleno)
#REFERENCES title (titleno);

#ALTER TABLE emp
#ADD CONSTRAINT fk_dept
#FOREIGN KEY (deptno)
#REFERENCES dept (deptno);

INSERT INTO title VALUES ('10','사원');
INSERT INTO title VALUES ('20','대리');
INSERT INTO title VALUES ('30','과장');
INSERT INTO title VALUES ('40','사장');
INSERT INTO title VALUES ('50','인턴');

INSERT INTO dept VALUES ('10','본사','서울');
INSERT INTO dept VALUES ('20','영업부','경기');
INSERT INTO dept VALUES ('30','생산부','부산');
INSERT INTO dept VALUES ('40','연구소','대전');

INSERT INTO emp VALUES ('1001','40','10','킹', NULL , 5000, '1997-01-01');
INSERT INTO emp VALUES ('1002','30','20','영업맨','1001', 4300,'1998-01-01');
INSERT INTO emp VALUES ('1003','30','30','생산맨','1001', 4800 ,'1999-01-01');
INSERT INTO emp VALUES ('1004','30','40','연구킹','1001', 4500,'1999-12-01');

INSERT INTO emp VALUES ('1005','20','20','이말숙','1002', 3300,'2000-01-01');
INSERT INTO emp VALUES ('1006','10','20','김말','1002', 2800,'2001-01-01');

INSERT INTO emp VALUES ('1007','20','30','하이','1003', 3500,'2000-12-01');
INSERT INTO emp VALUES ('1008','10','30','오이','1003', 2300,'2002-05-01');

INSERT INTO emp VALUES ('1009','20','40','흥국','1004', 3800,'2001-01-01');
INSERT INTO emp VALUES ('1010','10','40','병국','1004', 2500,'2002-12-01');


# 1. 직원정보를 출력한다. 직원이 연봉 정보와 연봉의 세금 정보를 같이 출력한다.
# 세금은 10%

# 직원정보 중 2000 이전에 입사 하였고 월급이 4000만원 미만인 직원을 조회

# manager가 있는 직원 중 이름에 '자'가 들어가 있는 직원정보 조회

# 월급이 2000미만은 '하' 4000미만은 '중' 4000이상은

SELECT * FROM emp;
SELECT empno, salary, (salary*0.1) AS tax FROM emp

SELECT * FROM emp WHERE YEAR(hdate) < 2001 AND salary < 4000;

SELECT * FROM emp WHERE empname like'%말%';

SELECT*,
	CASE
	WHEN salary < 2000 THEN '하'
	WHEN salary < 4000 THEN '중'
	WHEN salary >= 4000 THEN '고'
	END
FROM emp;


SELECT deptno, AVG(salary) FROM emp
GROUP BY deptno
HAVING AVG(salary) >= 3000;

SELECT deptno, AVG(salary)
FROM emp
WHERE titleno=10 OR titleno=20
GROUP BY deptno
HAVING AVG(salary) >=2500;

SELECT empno, AVG(salary)
FROM emp
WHERE YEAR(hdate) BETWEEN '2000' AND '2002';


SELECT RANK() OVER(ORDER BY SUM(salary) DESC) 'RK_SAL', deptno, SUM(salary)
FROM emp
GROUP BY deptno
ORDER BY 'RK_SAL';

#SELECT * FROM emp
#WHERE deptno='10';


SELECT * FROM emp
WHERE deptno=(SELECT deptno FROM dept
WHERE deptloc='서울')


SELECT * FROM emp
WHERE deptno = (SELECT deptno FROM emp WHERE empname='하이');

SELECT * FROM emp
WHERE titleno = (SELECT titleno FROM emp WHERE empname='흥국');