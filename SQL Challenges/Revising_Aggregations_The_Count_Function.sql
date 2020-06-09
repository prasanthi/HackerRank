/*
"COUNT()" -> To find the count of the number of cities
As we need cities with population more than 100000 use "POPULATION > 100000"
*/
SELECT COUNT(NAME) FROM CITY WHERE (POPULATION > 100000);
