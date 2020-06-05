/*
"ROUND()" -> Round the Minimum LAT_N values column (to 4 decimals) in the station table
"MIN()" -> To get the SMALLEST value of the Northern Latitudes (LAT_N)
Inorder to get the LAT_N values greater than 38.7780 use "LAT_N > 38.7780"
*/
SELECT ROUND(MIN(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7780;
