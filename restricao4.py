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
    lista_formula = [] # lista principal que vai guardar o resultado
    for sp in range(1, len(matriz)): #for que percorre os pacientes
        lista_paciente=[] # lista que vai ser usada para fazer o and de todos elementos da lista_secundaria
        for i in range(regras): #for que percorre as regras
            lista_secundaria = []  #lista que vai ser usada para guadar os atributos
            if matriz[sp][3] == "1":  #paciente com patologia
                for j in range(numeroAtributos):
                    if matriz[sp][j] == "0":
                        lista_secundaria.append(
                            Implies(Atom(str(matriz[0][j]) + "_" + str(i + 1) + '_' + ('le')),
                                    Not(Atom(str('C') + str(i + 1) + '_' + str(sp)))))
                    else:
                        lista_secundaria.append(
                            Implies(Atom(str(matriz[0][j]) + "_" + str(i + 1) + '_' + ('gt')),
                                    Not(Atom(str('C') + str(i + 1) + '_' + str(sp)))))
                if (len(lista_secundaria)!=0 and len(lista_secundaria)!=1):
                    lista_paciente.append(or_all(lista_secundaria))
                if(len(lista_secundaria)==1):
                     lista_paciente.append(lista_secundaria[0])
        if (len(lista_paciente) != 0 and len(lista_paciente) != 1):
            lista_formula.append(and_all(lista_paciente))
    if (len(lista_formula) != 0 and len(lista_formula) != 1):
        return and_all(lista_formula)
    if (len(lista_formula) == 1):
      return lista_formula[0]
    else:
        return []
print (restricao_quatro(2,3))
