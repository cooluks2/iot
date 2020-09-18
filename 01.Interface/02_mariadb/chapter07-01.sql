USE sqlDB;
SELECT AVG(amount) AS '평균 구매 개수' FROM buyTBL;

SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buyTBL;
SELECT CONVERT(AVG(amount) , SIGNED INTEGER) AS '평균 구매 개수' FROM buyTBL ;

SELECT CAST('2022$12$12' AS DATE);
SELECT CAST('2022/12/12' AS DATE);
SELECT CAST('2022%12%12' AS DATE);
SELECT CAST('2022@12@12' AS DATE);


SELECT
num,
CONCAT(CAST(price AS CHAR(10)), 'X', CAST(amount AS CHAR(4)) ,'=' )
AS '단가X수량',
price*amount AS '구매액'
FROM buyTBL ;

SELECT '100' + '200' ; -- 문자와 문자를 더함 (정수로 변환되서 연산됨)
SELECT CONCAT('100', '200'); -- 문자와 문자를 연결 (문자로 처리)
SELECT CONCAT(100, '200'); -- 정수와 문자를 연결 (정수가 문자로 변환되서 처리)
SELECT 1 > '2mega'; -- 정수 2로 변환되어서 비교
SELECT 3 > '2MEGA'; -- 정수 2로 변환되어서 비교
SELECT 0 = 'mega2'; -- 문자는 0으로 변환됨




SELECT IF (100>200, '참이다', '거짓이다');
SELECT IFNULL(NULL, '널이군요'), IFNULL(100, '널이군요');
SELECT NULLIF(100,100), NULLIF(200,100);

SELECT
CASE 10
WHEN 1 THEN '일'
WHEN 5 THEN '오'
WHEN 10 THEN '십'
ELSE '모름'
END;


SELECT ASCII('A'), CHAR(65);
SELECT BIT_LENGTH('abc'), CHAR_LENGTH('abc'), LENGTH('abc');
SELECT BIT_LENGTH('가나다'), CHAR_LENGTH('가나다'), LENGTH('가나다');

SELECT CONCAT_WS('/', '2022', '01', '01');


SELECT
ELT(2, '하나', '둘', '셋'),
FIELD('둘', '하나', '둘', '셋'),
FIND_IN_SET('둘', '하나,둘,셋'),
INSTR('하나둘셋', '둘'),
LOCATE('둘', '하나둘셋');

SELECT FORMAT(123456.123456, 4);
SELECT BIN(31), HEX(31), OCT(31);

SELECT INSERT('abcdefghi', 3, 4, '@@@@'), INSERT('abcdefghi', 3, 2, '@@@@');
SELECT LEFT('abcdefghi', 3), RIGHT('abcdefghi', 3);
SELECT LOWER('abcdEFGH'), UPPER('abcdEFGH');

SELECT LPAD('이것이', 5, '##'), RPAD('이것이', 5, '##');
SELECT LTRIM('   이것이'), RTRIM('이것이   ');
SELECT TRIM(' 이것이 '), TRIM(BOTH 'ㅋ' FROM 'ㅋㅋㅋ재밌어요.ㅋㅋㅋ');

SELECT REPEAT('이것이', 3);
SELECT REPLACE ('이것이 MariaDB다', '이것이' , 'This is');
SELECT REVERSE ('MariaDB');

SELECT CONCAT('이것이', SPACE(10), 'MariaDB다');
SELECT SUBSTRING('대한민국만세', 3, 2);
SELECT
	SUBSTRING_INDEX('cafe.naver.com', '.', 2),
	SUBSTRING_INDEX('cafe.naver.com', '.', -2);
	
	
SELECT
ADDDATE('2022-01-01', INTERVAL 31 DAY),
ADDDATE('2022-01-01', INTERVAL 1 MONTH);
SELECT
SUBDATE('2022-01-01', INTERVAL 31 DAY),
SUBDATE('2022-01-01', INTERVAL 1 MONTH);


SELECT
	ADDTIME('2022-01-01 23:59:59', '1:1:1'),
	ADDTIME('15:00:00', '2:10:10');
SELECT
	SUBTIME('2022-01-01 23:59:59', '1:1:1'),
	SUBTIME('15:00:00', '2:10:10');


SELECT YEAR(CURDATE()), MONTH(CURRENT_DATE()), DAYOFMONTH(CURRENT_DATE);
SELECT HOUR(CURTIME()), MINUTE(CURRENT_TIME()), SECOND(CURRENT_TIME),
MICROSECOND(CURRENT_TIME);

SELECT DATE(NOW()), TIME(NOW());

USE employees;
SELECT * FROM employees
WHERE MONTH(birth_date) = MONTH(NOW());

SELECT * FROM employees
WHERE MONTH(birth_date) = MONTH(NOW())
  AND DAY(birth_date) = DAY(NOW());
  
SELECT DATEDIFF('2022-01-01', NOW()), TIMEDIFF('23:23:59', '12:11:10');
SELECT DAYOFWEEK(CURDATE()), MONTHNAME(CURDATE()), DAYOFYEAR(CURDATE());

SELECT CURRENT_USER(), DATABASE();

USE sqlDB;
SELECT * FROM userTBL;
SELECT FOUND_ROWS();

USE sqlDB;
UPDATE buyTBL SET price=price*2;
SELECT ROW_COUNT();

USE sqlDB;
SELECT * INTO OUTFILE 'C:/temp/userTBL.txt' FROM usertbl;

CREATE TABLE memberTBL LIKE userTBL;
LOAD DATA LOCAL INFILE 'C:/temp/userTBL.txt' INTO TABLE memberTBL;
SELECT * FROM memberTBL;