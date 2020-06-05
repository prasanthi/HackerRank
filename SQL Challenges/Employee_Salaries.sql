/*
Inorder to get employee names having a salary greater than $2000 per month do "SALARY > 2000"
and employees for less than 10 months do "MONTHS < 10"
Inorder to combine both conditions use "AND" operator
Sort your result by ascending employee_id by using "ORDER BY EMPLOYEE_ID ASC"
"ASC" used for Ascending order.
*/
SELECT NAME FROM EMPLOYEE WHERE (SALARY > 2000) AND (MONTHS < 10) ORDER BY EMPLOYEE_ID ASC;
