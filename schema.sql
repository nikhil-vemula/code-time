-- ADT Project Phase 2
-- Contributors: Sohail, Nikhil


-- Instructions to import the database
-- In postgres shell run `\i schema.sql`

CREATE DATABASE coding_made_easy;
\c coding_made_easy;

-- User table
-- Contributed by: Nikhil 

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT,
  user_name TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);

-- Last logged in
-- Contributed by: Sohail 
CREATE TABLE last_logged_in (
  user_id INT,
  logged_time TIMESTAMP,
  CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- Question table
-- Contributed by: Nikhil

CREATE TYPE difficulty as ENUM ('easy', 'medium', 'hard');

CREATE TABLE questions (
  question_id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  short_desc TEXT,
  description TEXT,
  difficulty_level difficulty,
  tags TEXT,
  notes TEXT,
  user_id INT,
  CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Last revised
-- Contributed by: Sohail

CREATE TABLE last_revised (
  question_id INT,
  revised_time TIMESTAMP,
  solved BOOLEAN,
  CONSTRAINT fk_question_id FOREIGN KEY(question_id) REFERENCES questions(question_id)
);

-- Related resource
-- Contributed by: Sohail

CREATE TYPE resource_type AS ENUM ('article', 'video');

CREATE TABLE related_resource (
  question_id INT,
  url TEXT NOT NULL,
  type resource_type,
  CONSTRAINT fk_question_id FOREIGN KEY(question_id) REFERENCES questions(question_id)
);

-- Similar question
-- Contributed by: Nikhil

CREATE TABLE similar_question(
  question_id INT,
  similar_question_id INT,
  CONSTRAINT fk_question_id FOREIGN KEY(question_id) REFERENCES questions(question_id),
  CONSTRAINT fk_similar_question_id FOREIGN KEY(similar_question_id) REFERENCES questions(question_id)
);

-- Functions

CREATE OR REPLACE FUNCTION get_problems_count(userId INT)
RETURNS INT as $prob_count$
DECLARE
  prob_count INT;
BEGIN
  SELECT count(question_id) INTO prob_count FROM questions q WHERE user_id=userId;
  RETURN prob_count;
END;
$prob_count$ LANGUAGE plpgsql;

-- get_problems_solved
-- Contributed by: Nikhil 

CREATE OR REPLACE FUNCTION get_solved_problems_count(userId INT)
RETURNS INT as $prob_count$
DECLARE
  prob_count INT;
BEGIN
  SELECT count(*) INTO prob_count FROM questions q WHERE user_id=userId AND true=some(
    SELECT true from last_revised WHERE question_id = q.question_id and solved=TRUE
  );
  RETURN prob_count;
END;
$prob_count$ LANGUAGE plpgsql;

-- select * from get_problems_solved(1);

-- get_revise_questions
-- Contributed by: Sohail

CREATE OR REPLACE FUNCTION get_revise_questions(userId INT)
RETURNS TABLE (question_id INT, title TEXT, url TEXT, short_desc TEXT, 
description TEXT, difficulty_level TEXT, tags TEXT, notes TEXT, user_id INT, revised_time TIMESTAMP)
AS $$
  SELECT * from (
    SELECT q.*, max(revised_time) as revised_time FROM questions q NATURAL JOIN last_revised
    WHERE user_id=1 and solved=TRUE
    GROUP BY question_id ORDER BY revised_time
  ) as q 
  WHERE DATE_PART('day', NOW() - revised_time) > 7;
$$ LANGUAGE SQL;

-- select * from get_revise_questions(1);

-- Demo data
INSERT INTO users (first_name, last_name, user_name, password) VALUES
  ('Nikhil', 'Vemula', 'srvemu', '1234'),
  ('Sohail', 'Mohammed', 'sohamoha', '3456');


INSERT INTO last_logged_in (user_id, logged_time) VALUES
  (1, '03/04/2023 02:00:00'),
  (1, '04/04/2023 11:00:00'),
  (2, '02/04/2023 12:00:00'),
  (2, '04/04/2023 02:00:00');

INSERT INTO questions (title, url, short_desc, description, difficulty_level, tags, notes, user_id) VALUES 
  ('Sample question 1', 'https://www.google.com', '', '', 'easy', 'tag1,tag2,tag3', '', 1),
  ('Sample question 2', 'https://www.google.com', '', '', 'easy', 'tag1,tag2,tag3', '', 2),
  ('Sample question 3', 'https://www.google.com', '', '', 'easy', 'tag1,tag2,tag3', '', 1),
  ('Sample question 4', 'https://www.google.com', '', '', 'easy', 'tag1,tag2,tag3', '', 2),
  ('Sample question 5', 'https://www.google.com', '', '', 'easy', 'tag1,tag2,tag3', '', 1);

INSERT INTO last_revised (question_id, solved, revised_time) VALUES
  (1, TRUE, '04/03/2023 12:00:00'),
  (1, TRUE, '03/01/2023 12:00:00'),
  (3, TRUE, '03/25/2023 12:00:00'),
  (2, TRUE, '04/04/2023 12:00:00'),
  (4, TRUE, '03/24/2023 12:00:00'),
  (5, TRUE, '03/24/2023 12:00:00');

-- \c postgres
-- DROP DATABASE coding_made_easy;