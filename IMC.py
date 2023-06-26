import sys

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

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python3 IMC.py <peso> <altura>")
        sys.exit(1)

    peso = float(sys.argv[1])
    altura = float(sys.argv[2])

    resultado = calcImc(peso, altura)
    print(resultado)
