peso=float(input("Digite seu peso (em kg): "))
altura=float(input("Digite sua altura (em m): "))
#idade=int(input("Digite sua idade : "))
#gênero=input("Diga seu sexo (F/M): ").lower()

if altura>3:
    print("Digite sua altura em metro")

if peso>1000:
    print("Digite seu peso em kg")

#if gênero != "f" and gênero !="m":
    #print(" Sexo inválido")

imc= peso/altura**2


if imc<18.5:
    print("Abaixo do peso")

elif imc<25:
    print("Peso normal")
elif imc<30:
    print("Pré obesidade")
elif imc<35:
    print("Obesidade nível 1")
elif imc<40:
    print("Obesidade nível 2")
else:
    print("Obesidade nível 3")


    