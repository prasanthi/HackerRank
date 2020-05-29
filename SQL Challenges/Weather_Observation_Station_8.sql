/*
"LIKE" Operator -> Search for City names ending with a,e,i,o,u letters.
To represent the search pattern -> "%letter"-> searches words ending with that letter.
                                   "letter%"->searches words starting with the specified letter
As we need words both with their first and last characters as either of a,e,i,o,u we use the below specified pattern using AND operator.
"DISTINCT" keyword -> eliminates the repetitive appearance of the same data
i.e, Eliminates duplicate City names.
*/
SELECT DISTINCT station.city FROM station WHERE (station.city LIKE 'a%' OR
                                                 station.city LIKE 'e%' OR
                                                 station.city LIKE 'i%' OR
                                                 station.city LIKE 'o%' OR
                                                 station.city LIKE 'u%')
                                                 AND
                                                 (station.city LIKE '%a' OR
                                                 station.city LIKE '%e' OR
                                                 station.city LIKE '%i' OR
                                                 station.city LIKE '%o' OR
                                                 station.city LIKE '%u');
