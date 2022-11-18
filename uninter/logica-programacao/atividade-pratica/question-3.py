def metragem_limpeza():
    print('\n---------------------- Menu 1 de 3 - Metragem Limpeza -----------------------\n')

    valor = 0  # Definicição do valor inicial

    while True:  # Cria estrutura de repetição
        try:  # Utiliza estrutura de try...except para validar se a entrada é do tipo inteiro
            metragem = int(input('Entre com a metragem da casa: '))
            if metragem < 30 or metragem > 700:
                print('Não aceitamos casas com metragem menor que 30m² ou maior que 700m²')
                continue
            if 30 <= metragem < 300:
                print('Será necessário um(a) funcionário(a) para a limpeza.')
                valor = 60 + 0.3 * metragem
            elif 300 <= metragem < 700:
                print('Serão necessários(as) dois (duas) funcionários(as) para a limpeza.')
                valor = 120 + 0.5 * metragem
            return valor  # retorna valor que satisfazer a condição
        except ValueError:
            print('--- INVÁLIDO! Insira um valor numérico ---')


def tipo_limpeza():
    print('\n----------------------- Menu 2 de 3 - Tipo de Limpeza -----------------------\n')
    valor = 0

    while True:  # Cria estrutura de repetição
        tipo = input('Qual o tipo de limpeza?\n'
                     'B - Limpeza Básica - Indicada para sujeiras semanais ou quinzenais\n'
                     'C - Limpeza Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras\n'
                     '>> ')

        if tipo == 'B':
            valor = 1.0
            print('Você selecionou: Limpeza Básica')
            break
        elif tipo == 'C':
            valor = 1.3
            print('Você selecionou: Limpeza Completa')
            break
        else:
            print('--- Opção INVÁLIDA ---')
            continue  # Caso tenha caído nessa condição, significa que a entrada não foi 
            # nem 'B' nem 'C', então irá rodar essa função novamente
    return valor


def adicional_limpeza():
    print('\n---------------------- Menu 3 de 3 - Adicional Limpeza ----------------------\n')
    valor = 0

    while True:  # Cria estrutura de repetição
        adicional = int(input('Deseja mais algum adicional?\n'
                              '0 - Não desejo mais nada (encerrar)\n'
                              '1 - Passar 10 peças de roupas - R$ 10.00\n'
                              '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n'
                              '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00\n'
                              '>>> '))

        adicionais = {0: {'preco': 0},  # Dict com adicionais e seus preços
                      1: {'preco': 10},
                      2: {'preco': 12},
                      3: {'preco': 20}}

        # Se o valor da entrada for igual a algum valor do dict, entrará em outra condicional
        # que verificará se o valor da entrada é igual a 0, se for, ele encerra a função
        # se não, ele fará o cálculo dos valores
        if adicionais.keys().__contains__(adicional):
            if adicional == 0:
                break
            else:
                valor = valor + adicionais[adicional]['preco']
        else:
            print('--- INVÁLIDO! Insira um valor entre 0 e 3')
            continue  # Caso tenha inserido um valor diferente de 0, 1, 2 e 3, ele irá rodar a função novamente
    return valor


def soma_valores():  # Função que irá executar todas as outras funções e fará o cálculo do total
    print('Bem-Vindo ao Programa de Serviços de Limpeza do João Carlos de Farias Almeida')
    print('*****************************************************************************')

    valor_metragem = metragem_limpeza()
    valor_tipo = tipo_limpeza()
    valor_adicional = adicional_limpeza()

    print(
        f'TOTAL: R$ {valor_metragem * valor_tipo + valor_adicional:.2f} '
        f'(metragem: {valor_metragem:.2f} * tipo: {valor_tipo:.2f} + adicional: {valor_adicional:.2f})')


soma_valores()
