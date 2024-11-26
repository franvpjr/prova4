def media():
    
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    numero3 = int(input('Digite o terceiro número: '))
    
    soma = numero1 + numero2 + numero3
    mediaarit = soma / 3
    return mediaarit

mediatotal = media()
print(f'A média dos números é {mediatotal}')