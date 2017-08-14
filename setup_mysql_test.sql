-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
CREATE DATABASE IF NOT EXISTS performance_schema;
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
