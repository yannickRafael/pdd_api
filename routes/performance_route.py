from flask import Blueprint, request
from service.performance_service import Performance_Service


performance_bp = Blueprint('performance_bp', __name__)

@performance_bp.route('/', methods=['POST'])
def create_performance():
    form = request.form
    required_fields = ['p_nota', 'e_id', 'a_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400
    
    p_nota = form.get('p_nota')
    e_id = form.get('e_id')
    a_id = form.get('a_id')
    p_created_by = form.get('p_created_by', None)

    response = Performance_Service.create_performance(p_nota, e_id, a_id, p_created_by)

    return response

@performance_bp.route('/', methods=['PUT'])
def update_performance():
    form = request.form
    required_fields = ['p_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400
    
    p_id = form.get('p_id')
    p_nota = form.get('p_nota', None)
    p_edited_by = form.get('p_edited_by', None)

    response = Performance_Service.update_performance(p_id, p_nota, p_edited_by)

    return response

@performance_bp.route('/', methods=['DELETE'])
def delete_performance():
    form = request.form
    required_fields = ['p_id']
    missing_fields = []

    for field in required_fields:
        if field not in form:
            missing_fields.append(field)
    if missing_fields:
        return {"error": f"Missing required fields: {', '.join(missing_fields)}"}, 400
    
    p_id = form.get('p_id')
    p_edited_by = form.get('p_edited_by', None)

    response = Performance_Service.delete_performance(p_id, p_edited_by)

    return response