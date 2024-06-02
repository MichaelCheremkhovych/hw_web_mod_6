-- query8.sql
SELECT AVG(g.grade) AS avg_score
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.name = 'Certain Teacher';