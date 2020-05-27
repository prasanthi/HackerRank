/*
Inorder to find the difference between total number of city entries and distinct city enteries,
"COUNT(column_name)" function -> To find the number of rows of that specified column
"DISTINCT" keyword -> eliminates the repetitive appearance of the same data
"-" Arithmetic Operator -> To find out the difference between 2 city entries.
*/
SELECT ((COUNT(STATION.CITY)) - (COUNT(DISTINCT STATION.CITY))) FROM STATION;
