real = float(input('Quanto de dinheiro você quer trocar? R$ \n'))
dolar = real * 0.20
print('Com R${:.2f} você pode comprar U${:.2f}.'.format(real, dolar))