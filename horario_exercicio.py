print("Primeira entrada \n")
hora1 = int(input("Digite a hora: "))
min1 = int(input("Digite os minutos: "))
print("Segunda entrada \n")
hora2 = int(input("Digite a hora: "))
min2 = int(input("Digite os minutos: "))

hora3 = hora1 + hora2
min3 = min1 + min2

if min3 >= 60:
    hora3 += 1
    min3 -= 60
else:
    pass

if hora3 <= 12:
    print(f"{hora3}:{min3}")

elif 12 < hora3 < 24:
    hora3 -= 12
    print(f"{hora3}:{min3}")

elif 24 <= hora3 < 36:
    hora3 -= 24
    print(f"{hora3}:{min3}")

elif 36 <= hora3 < 48:
    hora3 -= 36
    print(f"{hora3}:{min3}")

elif hora3 >= 48:
    hora3 -= 48
    print(f"{hora3}:{min3}")
else:
    pass
