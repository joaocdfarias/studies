def cadastrar_funcionario(id):
    print('--------------------------- Menu Cadastro ---------------------------')
    print(f'Código do funcionário: {id}')

    nome = input('Qual o nome do funcionário? ')
    setor = input('Qual o setor do funcionário? ')

    while True:
        try:
            salario = float(input('Qual o salário do funcionário? (R$) '))
            # retorna dicionario de cadastro quando o salário é digitado
            return {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
        except ValueError:
            print('O salário deve ser um valor numérico')  # Verifica se o salário é em valor numérico


# Função para buscar funcionários, foi criada para evitar repetição de código nas funções 
# que precisam de uma busca de funcionários. Ela recebe 3 parâmetros:
# funcionarios = é um dicionario com id, nome, setor e salario
# tipo_busca = vai ser o tipo da busca por funcionário ou seja, irá buscar por id ou nome ou salario
# valor = será a função que receberá o número digitado no menu
def buscar_funcionarios(funcionarios, tipo_busca, valor):
    retorno = []  # Lista iniciadora vazia, ela vai conter o retorno do que tiver em funcionario

    for funcionario in funcionarios:
        if funcionario[tipo_busca] == valor:  # Exemplo: se funcionário com chave 'id' for igual o valor do id digitado
            # então seu retornoo vai ser colocado dentro da array retorno, que logo será retornada pela função
            retorno.append(funcionario)
    return retorno


def consultar_funcionarios(funcionarios):
    print('--------------------------- Menu Consulta ---------------------------')

    # Função para mostrar as informações dos funcionários, foi crida para
    # evitar repetição de código
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
                if not funcionarios:  # Caso não tenha funcionários no dicionário
                    print('Não há funcionários cadastrados')
                else:
                    for funcionario in funcionarios:
                        informacoes_funcionario(funcionario)  # Este loop retornará todos os funcionários cadastrados
                        # e irá rodar a função informacoes_funcionario em todos os funcionários cadastrados.
            elif consulta == 2:
                id_funcionario = int(input('Digite o ID do funcionário: '))
                resultado = buscar_funcionarios(funcionarios, 'id', id_funcionario)  # Essa lista vai conter uma busca
                # de funcionários, re

                if not funcionarios:  # Caso não tenha funcionários no dicionário
                    print('Não há funcionário com este ID')
                else:
                    for funcionario in resultado:
                        informacoes_funcionario(funcionario)  # Irá mostrar informações do funcionário consultado por 
                        # id no loop. Não precisaria ser necessariamente um loop, já que o ID é único, pois, sempre irá  
                        # retornar a lista de index 0
            elif consulta == 3:
                setor_funcionario = input('Digite o SETOR do funcionário: ')
                resultado = buscar_funcionarios(funcionarios, 'setor', setor_funcionario)

                if not funcionarios:  # Caso não tenha funcionários no dicionário
                    print('Não há funcionários neste setor')
                else:
                    for funcionario in resultado:
                        informacoes_funcionario(funcionario)  # Irá mostrar todos os funcionários do setor selecionado
                        # no menu
            elif consulta == 4:  # Irá voltar para o menu principal caso não tenha a opção escolhida
                break
            else:
                print('Valor inválido! Selecione de 1 a 4')
                continue  # Irá repetir a função caso tenha escolhido um valor diferente de 1, 2, 3 e 4
            break
        except ValueError:
            print('Use somente números para navegar pelo Menu')  # Caso tenha escolhido um valor não numérico


def remover_funcionarios(funcionarios):
    print('--------------------------- Menu Remover ----------------------------')
    remover = int(input('Digite o ID do funcionário a ser removido: '))

    resultado = buscar_funcionarios(funcionarios, 'id', remover)  # Lista com o funcionário selecioado através do input

    if not funcionarios:  # caso não tenha funcionários
        print('Não há funcionários com este ID')
    else:  # se houver funcionários vai rodar o loop e o selcionado será removido da lista de funcionarios
        for funcionario in resultado:
            funcionarios.remove(funcionario)
            print('Funcionário removido')


def main():
    print('Bem-Vindo ao Controle de Funcionários do João Carlos de Farias Almeida')

    funcionarios = []  # Lista iniciadora vazia
    counter = 0  # contador iniciando em 0

    while True:
        print('**********************************************************************\n')
        print('--------------------------- Menu Principal ---------------------------')

        menu = int(input('1 - Cadastrar Funcionário\n'
                         '2 - Consultar Funcionário(s)\n'
                         '3 - Remover Funcionário\n'
                         '4 - Sair\n'
                         '>>> '))
        # Se a opção 1 for escolhida, irá rodar a função cadastrar_funcionario com o contador sendo passado no 
        # parâmetro no id, isso garantirá que o ID nunca será igual
        if menu == 1:
            funcionarios.append(cadastrar_funcionario(counter))
            counter = counter + 1  # contador iniciará em 0, depois será auto incrementado com +1
        elif menu == 2:  # se escolhida a opção 2, irá rodar a função consultar_funcionarios, com a array de 
            # funcionarios sendo passada no parâmetro
            consultar_funcionarios(funcionarios)
        elif menu == 3:  # caso escolhida a opção 3 irá rodar a função remover_funcionarios passando a array de 
            # funcionarios no parâmetro da função
            remover_funcionarios(funcionarios)
        elif menu == 4:  # se escolhida a opção 4 irá finalizar a função principal de menu
            break
        else:
            print('Opção inválida, selecione de 1 a 4')  # caso seja escolhida uma opção diferente de 1, 2, 3 e 4


main()
