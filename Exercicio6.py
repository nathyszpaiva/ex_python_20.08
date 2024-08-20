nota = float(input("Digite uma nota entre 0 e 20: "))

# Verifica se a nota está dentro do intervalo permitido
if 0 <= nota <= 20:
    # Verifica se a nota é maior que 10
    if nota > 10:
        print("Nota validada.")
    else:
        print("Nota não validada.")
else:
    print("Nota inválida. A nota deve estar entre 0 e 20.")