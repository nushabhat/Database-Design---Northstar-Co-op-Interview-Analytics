# CS3200 - Database Design Final Project Repository

### Team Members: Quillian Alewine, Sarah Cooper, San Yan, Nusha Bhat, Lucia Yaniz
### Project Name: NorthStar Technologies
### LINK TO YOUTUBE VIDEO (6-9 min)

Brief intro of team and members
Include an “Elevator Pitch” for your application (30 - 45 seconds)
Quick review of the routes (code) you’ve created and how you’ve organized them in blueprints. (2 mins max).  You don’t need to go line-by-line.  Go through high level organization, point out the different types of routes (get, post, put, delete, etc)	
Demo of the front-end Streamlit application your team has created. (~ 5 mins)  
Be sure to show that for any POST/PUT/DELETE routes, the database reflects the results of the operation by looking at the data in DataGrip. 

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

## Prerequisites

- A GitHub Account
- A terminal-based or GUI git client
- VSCode with the Python Plugin
- A distrobution of Python running on your laptop (Choco (for Windows), brew (for Macs), miniconda, Anaconda, etc). 

## Current Project Components

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for your data model and data base in the `./database-files` directory 

## Controlling the Containers

- `docker compose up -d` to start all the containers in the background
- `docker compose down` to shutdown and delete the containers
- `docker compose up db -d` only start the database container (replace db with the other services as needed)
- `docker compose stop` to "turn off" the containers but not delete them. 
