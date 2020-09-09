# Source file
source = 'guardian.txt'
print('1.- Crea el fichero ' + str(source))

s = open(source, 'w', encoding='utf-8')

text = 'Pero lo que más me gustaba de aquel museo era que todo estaba siempre en el mismo sitio. No cambiaba nada. ' \
       'Podías ir cien mil veces distintas y el esquimal seguía pescando, y los pájaros seguían volando hacia el sur,' \
       ' y los ciervos seguían bebiendo en las charcas con esas patas tan finas y tan bonitas que tenían, y la india' \
       ' del pecho al aire seguía tejiendo su manta.'

print('2.- Escribe contenido en el fichero ' + str(source))
s.write(text)

print('3.- Cierra el fichero ' + str(source))
s.close

print('4.- Abre el fichero de nuevo ' + str(source) + ' y lo lee')
s = open(source, 'r', encoding='utf-8')
texto = s.read()
s.close

print('5.- Busca las frases')

frases = dict()
cuantas = 0

start = texto.find('seguía')

while start >= 0:

       frase = str()
       caracter = texto[start]
       while caracter not in [',', '.']:
              frase += caracter
              start += 1
              caracter = texto[start]

       cuantas += 1
       frases['frase ' + str(cuantas)] = frase
       start = texto.find('seguía', start)

output = 'seguia.txt'
print('6.- Crea el nuevo fichero: ' + output)
out = open(output, 'w', encoding='utf-8')

for frase in frases:
       out.write(frase + ': ' + frases[frase] + '\n')

out.close()








