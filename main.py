#        brancas      pretas    
# e4  == P4R     ou   P5R
# Cc3 == C3BD    ou   C6BD
# Th2 == T2TR

# notação algebrica
# peça*/ coluna / linha
# *omitido se for um peão

# notação descritiva
# peça / linha / coluna

#peças
# igual menos o peão

# colunas 
# a = TD
# b = CD 
# c = BD
# d = D
# e = R
# f = BR
# g = CR
# h = TR

# linhas
# se branco = notação algebrica (na)
# se preto = 9 - na

colunas = {"TD" : "a", 
           "CD" : "b", 
           "BD" : "c", 
           "D"  : "d",
           "R"  : "e",
           "BR" : "f",
           "CR" : "g",
           "TR" : "h"
           }

def obtem_linha_algebrica(eh_branco, linha_descritiva):
    if eh_branco:
        linha_algebrica = linha_descritiva
    else:
        linha_algebrica = 9 - linha_descritiva
    return linha_algebrica

def obtem_peca_algebrica(peca_descritiva):
    peca_algebrica = peca_descritiva if peca_descritiva != 'P' else ' '
    return peca_algebrica
    
while True:
    eh_branco = input('movimento das brancas? \n')
    notacao_descritiva = input('digite a notação: \n')
    
    notacao_descritiva = notacao_descritiva.upper()

    peca_descritiva = notacao_descritiva[0]
    linha_descritiva = notacao_descritiva[1]
    coluna_descritiva = notacao_descritiva[2:]
    
    linha_descritiva = int(linha_descritiva)
    eh_branco = int(eh_branco)

    peca_algebrica = obtem_peca_algebrica(peca_descritiva)

    linha_algebrica = obtem_linha_algebrica(eh_branco, linha_descritiva)
    
    coluna_algebrica = colunas.get(coluna_descritiva)

    print(f'Em notação algebrica:  {peca_algebrica}{coluna_algebrica}{linha_algebrica}')