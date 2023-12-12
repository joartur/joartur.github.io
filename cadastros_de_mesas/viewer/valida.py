import re
import getpass

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
def check(email):  
  
    if(re.search(regex,email)):
        #verificar se está no dicionário  
        return True           
    else:  
       return False

def verificasenha():
    senha = getpass.getpass("Nova senha: ")
    senha2 = getpass.getpass("Por favor confirme a senha.\nSenha: ")
    if senha == senha2:
        print("Senha alterada com sucesso!")
        return True
    else:
        print("As senhas não são iguais.")
        return False

def validaEntrada(nome, senha):
    gerentes = {
        'kaliane': {'kaliane@gmail.com': 'amoGoiaba'},
        'daniel': {'daniel@gmail.com': '12345678'},
        'kaline': {'kaline@gmail.com': 'Qw78@.'},
        'joamerson': {'joamerson@gmail.com': 'senha'}
    }

    print("Nome de usuário fornecido:", nome)
    print("Nomes de usuário no dicionário:", gerentes.keys())

    # Verificar se o nome está no dicionário
    if nome in gerentes:
        # Obter o dicionário de credenciais do gerente
        credenciais_gerente = gerentes[nome]

        print("Credenciais do gerente:", credenciais_gerente)

        # Verificar se a senha está correta
        if senha == list(credenciais_gerente.values())[0]:
            return True
        else:
            print("Senha incorreta.")
            return False
    else:
        print("Nome de usuário não encontrado.")
        return False

    
def emailCadastrado(email):
    gerentes = {
        'Kaliane': {'kaliane@gmail.com': 'amoGoiaba'},
        'Daniel': {'daniel@gmail.com': '12345678'},
        'Kaline': {'kaline@gmail.com': 'Qw78@.'},
        'Joamerson': {'joamerson@gmail.com': 'senha'}
    }

    for dadosGerentes in gerentes.values():
        if email in dadosGerentes:
            return True

    print("O e-mail fornecido não está cadastrado.")
    return False

'''# Example usage:
nome_usuario = input("Nome de Usuário: ")
senha_usuario = input("Senha: ")

if validaEntrada(nome_usuario, senha_usuario):
    print("Acesso concedido.")
else:
    print("Acesso negado.")'''
