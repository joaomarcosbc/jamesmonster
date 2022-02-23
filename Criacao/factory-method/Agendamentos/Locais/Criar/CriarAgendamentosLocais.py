from CriarAgendamento import criar_agendamento

class CriarBarbearia(CriarAgendamento):
    """
    Agendar horario na barbearia
    """
    def criar_agendamento(self):
        return ListarBarbearia.mostrar_agendamento()


class CriarSalaodeBeleza(CriarAgendamento):
    """
    Agendar horario no salao
    """
    def criar_agendamento(self):
        return ListarSalaodeBeleza.mostrar_agendamento()


class CriarRestaurante(CriarAgendamento):
    """
    Agendar lugar no restaurante
    """
    def criar_agendamento(self):
        return ListarRestaurante.mostrar_agendamento()

