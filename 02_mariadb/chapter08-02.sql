USE tableDB;
CREATE VIEW v_userTBL
AS
SELECT userid, name, addr FROM userTBL;
SELECT * FROM v_userTBL; -- 뷰를 테이블이라고 생각해도 무방

SELECT U.userid, U.name, B.prodName, U.addr,
CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM userTBL U
INNER JOIN buyTBL B
ON U.userid = B.userid ;

CREATE VIEW v_userbuyTBL
AS
SELECT U.userid, U.name, B.prodName, U.addr,
	CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM userTBL U
	INNER JOIN buyTBL B
	ON U.userid = B.userid ;

SELECT * FROM v_userbuyTBL WHERE name = N'김범수';

ALTER VIEW v_userbuyTBL
AS
	SELECT U.userid AS '사용자 아이디', U.name AS '이름',
		B.prodName AS '제품 이름', U.addr,
		CONCAT(U.mobile1, U.mobile2) AS '전화 번호'
	FROM userTBL U
		INNER JOIN buyTBL B
			ON U.userid = B.userid ;
SELECT `이름`,`전화 번호` FROM v_userbuyTBL;

DROP VIEW v_userbuyTBL;
