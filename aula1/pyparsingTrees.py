import pyparsing

grammar = pyparsing.Forward()
grammar << pyparsing.Suppress("(") + pyparsing.Word("0123456789") + pyparsing.ZeroOrMore(grammar) + pyparsing.Suppress(")")

query = "(1 (2 (3)) (4 (5 (6) (7) (8))))"
print(grammar.parseString(query))
