/*
Shortest City Name :
"LENGTH()" function -> Gives the total number of characters in each column
"ORDER BY CITY_LENGTH DESC" -> Used to oder all the city lengths in descending order.
"LIMIT 1" -> As we need only first shortest City name along with its length
Longest City Name:
Query for finding out the Longest City Name is also similar but we order City Lengths in "ASC" Ascending order to get longest city name.
*/
SELECT city c, LENGTH(city) AS city_length FROM station ORDER BY city_length DESC, c ASC LIMIT 1;

SELECT city c, LENGTH(city) AS city_length FROM station ORDER BY city_length ASC, c ASC LIMIT 1;
