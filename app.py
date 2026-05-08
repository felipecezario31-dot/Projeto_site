import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'uma_chave_secreta_para_desenvolvimento'


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'usuario' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Simulação de login sem banco
        session['usuario'] = 'admin'  # Simula usuário logado
        return redirect(url_for('home'))

    return render_template('login/login.html')


@app.route('/home')
def home():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    return render_template('index.html', titulo='Meu Site', usuario=session['usuario'])


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
    

