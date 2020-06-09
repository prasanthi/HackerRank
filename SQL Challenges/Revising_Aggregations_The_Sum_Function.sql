/*
"SUM()" -> To find the total population of all the cities
Inorder to know the cities where district is california do "DISTRICT = "California" using "WHERE" clause
*/
SELECT SUM(POPULATION) FROM CITY WHERE (DISTRICT = "California");
