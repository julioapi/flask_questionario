from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('questionario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    renda = request.form['renda']
    interesse_produto = request.form['interesse_produto']
    
    return render_template('obrigado.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
