from ListarAgendamento import mostrar_agendamento

class ListarBarbearia(ListarAgendamento):
    """
    Agendar horario na barbearia
    """
    def mostrar_agendamento(self):
        print(f"Olá, seu agendamento na barbearia foi um sucesso")


class ListarSalaodeBeleza(ListarAgendamento):
    """
    Alugar horario no salao
    """
    def mostrar_agendamento(self):
        print(f"Olá, seu agendamento na barbearia foi um sucesso")
        


class ListarRestaurante(ListarAgendamento):
    """
    Alugar lugar no restaurante
    """
    def mostrar_agendamento(self):
        print(f"Olá, seu agendamento na barbearia foi um sucesso")
        

