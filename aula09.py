# Aula #09 - Manipulando Texto

''' fatiando as letras da frase.'''

frase = 'Curso em Vídeo Python' #21 carácteres
print(frase[3])
# mostrará a segunda letras da frase (sempre contando os espaços e uma casa a menos)

print(frase[:22])
# dois pontos = começo / 22 = fim (mostrar tudo)

print(len(frase.strip()))
# LEN = contar caractéres e espaços / strip = não contar os espaços

print(frase.count('o'))
#contar quantas vezes a letra O aparece

print(frase.upper())
#todas as letras da frase em MAIÚSCULO

print(frase.lower())
#todas as letras da frase em minúsculo

print(frase.replace('Python', 'Android'))
# replace = trocar (substituir um valor por outro)

print(frase.find('em'))
#procurar EM frase

print(frase.find('vídeo'))
# como a frase 'Vídeo' tem sua letra inicial maiúscula, find(vídeo) não irá funcionar, logo aparecerá -1 qnd der 'RUN'
# para rodar, precisaria conter o LOWER (frase.lower().find('video'))

print(frase.split())
#criará uma lista separando palavra por palavra

dividindo = frase.split()
print(dividindo[0])
#mostrará apenas a primeira palavra da frase, onde 0 é a primeira, 1 é a segunda, etc.

print("""Para mostrar o texto inteiro quebrando linha, Usar 3 aspas-duplas.
Espero lembrar desta anotação pois será extremamente importante durante
minha trajetória.""")

