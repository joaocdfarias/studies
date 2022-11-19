quote = input('Digite ma frase: ')
quoteSize = len(quote)

halfQuote = quote[:quoteSize // 2]
print('Os dois últimos caractéres da metade da sua frase são:',
      halfQuote[-2:])
