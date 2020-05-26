/* 'C.NAME'(tablename.columnname) is used to select only the names.
    CITY is the table name, inorder to alias it use 'as'
    As we need columns with both population more than 120000 and with country code usa use 'and' operator.*/
Select C.NAME from CITY as C where C.POPULATION > 120000 and C.COUNTRYCODE="USA";
