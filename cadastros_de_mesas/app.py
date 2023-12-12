from flask import Flask, render_template, request, redirect, url_for, session
import getpass
from viewer.valida import validaEntrada, verificasenha, emailCadastrado
from controller.mesaController import CadastrarMesa, ExcluirMesa, BuscarMesa, ListarMesa, AlterarMesa

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Defina uma chave secreta para a sessão

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validaEntrada(username, password):
            session['username'] = username  # Armazena 'username' na sessão
            return redirect(url_for('gerenciamento_mesas'))
        else:
            error_message = "Usuário ou senha incorretos. Tente novamente."

    return render_template('login.html', error_message=error_message)

@app.route('/gerenciamento-mesas', methods=['GET', 'POST'])
def gerenciamento_mesas():
    # Recupera 'username' da sessão
    username = session.get('username')

    if not username:
        # Redireciona para a página de login se 'username' não estiver na sessão
        return redirect(url_for('login'))

    if request.method == 'POST':
        escolha = request.form['escolha']
        try:
            if escolha == '1':
                # Lógica para cadastrar mesa aqui
                return render_template('gerenciamento_mesas.html', username=username, message="Mesa cadastrada com sucesso!")

            if escolha == '2':
                # Lógica para alterar mesa aqui
                return render_template('gerenciamento_mesas.html', username=username, message="Update realizado com sucesso!")

            # Adicione outras opções conforme necessário

        except IndexError:
            message = "Mesa não encontrada no banco de dados."
        except ValueError:
            message = "Por favor, insira um ID de mesa válido (número inteiro)."

        return render_template('gerenciamento_mesas.html', username=username, message=message)

    return render_template('gerenciamento_mesas.html', username=username)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_mesa():
    # Recupera 'username' da sessão
    username = session.get('username')

    if not username:
        # Redireciona para a página de login se 'username' não estiver na sessão
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        qtdMesa = request.form['qtdMesa']
        idGarcom = request.form['idGarcom']

        try:
            CadastrarMesa.post(idGarcom, qtdMesa)
            message = 'Mesa cadastrada com sucesso!'
            return render_template('success.html', message=message)
        except Exception as e:
            # Redirecione para o template de erro em caso de exceção
            return render_template('error.html', error_message=str(e))

    return render_template('cadastrar.html')


@app.route('/alterar', methods=['GET', 'POST'])
def alterar_mesa():
    # Recupera 'username' da sessão
    username = session.get('username')

    if not username:
        # Redireciona para a página de login se 'username' não estiver na sessão
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            idMesa = request.form['idMesa']
            idGarcom = request.form['idGarcom']

            # Adicione sua lógica para alterar a mesa com os novos dados
            AlterarMesa.get(idMesa, idGarcom)

            return render_template('success.html', message='Mesa alterada com sucesso!')
        except Exception as e:
            return render_template('error.html', error_message=str(e))

    return render_template('alterar.html')


@app.route('/listar')
def listar_mesas():
    # Recupera 'username' da sessão
    username = session.get('username')

    if not username:
        # Redireciona para a página de login se 'username' não estiver na sessão
        return redirect(url_for('login'))
    
    try:
        mesas = ListarMesa.get()

        # Verificar se há mesas antes de renderizar o template
        if mesas:
            return render_template('listar.html', mesas=mesas)
        else:
            raise Exception("Nenhuma mesa encontrada no banco de dados.")

    except Exception as e:
        return render_template('error.html', error_message=str(e))

    

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_mesa():
    # Recupera 'username' da sessão
    username = session.get('username')

    if not username:
        # Redireciona para a página de login se 'username' não estiver na sessão
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        idMesa = request.form['idMesa']
        mesa = BuscarMesa.get(idMesa)

        # Verifica se a mesa foi encontrada
        if mesa:
            return render_template('buscar.html', mesa_id=mesa.getId(), capacidade=mesa.getCapacidade(), garcom_responsavel=mesa.getCodigoGarcom())
        else:
            return render_template('buscar.html', not_found=True)

    return render_template('buscar_form.html')


@app.route('/deletar', methods=['GET', 'POST'])
def deletar_mesa():
    # Recupera 'username' da sessão
    username = session.get('username')

    if not username:
        # Redireciona para a página de login se 'username' não estiver na sessão
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            idMesa = request.form['idMesa']
            
            # Verificar se a mesa com o ID fornecido existe antes de tentar excluí-la
            mesa_existente = BuscarMesa.get(idMesa)
            
            if mesa_existente:
                ExcluirMesa.get(idMesa)
                return render_template('success.html', message='Mesa deletada com sucesso!')
            else:
                raise Exception("Mesa não encontrada no banco de dados.")

        except Exception as e:
            return render_template('error.html', error_message=str(e))

    return render_template('deletar.html')



@app.route('/logout')
def logout():

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)