/*
 'Concat()' function is used to get both name and the occupation first character together.
 'Substr()' function is used to find the first letter of occupation of ever person.
 'Order by' is used to order them by Names_professions which we obtained by concatination.
*/
SELECT CONCAT(name,'(',SUBSTR(occupation,1,1),')') AS names_professions
FROM occupations ORDER BY names_professions;
/*
  Here 'Concat()'-> to obtain the specific format mentioned in the question. ie, There are total of 4 Actors.
  'Count()'-> Get the total no of Occurances of Occupation.
  'Lower()'-> Coverts complete string to lower case as the given format is in lower case.
  'Group by'-> groups the data by Occupation column.
*/
SELECT CONCAT('There are a total of ',COUNT(occupation),' ',LOWER(occupation),'s.')
FROM occupations GROUP BY occupation ORDER BY COUNT(occupation), occupation;
