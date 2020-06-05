/*
"ROUND()" -> Round the LONG_W values column (to 4 decimals) in the station table
Inorder to get LAT_N values less than 137.2345 use "LAT_N < 137.2345"
As we need to order LAT_N values in descending order do "ORDER BY LAT_N DESC"
We need only one value so use "LIMIT 1"
*/
SELECT ROUND(LONG_W, 4) FROM STATION WHERE (LAT_N < 137.2345) ORDER BY LAT_N DESC LIMIT 1;
