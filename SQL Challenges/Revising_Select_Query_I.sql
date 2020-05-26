/* '*' is used to select all the columns.
    CITY is the table name, inorder to alias it use 'as'
    As we need columns with both population more than 100000 and with country code usa use 'and' operator.*/
Select * from CITY as C where C.POPULATION > 100000 and C.COUNTRYCODE="USA";
