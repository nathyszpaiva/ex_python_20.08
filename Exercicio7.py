m = float(input("Digite o primeiro número (m): "))
n = float(input("Digite o segundo número (n): "))
produto = m * n
if produto > 0:
    print("O produto é positivo.")
elif produto < 0:
    print("O produto é negativo.")
else:
    print("O produto é zero.")