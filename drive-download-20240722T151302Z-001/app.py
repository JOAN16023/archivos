from flask import Flask, render_template
from models.tareas import Tarea

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    tareas = Tarea.get_all()
    return render_template('index.html', tareas=tareas)

@app.route('/', methods=['POST'])
def hello_world_post():
    return 'Hello, World! POST'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
