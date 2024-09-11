i = 0
nota2 = 0

alunos = int(input("Digite quantos alunos tem na turma: "))

while i < alunos:
    nota = float(input("Digite um valor: "))
    nota2 = nota2 + nota
    i += 1
media = nota2/alunos
print(f"A média dos alunos é {media}")
