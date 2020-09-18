-- employees TABLE에는 부서명이 없다.
-- departments TABLE에 dept_no과 dept_name이 있다.
-- dept_emp TABLE에 dept_no와 부서에 있었던 기간 정보가 있다.
-- dept_emp TABLE에 dept_no와 departments TABLE의 dept_no가 연결된다.

-- employees를 출력하는데 부서명, 부서에 있었던 기간을 출력하라.

USE employees;

SELECT E.first_name, E.last_name, D.dept_name, DE.from_date, DE.to_date
FROM employees E
	INNER JOIN dept_emp DE
	ON E.emp_no = DE.emp_no
	INNER JOIN departments D
	ON DE.dept_no = D.dept_no
ORDER BY E.first_name, E.last_name; -- 이걸 해주어야 사람 목록이 보인다.

SELECT E.first_name, E.last_name, D.dept_name, DE.from_date, DE.to_date
FROM employees E
	INNER JOIN dept_emp DE
	ON E.emp_no = DE.emp_no
	INNER JOIN departments D
	ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01'
ORDER BY E.first_name, E.last_name;
