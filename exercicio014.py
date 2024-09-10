soma = 0

for i in range(0,10,1):
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        soma = soma + num
print(soma)
