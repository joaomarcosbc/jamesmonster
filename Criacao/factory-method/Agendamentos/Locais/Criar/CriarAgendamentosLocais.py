from criarAgendamento import criar_agendamento

class CriarBarbearia(CriarAgendamentos):
    """
    Agendar horario na barbearia
    """
    def criar_agendamento(self):
        return ListarBarbearia.mostrar_agendamento()


class CriarSalaodeBeleza(CriarAgendamentos):
    """
    Agendar horario no salao
    """
    def criar_agendamento(self):
        return ListarSalaodeBeleza.mostrar_agendamento()


class CriarRestaurante(CriarAgendamentos):
    """
    Agendar lugar no restaurante
    """
    def criar_agendamento(self):
        return ListarRestaurante.mostrar_agendamento()

