DROP TABLE carts;

CREATE TABLE carts(
	userid VARCHAR(10),
	itemid INT(10),
	qt INT(10)
);
ALTER TABLE carts
ADD CONSTRAINT fk_user
FOREIGN KEY (userid)
REFERENCES users(id);

ALTER TABLE carts
ADD CONSTRAINT fk_item
FOREIGN KEY (itemid)
REFERENCES items(id);

ALTER TABLE carts
ADD CONSTRAINT pk_carts
PRIMARY KEY (userid,itemid);

INSERT INTO carts VALUES ('id01',1,10);
INSERT INTO carts VALUES ('id01',2,20);
INSERT INTO carts VALUES ('id01',3,30);
INSERT INTO carts VALUES ('id01',4,40);
INSERT INTO carts VALUES ('id02',1,10);
INSERT INTO carts VALUES ('id02',2,20);
INSERT INTO carts VALUES ('id02',3,30);
INSERT INTO carts VALUES ('id02',4,40);

SELECT userid,
	SUM(IF(itemid=1, qt, 0)) AS 'item1',
	SUM(IF(itemid=2, qt, 0)) AS 'item2',
	SUM(IF(itemid=3, qt, 0)) AS 'item3',
	SUM(IF(itemid=4, qt, 0)) AS 'item4'
FROM carts
GROUP BY userid;