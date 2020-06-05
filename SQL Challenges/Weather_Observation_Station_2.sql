/*
"ROUND()" -> Round the sum of lat,long values column (to 12 decimals) in the station table
"SUM()" -> To find Sum of all values in LAT_N, LONG_W
*/
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;
