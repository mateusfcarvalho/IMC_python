def calcImc(p, a):
    imc = p / (a * a)
    print("Seu IMC é: %.2f" % imc)
    print()

    if imc < 18.5:
        print("Você está abaixo do peso!")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso ideal!")
    elif imc >= 25.0 and imc <= 29.9:
        print("Levemente acima do peso!")
    elif imc >= 30.0 and imc <= 34.9:
        print("Obesidade grau I")
    elif imc >= 35.0 and imc <= 39.9:
        print("Obesidade grau II! (severa)")
    else:
        print("Obesidade grau III (mórbida)")

def calcImcUserInput():
    peso = float(input("Qual o seu peso: "))
    altura = float(input("Qual a sua altura (em metros): "))
    print()
    calcImc(peso, altura)

print("Calculadora de IMC em Python")
print()

calcImcUserInput()
