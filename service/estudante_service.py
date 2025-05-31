from database import get_db_connection
from flask import jsonify

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
            return jsonify({"message": "Estudante created successfully", "id": result}), 201
        except Exception as e:
            db.connection.rollback()
            return jsonify({"error": str(e)}), 500