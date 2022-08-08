-- MySQL setup development 
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the user on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
--Grant select privileges to the user on database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
