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

