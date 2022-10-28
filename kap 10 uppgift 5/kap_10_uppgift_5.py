a=int(input('Skriv ett pris med heltal'))

if a<500:
    print('ditt nettopris blir', a, 'kr')
elif a<1000:
    print('ditt nettopris blir', a*0.98, 'kr vilket motsvarar en 2% rabbatt.')
else:
    print('ditt nettopris blir', a*0.95, 'kr vilket motsvarar en 5% rabbatt.')