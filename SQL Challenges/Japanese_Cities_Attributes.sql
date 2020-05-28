/* Inorder to query all coloumns use '*' operator,
   To get attritubes of Japanese Cities use 'C.COUNTRYCODE= 'JPN'' i.e, tablename.attributename = 'attributevalue'*/
SELECT * FROM city AS c WHERE c.countrycode="JPN";
