from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'dev_key_change_in_production'


def login_required(f):
    """Decorator para proteger rotas que requerem login"""
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'usuario' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        
        if username:
            session['usuario'] = username
            return redirect(url_for('home'))
    
    return render_template('login/login.html')


@app.route('/home')
@login_required
def home():
    return render_template('index.html', usuario=session['usuario'])


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
    

