DROP DATABASE IF EXISTS tableDB;
CREATE DATABASE tableDB;

USE tableDB;

DROP TABLE IF EXISTS buyTBL, userTBL;
CREATE TABLE userTBL -- 회원 테이블
(  userID char(8), -- 사용자 아이디
	name nvarchar(10), -- 이름
	birthYear int, -- 출생연도
	addr nchar(2), -- 지역(경기,서울,경남 등으로 글자만 입력)
	mobile1 char(3), -- 휴대폰의국번(011, 016, 017, 018, 019, 010 등)
	mobile2 char(8), -- 휴대폰의 나머지 전화번호(하이픈 제외)
	height smallint, -- 키
	mDate date -- 회원 가입일
);

CREATE TABLE buyTBL -- 구매 테이블
(  num int, -- 순번(PK)
 	userid char(8), -- 아이디(FK)
 	prodName char(6), -- 물품명
 	groupName char(4), -- 붂류
 	price int , -- 단가
 	amount smallint -- 수량
);

USE tableDB;
DROP TABLE IF EXISTS buyTBL, userTBL;
CREATE TABLE userTBL
(  userID char(8) PRIMARY KEY ,
 	name varchar(10) NOT NULL,
	birthYear int NOT NULL,
 	addr char(2) NOT NULL,
 	mobile1 char(3) NULL,
 	mobile2 char(8) NULL,
 	height smallint NULL,
 	mDate date NULL
);

CREATE TABLE buyTBL
(  num int NOT NULL ,
 	userid char(8) PRIMARY KEY ,
 	prodName char(6) NOT NULL,
 	groupName char(4) NULL ,
 	price int NOT NULL,
 	amount smallint NOT NULL
);

USE tableDB;
DROP TABLE IF EXISTS buyTBL, userTBL;
CREATE TABLE userTBL
( userID char(8) PRIMARY KEY ,
 name varchar(10) NOT NULL,
 birthYear int NOT NULL,
 addr char(2) NOT NULL,
 mobile1 char(3) NULL,
 mobile2 char(8) NULL,
 height smallint NULL,
 mDate date NULL
);

CREATE TABLE buyTBL
( num int NOT NULL ,
 userid char(8) PRIMARY KEY ,
 prodName char(6) NOT NULL,
 groupName char(4) NULL ,
 price int NOT NULL,
 amount smallint NOT NULL
);


USE tableDB;
DROP TABLE IF EXISTS buyTBL, userTBL;
CREATE TABLE userTBL
( userID char(8) PRIMARY KEY,
 name varchar(10) NOT NULL,
 birthYear int NOT NULL,
 addr char(2) NOT NULL,
 mobile1 char(3) NULL,
 mobile2 char(8) NULL,
 height smallint NULL,
 mDate date NULL
);

CREATE TABLE buyTBL
( num int AUTO_INCREMENT NOT NULL PRIMARY KEY,
 prodName char(6) NOT NULL,
 groupName char(4) NULL ,
 price int NOT NULL,
 amount smallint NOT NULL
);

DROP TABLE IF EXISTS buyTBL;
CREATE TABLE buyTBL
( num int AUTO_INCREMENT NOT NULL PRIMARY KEY ,
 userid char(8) NOT NULL ,
 prodName char(6) NOT NULL,
 groupName char(4) NULL ,
 price int NOT NULL,
 amount smallint NOT NULL,
 FOREIGN KEY(userid) REFERENCES userTBL(userID)
);

INSERT INTO userTBL VALUES
('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES
('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES
('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');

INSERT INTO buyTBL VALUES(NULL, 'KBS', '운동화', NULL , 30, 2);
INSERT INTO buyTBL VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTBL VALUES(NULL, 'JYP', '모니터', '전자', 200, 1);

DROP TABLE IF EXISTS buyTBL;
DROP TABLE IF EXISTS userTBL;
CREATE TABLE userTBL
(
 userID CHAR(8) NOT NULL,
 name VARCHAR(10) NOT NULL,
 birthYear INT NOT NULL,
 CONSTRAINT PRIMARY KEY PK_userTBL_userID (userID)
);

DROP TABLE IF EXISTS prodTbl;
CREATE TABLE prodTbl
( prodCode CHAR(3) NOT NULL,
 prodID CHAR(4) NOT NULL,
 prodDate DATETIME NOT NULL,
 prodCur CHAR(10) NULL
);
ALTER TABLE prodTbl
ADD CONSTRAINT PRIMARY KEY (prodCode, prodID); -- 복합키

DROP TABLE IF EXISTS prodTbl;
CREATE TABLE prodTbl
( prodCode CHAR(3) NOT NULL,
 prodID CHAR(4) NOT NULL,
 prodDate DATETIME NOT NULL,
 prodCur CHAR(10) NULL,
 CONSTRAINT PK_prodTbl_proCode_prodID
PRIMARY KEY (prodCode, prodID)
);
SHOW INDEX FROM prodTbl ;

-- 두 컬럼의 실행 소요 시간 비교
USE employees;
SELECT * FROM employees WHERE emp_no = 10838;
SELECT * FROM employees WHERE first_name = 'Deniz';


DROP TABLE IF EXISTS buyTBL, userTBL;
CREATE TABLE userTBL
( userID CHAR(8) NOT NULL PRIMARY KEY,
 name VARCHAR(10) NOT NULL,
 birthYear INT NOT NULL
);
CREATE TABLE buyTBL
( num INT AUTO_INCREMENT NOT NULL PRIMARY KEY ,
 userID CHAR(8) NOT NULL,
 prodName CHAR(6) NOT NULL,
 FOREIGN KEY(userID) REFERENCES userTBL(userID)
);

DROP TABLE IF EXISTS buyTBL;
CREATE TABLE buyTBL
( num INT AUTO_INCREMENT NOT NULL PRIMARY KEY ,
 userID CHAR(8) NOT NULL,
 prodName CHAR(6) NOT NULL,
 CONSTRAINT FK_userTBL_buyTBL FOREIGN KEY(userID) REFERENCES userTBL(userID)
);

DROP TABLE IF EXISTS buyTBL;
CREATE TABLE buyTBL
( num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 userID CHAR(8) NOT NULL,
 prodName CHAR(6) NOT NULL
);
ALTER TABLE buyTBL
 ADD CONSTRAINT FK_userTBL_buyTBL
 FOREIGN KEY (userID) REFERENCES userTBL(userID);
SHOW INDEX FROM buyTBL ;

ALTER TABLE buyTBL
 DROP FOREIGN KEY FK_userTBL_buyTBL; -- 외래 키 제거
ALTER TABLE buyTBL
 ADD CONSTRAINT FK_userTBL_buyTBL
 FOREIGN KEY (userID) REFERENCES userTBL (userID) ON UPDATE CASCADE;
 
 
USE tableDB
;
DROP TABLE IF EXISTS buyTBL, userTBL
;
CREATE TABLE userTBL
( userID CHAR(8) NOT NULL PRIMARY KEY,
 name VARCHAR(10) NOT NULL,
 birthYear INT NOT NULL,
 email CHAR(30) NULL UNIQUE
);
DROP TABLE IF EXISTS userTBL
;
CREATE TABLE userTBL
( userID CHAR(8) NOT NULL PRIMARY KEY,
 name VARCHAR(10) NOT NULL,
 birthYear INT NOT NULL,
 email CHAR(30) NULL ,
 CONSTRAINT AK_email UNIQUE (email)
);

-- 출생연도가 1900년 이후 그리고 2020년 이젂, 이름은 반드시 넣어야 함.
DROP TABLE IF EXISTS userTBL;
CREATE TABLE userTBL
( userID CHAR(8) PRIMARY KEY,
 name VARCHAR(10) ,
 birthYear INT CHECK (birthYear >= 1900 AND birthYear <= 2020),
 mobile1 CHAR(3) NULL,
 CONSTRAINT CK_name CHECK ( name IS NOT NULL)
);

-- 휴대폰 국번 체크
ALTER TABLE userTbl
 ADD CONSTRAINT CK_mobile1
 CHECK (mobile1 IN ('010','011','016','017','018','019')) ;
 
DROP TABLE IF EXISTS userTBL;
CREATE TABLE userTBL
( userID char(8) NOT NULL PRIMARY KEY,
 name varchar(10) NOT NULL,
 birthYear int NOT NULL DEFAULT -1,
 addr char(2) NOT NULL DEFAULT '서울',
 mobile1 char(3) NULL,
 mobile2 char(8) NULL,
 height smallint NULL DEFAULT 170,
 mDate date NULL
);

DROP TABLE IF EXISTS userTBL;
CREATE TABLE userTBL
( userID char(8) NOT NULL PRIMARY KEY,
 name varchar(10) NOT NULL,
 birthYear int NOT NULL ,
 addr char(2) NOT NULL,
 mobile1 char(3) NULL,
 mobile2 char(8) NULL,
 height smallint NULL,
 mDate date NULL
);

ALTER TABLE userTBL
 ALTER COLUMN birthYear SET DEFAULT -1;
ALTER TABLE userTBL
 ALTER COLUMN addr SET DEFAULT '서울';
ALTER TABLE userTBL
 ALTER COLUMN height SET DEFAULT 170;
 
-- default 문은 DEFAULT로 설정된 값을 자동 입력한다.
INSERT INTO userTBL VALUES
('LHL', '이혜리', default, default, '011', '1234567', default, '2022.12.12');
-- 열이름이 명시되지 않으면 DEFAULT로 설정된 값을 자동 입력한다
INSERT INTO userTBL(userID, name) VALUES('KAY', '김아영');
-- 값이 직접 명기되면 DEFAULT로 설정된 값은 무시된다.
INSERT INTO userTBL VALUES
('WB', '원빈', 1982, '대전', '019', '9876543', 176, '2023.5.5');

SELECT * FROM usertbl;

USE employees;
CREATE TEMPORARY TABLE IF NOT EXISTS tempTBL (id INT, name CHAR(7));
CREATE TEMPORARY TABLE IF NOT EXISTS employees (id INT, name CHAR(7));
DESCRIBE tempTBL;
DESCRIBE employees;
INSERT INTO tempTBL VALUES (1, 'This');
INSERT INTO employees VALUES (2, 'MariaDB');
SELECT * FROM tempTBL;
SELECT * FROM employees;
-- 로그아웃 후 다시 로그인
USE employees;
SELECT * FROM tempTBL;
SELECT * FROM employees;

USE tableDB;
ALTER TABLE userTBL
 ADD homepage VARCHAR(30) -- 열추가
 DEFAULT 'http://www.hanbit.co.kr' -- 디폴트값
 NULL; -- Null 허용함
 
ALTER TABLE userTBL
 DROP COLUMN mobile1;

ALTER TABLE userTBL
 CHANGE COLUMN name uName VARCHAR(20) NULL ;
 
ALTER TABLE userTBL
 DROP PRIMARY KEY; -- 외래키 제약조건이 있으면 에러 발생

ALTER TABLE buyTBL
 DROP FOREIGN KEY FK_userTBL_buyTBL;