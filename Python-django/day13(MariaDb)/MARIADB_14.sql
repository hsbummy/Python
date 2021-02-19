SELECT * FROM users;

SELECT
JSON_OBJECT('id',id,'name',name) AS 'jsondata'
FROM users;