-- Exercise 1 (done for you): Selecting all columns
SELECT * FROM users;



-- Exercise 2 (done for you): Selecting some columns
SELECT id, first_name, last_name 
FROM users;



-- Exercise 3: Sorting
SELECT id, first_name, last_name 
FROM users
ORDER BY last_name;



-- Exercise 4: Filtering
SELECT id, image_url, user_id
FROM posts
WHERE user_id = 26;



-- Exercise 5: Filtering with logical operators
SELECT id, image_url, user_id
FROM posts
WHERE user_id = 26 OR user_id = 12;



-- Exercise 6: Using functions in a select statement
SELECT count(*)
FROM posts
ORDER BY count(*) DESC;



-- Exercise 7: Aggregating data
SELECT user_id, count(*)
FROM comments
GROUP BY user_id
ORDER BY count(*) DESC;



-- Exercise 8: Joining: two tables
SELECT posts.id, posts.image_url, user_id, username, first_name, last_name
FROM posts
INNER JOIN users ON users.id = posts.user_id
WHERE user_id = 26 OR user_id = 12;



-- Exercise 9: More joining practice: two tables
SELECT posts.id, pub_date, following_id
FROM following
INNER JOIN posts ON posts.user_id = following_id
WHERE following.user_id = 26;




-- Exercise 10: More joining practice: three tables (Optional)
SELECT posts.id, pub_date, following_id, username
FROM following
INNER JOIN posts ON posts.user_id = following_id
INNER JOIN users ON posts.user_id = users.id
WHERE following.user_id = 26
ORDER BY pub_date DESC;




-- Exercise 11: Inserting records
INSERT INTO bookmarks (user_id, post_id, timestamp)
VALUES (26, 219, NOW()), (26, 220, NOW()), (26, 221, NOW());


-- Exercise 12: Deleting records
DELETE FROM bookmarks
WHERE post_id IN (219, 220, 221);



-- Exercise 13: Updating records
UPDATE users
SET email = 'knick2022@gmail.com' 
WHERE id = 26;



-- Exercise 14: More Querying Practice (Optional)
SELECT posts.id, posts.user_id, count(*), caption
FROM comments
INNER JOIN posts ON posts.user_id = comments.user_id
WHERE posts.user_id = 26
GROUP BY posts.id;