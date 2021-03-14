from main import Pessoas, Usuarios

def insere_pessoa():
    pessoa = Pessoas(nome="Welder", idade=21)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Welder').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Welder').first()
    pessoa.idade = 23
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Welder').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuario():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    # insere_usuario('Welder', '12345')
    # insere_usuario('Valdirene', '54321')

    consulta_usuario()
    # insere_pessoa()
    # consulta_pessoa()
    # altera_pessoa()
    # exclui_pessoa()