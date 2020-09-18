use employees;
DESC titles;
DESC employees;

DROP TABLE IF EXISTS sqlDB; 
CREATE DATABASE sqlDB;

SELECT * FROM usertbl;
SELECT * FROM buytbl;

USE sqlDB; 
SELECT * FROM usertbl;

SELECT * FROM userTbl WHERE NAME='김경호';  -- 대입연사자 없다. 동등 연산자.

SELECT userID, Name 
FROM userTbl 
WHERE birthYear >= 1970 AND height >= 182;

SELECT userID, Name 
FROM userTbl 
WHERE birthYear >= 1970 OR height >= 182;

SELECT userID, Name 
FROM userTbl 
WHERE height >= 180 AND height <= 183;

SELECT userID, Name 
FROM userTbl 
WHERE height BETWEEN 180 AND 183;

SELECT Name, addr 
FROM userTbl 
WHERE addr = '경남' OR addr = '전남' OR addr = '경북';

SELECT Name, addr 
FROM userTbl 
WHERE addr IN('경남', '전남', '경북');

SELECT Name, height 
FROM userTbl 
WHERE name LIKE '김%';

SELECT Name, height 
FROM userTbl 
WHERE name LIKE '_종신';

USE employees; 
SELECT first_name AS 이름, gender AS 성별 FROM employees; 
SELECT first_name 이름, gender 성별, hire_date 입사일 FROM employees;

SELECT *
FROM employees 
WHERE last_name = 'Lenart';

SELECT *
FROM employees 
WHERE birth_date >= '1960-01-01'; -- 문자열을 알아서 date type으로 바꿔줌

SELECT *
FROM employees 
WHERE birth_date >= '1960-01-01' 
	AND birth_date <= '1960-12-31';

SELECT *
FROM employees 
WHERE birth_date BETWEEN '1960-01-01' AND '1960-12-31';

SELECT *
FROM employees 
WHERE last_name = 'Lenart' 
	OR last_name = 'Baaz' 
	OR last_name = 'Pillow';