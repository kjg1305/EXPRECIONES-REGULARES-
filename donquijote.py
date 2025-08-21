import re 
with open ('el_quijote.txt','r',encoding='Latin-1') as file :
    texto = file.read()

años = re.findall(r'\b\d{4}\b', texto)
palabras_de_6_letras = re.findall(r'\b\w{6}\b',texto)

print (f' se encontraron {len(años) } años')
print(' los primeros 100 años encontrados fueron :' , años[:100])
print(f' se encontraron {len(palabras_de_6_letras)} palabras con 6 letras ')
print(' las primeras 300 palabras encontradas con 6 letras fueron:' , palabras_de_6_letras[:300])