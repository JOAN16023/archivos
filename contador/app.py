from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Define una clave secreta para las sesiones
@app.route('/')
def index():
    if 'visit_count' not in session:
        session['visit_count'] = 1
    else:
        session['visit_count'] += 1
    return render_template('index.html', visit_count=session['visit_count'])
@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect(url_for('index'))
