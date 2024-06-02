-- query1.sql
SELECT s.name, AVG(g.grade) AS gpa
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.name
ORDER BY gpa DESC
LIMIT 5;