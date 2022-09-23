mot = 'allo'
autre_mot = 'a'
autre_mot += 'l'

liste = [i if i in autre_mot else '-' for i in mot]


print(''.join(liste))