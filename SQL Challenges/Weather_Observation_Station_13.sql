/*
"ROUND()" -> Round the sum of lat values column (to 4 decimals) in the station table
"SUM()" -> To find Sum of all values in LAT_N
Inorder to get values where LAT_N greater than 38.700 use "LAT_N > 38.7800"
To get values less than 137.2345 use "LAT_N < 137.2345"
Inorder to combine both conditions use "AND" operator
*/
SELECT ROUND(SUM(LAT_N), 4) FROM STATION WHERE (LAT_N > 38.7800) AND (LAT_N < 137.2345);
