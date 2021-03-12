import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']
     },
    {'nome': 'Galleani',
     'habilidades': ['Python', 'Django']}
]

@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrado da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro Excluido'})

@app.route('/dev/', methods=['POST', 'GET'])
def listaDesenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)