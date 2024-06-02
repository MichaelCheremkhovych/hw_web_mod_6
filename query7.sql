-- query7.sql
SELECT s.name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups grp ON s.group_id = grp.id
WHERE grp.name = 'Separate Group' AND sub.name = 'Specific Subject';