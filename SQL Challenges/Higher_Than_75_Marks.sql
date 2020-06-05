/*
Inorder to get student names with marks higher(greater) than 75 use "student.marks > 75"
As we need to order output by the last three characters of each name use "ORDER BY RIGHT (name, 3)"
Inorder to secondary sort them by ascending ID do "id ASC"
*/
SELECT name FROM students WHERE students.marks > 75 ORDER BY RIGHT(name, 3), id ASC;
