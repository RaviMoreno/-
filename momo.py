peso=float(input("Digite seu peso (em kg): "))
# "nsdclscd" -> string
# números inteiros -> int
# numeros quebrado -> float
# true/false -> bool
altura=float(input("Digite sua altura (em m): "))
#idade=int(input("Digite sua idade : "))
gênero=input("Diga seu sexo (F/M): ").lower()
#para gênero é preciso configurar o computador para entender que só podem ser aceitos dois gêneros

# +, -, *,/,**,//,% .


if gênero != "f" and gênero !="m":
    print(" Sexo inválido")




imc= peso/altura**2

if altura>3:
    print("Digite sua altura em metro")

if peso>1000:
    print("Digite seu peso em kg")

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
#  let indiceLinha = -1;
# (imc < 18.5) indiceLinha = 0;         // Abaixo do peso
 # (imc < 25) indiceLinha = 1;      // Peso normal
  #(imc < 30) indiceLinha = 2;      // Pré-obesidade
#  (imc < 35) indiceLinha = 3;      // Obesidade grau 1
 #(imc < 40) indiceLinha = 4;      // Obesidade grau 2
  #else indiceLinha = 5;                    // Obesidade grau 3

    