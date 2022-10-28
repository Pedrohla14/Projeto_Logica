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



def restricao_cinco(regras):
    lista_formula = [] # lista principal que vai guardar o resultado
    for sp in range(1, len(matriz)): #for que percorre os pacientes
        lista_paciente=[] # guarda temporariamente as informações de um paciente
        for i in range(regras): #for que percorre as regras
            lista_paciente.append(Atom(str("C") + "_" + str(sp ) + '_' + str(i+1)))

        if (len(lista_paciente) != 0 and len(lista_paciente) != 1):
            lista_formula.append(or_all(lista_paciente))
        if (len(lista_paciente) == 1):
            lista_formula.append(lista_paciente[0])

    if (len(lista_formula) != 0 and len(lista_formula) != 1):
        return and_all(lista_formula)
    if (len(lista_formula) == 1):
        return lista_formula[0]
    else:
        return []


print (restricao_cinco(4,3))
