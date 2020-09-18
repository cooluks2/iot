USE sqldb;

SELECT * FROM usertbl;

SELECT * FROM buytbl;

SELECT * FROM usertbl WHERE NAME='김경호'; -- 대입연사자 없다. 동등 연산자.

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

SELECT NAME, addr
FROM usertbl
WHERE addr = '경남' OR addr='전남' OR addr = '경북';

SELECT NAME, addr
FROM usertbl
WHERE addr IN('경남', '전남', '경북');

SELECT NAME, height
FROM usertbl
WHERE NAME LIKE '김%'; -- % : 아무 글자가 와도 상관 없음 - 개수에 제한 없음

SELECT Name, height
FROM userTbl
WHERE name like '_종신'; -- _ : 한 글자로 아무 글자가 와도 상관없음



USE employees;

SELECT first_name FROM employees;

SELECT first_name, last_name, gender FROM employees;

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

SELECT *
FROM employees
WHERE last_name IN('Lenart', 'Baaz', 'Pillow');


/*
❖ ANY/ALL/SOME 그리고 서브쿼리(SubQuery, 하위쿼리)
○ 서브쿼리
▪ FROM/WHERE 절에 SELECT 문을 제시
▪ 서브 쿼리는 반드시 ()안에 작성
*/

USE sqldb;
SELECT Name, height FROM userTBL WHERE height > 177;

SELECT Name, height FROM userTbl
WHERE height > (SELECT height FROM userTbl WHERE NAME = '김경호');
-- 단일행  (결과가 행 하나)

SELECT Name, height FROM userTbl
WHERE height >= (SELECT height FROM userTbl WHERE addr = '경남');
-- 오류 (행이 여러개 나온다.)

/*
❖ ANY/ALL/SOME 그리고 서브쿼리(SubQuery, 하위쿼리)
○ ANY/ALL
*/

SELECT height FROM userTbl WHERE addr = '경남';

SELECT Name, height FROM userTbl -- 또는
WHERE height >= ANY (SELECT height FROM userTbl WHERE addr = '경남');

SELECT Name, height FROM userTbl -- 그리고
WHERE height >= ALL (SELECT height FROM userTbl WHERE addr = '경남');

/*
❖ ANY/ALL/SOME 그리고 서브쿼리(SubQuery, 하위쿼리)
○ SOME
▪ ANY와 같은 의미
▪ = 연산자와 사용 → IN과 동일
*/

SELECT Name, height FROM userTbl
WHERE height = SOME (SELECT height FROM userTbl WHERE addr = '경남');

SELECT Name, height FROM userTbl
WHERE height IN (SELECT height FROM userTbl WHERE addr = '경남');

/*
❖ 원하는 순서대로 정렬하여 출력
○ 오름차순 : ASC (디폴트, 생략가능)
○ 내림차순: DESC
실전에서 항상 쓰인다!
*/


SELECT NAME, mDate FROM userTbl ORDER BY mDate;
SELECT NAME, mDate FROM userTbl ORDER BY mDate DESC;
SELECT NAME, height FROM userTbl ORDER BY height DESC, NAME DESC;

/*
❖ 중복된 것은 하나만 남기는 DISTINCT
*/

SELECT addr FROM userTbl;
SELECT addr FROM userTbl ORDER BY addr;
SELECT DISTINCT addr FROM userTbl; -- DISTINCT 사용 때 , 이용하면 오류

/*
❖ 출력하는 개수를 제한하는 LIMIT
*/

USE employees;
SELECT emp_no, hire_date FROM employees
	ORDER BY hire_date ASC;

SELECT emp_no, hire_date FROM employees
	ORDER BY hire_date ASC
	LIMIT 5;
	
--☆☆☆ 게시판 페이지 출력할 때 필요!
SELECT emp_no, hire_date FROM employees
	ORDER BY hire_date ASC
	LIMIT 0, 5; -- LIMIT 5 OFFSET 0 과 동일 ☆☆☆
	-- start = (page-1)*per_page
	-- end = start + per_page - 1
	-- ex) math.ceil(total/per_page)로 필요한 페이지 수 알 수 있다.(python)
	
	
	
/*
❖ 테이블을 복사하는 CREATE TABLE … SELECT
○ 기존 테이블과 동일한 구조로 테이블 생성
○ KEY 제약조건은 복사되지 않음
▪ 필드의 이름, 타입, 길이, NULL 여부가 동일
○ 특정 컬럼(SELECT 절 제시) 또는 특정 행만(WHERE절 제시) 복사 가능

형식]
CREATE TABLE 새로운 테이블명(SELECT 복사할열 FROM 기본테이블명)
*/

USE sqlDB;

CREATE TABLE buyTbl2 (SELECT * FROM buyTbl);
SELECT * FROM buytbl2;

CREATE TABLE buytbl3 (SELECT userID, prodName FROM buyTbl);
SELECT * FROM buytbl3;


-- 컬럼명이 user, product이 되도록 하세요.
CREATE TABLE buytbl4 (SELECT userID AS user, prodName AS product FROM buytbl); -- AS 생략가능
SELECT * FROM buytbl4;
-- subQuery에 where, order 사용하면 일부만 뽑을 수 있다.



/*
❖ GROUP BY 및 HAVING 그리고 집계 함수
○ GROUP BY 절
▪ 특정 컬럼에 대해 동일한 값을 가지는 행들을 하나의 행으로 처리
▪ 통계 작업에 사용
*/

/*
○ GROUP BY 절
*/
SELECT userID, amount
FROM buyTbl
ORDER BY userID;

SELECT userID, SUM(amount)
FROM buyTbl
GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수'
FROM buyTbl
GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(price*amount) AS '총 구매액'
FROM buyTbl
GROUP BY userID;

-- 비교
SELECT userID, price*amount, price, amount
FROM buytbl
GROUP BY userID;
-- group by 이용할 때 group by에 제시한 컬럼, 통계처리한 결과만 올 수 있따.



/*
○ 집계 함수
*/

SELECT COUNT(mobile1) FROM usertbl; -- null은 세지 않는다.
SELECT COUNT(userID) FROM usertbl;
SELECT COUNT(*) FROM buytbl; -- 그래서 * 많이 사용함.

USE sqlDB;
SELECT AVG(amount) AS '평균 구매 개수'
FROM buytbl;

SELECT userID, AVG(amount) AS '평균 구매 개수'
FROM buytbl
GROUP BY userID;

-- 잘못된 사용 예(1)
SELECT NAME, MAX(height), MIN(height) FROM usertbl;

-- 잘못된 사용 예(2)
SELECT NAME, MAX(height), MIN(height)
FROM usertbl
GROUP BY NAME;

-- 이렇게 해야 행이 2개가 나온다.
SELECT Name, height
FROM userTbl
WHERE height = (SELECT MAX(height)FROM userTbl)
OR height = (SELECT MIN(height)FROM userTbl) ;

SELECT COUNT(*) FROM usertbl; -- 전체 행의 개수

SELECT COUNT(mobile1) AS '휴대폰이 있는 사용자'
FROM usertbl; -- 지정한 컬럼에 NULL있는 행은 제외



/*
○ HAVING 절
▪ GROUP BY 결과에서 필터링
*/

USE sqlDB;

SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
FROM buytbl
GROUP BY userID;

-- 잘못된 코드 ( GROUP BY 동작 전에 filtering 한다.)
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
FROM buyTbl
WHERE SUM(price*amount) > 1000
GROUP BY userID ;

-- GROUP 되어 있는 것에 WHERE를 쓰고 싶을 때
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
FROM buyTbl
GROUP BY userID
HAVING SUM(price*amount) > 1000 ;

SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
FROM buyTbl
GROUP BY userID
HAVING SUM(price*amount) > 1000
ORDER BY SUM(price*amount) ;

-- 수식 대신에 컬럼명을 써도 됨.
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
FROM buyTbl
GROUP BY userID
HAVING 총구매액  > 1000
ORDER BY 총구매액 DESC ;


/*
○ ROLLUP
▪ 중간 합계와 총 합을 출력
*/

SELECT num, groupname, SUM(price*amount) AS '비용'
FROM buytbl
GROUP BY groupname, num -- grouping의 효과는 없다.
WITH ROLLUP;

-- GROUP BY 에서 groupname만 주었을 때
SELECT groupName, SUM(price * amount) AS '비용'
FROM buyTbl
GROUP BY groupName #
WITH ROLLUP; -- 합계만 나온다.






/*
❖ SQL 문의 종류
○ DDL : Data Definition Language
▪ 데이터베이스 객체(테이블, 인덱스, 뷰 등)의 생성, 수정, 삭제 조작
○ DML : Data Manipulation Language
▪ 데이터의 선택, 삽입, 수정, 삭제 등 데이터 조작
▪ SELECT, INSERT, UPDATE, DELETE
○ DCL : Data Control Language
▪ 권한 부여
*/

/*
❖ 데이터의 삽입: INSERT
*/

USE sqlDB;


CREATE TABLE testTBL1 (id INT, userName CHAR(3), age INT);

INSERT INTO testtbl1 VALUES (1, '홍길동', 25); -- cteate table 순서로 인식
INSERT INTO testtbl1(id, userName) VALUES (2, '설현'); -- 인수보다 적으면 반드시 이름을 주어야 한다.
INSERT INTO testtbl1(userName, age, id) VALUES ('초아',26, 3); -- 순서를 바꿔줄 수 있다.

/*
❖ 자동 증가하는 AUTO_INCREMENT
○ 값을 제시하지 않은 경우 자동 증가 값으로 추가
○ PRIMARY KEY 필드에 주로 사용 (반드시 값을 가져야하며, 중복되는 값이 있으면 안된다.)
*/

USE sqlDB;

CREATE TABLE testTBL2
	(id INT AUTO_INCREMENT PRIMARY KEY,
	 userName CHAR(3),
	 age INT );

INSERT INTO testTBL2 VALUES (NULL, '지민', 25);
INSERT INTO testTBL2 VALUES (NULL, '유나', 22);
INSERT INTO testTBL2 VALUES (NULL, '유경', 21);
INSERT INTO testtbl2(userName, age) VALUES ('둘리', 12);
-- AUTO_INCREMENT 없으면 오류이다.

SELECT * FROM testtbl2;

-- 최근 추가 데이터 순으로 출력
SELECT * FROM testtbl2
	ORDER BY id DESC;
	

/*
❖ 다중 입력
*/
CREATE TABLE testTBL3
	(id INT AUTO_INCREMENT PRIMARY KEY,
	 userName CHAR(3),
	 age INT );


INSERT INTO testTBL3 VALUES (NULL, '나연', 20);
INSERT INTO testTBL3 VALUES (NULL, '정연', 18);
INSERT INTO testTBL3 VALUES (NULL, '모모', 19);

-- 위와 같다.

INSERT INTO testTBL3 VALUES
(NULL, '나연', 20),
(NULL, '정연', 18),
(NULL, '모모', 19);


/*
❖ 대량의 샘플 데이터 생성
형식:
INSERT INTO 테이블이름(열 이름1, 열 이름2, …)
SELECT 문;
*/

-- SELECT subQuery 를 이용하여 값을 넣겠다.
-- SELECT 문장의 결과로써 대응하는 값을 넣으려고 한다.
USE sqlDB;
CREATE TABLE testTBL4
	(id INT, Fname VARCHAR(50), Lname VARCHAR(50));
	
INSERT INTO testTBL4
SELECT emp_no, first_name, last_name
FROM employees.employees; -- 데이터 타입과 컬럼 개수가 같아야한다.
-- 다른 DB에서 가져와서 앞에 employees 붙여주어야한다.
-- 만들어져 있는 TABLE에 집어 넣는거

-- 만들면서 넣는거
USE sqlDB;
CREATE TABLE testTBL5
	(SELECT emp_no, first_name, last_name FROM employees.employees) ;


/*
❖ 데이터의 수정 : UPDATE 문
형식:
UPDATE 테이블이름
SET 열1=값1, 열2=값2 …
[WHERE 조건];
※ WHERE 조건이 없으면 전체 행이 수정
*/
-- 먼저 kyoichi가 있는지 확인하자
SELECT * FROM testtbl4
WHERE Fname = 'kyoichi';

UPDATE testtbl4
SET Lname = '없음'
WHERE Fname = 'kyoichi'; -- 결과는 안나온다.

USE sqlDB;
UPDATE buytbl2 SET price = price*1.5 ;


/*
❖ 데이터의 삭제: DELETE FROM
DELETE FROM 테이블 이름
[WHERE 조건];
※ WHERE 조건이 없으면 전체 행이 삭제
*/

-- 먼저 Aamer 있는지 확인하자
SELECT * FROM testtbl4
WHERE Fname = 'Aamer';

USE sqlDB;
DELETE FROM testtbl4 WHERE Fname = 'Aamer';

-- 먼저 Mary 있는지 확인하자
SELECT * FROM testtbl4
WHERE Fname = 'Mary'; -- 데이터는 대소문자 구분한다.

DELETE FROM testtbl4 WHERE Fname = 'Mary' LIMIT 5;

