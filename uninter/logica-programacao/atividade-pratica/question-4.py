def cadastrar_funcionario(id):
    print('--------------------------- Menu Cadastro ---------------------------')
    print(f'Código do funcionário: {id}')

    nome = input('Qual o nome do funcionário? ')
    setor = input('Qual o setor do funcionário? ')

    while True:
        try:
            salario = float(input('Qual o salário do funcionário? (R$)'))
            break
        except ValueError:
            print('O salário deve ser um valor numérico')

    funcionario = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    return funcionario


def buscar_funcionarios(funcionarios, tipo_busca, valor):
    retorno = []

    for funcionario in funcionarios:
        if funcionario[tipo_busca] == valor:
            retorno.append(funcionario)
    return retorno


def consultar_funcionarios(funcionarios):
    print('--------------------------- Menu Consulta ---------------------------')

    def informacoes_funcionario(info):
        print(f'ID: {info["id"]}')
        print(f'Nome: {info["nome"]}')
        print(f'Setor: {info["setor"]}')
        print(f'Salário: R$ {info["salario"]:.2f}')

    while True:
        try:
            consulta = int(input('Escolha a opção desejada:\n'
                                 '1 - Consultar TODOS os funcionários\n'
                                 '2 - Consultar funcionários por ID\n'
                                 '3 - Consultar funcionários por SETOR\n'
                                 '4 - Retornar\n'
                                 '>>> '))
            if consulta == 1:
                if not funcionarios:
                    print('Não há funcionários cadastrados')
                else:
                    for funcionario in funcionarios:
                        informacoes_funcionario(funcionario)
            elif consulta == 2:
                id_funcionario = int(input('Digite o ID do funcionário: '))
                resultado = buscar_funcionarios(funcionarios, 'id', id_funcionario)

                if not funcionarios:
                    print('Não há funcionário com este ID')
                else:
                    for funcionario in resultado:
                        informacoes_funcionario(funcionario)
            elif consulta == 3:
                setor_funcionario = input('Digite o SETOR do funcionário: ')
                resultado = buscar_funcionarios(funcionarios, 'setor', setor_funcionario)

                if not funcionarios:
                    print('Não há funcionários neste setor')
                else:
                    for funcionario in resultado:
                        informacoes_funcionario(funcionario)
            elif consulta == 4:
                break
            else:
                print('Valor inválido! Selecione de 1 a 4')
                continue
            break
        except ValueError:
            print('Use somente números para navegar pelo Menu')


def remover_funcionarios(funcionarios):
    print('--------------------------- Menu Remover ----------------------------')
    remover = int(input('Digite o ID do funcionário a ser removido: '))

    resultado = buscar_funcionarios(funcionarios, 'id', remover)

    if not funcionarios:
        print('Não há funcionários com este ID')
    else:
        for funcionario in resultado:
            funcionarios.remove(funcionario)
            print('Funcionário removido')


def main():
    print('Bem-Vindo ao Controle de Funcionários do João Carlos de Farias Almeida')

    funcionarios = []
    counter = 0

    while True:
        print('**********************************************************************\n')
        print('--------------------------- Menu Principal ---------------------------')

        menu = int(input('1 - Cadastrar Funcionário\n'
                         '2 - Consultar Funcionário(s)\n'
                         '3 - Remover Funcionário\n'
                         '4 - Sair\n'
                         '>>> '))

        if menu == 1:
            funcionarios.append(cadastrar_funcionario(counter))
            counter = counter + 1
        elif menu == 2:
            consultar_funcionarios(funcionarios)
        elif menu == 3:
            remover_funcionarios(funcionarios)
        elif menu == 4:
            break
        else:
            print('Opção inválida, selecione de 1 a 4')


main()
