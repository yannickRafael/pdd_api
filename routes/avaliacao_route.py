from flask import Blueprint, request
from service.avaliacao_service import Avaliacao_Service

avaliacao_bp = Blueprint('avaliacao_bp', __name__)

@avaliacao_bp.route('/', methods=['POST'])
def create_avaliacao():
    form = request.form
    required_fields = ['a_nome', 'a_code', 'ca_id', 'a_nota_max']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400
    
    a_nome = form.get('a_nome')
    a_code = form.get('a_code')
    ca_id = form.get('ca_id')
    a_nota_max = form.get('a_nota_max')
    a_created_by = form.get('a_created_by', None)

    response = Avaliacao_Service.create_avaliacao(a_nome, a_code, ca_id, a_nota_max, a_created_by)

    return response

@avaliacao_bp.route('/', methods=['PUT'])
def update_avaliacao():
    form = request.form
    required_fields = ['a_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400
    
    a_id = form.get('a_id')
    a_nome = form.get('a_nome', None)
    a_code = form.get('a_code', None)
    ca_id = form.get('ca_id', None)
    a_nota_max = form.get('a_nota_max', None)
    a_edited_by = form.get('a_edited_by', None)

    response = Avaliacao_Service.update_avaliacao(a_id, a_nome, a_code, ca_id, a_nota_max, a_edited_by)

    return response

@avaliacao_bp.route('/', methods=['DELETE'])
def delete_avaliacao():
    form = request.form
    required_fields = ['a_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400
    
    a_id = form.get('a_id')
    a_deleted_by = form.get('a_deleted_by', None)

    response = Avaliacao_Service.delete_avaliacao(a_id, a_deleted_by)

    return response