# Print para dar boas-vindas à loja
print('Bem-vindo a Loja do João Carlos de Farias Almeida')

# Input solicitando valor unitário de um produto
valorUnitario = float(input('Entre com o valor do produto: '))

# Input solicitando quantidade de produtos
quantidade = int(input('Entre com o valor da quantidade: '))

# Cálculo do valor sem o frete
valorSemFrete = valorUnitario * quantidade
print(f'O valor sem frete foi: R$ {valorSemFrete:.2f}') # Print do valor sem frete

# Variável com valor do frete fora das condicionais
valorFrete = 0

# Verificação se a quantidade é igual ou maior que 0 e menor que 11, se for verdadeiro
# então o frete é de R$ 30.00
if 0 <= quantidade < 11:
    valorFrete = 30; # Modifica o valor da variável valorFrete para 30
    print(f'O valor com frete foi: R$ {(valorUnitario * quantidade) + valorFrete:.2f} (frete de R$ {valorFrete:.2f})')
elif 11 <= quantidade < 101:
    valorFrete = 60; # Modifica o valor da variável valorFrete para 60
    print(f'O valor com frete foi: R$ {(valorUnitario * quantidade) + valorFrete:.2f} (frete de R$ {valorFrete:.2f})')
elif 101 <= quantidade < 1001:
    valorFrete = 120; # Modifica o valor da variável valorFrete para 120
    print(f'O valor com frete foi: R$ {(valorUnitario * quantidade) + valorFrete:.2f} (frete de R$ {valorFrete:.2f})')
elif quantidade >= 1001:
    valorFrete = 240; # Modifica o valor da variável valorFrete para 240
    print(f'O valor com frete foi: R$ {(valorUnitario * quantidade) + valorFrete:.2f} (frete de R$ {valorFrete:.2f})')
