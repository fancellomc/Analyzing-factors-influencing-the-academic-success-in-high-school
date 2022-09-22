# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 09:18:52 2020

@author: evage
"""


import pandas as pd

#On définit la fonction get_file qui va demander a l'utilisateur de rentrer le nom du fichier de la base de donnees à utiliser.
def get_file():
    #On nomme file le nom du fichier rentre par l'utilisateur. 
        #Input nous permet de demander à l'utilisateur de rentrer un nom de fichier dans la console.
    file=input("Entrer un nom de fichier :") 
    #Tant que le nom du fichier n'est pas celui qu'on veut etudier, on continue de demander a l'utilisateur de rentrer un nom de fichier.
    while file != "student-mat.csv":
        print("Le nom du fichier est incorrect, cela doit etre student-mat.csv")
        file=input("Entrer un nom de fichier :")
    #Quand le fichier entre est le bon, on cree la variable f qui va stocker notre dataframe.
        #Le fichier passe d'un format CSV a dataframe grace au module pandas. 
    f=pd.read_csv('student-mat.csv',sep=',')
    return f

#On definit la fonction creation_var_note_moyenne qui prends comme entree notre dataframe et qui va nous permettre de faire la moyenne des notes de chaque individu.
def creation_var_note_moyenne (data): 
    #On cree une colonne G qui est la somme de G1, G2, G3.
    data['G']=data['G1']+data['G2']+data['G3'] 
    #On cree une colonne Grade qui est la moyenne de G1, G2, G3.
    data['Grade']=data['G']/3
    return data

#On définit une fonction del_var qui prend comme entree notre dataframe et qui supprime les colonnes que l'on ne veut pas etudier.
def del_var(data) :
    #On entre dans la variable listecol qui affiche le nom de toutes les variables de data.
    listecol=data.columns
    print(listecol)
    #On supprime de data la variable school.
    del data['school']
    del data['Mjob']
    del data['Fjob']
    del data['reason']
    del data['guardian']
    del data['traveltime']
    del data['schoolsup']
    del data['famsup']
    del data['paid']
    del data['nursery']
    del data['internet']
    del data['famrel']
    del data['freetime']
    del data['health']
    del data['failures']
    del data['G1']
    del data['G2']
    del data['G3']
    del data['G']
    newlistecol=data.columns
    print("Voici la nouvelle liste de variable de la base de donnees :", newlistecol)    
    return data

#On definit une fonction creation_var_indicatrice qui prends en entree notre base de donnees qui transforme les variables qualitatives en indicatrice.
def creation_var_indicatrice(data):
    #On cree la variable n qui est un compteur.
    n=0
    print("Les variables a modifier sont : Medu, Fedu, sex, address, famsize, Pstatus, activities, higher, romantic")
    '''n compte un tour si la variable que l'on veut modifier a ete entree par l'utilisateur.
    Tant que le compteur est plus petit que le nombre de variable que l'on veut modifier,
    l'utilisateur peut entrer un nom de variable a modifier. '''
    while n<9:
        var=input("Entrer un nom de variable qualitative :") 
        if var=="Medu":
            #A l'aide de la methode apply et lambda on parcours la colonne (axis=1) Medu. 
                #Si la valeur de la ligne est 4, on la change en mettant 1. 
                    #Sinon on met l valeur 0.
            data['Medu'] = data.apply(lambda x: 1 if x['Medu']==4 else 0, axis=1)
            print("La variable Medu vaut 1 lorsque sa valeur était 4 et 0 sinon")
            n=n+1
        elif var=="Fedu":
            data['Fedu'] = data.apply(lambda x: 1 if x['Fedu']==4 else 0, axis=1)
            print("La variable Fedu vaut 1 lorsque sa valeur était 4 et 0 sinon")
            n=n+1
        elif var=="sex":
            data['sex'] = data.apply(lambda x: 1 if x['sex']=='F' else 0, axis=1)
            print("La variable sex vaut 1 lorsque l'individu est une femme")
            n=n+1
        elif var=="address":
            data['address'] = data.apply(lambda x: 1 if x['address']=='U' else 0, axis=1)
            print("La variable address vaut 1 lorsque l'individu vit en zone urbaine")
            n=n+1
        elif var=="famsize":
            data['famsize'] = data.apply(lambda x: 1 if x['famsize']=='GT3' else 0, axis=1)
            print("La variable famsize vaut 1 lorsque que l'individu vit avec plus de 3 personnes, lui compris")
            n=n+1
        elif var=="Pstatus":
            data['Pstatus'] = data.apply(lambda x: 1 if x['Pstatus']=='T' else 0, axis=1)
            print("La variable Pstatus vaut 1 lorsque que l'individu a ses parents qui vivent ensemble")
            n=n+1
        elif var=="activities":
            data['activities'] = data.apply(lambda x: 1 if x['activities']=='yes' else 0, axis=1)
            print("La variable activities vaut 1 lorsque que l'individu pratique une activité")
            n=n+1
        elif var=="higher":
            data['higher'] = data.apply(lambda x: 1 if x['higher']=='yes' else 0, axis=1)
            print("La variable activities vaut 1 lorsque que l'individu a pour ambition de faire des etudes superieurs")
            n=n+1
        elif var=="romantic":
            data['romantic'] = data.apply(lambda x: 1 if x['romantic']=='yes' else 0, axis=1)
            print("La variable activities vaut 1 lorsque que l'individu est en couple")
            n=n+1
    return data

#On cree la fonction que l'on appelle dans le script principal.
#Elle fait tourner l'ensemble des fonctions en reprenant a chaque fois la data retourner precedemment.
def mise_en_forme():
    data=get_file()
    data=creation_var_note_moyenne(data)
    data=del_var(data)
    print(creation_var_indicatrice(data))
    #On exporte la nouvelle base de donnees dans un fichier excel qui se nomme bdd_corrige, sans mettre la position des lignes (index=False).
    data.to_excel(r"bdd_corrige.xlsx", index = False)
    return data

#On met nos appels de fonction dans if main afin qu'il ne s'affiche pas lorqu'on utilisera le module.
if __name__ == "__main__" :
    get_file()
    mise_en_forme()
