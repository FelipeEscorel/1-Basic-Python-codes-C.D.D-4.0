i = 0
soma = 0

alunos = int(input("Digite quantos alunos tem na turma: "))

while i < alunos:
    nota = float(input("Digite um valor: "))
    soma = soma + nota
    i += 1
media = soma/alunos
print(f"A média dos alunos é {media}")
