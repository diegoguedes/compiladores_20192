# Introdução a Linguagem Python

## Funções built-in
Funções built-in estão automaticamente disponíveis e podem ser chamadas em todo lugar do nosso código.

## print
    print (value,...,sep=’ ’, end=’\n’)

- Abaixo está os três primeiros valores que a função print pode receber:
  - value é o valor que queremos imprimir, as reticências indicam que a função pode receber mais de um valor, basta separá-los por vírgula.
  - sep é o separador entre os valores, por padrão o separador é um espaço em branco.
  - end é o que acontecerá ao final da função, por padrão há uma quebra de linha, uma nova linha (\n).

## Tipo da variável
    type(variável) # Mostra qual o tipo da variável

## Comparando dois inteiros

    numero_secreto = 42

    chute = int(input("Digite o seu número: "))

    if (chute == 2):
      print("acertou")
      print("parabéns")
    else:
      print("errou")
      print("que pena!")

    print("fim do jogo")



## While 

    total_de_tentativas = 3
    numero_secreto = 1

    while (total_de_tentativas > 0):
        total_de_tentativas = total_de_tentativas - 1
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

    print("Fim do jogo")


## Formatar String

    dia_ini = 24
    dia_fim = 28
    mes = "fevereiro"
    ano = 2017

    print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))

## Laço for

    for rodada in range(1,10,2):
       print(rodada)

## Formatando número

    print("R$ {:.3f}".format(1.59))
    print("Data {:02d}/{:02d}".format(9, 4))

## Números aleatórios

    import random

    aletorio1 = int(round(random.random()*100))
    aletorio2 = int(round(random.randrange(0,10))) # aleatório de 0 a 9

    print("n1 {} e n2 {}".format(aletorio1,aletorio2))

## Função
É consenso utilizar a nomenclatura snake_case

    def nome_da_funcao(): 		#definindo a função nome_da_funcao

## Função main

    def jogar():
        # código omitido

    if (__name__ == "__main__"): 	#executa se o arquivo for o main
        jogar()

## Operações com Conjuntos

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    c = {1,2}
    d = {3,4}

    print (a) #imprimir conjunto
    a.add(5) #adicionando um elemento no conjunto
    print( a.union(b)) #união
    print(a.intersection(b)) #interseção
    print(a.difference(b)) #diferença
    print (a.symmetric_difference(b)) #diferença simétrica
    print (7 in a) #elemento pertence ao conjunto
    print (c.issubset(a)) #subconjunto
    print (a.issuperset(c)) #superconjunto
    print (c.isdisjoint(d)) #são disjuntos

## Passo recursivo de uma linguagem

    def passo_recursivo(linguagem):
        nova_linguagem = linguagem.copy()
        i=1

        print("Como a linguagem era antes: {}".format(nova_linguagem))
        for val in linguagem:
            nova_linguagem.add(val+"aa")
            nova_linguagem.add(val+"ab")
            nova_linguagem.add(val+"ba")
            nova_linguagem.add(val+"bb")
            print("Passo {}: {}".format(i,nova_linguagem))
            i += 1

        print("Como a linguagem ficou: {}".format(nova_linguagem))

        return nova_linguagem.copy()

    linguagem = {"aa","bb"} #base
    if (__name__ == "__main__"):
        linguagem = passo_recursivo(linguagem)
        linguagem = passo_recursivo(linguagem)
        linguagem = passo_recursivo(linguagem)

    print("A linguagem final ficou: {}".format(sorted(linguagem,key=len)))
    print("aa" in linguagem)
    print("bb" in linguagem)
    print("" in linguagem)


## Manipulando Strings

### Pegando substring
    meuNome = "DIEGO"
    letra = meuNome[3]
    substr = meuNome[2:5]
    print(letra)
    print(substr)

## Regular Expression (RegEx)

### Módulo RegEx
    import re
    
### Funções RegEx

|Função| Descrição |
|---|---|
| findall  | Returns a list containing all matches  | 
| search  |  Returns a **Match object** if there is a match anywhere in the string |  
| split  | Returns a list where the string has been split at each match  |  
| sub | Replaces one or many matches with a string|

### RegEx in Python
    import re

    txt = "Disciplina de Compiladores"
    x = re.search("^The.*Spain$", txt)
    
### Metacharacteres

| Caracter | Descrição | Exemplo|
|--- |--- |---|
|[]| A set of characters | "[a-m]" |
|\ | Signals a special sequence (can also be used to escape special characters)	| "\d" |
| . | 	Any character (except newline character) | "he..o"	|
| ^	| Starts with | "^hello"	|
| $	| Ends with | "world$"	|
| *	| Zero or more occurrences | "aix*"	|
| +	| One or more occurrences | "aix+"	|
| {} | Exactly the specified number of occurrences  |  "al{2}"	|
| \|	| Either or	| "falls\|stays"	|
| () | 	Capture and group	 |  |

### Sequencias Especiais
| Caracter | Descrição | Exemplo|
|--- |--- |---|
| \A |	Returns a match if the specified characters are at the beginning of the string | "\AThe"	|
| \b |	Returns a match where the specified characters are at the beginning or at the end of a word	| r"\bain" r"ain\b"	|
| \B |	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word | r"\Bain" r"ain\B"	|
| \d |	Returns a match where the string contains digits (numbers from 0-9)	| "\d"	|
| \D |	Returns a match where the string DOES NOT contain digits |	"\D"	|
| \s |	Returns a match where the string contains a white space character |	"\s"	|
| \S |	Returns a match where the string DOES NOT contain a white space character |	"\S"	|
| \w |	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) |	"\w"	|
| \W |	Returns a match where the string DOES NOT contain any word characters |	"\W" |
| \Z |	Returns a match if the specified characters are at the end of the string |	"Spain\Z" |



Documentação
https://docs.python.org/3/library/string.html#formatexamples
https://www.w3schools.com/python/python_regex.asp
