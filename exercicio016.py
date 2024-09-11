i = 0
soma = 0

alunos = int(input("Digite quantos alunos tem na turma: "))

while i < alunos:
    num = float(input("Digite um valor: "))
    soma = soma + num
    i += 1
media = soma/alunos
print(f"A média dos alunos é {media}")
