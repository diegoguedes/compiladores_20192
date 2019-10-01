# simpleSQL.py
#
# Exemplo da biblioteca pyparsing da linguagem SQL
# Disponível em https://github.com/pyparsing/pyparsing/blob/master/examples/simpleSQL.py
# Copyright (c) 2003,2016, Paul McGuire
# Modificado pelo prof. Diego Guedes
#
from pyparsing import Word, delimitedList, Optional, \
    Group, alphas, alphanums, Forward, oneOf, quotedString, \
    infixNotation, opAssoc, \
    ZeroOrMore, restOfLine, CaselessKeyword, pyparsing_common as ppc

# definindo SQL tokens
selectStmt = Forward() # token de espaço reservado usado para definir padrões de token recursivos
SELECT, FROM, WHERE, AND, OR, IN, IS, NOT, NULL = map(CaselessKeyword,
                                                      "select from where and or in is not null".split())
NOT_NULL = NOT + NULL

ident          = Word( alphas, alphanums + "_$" ).setName("identificador")
columnName     = delimitedList(ident, ".", combine=True).setName("nome coluna") # delimitedList(expr, delim=',') - convenience function for matching one or more occurrences of expr, separated by delim
columnName.addParseAction(ppc.upcaseTokens) #  upcaseTokens  - converts all matched tokens to uppercase # addParseAction - faz a ação de transforma tudo em maiúsculo
columnNameList = Group( delimitedList(columnName))
tableName      = delimitedList(ident, ".", combine=True).setName("nome tabela")
tableName.addParseAction(ppc.upcaseTokens)
tableNameList  = Group(delimitedList(tableName))

binop = oneOf("= != < > >= <= eq ne lt le gt ge", caseless=True) # oneOf(string, caseless=False) - convenience function for quickly declaring an alternative set of Literal tokens, by splitting the given string on whitespace boundaries.
realNum = ppc.real()
intNum = ppc.signed_integer()

columnRval = realNum | intNum | quotedString | columnName # necessário para adicionar nas expressões algébricas
whereCondition = Group(
    ( columnName + binop + columnRval ) |
    ( columnName + IN + Group("(" + delimitedList( columnRval ) + ")" )) |
    ( columnName + IN + Group("(" + selectStmt + ")" )) |
    ( columnName + IS + (NULL | NOT_NULL))
)

whereExpression = infixNotation(whereCondition,
                                [
                                    (NOT, 1, opAssoc.RIGHT), # (expressão, número de termos, se o operador é associativo direito ou esquerdo)
                                    (AND, 2, opAssoc.LEFT), # whereCondition AND whereCondition , ou seja, whereCondition vai ficar do lado ESQUERDO do AND
                                    (OR, 2, opAssoc.LEFT),
                                ]) #infixNotation - função de conveniência para definir uma gramática para analisar expressões de notação de infixo com uma precedência hierárquica de operadores

# definindo a gramática
selectStmt <<= (SELECT + ('*' | columnNameList)("colunas") +
                FROM + tableNameList( "tabelas" ) +
                Optional(Group(WHERE + whereExpression), "")("where"))

simpleSQL = selectStmt

# definindo comentário no Oracle
oracleSqlComment = "--" + restOfLine
simpleSQL.ignore( oracleSqlComment )

if __name__ == "__main__":
    simpleSQL.runTests("""\

        # multiplas tabelas
        SELECT * from XYZZY, ABC

        # tabela com esquema
        select * from SYS.XYZZY

        Select A from Sys.dual

        Select A,B,C from Sys.dual

        Select A, B, C from Sys.dual, Table2

        # FAIL - palavra-chave SELECT inválida
        Xelect A, B, C from Sys.dual

        # FAIL - palavra-chave FROM inválida
        Select A, B, C frox Sys.dual

        # FAIL - declaração incompleta
        Select

        # FAIL - declaração incompleta
        Select * from

        # FAIL - column inválido
        Select &&& frox Sys.dual

        # cláusula where
        Select A from Sys.dual where a in ('RED','GREEN','BLUE')

        # cláusula where composta
        Select A from Sys.dual where a in ('RED','GREEN','BLUE') and b in (10,20,30)

        # cláusula where com operador de comparação
        Select A,b from table1,table2 where table1.id eq table2.id
        
        # where com consulta aninhada
        Select * from san.t002 where a in ( Select a from Sys.dual)
        
        # cláusula where composta
        Select A from Sys.dual where a in ('RED','GREEN','BLUE') and b in (10,20,30) and c = 3
        
         # cláusula where not
        Select A from Sys.dual Where NOT a = 2
        """)
