/*
"ROUND()" -> Round the MAX of lat values column (to 4 decimals) in the station table
"MAX()" -> To get the greatest value of the Northern Latitudes (LAT_N)
Inorder to get LAT_N values less than 137.2345 do "LAT_N < 137.2345"
*/
SELECT ROUND(MAX(LAT_N), 4) FROM STATION WHERE (LAT_N < 137.2345);
