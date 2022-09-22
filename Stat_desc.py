# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 09:34:13 2020

@author: evage
"""
#On definit la fonction description_table qui prends en entree une dataframe.
def description_table(data):
    #On affiche la taille de la base de donnees avec la methode shape.
    print("La taille de la base de donnees est :",data.shape)
    #On affiche la dimension de la base de donnees avec la methode ndim.
    print("La dimension de la base de donnes est" , data.ndim) 
    #On affiche le type de la base de donnees avec la fonction type.
    print("Le type de la base de donnees est :", type(data)) 
    return 

#On définit la fonction description_donnee qui prends en entree une dataframe.
    #Grace à la methode describe, on obtient le minimum, le maximum et les 3 quantiles pour chaque variable.
    # et la skewness et la kurtosis 
def description_donnee(data):
    stat=data.describe()
    stat.to_excel(r"statdesc.xlsx", index = False)
    return stat

#On definit la fonction skew qui prends en entree une dataframe.
    #Elle nous donne a valeur de la skewness pour chaque variable grace a la methode skew.
    #Elle nous donne également a valeur de la kurtosis pour chaque variable grace a la methode kurt.
def skewkurto(data):
    #On copie la base de donnees, en creant un autre dataframe qui se nomme cadre_social grace a l'option deep=True.
    dfcontinues=data.copy(deep=True)
    del dfcontinues['address']
    del dfcontinues['famsize']
    del dfcontinues['Pstatus']
    del dfcontinues['Medu']
    del dfcontinues['Fedu']
    del dfcontinues['activities']
    del dfcontinues['higher']
    del dfcontinues['romantic']
    del dfcontinues['goout']
    del dfcontinues['Dalc']
    del dfcontinues['Walc']
    del dfcontinues['absences']
    skew=dfcontinues.skew()
    kurt=dfcontinues.kurt()
    return skew,kurt
        
#On cree la fonction que l'on appelle dans le script principal.
#Elle fait tourner l'ensemble des fonctions utiles pour effectuer toutes les statistiques descriptives. 
def stat_des(data):
    print(description_table(data))
    print(description_donnee(data))
    print(skewkurto(data))
    return
