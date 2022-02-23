from abc import ABCMeta, abstractmethod

class ListarAgendamento(metaclass = ABCMeta):
    """
    Listar agendamentos
    """
    @abstractmethod
    def listar_agendamento(self):
        pass