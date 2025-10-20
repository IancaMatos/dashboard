from flask import Flask, render_template

app = Flask(__name__)

# Rota página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para relatórios
@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

# Rota para usuários
@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

# Rota para configurações
@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html')

if __name__ == '__main__':
    app.run(debug=True) 