# CS3200 - Database Design Final Project Repository

### Team Members: Quillian Alewine, Sarah Cooper, San Yan, Nusha Bhat, Lucia Yaniz
### Project Name: NorthStar Technologies
### [Link to Youtube Video (8:37)]((https://youtu.be/JiTbq1K2oYI)

**Project Overview** 

NorthStar is a data-driven app that streamlines interview preparation for students applying for co-op roles. It provides a centralized platform with detailed insights into interview experiences, peer connections for tips, and filters by industry, company, or role. Advisors and administrators can also leverage the platform to support students effectively.

## Starting the Project
1. Open the repository in the IDE of your choice.
2. In the new api folder create a file named ".env"
    Should be formated as such:
   
        SECRET_KEY=someCrazyS3cR3T!Key.!
        DB_USER=root
        DB_HOST=db
        DB_PORT=3306
        DB_NAME=northstar
        MYSQL_ROOT_PASSWORD= XXX 
   
    Replace the X's with a unique password
4. Open the terminal "Ctrl + `"
5. docker compose up -d
6. run http://localhost:8501 in your browser

## User Personas

1. Emma Chen (Student Researching Co-ops)

- A 2nd-year data science and biology major preparing for biotech co-op interviews.
- Needs targeted interview insights, peer connections, and efficient filtering tools to prepare.

2. Raaya Morova (Student Reviewing Co-ops)

- A 4th-year finance student who has completed her second co-op and wants to share her experiences.
- Needs a platform to share detailed feedback efficiently and anonymously while reducing repetitive conversations.
- Struggles to manage the high volume of similar queries from other students.

3. Holly Daize (Co-op Advisor)

- A career counselor with over 15 years of experience, guiding students through the co-op process.
- Needs centralized data, streamlined research processes, and tools for facilitating peer-to-peer sharing.
- Faces challenges with incomplete and time-intensive data collection.

4. Sarah Johnson (Administrator)

- A recent graduate who created NorthStar to address the lack of specific and accessible interview preparation resources.
- Needs a centralized platform to provide tailored interview insights and trends analysis.
- Aims to help students avoid the same struggles she experienced during her co-op application process.

## Controlling the Containers

- `docker compose up -d` to start all the containers in the background
- `docker compose down` to shutdown and delete the containers
- `docker compose up db -d` only start the database container (replace db with the other services as needed)
- `docker compose stop` to "turn off" the containers but not delete them. 
