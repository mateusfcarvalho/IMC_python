def calcImc(p, a):
    imc = p / (a * a)
    resultado = "Seu IMC é: %.2f" % imc

    if imc < 18.5:
        resultado += "\nVocê está abaixo do peso!"
    elif imc >= 18.5 and imc <= 24.9:
        resultado += "\nPeso ideal!"
    elif imc >= 25.0 and imc <= 29.9:
        resultado += "\nLevemente acima do peso!"
    elif imc >= 30.0 and imc <= 34.9:
        resultado += "\nObesidade grau I"
    elif imc >= 35.0 and imc <= 39.9:
        resultado += "\nObesidade grau II! (severa)"
    else:
        resultado += "\nObesidade grau III (mórbida)"

    return resultado

def calcImcUserInput():
    peso = float(input("Qual o seu peso: "))
    altura = float(input("Qual a sua altura (em metros): "))
    print()
    resultado = calcImc(peso, altura)
    print(resultado)

print("Calculadora de IMC em Python")
print()

calcImcUserInput()
