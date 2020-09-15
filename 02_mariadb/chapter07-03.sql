USE sqlDB;

SELECT *
FROM buyTBL
	INNER JOIN userTBL
	ON buyTBL.userID = userTBL.userID
WHERE buyTBL.userID = 'BBK'; -- 이름이 중복되면 테이블 명과 같이 줘야한다.

USE sqlDB;

SELECT *
FROM buyTBL
	INNER JOIN userTBL
	ON buyTBL.userID = userTBL.userID;
	
SELECT userID, name, prodName, addr, CONCAT(mobile1, mobile2) AS '연락처'
FROM buytbl
	INNER JOIN usertbl
	ON buyTBL.userID = userTBL.userID ;

SELECT buyTBL.userID, name, prodName, addr, CONCAT(mobile1,mobile2) AS '연락처'
FROM buyTBL
	INNER JOIN userTBL
	ON buyTBL.userID = userTBL.userID ;
	
SELECT buyTBL.userID, userTBL.name, buyTBL.prodName, userTBL.addr,
CONCAT(userTBL.mobile1, userTBL.mobile2) AS '연락처'
FROM buyTBL
INNER JOIN userTBL
ON buyTBL.userID = userTBL.userID;

SELECT B.userID, U.name, B.prodName, U.addr,
CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM buyTBL B
INNER JOIN userTBL U
ON B.userID = U.userID;

SELECT B.userID, U.name, B.prodName, U.addr,
CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM buyTBL B
INNER JOIN userTBL U
ON B.userID = U.userID
WHERE B.userID = 'JYP';

SELECT B.userID, U.name, B.prodName, U.addr,
CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM buyTBL B
INNER JOIN userTBL U
ON B.userID = U.userID
WHERE B.userID = 'JYP'
ORDER BY U.userID;

SELECT DISTINCT U.userID, U.name, U.addr
FROM userTBL U
INNER JOIN buyTBL B
ON U.userID = B.userID
ORDER BY U.userID ;

SELECT U.userID, U.name, U.addr
FROM userTBL U
WHERE EXISTS (
SELECT *
FROM buyTBL B
WHERE U.userID = B.userID );

-- 예제
SELECT U.addr, SUM(B.amount) '수량', SUM(B.amount*B.price) '매출액'
FROM usertbl U
	INNER JOIN buytbl B
	ON B.userID = U.userID
GROUP BY U.addr;



USE sqlDB;
CREATE TABLE stdTBL(
 stdName VARCHAR(10) NOT NULL PRIMARY KEY, -- NULL을 허용하지 않음
 addr CHAR(4) NOT NULL
);

CREATE TABLE clubTBL(
 clubName VARCHAR(10) NOT NULL PRIMARY KEY,
 roomNo CHAR(4) NOT NULL
);

CREATE TABLE stdclubTBL(
 num int AUTO_INCREMENT NOT NULL PRIMARY KEY,
 stdName VARCHAR(10) NOT NULL,
 clubName VARCHAR(10) NOT NULL,
 FOREIGN KEY(stdName) REFERENCES stdTBL(stdName),   -- ☆
 FOREIGN KEY(clubName) REFERENCES clubTBL(clubName) -- ☆
);

INSERT INTO stdTBL VALUES
(N'김범수', N'경남'), (N'성시경', N'서울'), (N'조용필', N'경기'),
(N'은지원', N'경북'), (N'바비킴', N'서울');

INSERT INTO clubTBL VALUES
(N'수영', N'101호'), (N'바둑', N'102호'), (N'축구', N'103호'),
(N'봉사', N'104호');

INSERT INTO stdclubTBL VALUES
(NULL, N'김범수', N'바둑'), (NULL, N'김범수', N'축구'),
(NULL, N'조용필', N'축구'), (NULL, N'은지원', N'축구'),
(NULL, N'은지원', N'봉사'), (NULL, N'바비킴', N'봉사');


-- 3개의 테이블 조인
SELECT S.stdName, S.addr, C.clubName, C.roomNo
FROM stdTBL S
INNER JOIN stdclubTBL SC
ON S.stdName = SC.stdName
INNER JOIN clubTBL C
ON SC.clubName = C.clubName
ORDER BY S.stdName;



-- outer join
USE sqlDB;
SELECT U.userID, U.name, B.prodName, U.addr,
CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM userTBL U
LEFT OUTER JOIN buyTBL B
ON U.userID = B.userID
ORDER BY U.userID;

SELECT U.userID, U.name, B.prodName, U.addr,
CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM buyTBL B
RIGHT OUTER JOIN userTBL U
ON U.userID = B.userID
ORDER BY U.userID;

-- 구매이력이 없는 사용자만 출력
SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM userTBL U
  LEFT OUTER JOIN buyTBL B
    ON U.userID = B.userID
WHERE B.prodName IS NULL
ORDER BY U.userID;

-- 모든 사용자에 대한 구매액
SELECT U.userID, U.name, SUM(B.price*B.amount) AS '총구매액'
FROM userTBL U
  LEFT OUTER JOIN buyTBL B
    ON U.userID = B.userID
GROUP BY U.userID
ORDER BY U.userID;

-- NULL 부분 보기 좋게 처리
SELECT U.userID, U.name, IFNULL(SUM(B.price*B.amount), 0) AS '총구매액'
FROM userTBL U
  LEFT OUTER JOIN buyTBL B
    ON U.userID = B.userID
GROUP BY U.userID
ORDER BY U.userID;


-- SELF JOIN
USE sqlDB;
CREATE TABLE empTbl (emp CHAR(3), manager CHAR(3), empTel VARCHAR(8));
INSERT INTO empTbl VALUES
(N'나사장',NULL,'0000'),
(N'김재무',N'나사장','2222'),
(N'김부장',N'김재무','2222-1'),
(N'이부장',N'김재무','2222-2'),
(N'우대리',N'이부장','2222-2-1'),
(N'지사원',N'이부장','2222-2-2'),
(N'이영업',N'나사장','1111'),
(N'한과장',N'이영업','1111-1'),
(N'최정보',N'나사장','3333'),
(N'윤차장',N'최정보','3333-1'),
(N'이주임',N'윤차장','3333-1-1');

SELECT A.emp AS '부하직원' , B.emp AS '직속상관', B.empTel AS '직속상관연락처'
FROM empTbl A
INNER JOIN empTbl B
ON A.manager = B.emp
WHERE A.emp = '우대리';

USE sqlDB;
SELECT stdName, addr FROM stdTBL
UNION ALL
SELECT clubName, roomNo FROM clubTBL;

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTBL
WHERE name NOT IN ( SELECT name FROM userTBL WHERE mobile1 IS NULL) ;

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTBL
WHERE name IN ( SELECT name FROM userTBL WHERE mobile1 IS NULL) ;

