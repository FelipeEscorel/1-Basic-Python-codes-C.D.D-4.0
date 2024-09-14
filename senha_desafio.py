erros = 3
senha = 1417

senha2 = int(input("Digite sua senha: "))
erros -= 1
while senha!= senha2 and erros > 0:
    senha2 = int(input(f"Senha incorreta. Digite novamente sua senha (Tentativas restantes -> {erros}): "))
    erros -= 1
if senha == senha2:
    print("Saldo: R$ 50.000.00")
else:
    print("Acesso bloqueado.")