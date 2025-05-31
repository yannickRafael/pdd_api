from flask import Flask
from routes.estudante_route import estudante_bp

app = Flask(__name__) 

app.register_blueprint(estudante_bp, url_prefix='/estudante')

@app.route('/', methods=['GET'])
def home():
    return "PDD API is running!"

if __name__ == '__main__':
    app.run(debug=True)
