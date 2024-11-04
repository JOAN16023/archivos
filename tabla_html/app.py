from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    users = [
        {'first_name' : 'matias', 'last_name' : 'andres'},
        {'first_name' : 'Joan', 'last_name' : 'ignacio'},
        {'first_name' : 'juan', 'last_name' : 'thomas'},
        {'first_name' : 'jose', 'last_name' : 'rodolfo'}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)