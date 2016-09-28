import cPickle as pic
import os
import matplotlib.pyplot as plt
import numpy as np
import operator

fold = '/Users/student/Documents/PUBS'

def import_dicts(folder):
    os.chdir(folder)
    Allele_dic = pic.load(open('allele_dic.pkl','rb'))
    #key = barkode numerous sequences, value = residuenumber_codon
    Translate = pic.load(open('translate.pkl','rb'))
    #key = codon, velue = amino acid
    Aminotonumber = pic.load(open('aminotonumber.pkl','rb'))
    #key = amino acid, value = number
    return Allele_dic, Translate, Aminotonumber


def codons_by_positions(al_dict,trans):
    c_by_p = {}
    for bar in al_dict:
        position = int(str(al_dict[bar][0]).split('_')[0])
        codon = str(al_dict[bar][0]).split('_')[1]
        aa = trans[codon]
        #print(bar,position,codon)
        if position not in c_by_p:
            c_by_p[position] = {}
        c_by_p[position][aa] = c_by_p[position].get(aa,0) + 1
    #for i in c_by_p:
    #    print(i, c_by_p[i])
    #print(c_by_p)
    return c_by_p

def matrix(c_by_p,amino):
    redund_matrix = [[x for x in range(len(c_by_p))] for y in range(len(amino))]
    sorted_amino = sorted(amino.items(), key=operator.itemgetter(1))
    #print(redund_matrix)
    #print(sorted_amino)
    for position in c_by_p:
        for d in sorted_amino:
            #print(c_by_p[position])
            #print(d[0])
            number = 0
            for aa in c_by_p[position]:
                if d[0] == aa:
                    number += c_by_p[position][aa]
            #print(position,d[1])
            redund_matrix[d[1]][position - 2] = number
    return redund_matrix

def heat(matr):
    plt.imshow(matr, cmap='hot', interpolation='nearest')
    plt.show()

def main():
    allele_dic, translate, aminotonumber = import_dicts(fold)
    translate_new = {}
    for i in translate:
        translate_new[i.replace('U','T')] = translate[i]
    print(allele_dic)
    print(translate_new)
    print(aminotonumber)
    #print(sorted(aminotonumber.values()))
    c_by_p = codons_by_positions(allele_dic,translate_new)
    y = matrix(c_by_p, aminotonumber)
    heat(y)

main()
#show you titties.. do it
#a = [[1,2,3],[1,3,3],[2,3,3]]
#print(a)
#plt.imshow(a, cmap='hot', interpolation='nearest')
#plt.show()
# Pooja is so awesome, I can't even. #NOT
