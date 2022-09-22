#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:47:24 2020

@author: fancellomarieclara
"""

import statsmodels.api as sm

#On definit la fonction modellinear qui prends en argument une dataframe. 
#Elle estime modele multilineaire par la methode des MCO.
def modellinear(bdd):
    #On demande a l'utilisateur d'entrer la variable expliquee du modele.
    var_expli=input("Veuillez entrer la variable expliquee : ")
    #On cree une dataframe qui est compose des variables explicatives.
        #On a supprime la variable expliquee.
    X=bdd.copy(deep=True)
    del X[var_expli]
    #On extrait la variable expliquee et on la mets dans Y.
    Y=bdd[var_expli]
    #On ajoute la constante a X.
    X = sm.add_constant(X) 
    #on estima le modele.
    model = sm.OLS(Y, X).fit() 
    #On affiche le resume des resultats du modele.
    print_model = model.summary()
    return print_model

#Difficulte rencontree: lorsqu'on appelle dans notre script principal la fonction modellinear, les resultats ne s'affichent pas.
#Cela fonctionne seulement si on cree la fonction principal model.
def model(bdd):
    print(modellinear(bdd))
    return