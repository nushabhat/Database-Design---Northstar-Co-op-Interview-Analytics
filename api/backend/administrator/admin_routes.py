from flask import Blueprint, request, jsonify
from backend.db_connection import db
import logging

administrator = Blueprint('administrator', __name__)


@administrator.route('/delete_student', methods=['DELETE'])
def delete_student():
    try:
        # Parse JSON payload
        data = request.get_json()
        username = data.get('username')
        student_id = data.get('id')
        
        # Validate input
        if not username or not student_id:
            return jsonify({'error': 'Username and ID are required'}), 400

        # Query to delete the student
        query = "DELETE FROM Student WHERE UserName = %s AND ID = %s"
        cursor = db.get_db().cursor()
        cursor.execute(query, (username, student_id))
        db.get_db().commit()  # Commit the transaction

        # Check if a row was deleted
        if cursor.rowcount > 0:
            return jsonify({'message': 'Student deleted successfully'}), 200
        else:
            return jsonify({'error': 'No student found with the provided username and ID'}), 404

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@administrator.route('/get_all_students', methods=['GET'])
def get_all_students():
    try:
        # Query to fetch all student data
        query = """
            SELECT ID, GraduationYear, Major, Minor, EmailAddress, UserName, Name, 
                   NumPreviousCoops, GPA, AdvisorID 
            FROM Student
            ORDER BY ID
        """
        cursor = db.get_db().cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        # Structure results as a list of dictionaries
        students_list = [dict(row) for row in results]

        return jsonify(students_list), 200

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@administrator.route('/edit_student', methods=['PUT'])
def edit_student():
    try:
        # Parse JSON payload
        data = request.get_json()
        student_id = data.get('id')  # Student ID is mandatory
        updates = {}

        # Add fields to update based on the provided data
        for field in ['GraduationYear', 'Major', 'Minor', 'EmailAddress', 'UserName', 'Name', 
                      'NumPreviousCoops', 'GPA']:
            if field in data:
                updates[field] = data[field]

        if not student_id:
            return jsonify({'error': 'Student ID is required'}), 400
        
        if not updates:
            return jsonify({'error': 'No updates provided'}), 400

        # Construct the dynamic SQL query
        set_clause = ', '.join([f"{key} = %s" for key in updates.keys()])
        query = f"UPDATE Student SET {set_clause} WHERE ID = %s"
        values = list(updates.values()) + [student_id]

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()

        if cursor.rowcount > 0:
            return jsonify({'message': 'Student information updated successfully'}), 200
        else:
            return jsonify({'error': 'No student found with the given ID'}), 404

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500
