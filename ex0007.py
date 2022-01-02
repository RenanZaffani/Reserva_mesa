print('Olá, sou um programa de reservas! Irei te ajudar da melhor forma possível.')

name = str(input('A reserva deve ser feita no nome de: ')).capitalize().strip()
idade = str(input('Você é maior de idade? [S/N] ')).capitalize().strip()
while idade == 'N':
    print('Menores de idade não podem reservar! Peça ao seu responsável que o faça.')
    name = str(input('A reserva deve ser feita no nome de: ')).capitalize().strip()
    idade = str(input("Você é maior de idade? [S/N] ")).capitalize().strip()

print('Cada mesa só comporta quatro pessoas! Se necessário, reserve mais de uma mesa.')

pessoas = int(input('Quantidade de pessoas para a reserva: '))
while pessoas < 1 or pessoas > 120:
    print('Digite um valor válido!')
    pessoas = int(input('Quantidade de pessoas para a reserva: '))

mesa = 0
if pessoas <= 4:
    print('Você precisará de 1 mesa.')
if pessoas > 4:
    mesa = (pessoas % 4) + 1
    print(f'Você precisará de {mesa} mesas.')

print('Para confirmar a idade, será pedido o documento no estabelecimento.')
price = pessoas * 30
npgt = int(input('Quantos menores de 12 anos irão? '))
while npgt > pessoas - 1:
    print('Digite um valor válido.')
    npgt = int(input('Quantos menores de 12 anos irão? '))
price = price - (npgt * 30)
mpgt = int(input('Quantos maiores de 12 e menores de 18 irão? '))
while mpgt > pessoas - 1:
    print('Digite um valor válido.')
    mpgt = int(input('Quantos maiores de 12 e menores de 18 irão? '))
price = price - (mpgt * 15)

print(f'O valor total ficou em R${price}.')
print(f'Ficou reservado {mesa} mesa(s) e o valor de R${price}.')
confirm = str(input('Podemos confirmar? [S/N] ')).strip().capitalize()
if confirm == 'S':
    print('Ok, confirmado.')
    print(f'Te aguardamos ansiosamente, {name}.')
elif confirm == 'N':
    print('Ok, cancelado.')
else:
    print('Digite um valor válido.')
    while confirm != 'S' and confirm != 'N':
        confirm = str(input('Podemos confirmar? [S/N] ')).strip().capitalize()

print('Tenha um bom dia!')
