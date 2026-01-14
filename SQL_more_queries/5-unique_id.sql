-- Creates the table unique_id with a unique id field
-- The table is created only if it does not already exist

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
