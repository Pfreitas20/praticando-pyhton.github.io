# imc
from time import sleep
nm = str(input("Digite o seu nome: "))
id = int(input("digite sua idade: "))
pe = float(input("Digite seu peso em (Kg): "))
al = float(input("Digite sua altura em (M): "))
se = str(input("Digite seu sexo [M/F]: "))
imc = pe/al**2

if imc < 18.5:
    print("CUIDADO...")
    sleep(2)
    print("você está abaixo do peso ideal.")
elif imc < 24.9:
    print("PARABÉNS...")
    sleep(2)
    print("Você está no peso ideal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
elif imc < 34.9:
    print("CUIDADO...")
    sleep(2)
    print("Você está com obesidade-1")
elif imc < 39.9:
    print("CUIDADO...")
    sleep(2)
    print("Você está com obesidade-2")
else:
    print("Você está com obesidade GRAVE.")
