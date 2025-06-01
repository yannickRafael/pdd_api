from flask import Flask
from routes.estudante_route import estudante_bp
from routes.curso_route import curso_bp
from routes.cadeira_route import cadeira_bp
from routes.avaliacao_route import avaliacao_bp
from routes.performance_route import performance_bp


app = Flask(__name__) 

app.register_blueprint(estudante_bp, url_prefix='/estudante')
app.register_blueprint(curso_bp, url_prefix='/curso')
app.register_blueprint(cadeira_bp, url_prefix='/cadeira')
app.register_blueprint(avaliacao_bp, url_prefix='/avaliacao')
app.register_blueprint(performance_bp, url_prefix='/performance')

@app.route('/', methods=['GET'])
def home():
    return "PDD API is running!"

if __name__ == '__main__':
    app.run(debug=True)
