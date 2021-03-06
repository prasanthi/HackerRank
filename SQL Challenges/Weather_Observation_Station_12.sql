/*
"DISTINCT" keyword -> removes all duplicate values in the result.
"NOT" operator -> displays records if the condition is NOT TRUE.
In this case, we need list of CITY names from STATION table that do not start with vowels "and" do not end with vowels
i.e, NOT ((tablename.columnname LIKE "letter%") OR (tablename.columnname LIKE "%letter")).
LIKE "letter%" -> returns values that start with that letter.
LIKE "%letter" -> returns values that end with that letter.
To satisfy both the conditions "OR" operator is used.
*/
SELECT DISTINCT station.city FROM station WHERE NOT ((station.city LIKE "a%" OR
                                                     station.city LIKE "e%" OR
                                                     station.city LIKE "i%" OR
                                                     station.city LIKE "o%" OR
                                                     station.city LIKE "u%")
                                                     OR
                                                     (station.city LIKE "%a" OR
                                                     station.city LIKE "%e" OR
                                                     station.city LIKE "%i" OR
                                                     station.city LIKE "%o" OR
                                                     station.city LIKE "%u"));
