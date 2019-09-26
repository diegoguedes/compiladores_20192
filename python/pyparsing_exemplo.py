from pyparsing import *

inteiro  = Word(nums)           
variavel = Word(alphas, max=1)   
op_aritmetico  = Word("+-*/", max=1)   
equacao = variavel + "=" + inteiro + op_aritmetico + inteiro
real = Combine(Word(nums) + '.' + Word(nums))
equacao_real = variavel + "=" + real + ZeroOrMore(op_aritmetico + real)

texto = "x = 2 + 3"
texto_real = "12.8"
texto_eq_real = "x = 2.3 + 4.5 * 3.2 / 4.3 * 3.1"
print equacao.parseString(texto)
print real.parseString(texto_real)
print equacao_real.parseString(texto_eq_real)

