SELECT * FROM items;

SELECT
	ROW_NUMBER() OVER (ORDER BY price DESC, name ASC) AS 'RK', name, price
FROM items
LIMIT 10

SELECT
	RANK() OVER (ORDER BY price DESC) AS 'RK', name, price
FROM items
LIMIT 10;

SELECT
	DENSE_RANK() OVER (ORDER BY price DESC) AS 'RK', name, price
FROM items
LIMIT 10;

SELECT cate, ROW_NUMBER() OVER (PARTITION BY cate ORDER BY price DESC), name, price
FROM items;

SELECT ROW_NUMBER() OVER(ORDER BY AVG(price)) AS 'RK', cate, AVG(price) AS 'avgp'
FROM items
GROUP BY cate
ORDER BY RK;