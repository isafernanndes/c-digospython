import math

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))

cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa =  cateto_oposto**2 + cateto_adjacente**2
print('Comprimento do cateto oposto {} e do cateto adjacente {},'
      'Comprimento da hipotenusa: {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))
