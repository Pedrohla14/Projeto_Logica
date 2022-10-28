import csv
from functions import *
from formula import *
arquivo = open('column_bin_3a_2p.csv')

linhas = csv.reader(arquivo)
matriz=[]
#[['PI <= 42.09', 'PI <= 48.12', 'PI <= 54.92', 'P'], ['0', '0', '0', '1'], ['1', '1', '1', '1']]
for linha in linhas:
   matriz.append(linha)

def and_all(list_formulas):

    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = And(first_formula, formula)
    return first_formula


def or_all(list_formulas):

    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = Or(first_formula, formula)
    return first_formula



def restricao_quatro(regras,numeroAtributos):
    lista_formula = []
    for i in range(regras):
        for sp in range(1,len(matriz)):
            lista_secundaria = []
            if matriz[sp][3] == "1":
                for j in range(numeroAtributos):
                    print(j)
                    if matriz[sp][j] == "1":
                        lista_secundaria.append(
                            Implies( Atom(str(matriz[0][j]) + "_" + str(i+1) + '_' + ('le')),
                                    Not (Atom(str( 'C')+str(i+1)+'_'+str(sp)))))
                    else:
                        lista_secundaria.append(
                            Implies(Atom(str(matriz[0][j]) + "_" + str(i + 1) + '_' + ('le')),
                                    Not(Atom(str('C') + str(i + 1) + '_' + str(sp)))))
                lista_formula.append(or_all(lista_secundaria))
    return and_all(lista_formula)



print (restricao_quatro(2,3))
