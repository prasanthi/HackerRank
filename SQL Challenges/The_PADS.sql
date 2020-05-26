/*
 'Concat()' function is used to get both name and the occupation first character together.
 'Substr()' function is used to find the first letter of occupation of ever person.
 'Order by' is used to order them by Names_professions which we obtained by concatination.
*/
Select Concat(Name,'(',Substr(Occupation,1,1),')') as Names_professions from Occupations order by Names_professions;
/*
  Here 'Concat()'-> to obtain the specific format mentioned in the question. ie, There are total of 4 Actors.
  'Count()'-> Get the total no of Occurances of Occupation.
  'Lower()'-> Coverts complete string to lower case as the given format is in lower case.
  'Group by'-> groups the data by Occupation column.
*/
Select Concat('There are a total of ',Count(Occupation),' ',Lower(Occupation),'s.') from Occupations Group by Occupation Order by count(Occupation), Occupation;
