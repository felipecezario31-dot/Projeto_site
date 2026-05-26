import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
load_dotenv()
# ── App & configuração ─────────────────────────────────────────────────────────
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'dev_key_change_in_production'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///escola.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ── Modelos do banco de dados ──────────────────────────────────────────────────
class Aluno(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha    = db.Column(db.String(200), nullable=False)
    nome     = db.Column(db.String(120), nullable=False)

    notas  = db.relationship('Nota',  backref='aluno', lazy=True)
    faltas = db.relationship('Falta', backref='aluno', lazy=True)


class Nota(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    aluno_id  = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    materia   = db.Column(db.String(80), nullable=False)
    valor     = db.Column(db.Float, nullable=False)
    bimestre  = db.Column(db.Integer, nullable=False)


class Falta(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    aluno_id   = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    materia    = db.Column(db.String(80), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)


# ── Decorator de autenticação ──────────────────────────────────────────────────
def login_required(f):
    """Protege rotas que exigem login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# ── Rotas ──────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se já estiver logado, manda direto para home
    if 'usuario' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        senha    = request.form.get('senha', '').strip()

        aluno = Aluno.query.filter_by(username=username).first()

        if aluno and check_password_hash(aluno.senha, senha):
            session['usuario']    = aluno.username
            session['usuario_id'] = aluno.id
            session['nome']       = aluno.nome
            return redirect(url_for('home'))
        
        # Login inválido — avisa o usuário
        flash('Usuário ou senha incorretos.', 'erro')

    return render_template('login/login.html')


@app.route('/home')
@login_required
def home():
    return render_template('index.html', usuario=session['nome'])


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ── Inicialização
with app.app_context():
    db.create_all()  # Cria as tabelas se não existirem

# REMOVER após os testes
with app.app_context():
    from werkzeug.security import generate_password_hash
    if not Aluno.query.filter_by(username='admin').first():
        teste = Aluno(
            username='admin',
            senha=generate_password_hash('1234'),
            nome='Administrador'
        )
        db.session.add(teste)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
    