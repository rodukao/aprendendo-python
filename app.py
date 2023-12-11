from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/criando-bancos')
def criandoBancos():
    return render_template('criando-bancos.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)