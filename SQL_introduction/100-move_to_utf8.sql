-- Converts the database hbtn_0c_0 to UTF8
-- Database conversion
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Select the database
USE hbtn_0c_0;

-- Converts the table first_table to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Converts the name field to UTF8
ALTER TABLE first_table
MODIFY name VARCHAR(256)
COLLATE utf8mb4_unicode_ci;
