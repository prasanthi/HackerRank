/* '*' is used to select all the columns.
    CITY is the table name, inorder to alias it use 'as'
    As we need columns with both population more than 100000 and with country code usa use 'and' operator.*/
SELECT * FROM city AS c WHERE c.population > 100000 AND c.countrycode="USA";
