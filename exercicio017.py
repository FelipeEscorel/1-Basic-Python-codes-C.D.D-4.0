opcao = 1
while opcao != 2:
    negativos = 0
    for i in range(10):
        num = float(input("Digite um valor: "))
        if num < 0:
            negativos += 1
    print(f"Foram digitados {negativos} números negativos.\n")
    opcao = int(input("Deseja continuar? Digite 1 para sim e 2 para não: "))
