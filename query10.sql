-- query10.sql
SELECT sub.name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE s.name = 'Student Name' AND t.name = 'Teacher Name';