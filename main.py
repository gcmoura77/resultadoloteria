from flask import Flask, render_template
from loteria import get_ultimo_concurso

app = Flask(__name__)

@app.route("/resultado")
def resultado():
    resultado = get_ultimo_concurso()

    ultimo_concurso = resultado['id']
    dezenas = resultado['dezenas_sorteadas']
    dezenas.sort()

    return render_template('resultado.html', concurso=ultimo_concurso, datasorteio=resultado['data_apuracao'], dezenas=dezenas)

# colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)