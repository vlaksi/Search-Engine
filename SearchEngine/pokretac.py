"""
Modul koji predstavlja pokretacki deo aplikacije.
"""

from unos import *
from rangiranjePretrage import rangiranjePretrage
from pagination import *
from naprednap.napredna_pretraga import *
from unos import *
import sys
import time


if __name__ == '__main__':
    np = NasParser()

    globalResultSet = Set('')
    resultSet = Set('')
    setSvihDatoteka = Set('')
    stablo = Tree()
    unesene_reci = ''
    stablo, g, setSvihDatoteka, recnikStranicaReci, unos, dokumentiKojiImajuLinkKaDokumentu,bekLinkovi = unosPutanje()
    while True:
        print("\n\t\t\t\t ------------------------------------- GLAVNI MENI -------------------------------------")
        print("\t\t\t\t\t1 - Prosta pretraga [ AND, OR, NOT - operatori].")
        print("\t\t\t\t\t2 - Napredna pretraga.")
        print("\t\t\t\t\tK - Kraj programa.")
        print("\n\t\t\t\t ---------------------------------------------------------------------------------------")
        indexPretrage = input("Unos[1,2]: ")

        if indexPretrage == "K" or indexPretrage == "k":
            break

        if indexPretrage not in [str(1),str(2)]:
            continue


        if indexPretrage == str(1):
            unesene_reci = unosProstePretrage()

            if len(unesene_reci) == 3:
                if 'and' == unesene_reci[0] or 'or' == unesene_reci[0] or 'not' == unesene_reci[0] or 'and' == \
                        unesene_reci[2] or 'or' == unesene_reci[2] or 'not' == unesene_reci[2]:
                    print("Warning: Neispravno koriscenje logickih operatora")
                    continue

            start = time.time()
            globalResultSet = pretraga(unesene_reci, stablo, unos)
            end = time.time()
            #print("Za pretragu je potrebno " + str((end - start).__round__(2)) + " sekundi.")
            #break
        if indexPretrage == str(2):
            unosUpit = input("Unesite pretragu:")
            unosUpit = unosUpit.strip().lower()
            unesene_reci = unosUpit.split()
            print("Please wait...")

            start = time.time()
            globalResultSet = np.parsiraj(unosUpit).evaluiraj(setSvihDatoteka, stablo)
            #print(len(globalResultSet))
            end = time.time()
            #print("Za pretragu je potrebno " + str((end - start).__round__(2)) + " sekundi.")

            #break



        if len(globalResultSet.elements) != 0:
        #Rangiranje i stampanje pretrage
            start = time.time()
            rangiranSet = rangiranjePretrage(setSvihDatoteka,globalResultSet, dokumentiKojiImajuLinkKaDokumentu, bekLinkovi, unesene_reci,recnikStranicaReci)
            end = time.time()
            #print("Za rangiranje pretrage je potrebno " + str((end - start).__round__(2)) + " sekundi.")
            paginacija(rangiranSet)
        else:
            print("Not successful search!")




