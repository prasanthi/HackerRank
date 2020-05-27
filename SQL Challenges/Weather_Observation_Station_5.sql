/*
Shortest City Name :
"LENGTH()" function -> Gives the total number of characters in each column
"ORDER BY CITY_LENGTH DESC" -> Used to oder all the city lengths in descending order.
"LIMIT 1" -> As we need only first shortest City name along with its length
Longest City Name:
Query for finding out the Longest City Name is also Similar but we order City Lengths in "ASC" Ascending order. 
*/
SELECT CITY C, LENGTH(CITY) AS CITY_LENGTH FROM STATION ORDER BY CITY_LENGTH DESC, C ASC LIMIT 1;

SELECT CITY C, LENGTH(CITY) AS CITY_LENGTH FROM STATION ORDER BY CITY_LENGTH ASC, C ASC LIMIT 1;
