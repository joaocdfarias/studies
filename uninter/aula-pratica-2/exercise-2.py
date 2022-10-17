kmsTraveled = float(input('Quantidade de KMs percorridos: '))
daysWithCar = float(input('Quantidade de dias com o carro: '))

pricePerDay = 60
pricePerKm = 0.15

finalPrice = pricePerDay * daysWithCar + pricePerKm * kmsTraveled

print(
    f'Você viajou {kmsTraveled} KMs e ficou {daysWithCar} dias com o carro. O custo da sua viajem foi {finalPrice}'
)
