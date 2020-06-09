/*
"ROUND()" -> Round the Minimum LAT_N values column (to 4 decimals) in the station table
Inorder to get the LAT_N values greater than 38.7780 use "LAT_N > 38.7780"
As we need to order LAT_N values in ascending order do "ORDER BY LAT_N ASC"
We need only one value so use "LIMIT 1"
*/
SELECT ROUND(LONG_W, 4) FROM STATION WHERE (LAT_N > 38.7780) ORDER BY (LAT_N) ASC LIMIT 1 ;
