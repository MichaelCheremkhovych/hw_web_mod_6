-- query2.sql
SELECT s.name, AVG(g.grade) AS gpa
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Math'
GROUP BY s.name
ORDER BY gpa DESC
LIMIT 1;