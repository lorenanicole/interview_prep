/* Step 3 - Solution #1 if wanted to insert into the table and overrde what exists 
   using a temporary table should you like! Presumably you've ran and 
   seeded data with the provided database.sql file.
*/

CREATE TEMPORARY TABLE temp_seat( 
    id INT, 
    student VARCHAR(255) 
); 

INSERT temp_seat(id, student)
    SELECT (
        CASE 
            WHEN seat.id % 2 != 0 AND count != seat.id THEN seat.id + 1 
            WHEN seat.id % 2 != 0 AND count = seat.id THEN seat.id
            ELSE seat.id - 1
        END 
    ) AS id,
    seat.student AS student
FROM seat,
(SELECT count(*) AS count FROM seat) AS seat_qty;

SELECT * FROM temp_seat;

UPDATE seat AS s_1
    JOIN temp_seat AS s_2
    ON s_1.student = s_2.student
    SET s_1.id = s_2.id;

SELECT * FROM seat;

/* Step 3 - Solution #2 for the SQL Query itself */

SELECT (
    CASE 
        -- swap even with odd seat number
        WHEN seat.id % 2 != 0 AND count != seat.id 
            THEN seat.id + 1 
        -- do not modify if the count of rows is odd
        WHEN seat.id % 2 != 0 AND count = seat.id 
            THEN seat.id
        -- swap odd with even seat number
        ELSE seat.id - 1
    END 
) AS id,
    seat.student AS student
FROM seat,
    (SELECT count(*) AS count FROM seat) AS seat_qty
ORDER BY id ASC;

/* Step 4 - Iterate on the solution! Measure length of time, 
 use the query planner, etc to improve performance! */