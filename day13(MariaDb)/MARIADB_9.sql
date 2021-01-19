SELECT id,name, price, CAST(rate AS SIGNED INTEGER), regdate FROM items;

ALTER TABLE items ADD cate NVARCHAR(10);

SELECT * FROM items;
UPDATE items SET cate='c3' WHERE ID=10;
UPDATE items SET NAME='item11' WHERE ID=11;

SELECT cate , CONVERT(AVG(price),INTEGER) FROM items
GROUP BY cate

SELECT CONCAT(id, name), price, CAST(REGDATE AS DATE) FROM items;

SELECT DATE_FORMAT(REGDATE, "%Y%m%d") FROM items;

SELECT COUNT(IFNULL(price, 1)) FROM items;

SELECT * FROM items;

SELECT *,
	CASE
		WHEN price <= 10000 THEN 'low'
		WHEN price <= 20000 THEN 'middle'
		WHEN price > 20000 THEN 'high'
		END
FROM items;

SELECT cate, AVG(price),
	CASE
		WHEN AVG(price) <= 10000 THEN 'low'
		WHEN AVG(price) <= 20000 THEN 'middle'
		WHEN AVG(price) > 20000 THEN 'high'
		ELSE 'NONE'
		END
	CASE
		WHEN cate = 'c1' THEN '반바지'
		WHEN cate = 'c2' THEN '긴바지'
		WHEN cate = 'c3' THEN '통바지'
		END
FROM items	
GROUP BY cate;

SELECT name, price, FORMAT(price*rate,3),
DATE_FORMAT(regdate, '%Y%m%d')
FROM items;