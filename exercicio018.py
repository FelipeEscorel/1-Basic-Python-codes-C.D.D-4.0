repita = 1
while repita == 1:
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Nota inválida! Digite a primeira nota novamente: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Nota inválida! Digite a segunda nota novamente: "))

    media = (nota1 + nota2)/2
    print(f"A média do aluno é de {media}\n")
    repita = int(input("Deseja repetir o processo? Digite 1 para sim ou qualquer outro valor para não: "))
