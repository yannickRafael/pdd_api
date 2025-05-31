from flask import Blueprint, request, jsonify
from service.curso_service import Curso_Service

curso_bp = Blueprint('curso_bp', __name__, url_prefix='/curso')

@curso_bp.route('/', methods=['POST'])
def create_curso():
    form = request.form
    required_fields = ['cu_nome', 'cu_code']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    cu_nome = form.get('cu_nome')
    cu_code = form.get('cu_code')
    cu_created_by = form.get('cu_created_by', None)

    response = Curso_Service.create_curso(cu_nome, cu_code, cu_created_by)
    
    return response


@curso_bp.route('/', methods=['PUT'])
def update_curso():
    form = request.form
    required_fields = ['cu_id', 'cu_nome', 'cu_code']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    cu_nome = form.get('cu_nome')
    cu_id = form.get('cu_id')
    cu_code = form.get('cu_code')
    cu_edited_by = form.get('cu_edited_by', None)


    response = Curso_Service.update_curso(cu_id, cu_nome, cu_code, cu_edited_by)
    
    return response

@curso_bp.route('/', methods=['DELETE'])
def delete_curso():
    form = request.form
    required_fields = ['cu_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400 
    
    cu_id = form.get('cu_id')
    cu_edited_by = form.get('cu_edited_by', None)


    response = Curso_Service.delete_curso(cu_id, cu_edited_by)
    
    return response

