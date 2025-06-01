from flask import Blueprint, request, jsonify
from service.estudante_service import Estudante_Service

estudante_bp = Blueprint('estudante_bp', __name__)

@estudante_bp.route('/', methods=['POST'])
def create_estudante():
    form = request.form
    required_fields = ['e_nome', 'e_code']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    e_nome = form.get('e_nome')
    e_code = form.get('e_code')
    e_created_by = form.get('e_created_by', 0)

    response = Estudante_Service.create_estudante(e_nome, e_code, e_created_by)
    
    return response


@estudante_bp.route('/', methods=['PUT'])
def update_estudante():
    form = request.form
    required_fields = ['e_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    e_nome = form.get('e_nome', None)
    e_id = form.get('e_id')
    e_edited_by = form.get('e_edited_by', 0)


    response = Estudante_Service.update_estudante(e_id, e_nome, e_edited_by)
    
    return response

@estudante_bp.route('/', methods=['DELETE'])
def delete_estudante():
    form = request.form
    required_fields = ['e_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    e_id = form.get('e_id')
    e_edited_by = form.get('e_edited_by', 0)


    response = Estudante_Service.delete_estudante(e_id, e_edited_by)
    
    return response

