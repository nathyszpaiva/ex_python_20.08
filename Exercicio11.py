copias = int(input("Digiteo número de cópias: "))

if copias <= 10:
    valor = copias * 0.25
    print(f"Valor: {valor}")
if(copias > 10 and copias <=30):
    valor20 = (copias-10) * 0.20 +2.5
    print(f"Valor:{valor20}")

if(copias > 30):
    valor10 = (copias-30) * 0.10 + 6.5
    print(f"Valor:{valor10}")
