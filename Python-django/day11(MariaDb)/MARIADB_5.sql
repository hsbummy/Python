SELECT * FROM items;

DESC items;

SELECT * FROM users;
DESC users;

DROP TABLE cart
CREATE TABLE cart(
	id INT(10) AUTO_INCREMENT PRIMARY KEY,
	userid CHAR(4),
	itemid INT(10),
	regdate DATE,
	qt INT(10)
);

ALTER TABLE cart ADD CONSTRAINT user_fk FOREIGN KEY (userid) REFERENCES users(id);
ALTER TABLE cart ADD CONSTRAINT item_fk FOREIGN KEY (itemid) REFERENCES items(id);

INSERT INTO cart VALUES (id, 'id01','1000',CURRENT_DATE, 4);
SELECT * FROM cart;

SELECT c.id, c.regdate, u.id, u.name, i.name, i.price FROM cart c
INNER JOIN users u ON c.userid = u.id
INNER JOIN items i ON c.itemid = i.id;