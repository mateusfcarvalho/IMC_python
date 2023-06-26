def calcImc(p, a):
    imc = p / (a * a)
    resultado = "Seu IMC é: %.2f\n" % imc

    if imc < 18.5:
        resultado += "Você está abaixo do peso!"
    elif imc >= 18.5 and imc <= 24.9:
        resultado += "Peso ideal!"
    elif imc >= 25.0 and imc <= 29.9:
        resultado += "Levemente acima do peso!"
    elif imc >= 30.0 and imc <= 34.9:
        resultado += "Obesidade grau I"
    elif imc >= 35.0 and imc <= 39.9:
        resultado += "Obesidade grau II! (severa)"
    else:
        resultado += "Obesidade grau III (mórbida)"

    return resultado

def runTests():
    test_cases = [
        {'weight': 50, 'height': 1.65, 'expected': "Seu IMC é: 18.37\nVocê está abaixo do peso!"},
        {'weight': 70, 'height': 1.75, 'expected': "Seu IMC é: 22.86\nPeso ideal!"},
        {'weight': 80, 'height': 1.70, 'expected': "Seu IMC é: 27.68\nLevemente acima do peso!"},
        {'weight': 90, 'height': 1.80, 'expected': "Seu IMC é: 27.78\nObesidade grau I"},
        {'weight': 100, 'height': 1.70, 'expected': "Seu IMC é: 34.60\nObesidade grau II! (severa)"},
        {'weight': 120, 'height': 1.80, 'expected': "Seu IMC é: 37.04\nObesidade grau III (mórbida)"}
    ]

    for case in test_cases:
        weight = case['weight']
        height = case['height']
        expected = case['expected']

        result = calcImc(weight, height)
        assert result == expected

        print(f"Test case passed. Weight: {weight}, Height: {height}, Expected: {expected}, Result: {result}")

if __name__ == "__main__":
    runTests()
