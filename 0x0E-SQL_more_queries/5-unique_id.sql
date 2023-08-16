-- This script is creating 0x0E. SQL - More queries, task 5. Unique ID
-- Table = `unique_id` with `id and `name` fields. DB in args.
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
); 
