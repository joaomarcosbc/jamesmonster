


if __name__ == '__main__':
    CriarAgendamento agendar = new CriarBarbearia()
    ListarBarbearia barbearia = agendar.criar_agendamento()
    barbearia.mostrar_agendamento()

    agendar = new CriarSalaodeBeleza()
    salao = agendar.criar_agendamento()
    salao.mostrar_agendamento()

    agendar = new CriarRestaurante()
    restaurante = agendar.criar_agendamento()
    restaurante.mostrar_agendamento()