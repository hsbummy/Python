CREATE TABLE cart_no_main (
	cart_no INT(20),
	cart_mem_id VARCHAR(12),
	cart_p_no INT(20),
	cart_amount INT(20)
);
ALTER TABLE cart_no ADD CONSTRAINT my_pk
PRIMARY KEY (cart_no, cart_mem_id, cart_p_no);

CREATE TABLE product (
	p_no VARCHAR(6),
	pcategory_code INT(20),
	p_stock INT(20),
 	p_name VARCHAR(50),
 	p_cost INT(20),
 	p_date DATE,
 	p_status INT(20),
 	p_salesCount INT(20)
);

ALTER TABLE product ADD CONSTRAINT pt_pk
PRIMARY KEY (p_no, pcategory_code)

CREATE TABLE member (
	mem_id VARCHAR(12),
	mem_name VARCHAR(500),
	mem_zip VARCHAR(10),
	mem_phone VARCHAR(20),
	mem_email VARCHAR(80)
);

ALTER TABLE member ADD CONSTRAINT mb_pk
PRIMARY KEY (mem_id)

CREATE TABLE order_main (
	order_no VARCHAR(13),
	order_mem_id VARCHAR(12),
	order_recv_name VARCHAR(10),
	order_recv_phone VARCHAR(20),
	order_date DATE
);

ALTER TABLE order_main ADD CONSTRAINT om_pk
PRIMARY KEY (order_no)

CREATE TABLE order_detail (
	order_detail_no INT(20),
	order_no VARCHAR(18),
	orderDetail_p_no INT(20),
	order_p_amount INT(20)
);

ALTER TABLE order_detail ADD CONSTRAINT od_pk
PRIMARY KEY (order_detail_no, order_no, orderDetail_p_no)
