print('Bem-Vindo a Sorveteria do João Carlos de Farias Almeida')

print('--------------------------------------------CARDÁPIO-------------------------------------------')
print('| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |       R$ 6,00     |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Descrição Especiais  |       R$ 7,00     |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Descrição Premium    |       R$ 8,00     |      R$ 14,00      |      R$ 24,00      |')
print('-----------------------------------------------------------------------------------------------')

# Variável iniciadora total, valendo 0
total = 0

# Início da estrutura de repetição, enquanto for true, ela vai se repetir
while True:
    # Input para o usuário definir tamanho e sabor desejado
    tamanho = input('Entre com o TAMANHO do pote desejada (P/M/G): ')
    sabor = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')

    # Dict com sabores, nomes e tamanhos
    sabores = {'TR': {'nome': 'Tradicional', 'tamanhos': {'P': 6.00, 'M': 10.00, 'G': 18.00}},
               'ES': {'nome': 'Especial', 'tamanhos': {'P': 7.00, 'M': 12.00, 'G': 21.00}},
               'PR': {'nome': 'Premium', 'tamanhos': {'P': 8.00, 'M': 14.00, 'G': 24.00}}
               }

    # Lista de tamanhos e códigos de sabores para fazer a
    # verificação se a entrada do usuário é válida
    tamanhos = ['P', 'M', 'G']
    codigos_sabores = ['TR', 'ES', 'PR']

    # Verifica se a entrada do usuário em tamanhos e sabores é inválida
    # se for inválida, ele volta para o primeiro input
    # se não for inválido, ele mostra o sorvete e o valor selecionado
    if tamanho not in tamanhos or sabor not in codigos_sabores:
        print('!!!!! TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!')
        continue
    else:
        print(
            f"Você pediu um sorvete sabor {sabores[sabor]['nome']} {tamanho} de R$ {sabores[sabor]['tamanhos'][tamanho]:.2f}")
        print('---------------------------------------------------------')

    # Calcula a todos os valores de sorvetes escolhidos
    total = total + sabores[sabor]['tamanhos'][tamanho]

    # Pergunta se o usuário deseja pedir mais sorvetes
    deseja_pedir_mais = input('Deseja pedir mais alguma coisa? (S/N): ')

    # Verifica se a resposta é 'S' ou 'N' se não for nenhuma dessas duas
    # irá dar print como 'Resposta Inválida'

    # Caso o usuário selecione S ele repetirá
    # o código inteiro, senão, vai mostrar o valor total e finalizará o programa
    if deseja_pedir_mais not in ('S', 'N'):
        print('Resposta Inválida')
    if deseja_pedir_mais == 'S':
        continue
    else:
        print(f'O total a ser pago é: R$ {total:.2f}')
        break
