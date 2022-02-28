import math

def Bhaskara(a, b , c):
    delta = (math.pow(b, 2)) - (4 * a * c)
    
    if a == 0:
        print('\nO valor de A deve ser diferente de 0')
    elif delta < 0:
        print('\nSem raizes reais')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    
    print('\nValor de x1: {0}'.format(x1))
    print('Valor de x2: {0}'.format(x2))

if __name__ == '__main__':
    while True:
        print('Calculando as raízes de uma equação de 2º grau\n')
        
        a = float(input('Digite um valor para A: '))
        b = float(input('Digite um valor para B: '))
        c = float(input('Digite um valor para C: '))
        
        Bhaskara(a, b, c)

        continua = input('\nDeseja sair? Digite q ou Enter para um novo cálculo: \n')
        if (continua == 'q'):
            break
