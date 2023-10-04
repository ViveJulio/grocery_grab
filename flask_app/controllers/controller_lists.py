from flask_app import app
from flask import render_template, redirect, g, session
from flask_app.models.model_user import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('dashboard.html', user = user)