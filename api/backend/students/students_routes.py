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
    
