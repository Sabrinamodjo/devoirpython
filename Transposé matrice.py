"""Soit un programme prennant en paramètre une matrice quelconque, ce programme sera chargé d'effectuer
la transposée de cette matrice"""
#soit la matrice A=[[2,4,6,8],[5,0,-5,-3],[1,4,7,8],[2,0,6,4]]
def TM(A):
    #soit TA la matrice vide
    TA=[]
    #On choisit les premiers éléments de chaque matrice
    l=len(A[0])
    for i in range(l):
        #Soit C le compteur
        C=[]
        for L in A:
            #le compteur C prendra les premiers élèments de chaque matrice de manière permanente
            C.append(L[i])
        #On ajoute le resultat dans la matrice vide précedement crée qui prendra la matrice finale
        TA.append(C)
    return TA
