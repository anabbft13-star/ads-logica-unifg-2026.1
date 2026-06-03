def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total


print(calcular_total(50, 2))  # 90
print(calcular_total(100, 1)) #90
print(calcular_total(20, 5)) #90

