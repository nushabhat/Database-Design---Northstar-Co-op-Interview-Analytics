-- drop database northstar;
CREATE DATABASE IF NOT EXISTS northstar;

Use northstar;

-- Table: Advisor
CREATE TABLE IF NOT EXISTS Advisor (
   ID INT PRIMARY KEY AUTO_INCREMENT,
   Name VARCHAR(100),
   UserName VARCHAR(50),
   Email VARCHAR(100)
);


-- Table: Administrator
CREATE TABLE IF NOT EXISTS Administrator (
   ID INT PRIMARY KEY AUTO_INCREMENT,
   Name VARCHAR(100),
   EmailAddress VARCHAR(100),
   UserName VARCHAR(50)
);


-- Table: Student
CREATE TABLE IF NOT EXISTS Student (
   ID INT PRIMARY KEY AUTO_INCREMENT,
   GraduationYear INT,
   Major VARCHAR(50),
   Minor VARCHAR(50),
   EmailAddress VARCHAR(100),
   UserName VARCHAR(50),
   Name VARCHAR(50),
   NumPreviousCoops INT,
   GPA DECIMAL(4, 2),
   AdvisorID INT,
   FOREIGN KEY (AdvisorID) REFERENCES Advisor(ID) ON DELETE SET NULL ON UPDATE CASCADE
);


-- Table: Extracurricular
CREATE TABLE IF NOT EXISTS Extracurricular (
   ActivityID INT PRIMARY KEY AUTO_INCREMENT,
   Name VARCHAR(100),
   Type VARCHAR(50),
   LeadershipYN CHAR(1) CHECK (LeadershipYN IN ('Y', 'N')),
   StudentID INT, -- Ensure this references the Student table
   FOREIGN KEY (StudentID) REFERENCES Student(ID) ON DELETE CASCADE ON UPDATE CASCADE
);



-- Table: Co_op
CREATE TABLE IF NOT EXISTS Co_op (
   CoOpID INT PRIMARY KEY AUTO_INCREMENT,
   RoleName VARCHAR(100),
   InterviewRounds INT,
   DifficultyRating DECIMAL(2, 1),
   AdminID INT,
   Industry VARCHAR(100),
   FOREIGN KEY (AdminID) REFERENCES Administrator(ID) ON DELETE SET NULL ON UPDATE CASCADE
);


-- Table: Student_Notes
CREATE TABLE IF NOT EXISTS Student_Notes (
   NoteID INT PRIMARY KEY AUTO_INCREMENT,
   StudentID INT,
   Summary TEXT,
   DatePublished DATE,
   CoOpID INT,
   AdminID INT,
   FOREIGN KEY (StudentID) REFERENCES Student(ID) ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY (CoOpID) REFERENCES Co_op(CoOpID) ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY (AdminID) REFERENCES Administrator(ID) ON DELETE SET NULL ON UPDATE CASCADE
);


-- Table: Co_op_Student
CREATE TABLE IF NOT EXISTS Co_op_Student
(
   StudentID INT,
   CoOpID    INT,
   PRIMARY KEY (StudentID, CoOpID),
   FOREIGN KEY (StudentID) REFERENCES Student (ID) ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY (CoOpID) REFERENCES Co_op (CoOpID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Table: Co_op_Adv
CREATE TABLE IF NOT EXISTS Co_op_Adv (
   AdvID INT,
   CoOpID INT,
   PRIMARY KEY (AdvID, CoOpID),
   FOREIGN KEY (AdvID) REFERENCES Advisor(ID) ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY (CoOpID) REFERENCES Co_op(CoOpID) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Table: Company
CREATE TABLE IF NOT EXISTS Company (
   CompanyID INT PRIMARY KEY AUTO_INCREMENT,
   CompanyName VARCHAR(100),
   CompanyAddress TEXT,
   Sector VARCHAR(50)
);


-- Table: Company_Co_op
CREATE TABLE IF NOT EXISTS Company_Co_op (
   CompanyID INT,
   CoOpID INT,
   PRIMARY KEY (CompanyID, CoOpID),
   FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID) ON DELETE CASCADE ON UPDATE  CASCADE,
   FOREIGN KEY (CoOpID) REFERENCES Co_op(CoOpID) ON DELETE CASCADE ON UPDATE CASCADE
);



-- Insert data into Advisor
INSERT INTO Advisor (Name, UserName, Email)
VALUES
('Holly Daize', 'holly', 'holly.daize@example.com'),
('Dr. Bob Smith', 'bsmith', 'bob.smith@example.com'),
('Dr. Carol Johnson', 'cjohnson', 'carol.johnson@example.com');

-- Insert data into Administrator
INSERT INTO Administrator (Name, EmailAddress, UserName)
VALUES
('Sarah Johnson', 'sarah.johnson@example.com', 'sarahjohnson'),
('John Roe', 'john.roe@example.com', 'jroe'),
('Mary Major', 'mary.major@example.com', 'mmajor');

-- Insert data into Student
INSERT INTO Student (ID, GraduationYear, Major, Minor, EmailAddress, UserName, Name, NumPreviousCoops, GPA, AdvisorID)
VALUES
(1001, 2025, 'Computer Science', 'Mathematics', 'emma.chen@example.com', 'emma', 'Emma Chen', 2, 3.8, 1),
(1002, 2024, 'Data Science', 'Statistics', 'raaya.monrovia@example.com', 'raaya', 'Raaya Monrovia', 1, 3.5, 2),
(1003, 2026, 'Mechanical Engineering', 'Physics', 'sarah.smith@example.com', 'sarah', 'Sarah Smith', 0, 3.9, 3);

-- Insert data into Extracurricular
INSERT INTO Extracurricular (Name, Type, LeadershipYN, StudentID)
VALUES
('Robotics Club', 'Technical', 'Y', 1001),
('Basketball Team', 'Sports', 'N', 1002),
('Debate Club', 'Social', 'Y', 1003);

-- Insert data into Co_op
INSERT INTO Co_op (RoleName, InterviewRounds, DifficultyRating, AdminID, Industry)
VALUES
('Software Developer Intern', 3, 4.2, 1, 'Technology'),
('Data Analyst Intern', 2, 3.5, 2, 'Finance'),
('Mechanical Design Intern', 1, 3.8, 3, 'Engineering'),
('Software Engineering Intern', 2, 3.5, 2, 'Finance');
   
-- Insert data into Student_Notes
INSERT INTO Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID)
VALUES
(1001, 'Emma had a great experience with the software development role.', '2024-11-19', 1, 1),
(1002, 'Raaya found the data analyst position to be moderately challenging.', '2024-11-19', 2, 2),
(1003, 'Sarah enjoyed the hands-on work in mechanical design.', '2024-11-19', 3, 3);

-- Insert data into Co_op_Student
INSERT INTO Co_op_Student (StudentID, CoOpID)
VALUES
(1001, 1),
(1002, 2),
(1003, 3);

-- Insert data into Co_op_Adv
INSERT INTO Co_op_Adv (AdvID, CoOpID)
VALUES
(1, 1),
(2, 2),
(3, 3);

-- Insert data into Company
INSERT INTO Company (CompanyName, CompanyAddress, Sector)
VALUES
('TechCorp', '123 Tech Street, Silicon Valley, CA', 'Technology'),
('FinancePlus', '456 Wall Street, New York, NY', 'Finance'),
('MechWorks', '789 Industrial Road, Detroit, MI', 'Engineering'),
('FinanceMinus', '456 Wall Street, New York, NY', 'Finance');

-- Insert data into Company_Co_op
INSERT INTO Company_Co_op (CompanyID, CoOpID)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);


-- Drop all users created in the original code
DROP USER IF EXISTS 'emma_user'@'localhost';
DROP USER IF EXISTS 'holly_user'@'localhost';
DROP USER IF EXISTS 'raaya_user'@'localhost';
DROP USER IF EXISTS 'sarah_user'@'localhost';

-- Create user for Emma
CREATE USER 'emma_user'@'localhost' IDENTIFIED BY 'emma_password';
GRANT SELECT ON northstar.* TO 'emma_user'@'localhost';


-- Create user for Holly
CREATE USER 'holly_user'@'localhost' IDENTIFIED BY 'holly_password';
GRANT SELECT, INSERT ON northstar.* TO 'holly_user'@'localhost';


-- Create user for Raaya
CREATE USER 'raaya_user'@'localhost' IDENTIFIED BY 'raaya_password';
GRANT SELECT, INSERT, UPDATE ON northstar.* TO 'raaya_user'@'localhost';


-- Create user for Sarah
CREATE USER 'sarah_user'@'localhost' IDENTIFIED BY 'sarah_password';
GRANT SELECT, INSERT, UPDATE ON northstar.* TO 'sarah_user'@'localhost';


FLUSH PRIVILEGES;

-- Persona #1: Emma Chen
-- 1.1
SELECT AVG(s.GPA) AS avg_GPA
FROM Student s
JOIN Co_op_Student cs ON s.ID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID;

-- 1.2
SELECT c.RoleName, c.InterviewRounds, com.CompanyName
FROM Co_op c
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID;

-- 1.3

SELECT s.NoteID, s.Summary, s.DatePublished, com.CompanyName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE com.Sector = 'Bio-Tech';

-- 1.4
SELECT DISTINCT s.UserName, s.EmailAddress
FROM Student s
JOIN Co_op_Student cs ON s.ID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE com.Sector = 'Bio-Tech';

-- 1.5
SELECT s.Summary, s.DatePublished, com.CompanyName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE com.Sector = 'Bio-Tech';

-- 1.6
SELECT s.NoteID, s.Summary, s.DatePublished, com.CompanyName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE com.Sector = 'Bio-Tech';

-- Persona #2: Holly Daize
-- 2.1
SELECT AVG(s.GPA) AS avg_GPA
FROM Student s
JOIN Co_op_Student cs ON s.ID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID;

-- 2.2
SELECT c.RoleName, AVG(c.DifficultyRating) AS avg_difficulty, AVG(c.InterviewRounds) AS avg_interview_rounds
FROM Co_op c
GROUP BY c.RoleName;



-- 2.3
SELECT DISTINCT s.UserName, s.EmailAddress
FROM Student s
JOIN Co_op_Student cs ON s.ID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
WHERE c.RoleName IN (SELECT RoleName FROM Co_op_Student WHERE StudentID = '[Current_StudentID]');

-- 2.4
SELECT s.Summary, s.DatePublished, c.RoleName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
WHERE s.Summary LIKE '%challenge%' OR s.Summary LIKE '%success%';

-- 2.5
SELECT s.Summary, s.DatePublished, com.CompanyName, c.RoleName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE c.Industry = 'Bio-Tech';  -- Adjust the industry based on the advisor's focus

-- 2.6
SELECT DISTINCT s.UserName, s.EmailAddress, com.CompanyName
FROM Student s
JOIN Co_op_Student cs ON s.ID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE com.CompanyName = '[Company_Name]';  -- Replace with specific company name

-- Persona #3: Raaya Morova
-- 3.1
INSERT INTO Student_Notes (StudentID, Summary, DatePublished, CoOpID)
VALUES (1001, 'Interview experience summary', '2024-11-19', 1);

-- 3.2
INSERT INTO Student_Notes (StudentID, Summary, DatePublished, CoOpID)
VALUES (1001, 'Advice on interview type and required skills', '2024-11-19', 1);

-- 3.3
INSERT INTO Student_Notes (StudentID, Summary, DatePublished, CoOpID)
VALUES (1001, 'Positive advocacy for the interview process', '2024-11-19', 1);

-- 3.4
INSERT INTO Student_Notes (StudentID, Summary, DatePublished, CoOpID)
VALUES (1001, 'Honest feedback on interview process', '2024-11-19', 1);


-- 3.5
UPDATE Student_Notes
SET Summary = 'Updated interview experience summary', DatePublished = '2024-11-19'
WHERE NoteID = 1;

-- 3.6
SELECT s.Summary, s.DatePublished, c.RoleName, com.CompanyName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE com.CompanyName = '[CompanyName]' AND c.RoleName = '[RoleName]';  -- Replace with specific company and role

-- Persona #4: Sarah Johnson
-- 4.1
SELECT s.Summary, s.DatePublished, com.CompanyName, c.RoleName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE com.CompanyName = 'TechCorp' AND c.RoleName = 'Software Engineer';  -- Replace with specific company and role

-- 4.2
SELECT s.Summary, s.DatePublished, c.RoleName, com.CompanyName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE c.RoleName = 'Intern' AND com.CompanyName = 'TechCorp' AND s.Summary LIKE '%coding challenge%';  -- Replace with specific criteria

-- 4.3
SELECT DISTINCT s.UserName, s.EmailAddress, c.RoleName, com.CompanyName
FROM Student s
JOIN Co_op_Student cs ON s.ID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE c.RoleName = 'Data Scientist' AND com.CompanyName = 'DataCo';  -- Replace with specific role and company

-- 4.4
SELECT DISTINCT s.Summary, c.RoleName, com.CompanyName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE s.Summary LIKE '%question%' AND s.Summary LIKE '%format%';  -- Example criteria for identifying trends

-- 4.5
SELECT c.RoleName, AVG(c.DifficultyRating) AS avg_difficulty,
    SUM(CASE WHEN s.Summary LIKE '%technical%' THEN 1 ELSE 0 END) AS technical_questions,
    SUM(CASE WHEN s.Summary LIKE '%behavioral%' THEN 1 ELSE 0 END) AS behavioral_questions
FROM Co_op c
JOIN Co_op_Student cs ON c.CoOpID = cs.CoOpID
JOIN Student_Notes s ON cs.StudentID = s.StudentID
GROUP BY c.RoleName;

-- 4.6
SELECT s.Summary, s.DatePublished, com.CompanyName, c.RoleName
FROM Student_Notes s
JOIN Co_op_Student cs ON s.StudentID = cs.StudentID
JOIN Co_op c ON cs.CoOpID = c.CoOpID
JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
JOIN Company com ON cc.CompanyID = com.CompanyID
WHERE s.Summary LIKE '%success%' AND com.CompanyName = 'TechCorp' AND c.RoleName = 'Software Engineer';  -- Replace with specific company and role