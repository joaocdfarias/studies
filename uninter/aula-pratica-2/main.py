# O somatório dos 5 primeiros números inteiros e positivos
firstPositiveNumbers = [1, 2, 3, 4, 5]

sumOfFirstPositiveNumbers = 0
for number in firstPositiveNumbers:
    sumOfFirstPositiveNumbers = sumOfFirstPositiveNumbers + number
print('Soma:', sumOfFirstPositiveNumbers)

# -----------------------------------------------------------------
# A média entre 23, 19 e 31
numbers = [23, 19, 31]

averageNumber = 0
for number in numbers:
    averageNumber = (averageNumber + number)
print('Média:', averageNumber / len(numbers))

# -----------------------------------------------------------------
# O número de vezes que 73 cabe em 403
print('Número de vezes que 73 cabe em 403:', 403 // 73)

# -----------------------------------------------------------------
# A sobra quando 403 é dividido por 73
print('Sobra divisão entre 403 e 73:', 403 % 73)

# -----------------------------------------------------------------
# 2 elevado à 10ª potência

print('2¹⁰:', 2 ** 10)

# -----------------------------------------------------------------
# O valor absoluto da diferença entre 54 e 57
absoluteValue = abs(54 - 57)
print('Valor absoluto:', absoluteValue)

# -----------------------------------------------------------------
# O menor valor entre 34, 29 e 31
smallerValue = [34, 29, 31]
print('Menor valor:', min(smallerValue))
# -----------------------------------------------------------------
a = 3
b = 4
c = a * a + b * b
print('Operação:', c)

# -----------------------------------------------------------------
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1 + ' ' + s2 + ' ' + s3)
print(10 * (s1 + ' '))
print(s1 + ' ' + (2 * (s2 + ' ')) + (3 * (s3 + ' ')))
print(7 * (s1 + ' ' + s2 + ' '))
print(5 * (s2 * 2 + s3 + ' '))
