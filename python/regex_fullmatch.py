import re

texto = "ab,aaa,ababa,ababaaaaa,ababbbb,ababab"
padrao = "(ab)*|a*"
texto_separado = re.split("\W+",texto)

for palavra in texto_separado:
    resposta = re.fullmatch(padrao,palavra)
    
    if(resposta is None):
        print("{} não pertence a linguagem".format(palavra))
    else:
        print("{} pertence a linguagem".format(palavra))

