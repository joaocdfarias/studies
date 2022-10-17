productPrice = float(input('Preço do produto: '))
productDiscount = float(input('Desconto do produto: '))

discount = productPrice * (productDiscount / 100)
finalPrice = productPrice - discount
print(f'O preço do produto é R$ {productPrice}. Desconto é {productDiscount}%. Preço final é R$ {finalPrice}')
