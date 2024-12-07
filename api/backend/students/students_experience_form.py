from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
from datetime import datetime

# Create a new Blueprint object for experience submission
experience_submission = Blueprint('experience_submission', __name__)

#------------------------------------------------------------
# Submit Experience Endpoint
@experience_submission.route('/submit_experience', methods=['POST'])
def submit_experience():
    try:
        # Get data from the form submission
        data = request.json
         # List of required fields
        required_fields = [
            'company_name', 'role_name', 'interview_date', 'industry',
            'difficulty_rating', 'graduation_year',
            'major', 'gpa', 'student_id'
        ]

        # Check for missing fields
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return make_response(
                jsonify({"error": f"Please complete the following fields before submitting: {', '.join(missing_fields)}"}),
                400
            )
        # Extract necessary fields from the request
        company_name = data['company_name']
        role_name = data['role_name']
        interview_date = data['interview_date']
        industry = data['industry']
        difficulty_rating = data['difficulty_rating']
        difficulty_elaboration = data['difficulty_elaboration']
        graduation_year = data['graduation_year']
        major = data['major']
        minor = data['minor']
        gpa = data['gpa']
        num_internships = data['num_internships']
        num_extracurriculars = data['num_extracurriculars']
        num_academic_extracurriculars = data['num_academic_extracurriculars']
        leadership_position = data['leadership_position']
        student_id = data['student_id']
        # Database connection
        cursor = db.get_db().cursor()

        # Insert or find the company
        cursor.execute("SELECT CompanyID FROM Company WHERE CompanyName = %s", (company_name,))
        company = cursor.fetchone()
        if not company:
            # Insert new company with only the name
            cursor.execute(
                "INSERT INTO Company (CompanyName) VALUES (%s)",
                (company_name,)
            )
            db.get_db().commit()
            company_id = cursor.lastrowid
        else:
            company_id = company['CompanyID']

        # Insert co-op details
        cursor.execute("""
            INSERT INTO Co_op (RoleName, InterviewRounds, DifficultyRating, Industry)
            VALUES (%s, %s, %s, %s)
        """, (role_name, data.get('interview_rounds', 0), difficulty_rating, industry))
        db.get_db().commit()
        co_op_id = cursor.lastrowid

        # Link co-op to company
        cursor.execute("""
            INSERT INTO Company_Co_op (CompanyID, CoOpID)
            VALUES (%s, %s)
        """, (company_id, co_op_id))
        db.get_db().commit()

        # Insert or update student details
        cursor.execute("SELECT ID FROM Student WHERE ID = %s", (student_id,))
        student = cursor.fetchone()
        if not student:
            # Insert new student record
            cursor.execute("""
                INSERT INTO Student (ID, GraduationYear, Major, Minor, GPA, NumPreviousCoops)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (student_id, graduation_year, major, minor, gpa, num_internships))
        else:
            # Update existing student record
            cursor.execute("""
                UPDATE Student
                SET GraduationYear = %s, Major = %s, Minor = %s, GPA = %s, NumPreviousCoops = %s
                WHERE ID = %s
            """, (graduation_year, major, minor, gpa, num_internships, student_id))
        db.get_db().commit()

        # Link student to co-op
        cursor.execute("""
            INSERT INTO Co_op_Student (StudentID, CoOpID)
            VALUES (%s, %s)
        """, (student_id, co_op_id))
        db.get_db().commit()

        # Optionally add student notes
        if 'student_note_summary' in data:
            cursor.execute("""
                INSERT INTO Student_Notes (StudentID, Summary, DatePublished, CoOpID)
                VALUES (%s, %s, %s, %s)
            """, (student_id, data['student_note_summary'], datetime.now(), co_op_id))
            db.get_db().commit()

        # Return success response
        return make_response(jsonify({"message": "Experience submitted successfully!"}), 200)

    except Exception as e:
        current_app.logger.error(f"Error submitting experience: {str(e)}")
        return make_response(jsonify({"error": "An error occurred during submission."}), 500)

#------------------------------------------------------------
# Get Co-op information by student ID
@experience_submission.route('/get_co_op_info/<student_id>', methods=['GET'])
def get_co_op_info(student_id):
    try:
        cursor = db.get_db().cursor()
        cursor.execute("""
            SELECT c.role_name, c.interview_date, c.difficulty_rating, c.difficulty_elaboration, co.company_name
            FROM co_op c
            JOIN company co ON c.company_id = co.company_id
            WHERE c.student_id = %s
        """, (student_id,))
        
        co_op_info = cursor.fetchall()
        
        if co_op_info:
            return make_response(jsonify(co_op_info), 200)
        else:
            return make_response(jsonify({"message": "No co-op information found for this student."}), 404)
    
    except Exception as e:
        current_app.logger.error(f"Error retrieving co-op info: {str(e)}")
        return make_response(jsonify({"error": "An error occurred while retrieving the information."}), 500)

#------------------------------------------------------------
# Get Student details
@experience_submission.route('/get_student_info/<student_id>', methods=['GET'])
def get_student_info(student_id):
    try:
        cursor = db.get_db().cursor()
        cursor.execute("""
            SELECT graduation_year, major, minor, gpa, num_internships, num_extracurriculars 
            FROM student 
            WHERE student_id = %s
        """, (student_id,))
        
        student_info = cursor.fetchall()

        if student_info:
            return make_response(jsonify(student_info), 200)
        else:
            return make_response(jsonify({"message": "No student information found for this ID."}), 404)
    
    except Exception as e:
        current_app.logger.error(f"Error retrieving student info: {str(e)}")
        return make_response(jsonify({"error": "An error occurred while retrieving the information."}), 500)
