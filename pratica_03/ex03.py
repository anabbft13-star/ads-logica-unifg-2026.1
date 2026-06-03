def calcular media(n1, n2):
    return (n1 + n2) /2

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = calcular_media(nota1, nota2)

print(f"Media: {media:.1f}")