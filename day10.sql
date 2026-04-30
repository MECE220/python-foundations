-- CREATE a students table 
CREATE TABLE students (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(100) NOT NULL,
    age     INTEGER,
    city    VARCHAR(100),
    degree  CARCHAR(100)
);

-- CREATE a scores table
CREATE TABLE scores  (
    id          SERIAL PRIMARY KEY,
    student_id  INTEGER REFERENCES students(id),
    subject     VARCHAR(100)
    score       DECIMAL(5,2),
    grade       CHAR(1)
);

-- Insert students
INSERT INTO student (name, age, city, degree) VALUES
    (1, 'Python', 95.0, 'A'),
    (1, 'Mathematics', 88.0, 'B'),
    (1, 'Data Structures', 91.0, 'A'),
    (2, 'Python', 98.0, 'A'),
    (2, 'Mathematics', 85.0, 'B'),
    (2, 'Data Structures', 94.0, 'A'),
    (3, 'Pyhton', 94.0, 'B'),
    (3, 'Mathematics', 79.0, 'C'),
    (3, 'Data Structures', 87.0, 'B'),
    (4, 'Python', 75.0, 'C'),
    (4, 'Mathematics', 65, 'D'),
    (4, 'Data Structures', 70.0, 'C'),
    (5, 'Python', 93.0, 'A'),
    (5, 'Mathematics', 91.0, 'A'),
    (5, 'Data Structures', 89.0, 'A');

-- See all students
SELECT * FROM students;

-- See specific columns only
SELECT name, city FROM students;

-- Filter with WHERE — same as pandas filtering
SELECT * FROM students WHERE city = 'Manila';

-- Multiple conditions
SELECT * FROM students WHERE city = 'Manila' AND age < 25;

-- NOT equal
SELECT * FROM students WHERE city != 'Manila';

-- Sort results
SELECT * FROM students ORDER BY age ASC;   -- youngest first
SELECT * FROM students ORDER BY age DESC;  -- oldest first

-- Limit results
SELECT * FROM students LIMIT 3;

-- Search with LIKE — % means "anything"
SELECT * FROM students WHERE name LIKE 'R%';   -- names starting with R
SELECT * FROM students WHERE degree LIKE '%Engineering%';   

-- INNER JOIN — show students WITH their scores
SELECT
    students.name,
    students.city,
    scores.subject,
    scores.score,
    scores.grade
FROM students
INNER JOIN scores ON students.id = scores.student_id;

-- Same query but cleaner with aliases
SELECT
    s.name,
    s.city,
    sc.subject,
    sc.score,
    sc.grade
FROM students s
JOIN scores sc ON s.id = sc.student_id;

-- Filter after joining
SELECT
    s.name,
    sc.subject,
    sc.score
FROM students s
JOIN scores sc ON s.id = sc.student_id
WHERE sc.score >= 90
ORDER BY sc.score DESC;

-- Show only Manila students' Python scores
SELECT
    s.name,
    sc.score
FROM students s
JOIN scores sc ON s.id = sc.student_id
WHERE s.city = 'Manila'
AND sc.subject = 'Python'
ORDER BY sc.score DESC;

-- Average score per student
SELECT
    s.name,
    ROUND(AVG(sc.score), 2) AS average_score,
    COUNT(sc.id) AS total_subjects
FROM students s
JOIN scores sc ON s.id = sc.student_id
GROUP BY s.name
ORDER BY average_score DESC;

-- Average score per subject
SELECT
    subject,
    ROUND(AVG(score), 2) AS avg_score,
    MAX(score) AS highest,
    MIN(score) AS lowest,
    COUNT(*) AS total_students
FROM scores
GROUP BY subject
ORDER BY avg_score DESC;

-- Count students per city
SELECT
    city,
    COUNT(*) AS total_students
FROM students
GROUP BY city
ORDER BY total_students DESC;

-- Students with average above 85
SELECT
    s.name,
    ROUND(AVG(sc.score), 2) AS average_score
FROM students s
JOIN scores sc ON s.id = sc.student_id
GROUP BY s.name
HAVING AVG(sc.score) > 85
ORDER BY average_score DESC;

# day10_notes.py
# SQL Cheat Sheet — Day 10

sql_commands = {
    "SELECT":   "Read data from a table",
    "FROM":     "Which table to read from",
    "WHERE":    "Filter rows by condition",
    "JOIN":     "Combine two tables",
    "GROUP BY": "Group rows and aggregate",
    "ORDER BY": "Sort results",
    "HAVING":   "Filter after grouping",
    "INSERT":   "Add new rows",
    "CREATE":   "Make a new table",
    "LIMIT":    "Restrict number of rows returned"
}

print("=== SQL COMMAND REFERENCE ===")
for command, description in sql_commands.items():
    print(f"  {command:<12} → {description}")

# SQL vs pandas equivalents
print("\n=== SQL vs PANDAS ===")
equivalents = [
    ("SELECT * FROM table",          "df"),
    ("SELECT col FROM table",        "df['col']"),
    ("WHERE col = value",            "df[df['col'] == value]"),
    ("ORDER BY col DESC",            "df.sort_values('col', ascending=False)"),
    ("GROUP BY col",                 "df.groupby('col')"),
    ("COUNT(*)",                     "len(df)"),
    ("AVG(col)",                     "df['col'].mean()"),
    ("JOIN",                         "pd.merge(df1, df2)"),
]

for sql, pandas in equivalents:
    print(f"  SQL   : {sql}")
    print(f"  pandas: {pandas}")
    print()