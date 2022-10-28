import csv
from functions import *
from formula import *
arquivo = open('column_bin_3a_2p.csv')

linhas = csv.reader(arquivo)
matriz=[]
#[['PI <= 42.09', 'PI <= 48.12', 'PI <= 54.92', 'P'], ['0', '0', '0', '1'], ['1', '1', '1', '0']]
for linha in linhas:
   matriz.append(linha)



lista_total = matriz[0]



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



def restricao_dois(regras):
    lista_formula = []
    for  j in range(regras):
        lista_secundaria = []
        for i in range(len(lista_total)):
            lista_secundaria.append(( Not(Atom(str(lista_total[i]) + "_" + str(j + 1) + '_' + ('S'))) ))
        lista_formula.append( or_all(lista_secundaria))
    return and_all(lista_formula)



list= restricao_dois(3)
print(list)
