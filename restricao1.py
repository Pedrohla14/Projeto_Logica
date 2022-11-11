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
    for j in range(regras):
        lista_secundaria = []
        for i in range(len(lista_total)):
            lista_atomsOR = []
            lista_atomsAndNot = []
            lista_atomsAndTotal = []

            s=Atom(str(lista_total[i]) + "_" + str(j + 1) + '_' + ('S'))
            le=Atom(str(lista_total[i]) + "_" + str(j + 1) + '_' + ('le'))
            gt= Atom(str(lista_total[i]) + "_" + str(j + 1) + '_' + ('gt'))

            lista_atomsOR.append(s)
            lista_atomsOR.append(le)
            lista_atomsOR.append(gt)

            lista_atomsAndNot.append(s)
            lista_atomsAndNot.append(le)
            lista_atomsAndNot.append(gt)

            lista_atomsAndTotal.append(or_all(lista_atomsOR))
            lista_atomsAndTotal.append(Not(and_all(lista_atomsAndNot)))

            lista_secundaria.append(and_all(lista_atomsAndTotal))

        lista_formula.append( or_all(lista_secundaria))
    return and_all(lista_formula)
