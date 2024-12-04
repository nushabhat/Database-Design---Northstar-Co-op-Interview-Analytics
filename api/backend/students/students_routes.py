from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
import logging 

# Create a new Blueprint object for co-op routes
students = Blueprint('students', __name__)

@students.route('/search_coops', methods=['GET'])
def get_coops():
    industry = request.args.get('industry')
    company_name = request.args.get('company_name')
    role_name = request.args.get('role_name')

    query = '''
        SELECT 
            Co_op.CoOpID, 
            Co_op.RoleName, 
            Co_op.Industry, 
            Co_op.DifficultyRating, 
            Company.CompanyName
        FROM Co_op
        LEFT JOIN Company_Co_op ON Co_op.CoOpID = Company_Co_op.CoOpID
        LEFT JOIN Company ON Company_Co_op.CompanyID = Company.CompanyID
        WHERE 1=1
    '''

    params = []
    if industry:
        query += " AND Co_op.Industry = %s"
        params.append(industry)
    if company_name:
        query += " AND Company.CompanyName LIKE %s"
        params.append(f"%{company_name}%")
    if role_name:
        query += " AND Co_op.RoleName LIKE %s"
        params.append(f"%{role_name}%")

    cursor = db.get_db().cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()

    response = make_response(jsonify(results))
    response.status_code = 200
    return response

@students.route('/get_coop_details/<int:coop_id>', methods=['GET'])
def get_coop_details(coop_id):
    cursor = db.get_db().cursor()
    
    # Query for co-op details including company information
    coop_query = '''
        SELECT 
            c.CoOpID,
            c.RoleName,
            c.Industry,
            c.InterviewRounds,
            c.DifficultyRating,
            comp.CompanyName,
            comp.CompanyAddress,
            comp.Sector
        FROM Co_op c
        LEFT JOIN Company_Co_op cc ON c.CoOpID = cc.CoOpID
        LEFT JOIN Company comp ON cc.CompanyID = comp.CompanyID
        WHERE c.CoOpID = %s
    '''
    
    # Query for all notes associated with this co-op
    notes_query = '''
        SELECT 
            n.NoteID,
            n.Summary,
            n.DatePublished,
            s.Name as StudentName,
            a.Name as AdminName
        FROM Student_Notes n
        LEFT JOIN Student s ON n.StudentID = s.ID
        LEFT JOIN Administrator a ON n.AdminID = a.ID
        WHERE n.CoOpID = %s
        ORDER BY n.DatePublished DESC
    '''
    
    try:
        # Execute queries
        cursor.execute(coop_query, (coop_id,))
        coop_details = cursor.fetchone()
        
        if not coop_details:
            return jsonify({"error": "Co-op not found"}), 404
            
        cursor.execute(notes_query, (coop_id,))
        notes = cursor.fetchall()
        
        # Combine the results
        response = {
            "coop_details": coop_details,
            "notes": notes
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        current_app.logger.error(f"Error fetching co-op details: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@students.route('/industries', methods=['GET'])
def get_unique_industries():
    try:
        cursor = db.get_db().cursor()
        query = "SELECT DISTINCT Industry FROM Co_op ORDER BY Industry;"
        cursor.execute(query)
        results = cursor.fetchall()
        print(results, flush=True)
        industries = [item['Industry'] for item in results]
        #print(industries, flush=True)

        return jsonify(industries)
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error exception': str(e)}), 500
    
