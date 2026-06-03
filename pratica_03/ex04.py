def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return"Reprovado"
    
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))

media = calcular_media(n1, n2)
situacao = verificar_situacao(media)

print(f"Media: {media:.1f}")
print(f"situacao: {situacao}")