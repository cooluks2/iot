USE sqlDB;
SELECT * FROM userTBL;
SHOW INDEX FROM userTBL;
SHOW TABLE STATUS LIKE 'userTBL';
CREATE INDEX idx_userTBL_addr
ON userTBL (addr);
SHOW INDEX FROM userTBL ;

DROP INDEX idx_userTBL_name ON userTBL;
SHOW INDEX FROM userTBL ;

-- iot_user 계정 만들기
create user 'iot_user'@'%' identified by '1234';

-- 데이터 베이스 사용 권한 부여
grant all privileges on sqlDB.* to 'iot_user'@'%';

SELECT * FROM employees.employees;

grant all privileges on employees.* to 'iot_user'@'%';