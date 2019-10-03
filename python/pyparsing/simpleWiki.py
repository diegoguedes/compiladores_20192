# simpleWiki.py
#
# Exemplo da biblioteca pyparsing para converter um texto wiki para HTML
# Disponível em https://github.com/pyparsing/pyparsing/blob/master/examples/simpleWiki.py
# Copyright (c) 2003,2016, Paul McGuire
# Modificado pelo prof. Diego Guedes
#
from pyparsing import *

wikiInput = """
Aqui é um entrada simples de Wiki:
  *Isso é itálico.*
  **Isso é negrito!**
  ***Isso é negrito e itálico!***
  Aqui está uma URL para {{Página Wiki da Pyparsing->https://site-closed.wikispaces.com}}
"""

def convertToHTML(opening,closing):
    def conversionParseAction(original,posicao_inicio,tokens): #declaração de função de função
        return opening + tokens[0] + closing
    return conversionParseAction

def convertToHTML_URL(s,l,t):
    try:
        text,url=t[0].split("->")
    except ValueError:
        raise ParseFatalException(s,l,"invalid URL link reference: " + t[0])
    return '<A href="{0}">{1}</A>'.format(url, text)


# setParseAction (*funcao) - especifica uma ou mais funções para chamar após a correspondência bem-sucedida do elemento;
#  cada função é definida como fn (s, loc, toks), em que:
# - s é a sequência de análise original
# - loc é o local na string em que a correspondência começou
# - toks é a lista dos tokens correspondentes, compactados como um objeto ParseResults
italicized = QuotedString("*").setParseAction(convertToHTML("<I>","</I>")) # QuotedString é usada para pegar a String que começa com * e termina com *
bolded = QuotedString("**").setParseAction(convertToHTML("<B>","</B>"))
boldItalicized = QuotedString("***").setParseAction(convertToHTML("<B><I>","</I></B>"))

urlRef = QuotedString("{{",endQuoteChar="}}").setParseAction(convertToHTML_URL) # Inicia com {{ e termina com }}

wikiMarkup = urlRef | boldItalicized | bolded | italicized

print(wikiInput)
print()
print(wikiMarkup.transformString(wikiInput))
