-- Display all values of the table

-- Set the table name as a parameter
SET @table_name = ?;

-- Dynamically construct and execute the SQL query
SET @query = CONCAT('SELECT * FROM ', @table_name);
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
