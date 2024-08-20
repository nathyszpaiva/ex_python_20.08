quantidade_fotocopias = int(input("Digite a quantidade de fotocópias realizadas: "))

if quantidade_fotocopias <= 10:
    custo_total = quantidade_fotocopias * 0.25
elif quantidade_fotocopias <= 30:
    custo_total = 10 * 0.25 + (quantidade_fotocopias - 10) * 0.20
else:
    custo_total = 10 * 0.25 + 20 * 0.20 + (quantidade_fotocopias - 30) * 0.10

print(f"O custo total das fotocópias é R$ {custo_total:.2f}.")