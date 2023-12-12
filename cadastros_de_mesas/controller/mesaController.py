from model.mesaModel import Mesa

class CadastrarMesa:
    @staticmethod
    def post(codigoGarcom, capacidade):
        mesa = Mesa(codigoGarcom, capacidade)
        mesa.inserir()

class AlterarMesa:
    @staticmethod
    def get(id, codigoGarcom):
        mesa = Mesa.buscar_por_id(id)
        mesa.setCodigoGarcom(codigoGarcom)
        mesa.alterar()

class ExcluirMesa:
    @staticmethod
    def get(id):
        mesa = Mesa.buscar_por_id(id)
        mesa.excluir()

class ListarMesa:
    @staticmethod
    def get():
        mesas = Mesa.listar()
        if mesas is not None:
            for mesa_info in mesas:
                print(f'ID_MESA: {mesa_info[0]}, CAPACIDADE: {mesa_info[1]}, GARÇOM_RESPONSÁVEL: {mesa_info[2]}')
            return mesas
        else:
            return []

class BuscarMesa:
    @staticmethod
    def get(id):
        mesa = Mesa.buscar_por_id(id)

        if mesa:
            return mesa
        else:
            # Se a mesa não for encontrada, retorne uma instância de Mesa com valores padrão
            return Mesa(None, None, None)


