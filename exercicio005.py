time1 = input("Digite o primeiro time do jogo em questão: ")
gol1 = int(input(f"Quantos gols o {time1} marcou? "))
time2 = input("Digite o segundo time: ")
gol2 = int(input(f"Quantos gols o {time2} marcou? "))

if gol1 > gol2:
    print(f"{time1} foi o vencedor com {gol1} gols contra {gol2} do {time2}")
elif gol1 < gol2:
    print(f"{time2} foi o vencedor com {gol2} gols contra {gol1} do {time1}")
else:
    print(f"{time1} e {time2} empataram ({gol1} x {gol2})")
