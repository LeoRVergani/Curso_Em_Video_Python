preco = float(input('Qual é o preço do produto? R$ '))
desconto = preco*5/100
desconto = preco - desconto
print('Você vai pagar R$ {:.2f} e vamos descontar 5% que ficará no valor de R$ {:.2f}. '.format(preco,desconto))
print('O total que você vai pagar é R$ {:.2f}'.format(desconto))