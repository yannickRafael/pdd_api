from flask import Blueprint, request, jsonify
from service.estudante_service import Estudante_Service

estudante_bp = Blueprint('estudante_bp', __name__, url_prefix='/staff')

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

    response = Estudante_Service.create_estudante(e_nome, e_code)
    
    return response


@estudante_bp.route('/', methods=['PUT'])
def update_estudante():
    data = request.form
    print(data)

@estudante_bp.route('/', methods=['DELETE'])
def delete_estudante():
    data = request.form
    print(data)

