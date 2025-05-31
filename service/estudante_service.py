import psycopg2
from database import get_db_connection
from flask import jsonify
from utils.utils import get_error_message
class Estudante_Service:
    

    def create_estudante(e_nome, e_code):
        """Create a new estudante in the database."""
        db = get_db_connection()
        try:
            query = "SELECT * FROM create_estudante(%s, %s);"
            db.execute(query, (e_nome, e_code))
            result = db.fetchone()
            print(result)
            db.connection.commit()
            return jsonify({
                    "message": "Estudante created successfully", 
                    "success": True,
                    "status": 201,
                    "data": result
                }), 201
        except psycopg2.Error as e:
            message, code = get_error_message(e.diag.message_detail)
            db.connection.rollback()
            return jsonify({
                "message": message,
                "success": False,
                "status": code,
                "data": None
            }), code
        except Exception as e:
            message, code = get_error_message(e.diag.message_detail)
            db.connection.rollback()
            return jsonify({
                "message": message,
                "success": False,
                "status": code,
                "data": None
            }), code