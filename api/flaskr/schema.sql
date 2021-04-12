#the following sql script creates a customer table (drops it if already exisists) and sets 
#up the schema for the table, which defines the structure of the table, what each column 
#represents and what type of data can be added to each column. Then the script inserts 
#7 sample records into the table.

DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstName TEXT UNIQUE NOT NULL,
  lastName TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  phone TEXT UNIQUE NOT NULL,
  address TEXT UNIQUE NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip TEXT NOT NULL
);

-- Creates new rows containing data in all named columns --
INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)
VALUES ("Ahmed", "Rashad", "test@test.com", "8345242340",'124 Mullberry lan',"Charlotte",'NC','28262');

INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)
VALUES ("Mugsy", "Bogues", "mugsy@test.com", "831523530",'1124 Hornets drive',"Raliegh",'NC','28235');

INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)
VALUES ("RJ", "Barret", "rj@test.com", "1110002222",'124 Lexington Av',"New York",'NY','11231');

INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)
VALUES ("Julius", "Randall", "julius@test.com", "1113332222",'122 36th st',"Brooklyn",'NY','11232');

INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)
VALUES ("Kevin", "Durant", "kd@test.com", "1114442222",'123 36th st',"Queens",'NY','11242');

INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)
VALUES ("Lebron", "James", "lbj@test.com", "1155552222",'1222 36th st',"Los Angeles","CA",'90202');

INSERT INTO customer (firstName, lastName, email, phone, address,city,state,zip)
VALUES ("Kawhi", "Leonard", "kl@test.com", "1156662222",'1222 324th st',"Santa Monica","CA",'90203');

