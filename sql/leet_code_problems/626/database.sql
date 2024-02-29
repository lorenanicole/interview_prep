-- Step 1: Create database and schemas
CREATE DATABASE IF NOT EXISTS interview_prep;

USE interview_prep;

CREATE TABLE seat(
    id INT NOT NULL,
    student VARCHAR(255) NOT NULL
);

-- Step 2: Seed data for test case
INSERT INTO seat(id, student) 
VALUES
    (1, 'Abbot'),
    (2, 'Doris'),
    (3, 'Emerson'),
    (4, 'Green'),
    (5, 'Jeames');