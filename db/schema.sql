CREATE TABLE vendors(id serial primary key,name text not null unique);
CREATE TABLE products(id serial primary key,name text not null unique,stock integer not null default 0 check(stock>=0));
CREATE TABLE purchases(id serial primary key,vendor_id int references vendors not null,product_id int references products not null,qty int not null check(qty>0),cost_cents bigint not null check(cost_cents>0),status text not null default 'pending' check(status in ('pending','approved','paid')));
CREATE TABLE journals(id serial primary key,purchase_id int references purchases not null,account text not null,debit bigint not null default 0,credit bigint not null default 0,check(debit>=0 and credit>=0),check((debit=0)<>(credit=0)),unique(purchase_id,account));
INSERT INTO vendors(name) VALUES ('Demo supplier'); INSERT INTO products(name) VALUES ('Demo laptop');
