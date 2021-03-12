from main import Pessoas

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

if __name__ == '__main__':
    insere_pessoa()
    # consulta_pessoa()
    # altera_pessoa()
    # exclui_pessoa()