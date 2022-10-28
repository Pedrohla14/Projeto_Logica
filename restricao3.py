import csv
from functions import *
from formula import *
arquivo = open('column_bin_3a_2p.csv')

linhas = csv.reader(arquivo)
matriz=[]
#[['PI <= 42.09', 'PI <= 48.12', 'PI <= 54.92', 'P'], ['0', '0', '0', '1'], ['1', '1', '1', '0']]
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



def restricao_tres(regras,numeroAtributos):
    lista_formula = []
    for i in range(regras):
        for sp in range(1,len(matriz)):
            lista_secundaria = []
            if matriz[sp][3] == "0":
                for j in range(numeroAtributos):
                    print(j)
                    if matriz[sp][j] == "0":
                        lista_secundaria.append(Atom(str(matriz[0][j]) + "_" + str(i+1) + '_' + ('le')))
                    else:
                       lista_secundaria.append(Atom(str(matriz[sp][j]) + "_" + str(i+1) + '_' + ('gt')))
                lista_formula.append(or_all(lista_secundaria))
    return and_all(lista_formula)



print (restricao_tres(2,3))
