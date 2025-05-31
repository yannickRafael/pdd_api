from flask import Flask
from routes.estudante_route import estudante_bp
from routes.curso_route import curso_bp

app = Flask(__name__) 

app.register_blueprint(estudante_bp, url_prefix='/estudante')
app.register_blueprint(curso_bp, url_prefix='/curso')

@app.route('/', methods=['GET'])
def home():
    return "PDD API is running!"

if __name__ == '__main__':
    app.run(debug=True)
