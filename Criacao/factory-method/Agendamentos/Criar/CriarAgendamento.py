from abc import ABCMeta, abstractmethod

class CriarAgendamento(metaclass = ABCMeta):
    """
    Criar agendamentos
    """
    @abstractmethod
    def criar_agendamento(self):
        pass