/*
Use "DISTINCT" keyword to exclude duplicates from the result
Inorder to only list of city names with even number of ids do "ID%2=0",
as "%" returns remainder.
*/
SELECT DISTINCT STATION.CITY FROM STATION WHERE (ID%2=0)
