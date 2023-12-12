# Em valida.py

def validaEntrada(nome, senha):
    gerentes = {
        'kaliane': {'kaliane@gmail.com': 'amoGoiaba'},
        'daniel': {'daniel@gmail.com': '12345678'},
        'kaline': {'kaline@gmail.com': 'Qw78@.'},
        'joamerson': {'jojo@gmail.com': 'senha'}
    }

    return nome in gerentes and senha == gerentes[nome].get(list(gerentes[nome].keys())[0])

# As outras funções permanecem inalteradas ou podem ser ajustadas conforme necessário
