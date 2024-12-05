Use northstar;

-- mock data for adminastrators 20 rows
INSERT INTO Administrator (Name, EmailAddress, UserName) VALUES
('Karalee Sedgemore', 'ksedgemore0@google.com.br', 'ksedgemore0'),
('Markos Kerins', 'mkerins1@tripadvisor.com', 'mkerins1'),
('Gilly Landsborough', 'glandsborough2@nhs.uk', 'glandsborough2'),
('Quintina Joscelyne', 'qjoscelyne3@twitpic.com', 'qjoscelyne3'),
('Alaine Howison', 'ahowison4@apple.com', 'ahowison4'),
('Brooks Abys', 'babys5@elpais.com', 'babys5'),
('Bride Guttridge', 'bguttridge6@webs.com', 'bguttridge6'),
('Bryce Salmon', 'bsalmon7@behance.net', 'bsalmon7'),
('Bess Wallbanks', 'bwallbanks8@mac.com', 'bwallbanks8'),
('Brittney Whitehair', 'bwhitehair9@blogspot.com', 'bwhitehair9'),
('Tarrah Loxly', 'tloxlya@huffingtonpost.com', 'tloxlya'),
('Umberto Stonner', 'ustonnerb@ca.gov', 'ustonnerb'),
('Charmine Lardez', 'clardezc@hugedomains.com', 'clardezc'),
('Selby Berre', 'sberred@ocn.ne.jp', 'sberred'),
('Virginia Lampart', 'vlamparte@adobe.com', 'vlamparte'),
('Richart Bucknill', 'rbucknillf@deviantart.com', 'rbucknillf'),
('Shermie Craft', 'scraftg@aboutads.info', 'scraftg'),
('Zulema Kordova', 'zkordovah@illinois.edu', 'zkordovah'),
('Gwenette Bothwell', 'gbothwelli@booking.com', 'gbothwelli'),
('Padget Serginson', 'pserginsonj@icq.com', 'pserginsonj');

-- Mock data for co-op table 40
INSERT INTO Co_op (RoleName, InterviewRounds, DifficultyRating, AdminID, Industry) VALUES
('GIS Technical Architect', 2, 4.8, 11, 'Finance'),
('Media Manager I', 1, 3.2, 5, 'Aerospace'),
('Social Worker', 3, 4.7, 6, 'Fashion'),
('Desktop Support Technician', 5, 2.5, 4, 'Manufacturing'),
('Assistant Manager', 3, 3.4, 17, 'Fashion'),
('Staff Scientist', 2, 2.7, 15, 'Engineering'),
('Safety Technician III', 3, 3.4, 2, 'Biotechnology'),
('Research Assistant I', 3, 1.7, 14, 'Biotechnology'),
('Nurse', 3, 1.6, 4, 'Engineering'),
('Registered Nurse', 5, 2.9, 3, 'Energy'),
('VP Quality Control', 1, 4.5, 10, 'Engineering'),
('Project Manager', 4, 2.2, 7, 'Finance'),
('Statistician IV', 1, 3.6, 6, 'E-commerce'),
('Operator', 2, 4.7, 3, 'Engineering'),
('Clinical Specialist', 4, 4.0, 11, 'Aerospace'),
('Executive Secretary', 5, 1.8, 16, 'Manufacturing'),
('Business Systems Development Analyst', 4, 5.0, 19, 'Manufacturing'),
('Physical Therapy Assistant', 4, 4.2, 1, 'Engineering'),
('Web Designer III', 3, 3.9, 3, 'Biotechnology'),
('Director of Sales', 3, 4.1, 12, 'Biotechnology'),
('Legal Assistant', 2, 2.0, 2, 'Healthcare'),
('Executive Secretary', 5, 1.7, 18, 'Consulting'),
('Compensation Analyst', 3, 1.6, 17, 'E-commerce'),
('Budget/Accounting Analyst III', 4, 4.3, 9, 'Aerospace'),
('Librarian', 2, 1.7, 18, 'Technology'),
('Software Engineer III', 2, 1.4, 2, 'Engineering'),
('Recruiting Manager', 3, 3.0, 15, 'Engineering'),
('Assistant Media Planner', 5, 4.1, 17, 'Finance'),
('Human Resources Assistant II', 5, 4.3, 16, 'Technology'),
('Legal Assistant', 5, 3.0, 16, 'Cybersecurity'),
('Senior Sales Associate', 3, 4.7, 6, 'Finance'),
('Data Coordinator', 3, 2.1, 12, 'Finance'),
('Professor', 4, 4.9, 13, 'Energy'),
('Administrative Assistant III', 3, 3.9, 8, 'Technology'),
('Actuary', 5, 3.8, 19, 'Cybersecurity'),
('Recruiter', 4, 4.0, 17, 'Aerospace'),
('Nurse', 5, 3.9, 18, 'Biotechnology'),
('Technical Writer', 2, 1.4, 16, 'Healthcare'),
('Senior Cost Accountant', 5, 1.3, 20, 'Healthcare');

-- Mock data for company table 30
INSERT INTO Company (CompanyName, CompanyAddress, Sector) 
VALUES 
    ('Edgepulse', '3064 Lyons Alley', 'Biotechnology'),
    ('Dabshots', '2156 Sommers Circle', 'E-commerce'),
    ('Flipbug', '8814 Bashford Crossing', 'Biotechnology'),
    ('Kanoodle', '1336 Lakeland Circle', 'Technology'),
    ('Trudoo', '921 Scofield Place', 'Biotechnology'),
    ('Demivee', '9 Northview Trail', 'Aerospace'),
    ('LiveZ', '1 Homewood Pass', 'Energy'),
    ('Edgewire', '42062 Bartelt Center', 'Engineering'),
    ('Zoomlounge', '3326 Johnson Avenue', 'Finance'),
    ('Quinu', '04175 Service Hill', 'Energy'),
    ('Kwilith', '62 Mariners Cove Park', 'Fashion'),
    ('Gigaclub', '7742 Grayhawk Park', 'Fashion'),
    ('Janyx', '4 Vernon Way', 'Energy'),
    ('Avamba', '8311 Prairie Rose Circle', 'Engineering'),
    ('Ntag', '5 Meadow Valley Way', 'Fashion'),
    ('Trudeo', '220 Prentice Circle', 'Fashion'),
    ('Devshare', '366 Anzinger Court', 'Biotechnology'),
    ('Skinte', '61 Lawn Center', 'Consulting'),
    ('Zazio', '024 Kedzie Place', 'Healthcare'),
    ('Oodoo', '8 Sachtjen Lane', 'Energy'),
    ('Twimm', '0 Harbort Trail', 'E-commerce'),
    ('Riffwire', '60 Maple Wood Crossing', 'Manufacturing'),
    ('Topdrive', '83 Pearson Pass', 'Consulting'),
    ('Gabspot', '71246 Dahle Place', 'Finance'),
    ('Wikizz', '7298 Farmco Center', 'Energy'),
    ('Meetz', '566 Monterey Junction', 'Healthcare'),
    ('Buzzdog', '05330 Eastlawn Circle', 'Fashion'),
    ('Devshare', '20 Basil Point', 'Engineering'),
    ('Ailane', '51840 Graceland Terrace', 'E-commerce'),
    ('Feednation', '114 Rieder Road', 'Energy');


-- mock data for Advisors 20 rows
INSERT INTO Advisor (Name, UserName, Email) VALUES 
('Matthiew Gilphillan', 'mgilphillan0', 'mgilphillan0@msn.com'),
('Octavia Harty', 'oharty1', 'oharty1@mozilla.com'),
('Gannon Stirland', 'gstirland2', 'gstirland2@typepad.com'),
('Ericha Stearndale', 'estearndale3', 'estearndale3@rediff.com'),
('Caro Izchaki', 'cizchaki4', 'cizchaki4@bloomberg.com'),
('Brandise Shackell', 'bshackell5', 'bshackell5@histats.com'),
('Ula Cancellieri', 'ucancellieri6', 'ucancellieri6@wunderground.com'),
('Beverly Cullin', 'bcullin7', 'bcullin7@dell.com'),
('Maurine Leftbridge', 'mleftbridge8', 'mleftbridge8@spiegel.de'),
('Karyl Heatley', 'kheatley9', 'kheatley9@ning.com'),
('Carlotta Nickless', 'cnicklessa', 'cnicklessa@dion.ne.jp'),
('Constantin Whittington', 'cwhittingtonb', 'cwhittingtonb@nsw.gov.au'),
('Miguela Avard', 'mavardc', 'mavardc@mapquest.com'),
('Hagan Librey', 'hlibreyd', 'hlibreyd@mtv.com'),
('Reinold Dumbar', 'rdumbare', 'rdumbare@ftc.gov'),
('Leroy Tatters', 'ltattersf', 'ltattersf@freewebs.com'),
('Antonius Lahiff', 'alahiffg', 'alahiffg@alibaba.com'),
('Anselma Shubotham', 'ashubothamh', 'ashubothamh@mapy.cz'),
('Keeley Vardey', 'kvardeyi', 'kvardeyi@1688.com'),
('Noel Boddam', 'nboddamj', 'nboddamj@elegantthemes.com');


-- mock data for Student table 40 17 no coop
INSERT INTO Student (GraduationYear, Major, Minor, EmailAddress, UserName, Name, NumPreviousCoops, GPA, AdvisorID) VALUES
(2024, 'Technology', 'Communication', 'mgregoraci0@opensource.org', 'mgregoraci0', 'Marlyn Gregoraci', 0, 3.6, 8),
(2025, 'Biology', 'Linguistics', 'qclemitt3@google.com.au', 'qclemitt3', 'Quinlan Clemitt', 0, 4.0, 10),
(2024, 'Computer Science', 'Economics', 'srome4@sfgate.com', 'srome4', 'Shanie Rome', 0, 3.5, 15),
(2022, 'Fashion', 'Environmental Science', 'rdewsnap5@tinyurl.com', 'rdewsnap5', 'Ritchie Dewsnap', 0, 4.0, 17),
(2021, 'Fashion', 'Business', 'kthorndale6@yahoo.co.jp', 'kthorndale6', 'Kitty Thorndale', 0, 3.8, 17),
(2028, 'Fashion', 'Philosophy', 'awhiskerd7@huffingtonpost.com', 'awhiskerd7', 'Asher Whiskerd', 0, 3.8, 13),
(2025, 'Finance', 'Computer Science', 'hhasty9@opensource.org', 'hhasty9', 'Herold Hasty', 0, 2.6, 3),
(2022, 'Data Science', 'Computer Science', 'bmattheeuwb@vk.com', 'bmattheeuwb', 'Bernardine Mattheeuw', 0, 4.0, 3),
(2028, 'Economics', 'Environmental Science', 'smilazzod@xinhuanet.com', 'smilazzod', 'Sully Milazzo', 0, 2.5, 17),
(2025, 'Healthcare', 'Communication', 'bcrayf@g.co', 'bcrayf', 'Brandtr Cray', 0, 3.2, 17),
(2027, 'Computer Science', 'Sociology', 'sbardsleyh@histats.com', 'sbardsleyh', 'Shelley Bardsley', 0, 3.3, 14),
(2020, 'Biology', 'History', 'qcardoek@devhub.com', 'qcardoek', 'Quinta Cardoe', 0, 3.0, 20),
(2025, 'Engineering', 'Mathematics', 'felkinsm@unicef.org', 'felkinsm', 'Federico Elkins', 0, 2.7, 2),
(2024, 'Economics', 'Linguistics', 'amcenenyp@newyorker.com', 'amcenenyp', 'Adolphe McEneny', 0, 2.7, 3),
(2025, 'Economics', 'Communication', 'oartheyq@gizmodo.com', 'oartheyq', 'Otes Arthey', 0, 3.6, 3),
(2023, 'Finance', 'Sociology', 'craecroftx@virginia.edu', 'craecroftx', 'Curcio Raecroft', 0, 3.5, 6),
(2022, 'Technology', 'Mathematics', 'bwildgoose13@moonfruit.com', 'bwildgoose13', 'Brietta Wildgoose', 0, 3.0, 4),
(2026, 'Technology', 'Statistics', 'twoodrup1@ihg.com', 'twoodrup1', 'Talyah Woodrup', 3, 3.3, 13),
(2021, 'Cybersecurity', 'Statistics', 'rrait2@theglobeandmail.com', 'rrait2', 'Rutledge Rait', 3, 2.6, 18),
(2024, 'Healthcare', 'Linguistics', 'bdooney8@jigsy.com', 'bdooney8', 'Bartel Dooney', 3, 3.6, 3),
(2022, 'Technology', 'Psychology', 'dvinerg@istockphoto.com', 'dvinerg', 'Deonne Viner', 2, 4.0, 19),
(2026, 'Computer Science', 'Environmental Science', 'ahatryo@google.ca', 'ahatryo', 'Aleen Hatry', 2, 3.0, 14),
(2020, 'Cybersecurity', 'Psychology', 'jchappelowu@soundcloud.com', 'jchappelowu', 'Jorge Chappelow', 1, 3.0, 12),
(2021, 'Economics', 'Environmental Science', 'rmcgeffeni@123-reg.co.uk', 'rmcgeffeni', 'Reyna McGeffen', 2, 3.4, 20),
(2020, 'Economics', 'Art', 'imaasza@abc.net.au', 'imaasza', 'Ingeborg Maasz', 1, 3.3, 19),
(2022, 'Healthcare', 'Environmental Science', 'lirvinec@mozilla.org', 'lirvinec', 'Laurie Irvine', 1, 2.8, 1),
(2024, 'Healthcare', 'Psychology', 'espringhame@seesaa.net', 'espringhame', 'Elsa Springham', 3, 3.8, 17),
(2026, 'Technology', 'Sociology', 'rananj@mashable.com', 'rananj', 'Rickie Anan', 3, 3.8, 18),
(2027, 'Cybersecurity', 'Political Science', 'tnoadsl@plala.or.jp', 'tnoadsl', 'Thoma Noads', 1, 3.3, 1),
(2021, 'Healthcare', 'Psychology', 'rmenichinin@si.edu', 'rmenichinin', 'Rafa Menichini', 1, 3.2, 17),
(2027, 'Computer Science', 'Sociology', 'wciccottior@about.me', 'wciccottior', 'Winny Ciccottio', 2, 2.8, 14),
(2026, 'Healthcare', 'Linguistics', 'tsauvans@stumbleupon.com', 'tsauvans', 'Tammie Sauvan', 1, 2.8, 4),
(2020, 'Computer Science', 'Communication', 'helfordt@yolasite.com', 'helfordt', 'Hagan Elford', 1, 2.6, 5),
(2027, 'Healthcare', 'History', 'dnajerav@bloomberg.com', 'dnajerav', 'Dominik Najera', 1, 3.6, 3),
(2027, 'Finance', 'Economics', 'eledsonw@acquirethisname.com', 'eledsonw', 'Earl Ledson', 1, 2.7, 12),
(2021, 'Computer Science', 'Mathematics', 'bworsallsy@bigcartel.com', 'bworsallsy', 'Brynne Worsalls', 3, 3.8, 15),
(2020, 'Technology', 'Computer Science', 'atomesz@wikia.com', 'atomesz', 'Arnold Tomes', 3, 3.6, 6),
(2028, 'Engineering', 'Art', 'amaccallion10@nationalgeographic.com', 'amaccallion10', 'Ardella MacCallion', 3, 3.1, 2),
(2025, 'Economics', 'Chemistry', 'sofeeny11@sphinn.com', 'sofeeny11', 'Salomi O''Feeny', 1, 2.7, 13),
(2024, 'Fashion', 'Linguistics', 'ssymmers12@independent.co.uk', 'ssymmers12', 'Stu Symmers', 1, 3.8, 14);

-- mock data for extracurriculars 50 rows


-- mock data for students notes table 50
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (32, 'In hac habitasse platea dictumst. Etiam faucibus cursus urna.', '2023-01-09', 30, 14);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (37, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est.', '2024-03-25', 12, 6);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (6, 'Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum.', '2022-07-07', 3, 9);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (14, 'Quisque ut erat.', '2023-07-08', 17, 14);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (9, 'Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.', '2018-10-10', 26, 16);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (1, 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum.', '2023-01-27', 7, 18);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (7, 'Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.', '2024-09-09', 20, 14);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (7, 'Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', '2021-03-21', 3, 12);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (38, 'Mauris ullamcorper purus sit amet nulla.', '2021-12-02', 4, 3);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (32, 'Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.', '2023-11-29', 22, 1);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (18, 'Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo.', '2022-09-23', 24, 10);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (16, 'Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.', '2019-02-11', 4, 7);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (28, 'Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.', '2019-06-01', 10, 7);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (37, 'Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus.', '2020-11-04', 37, 8);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (9, 'Sed ante.', '2020-07-18', 18, 1);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (7, 'Ut at dolor quis odio consequat varius. Integer ac leo.', '2017-07-08', 24, 15);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (24, 'Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.', '2021-02-10', 38, 8);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (9, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum.', '2020-01-16', 37, 2);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (34, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.', '2020-03-09', 34, 5);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (23, 'Pellentesque at nulla.', '2021-04-22', 6, 3);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (23, 'Morbi a ipsum. Integer a nibh. In quis justo.', '2024-03-12', 24, 6);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (28, 'Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue.', '2021-12-31', 3, 12);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (40, 'Aliquam non mauris. Morbi non lectus.', '2022-06-07', 26, 4);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (31, 'Donec dapibus.', '2019-01-21', 1, 16);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (3, 'Sed ante. Vivamus tortor.', '2017-09-05', 26, 6);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (20, 'Duis bibendum. Morbi non quam nec dui luctus rutrum.', '2020-11-26', 25, 17);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (12, 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi.', '2020-11-26', 4, 15);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (15, 'Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.', '2024-04-25', 34, 1);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (15, 'Suspendisse accumsan tortor quis turpis. Sed ante. Vivamus tortor. Duis mattis egestas metus.', '2021-08-08', 39, 19);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (31, 'Quisque porta volutpat erat.', '2024-05-21', 12, 19);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (3, 'Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus.', '2021-09-29', 37, 19);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (26, 'Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi.', '2019-01-07', 22, 16);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (38, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.', '2024-01-27', 32, 13);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (14, 'Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem.', '2021-07-08', 7, 20);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (38, 'Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', '2020-10-05', 4, 15);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (23, 'Nulla tellus.', '2017-09-21', 37, 18);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (16, 'Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.', '2017-03-21', 13, 15);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (28, 'Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', '2021-11-16', 32, 5);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (30, 'Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', '2017-01-22', 24, 2);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (32, 'Etiam vel augue.', '2020-12-31', 4, 3);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (20, 'Vivamus tortor. Duis mattis egestas metus. Aenean fermentum.', '2020-05-26', 35, 1);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (26, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi.', '2023-08-14', 15, 6);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (5, 'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.', '2019-08-05', 3, 5);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (24, 'Maecenas pulvinar lobortis est.', '2021-01-03', 10, 5);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (24, 'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo.', '2022-05-01', 34, 10);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (21, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti. Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum.', '2018-10-16', 38, 7);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (29, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio.', '2020-04-15', 36, 17);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (14, 'Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti.', '2021-02-05', 7, 18);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (29, 'Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus.', '2023-08-23', 13, 18);
insert into Student_Notes (StudentID, Summary, DatePublished, CoOpID, AdminID) values (37, 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', '2019-11-01', 24, 4);

-- mock data for Co_op_Student 100 rows
INSERT INTO Co_op_Student (StudentID, CoOpID) 
VALUES 
(28, 24), (38, 21), (36, 17), (39, 14), (32, 26), (39, 32), (27, 27), (23, 38),
(38, 11), (31, 34), (29, 22), (24, 27), (34, 28), (35, 13), (29, 2), (29, 21),
(22, 37), (37, 1), (28, 7), (36, 1), (22, 6), (34, 11), (28, 8), (29, 28),
(38, 19), (18, 7), (24, 5), (31, 31), (26, 18), (39, 4), (31, 28), (22, 11),
(20, 33), (23, 17), (33, 15), (36, 9), (18, 32), (22, 2), (36, 29), (18, 8),
(18, 38), (37, 17), (17, 22), (25, 31), (31, 38), (24, 29), (18, 36), (26, 3),
(18, 35), (23, 8), (39, 20), (27, 16), (25, 24), (17, 35), (33, 3), (35, 18),
(17, 28), (23, 3), (20, 7), (18, 37), (39, 39), (27, 14), (21, 24), (37, 11),
(34, 12), (34, 36), (17, 20), (35, 7), (33, 28), (31, 11), (38, 35), (20, 20),
(39, 11), (27, 3), (24, 15), (30, 23), (28, 18), (36, 35), (21, 5), (25, 14),
(30, 38), (29, 27), (34, 18), (32, 33), (18, 12), (22, 1), (31, 33), (30, 30),
(26, 6), (39, 36), (26, 9), (32, 7), (25, 28), (30, 24), (38, 18), (25, 30),
(27, 33), (29, 13), (24, 33), (35, 37);



-- mock data for Co_op_Adv 100 rows
INSERT INTO Co_op_Adv (AdvID, CoOpID) 
VALUES 
(13, 2), (15, 34), (1, 1), (18, 16), (8, 21), (20, 14), (15, 2), 
(3, 37), (2, 35), (7, 5), (4, 27), (11, 24), (16, 14), (6, 22), 
(14, 30), (13, 26), (20, 6), (15, 11), (19, 36), (1, 28), (7, 4), 
(13, 22), (7, 16), (3, 27), (9, 9), (17, 7), (15, 33), (1, 23), 
(15, 13), (5, 18), (12, 15), (3, 31), (15, 16), (8, 15), 
(19, 2), (20, 12), (12, 23), (5, 20), (10, 28), (11, 28), 
(7, 38), (10, 3), (13, 9), (17, 1), (18, 8), (12, 20), (1, 34), 
(2, 28), (4, 17), (14, 7), (3, 19), (17, 11), (8, 13), (15, 27), 
(11, 34), (13, 39), (7, 25), (17, 39), (14, 12), (19, 17), (19, 1), 
(19, 31), (16, 27), (9, 14), (7, 34), (9, 4), (3, 22), (2, 32), 
(4, 39), (13, 6), (13, 28), (5, 35);


-- mock data for Company_Co_op 100 rows
INSERT INTO Company_Co_op (CompanyID, CoOpID) 
VALUES 
(23, 16), (6, 33), (11, 7), (14, 33), (16, 1), (4, 4), (19, 5), 
(7, 38), (22, 37), (20, 15), (22, 10), (12, 34), (21, 10), (13, 27), 
(18, 4), (9, 22), (3, 14), (26, 30), (2, 4), (15, 27), (10, 23), 
(24, 38), (20, 23), (5, 4), (3, 33), (16, 11), (8, 36), (9, 9), 
(21, 33), (7, 5), (28, 28), (28, 8), (2, 32), (20, 12), (6, 20), 
(5, 5), (3, 28), (5, 17), (21, 36), (17, 22), (2, 3), (25, 18), 
(27, 10), (21, 3), (5, 9), (5, 25), (26, 15), (8, 29), (1, 38), 
(19, 9), (7, 8), (13, 25), (19, 27), (23, 15), (9, 6), (23, 1), 
(3, 38), (10, 21), (12, 17), (4, 34), (19, 16), (2, 33), (9, 27), 
(5, 30), (13, 12), (15, 28), (5, 15), (3, 37), (28, 27), (22, 12), 
(8, 4), (5, 14), (16, 6), (18, 27), (3, 10), (5, 10), (2, 20);



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

-- Insert data into Company
INSERT INTO Company (CompanyName, CompanyAddress, Sector)
VALUES
('TechCorp', '123 Tech Street, Silicon Valley, CA', 'Technology'),
('FinancePlus', '456 Wall Street, New York, NY', 'Finance'),
('MechWorks', '789 Industrial Road, Detroit, MI', 'Engineering'),
('FinanceMinus', '456 Wall Street, New York, NY', 'Finance');


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
