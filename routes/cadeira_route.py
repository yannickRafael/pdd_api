from flask import Blueprint, request, jsonify
from service.cadeira_service import Cadeira_Service

cadeira_bp = Blueprint('cadeira_bp', __name__)

@cadeira_bp.route('/', methods=['POST'])
def create_cadeira():
    form = request.form
    required_fields = ['ca_nome', 'ca_code', 'cu_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    ca_nome = form.get('ca_nome')
    ca_code = form.get('ca_code')
    cu_id = form.get('cu_id')
    ca_link = form.get('ca_link', None)
    ca_created_by = form.get('ca_created_by', None)

    response = Cadeira_Service.create_cadeira(ca_nome, ca_code, cu_id, ca_link, ca_created_by)
    
    return response


@cadeira_bp.route('/', methods=['PUT'])
def update_cadeira():
    form = request.form
    required_fields = ['ca_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    ca_id = form.get('ca_id')
    ca_nome = form.get('ca_nome', None)
    ca_code = form.get('ca_code', None)
    cu_id = form.get('cu_id', None)
    ca_link = form.get('ca_link', None)
    ca_edited_by = form.get('ca_edited_by', None)


    response = Cadeira_Service.update_cadeira(ca_id, ca_nome, ca_code, cu_id, ca_link, ca_edited_by)
    
    return response

@cadeira_bp.route('/', methods=['DELETE'])
def delete_cadeira():
    form = request.form
    required_fields = ['ca_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    ca_id = form.get('ca_id')
    ca_edited_by = form.get('ca_edited_by', None)


    response = Cadeira_Service.delete_cadeira(ca_id, ca_edited_by)
    
    return response

