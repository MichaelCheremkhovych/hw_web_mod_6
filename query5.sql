-- query5.sql
SELECT sub.name
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
WHERE t.name = 'John Doe';