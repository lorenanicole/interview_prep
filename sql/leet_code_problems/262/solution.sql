-- Step 1: Create database and schemas
CREATE DATABASE IF NOT EXISTS interview_prep;

USE interview_prep;

DROP TABLE users IF EXISTS;
-- TRUNCATE TABLE users;
CREATE TABLE users (
    users_id int NOT NULL UNIQUE,
    banned ENUM('yes', 'no') NOT NULL,
    `role` ENUM('client', 'driver', 'partner') NOT NULL,
    PRIMARY KEY (users_id)
);

DROP TABLE trips IF EXISTS;
-- TRUNCATE TABLE trips;
CREATE TABLE trips (
    id int NOT NULL AUTO_INCREMENT,
    client_id int NOT NULL,
    driver_id int NOT NULL,
    city_id int NOT NULL,
    `status` ENUM('completed', 'cancelled_by_driver', 'cancelled_by_client') NOT NULL,
    request_at date NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (client_id) REFERENCES users(users_id),
    FOREIGN KEY (driver_id) REFERENCES users(users_id)
);

-- Step 2: Seed data as relevant to the test case

-- Test Case: Happy Path
-- INSERT INTO users(users_id, banned, `role`) 
-- VALUES
--     (1, 'no', 'client'),
--     (2, 'yes', 'client'),
--     (3, 'no', 'client'),
--     (4, 'no', 'client'),
--     (10, 'no', 'driver'),
--     (11, 'no', 'driver'),
--     (12, 'no', 'driver'),
--     (13, 'no', 'driver');

-- INSERT INTO trips(client_id, driver_id, city_id, `status`, request_at)
-- VALUES
--     (1, 10, 1, 'completed', '2013-10-01'), 
--     (2, 11, 1, 'cancelled_by_driver', '2013-10-01'), 
--     (3, 12, 6, 'completed', '2013-10-01'), 
--     (4, 13, 6, 'cancelled_by_client', '2013-10-01'), 
--     (1, 10, 1, 'completed', '2013-10-02'), 
--     (2, 11, 6, 'completed', '2013-10-02'), 
--     (3, 12, 6, 'completed', '2013-10-02'), 
--     (2, 12, 12, 'completed', '2013-10-03'), 
--     (3, 10, 12, 'completed', '2013-10-03'), 
--     (4, 13, 12, 'cancelled_by_driver', '2013-10-03'); 

/*
Goal: Caclculate the cancellation rate as # cancelled trips unbanned users / total requests unbanned users

Logic below:
- Select from table of trips since need to filter out users that do not meed out requirements above
- Left join does this as table 1 will only select those that match the filter (left join = 'filter' of outer select)
*/

DROP PROCEDURE IF EXISTS daily_cancellation_rate;
delimiter //
CREATE PROCEDURE daily_cancellation_rate()
    BEGIN
        SELECT trips.request_at AS `Day`, ROUND(SUM(trips.`status` IN ('cancelled_by_driver', 'cancelled_by_client'))/COUNT(*), 2) AS 'Cancellation Rate' 
        FROM trips 
            LEFT JOIN users ON users.users_id = trips.client_id
            WHERE users.banned = 'no' 
            AND users.`role` = 'client'
        WHERE trips.request_at BETWEEN "2013-10-01" AND "2013-10-03"
        ORDER BY trips.request_at;
    END//
delimiter ;

-- Step 3: Iterate on query to accommodate all test cases

-- Test Case: Returns an empty set
 
-- INSERT INTO users(users_id, banned, `role`) 
-- VALUES
--     (1, 'no', 'client'),
--     (10, 'no', 'driver');

-- INSERT INTO trips(client_id, driver_id, city_id, `status`, request_at)
-- VALUES
--     (1, 10, 1, 'cancelled_by_client', '2013-10-04');


/*
Logic below: This deviates from previous test case as it:
- Removes the PROCEDURE usage
- Uses a CASE statement for the "Cancellation Rate" calcuation!
- Stikees the LEGT JOIN for filtering and does the filtering directly within the WHERE clauses for client and 
  driver user IDs (thereby increasing readability!)

*/

SELECT trips.request_at AS `Day`, ROUND(SUM(CASE WHEN trips.`status` LIKE '%cancelled%' THEN 1 ELSE 0 END)/COUNT(*), 2) AS 'Cancellation Rate' 
FROM trips 
    WHERE trips.client_id IN (SELECT users.users_id FROM users WHERE users.banned = 'no')
    AND trips.driver_id IN (SELECT users.users_id FROM users WHERE users.banned = 'no')
    AND trips.request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY trips.request_at;

/*
Step 4: Iterate on query for optimal performance

Areas for improvement:
- Can we iterate on the schema (e.g. add PRIMARY KEY CONSTRAINT to better index the data?)
- Re-evaluate the query structure to reduce number of rows scanned (e.g. use the DESCRIBE keyword to reduce number rows scanned)

  The following is the output from the DESCRIBE:

+----+-------------+-------+------------+--------+---------------------+---------+---------+--------------------------------+------+----------+------------------------------+
| id | select_type | table | partitions | type   | possible_keys       | key     | key_len | ref                            | rows | filtered | Extra                        |
+----+-------------+-------+------------+--------+---------------------+---------+---------+--------------------------------+------+----------+------------------------------+
|  1 | SIMPLE      | trips | NULL       | ALL    | client_id,driver_id | NULL    | NULL    | NULL                           |   10 |    11.11 | Using where; Using temporary |
|  1 | SIMPLE      | users | NULL       | eq_ref | PRIMARY,users_id    | PRIMARY | 4       | interview_prep.trips.client_id |    1 |    50.00 | Using where                  |
|  1 | SIMPLE      | users | NULL       | eq_ref | PRIMARY,users_id    | PRIMARY | 4       | interview_prep.trips.driver_id |    1 |    50.00 | Using where                  |
+----+-------------+-------+------------+--------+---------------------+---------+---------+--------------------------------+------+----------+------------------------------+

- Are there any wins with using SQL features like a temporary table in memory?

*/