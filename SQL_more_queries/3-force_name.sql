-- Creates the table force_name with a mandatory name field
-- The table is created only if it does not already exist

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
