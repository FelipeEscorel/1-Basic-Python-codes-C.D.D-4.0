print("Digite a primeira entrada")
hora1 = int(input("Digite as horas: "))
min1 = int(input("Digite os minutos: "))
print("Digite a segunda entrada")
hora2 = int(input("Digite as horas: "))
min2 = int(input("Digite os minutos: "))

soma1 = hora1 + hora2
soma2 = min1 + min2

if soma1 > 12 and soma2 > 60:
    calc1 = soma1 - 12
    calc2 = soma2 - 60
    print(f"{calc1}:{calc2}")
elif soma1 > 12 or soma2 > 60:
    calc1 = soma1 - 12
    calc2 = soma2 - 60
    print(f"{calc1}:{calc2}")
elif soma1 <= 12 or soma2 < 60:
    print(f"{soma1}:{soma2}")
else:
    pass
