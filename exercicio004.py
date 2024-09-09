nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"Média = {media}: Aluno aprovado.")
elif media >= 4:
    print(f"Média = {media}: Aluno em recuperação.")
else:
    print(f"Média = {media}: Aluno reprovado.")
