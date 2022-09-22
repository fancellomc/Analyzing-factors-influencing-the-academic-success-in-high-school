# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:08:01 2020

@author: evage
"""

#Boxplot 

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

#On definit la fonction boxplot qui prends en argument une dataframe.
    #Elle nous permet d'afficher un boxplot pour les variables continues.
def boxplot(bdd):
    df = pd.DataFrame(bdd, columns=['age', 'studytime','Grade','absences'])
    df.plot.box(showmeans=True)
    return boxplot

#On definit la fonction boxplot_sans_var qui prends en argument une dataframe.
    #Elle nous permet d'afficher un boxplot pour les variables continues en enlevant une variable.
    #En effet, on constate que pour la variables absences il y a beaucoup de valeur extreme, ce qui modifie l'echelle et nous permet pas de bien analyser les autres variables.
def boxplot_sans_une_var(bdd):
    n=input("Entrez une variable a omettre du boxplot : ")
    df = pd.DataFrame(bdd, columns=['age', 'studytime','Grade','absences'])
    del df[n]
    df.plot.box(showmeans=True)
    return boxplot_sans_une_var

#On definit la fonction hist_continues qui va tracer les histogrammes des variables continues de la dataframe.
#Pour cela, on utilise le module matplotlib.pyplot.
def hist_continues(data):
    n=0
    while n<4:
        var_continue=input("Entrer une variable continue : ")
        if var_continue=="age":
            plt.hist(data['age'])
            #On donne un titre au graphique.
            plt.title("Histogramme de la variable age")
            #On donne un nom a l'axe des abscisses.
            plt.xlabel("Age")
            #On donne un nom a l'axe des ordonnees.
            plt.ylabel("Frequence")
            #On affiche l'histogramme.
            plt.show()
            n=n+1
        elif var_continue=="studytime":
            plt.hist(data['studytime']) 
            plt.title("Histogramme du temps passe a etudier")
            plt.xlabel("Studytime")
            plt.ylabel("Frequence")
            plt.show()
            n=n+1
        elif var_continue=="Grade":
            plt.hist(data['Grade']) 
            plt.title("Histogramme de la moyenne des notes sur l'annee")
            plt.xlabel("Grade")
            plt.ylabel("Frequence")
            plt.show()
            n=n+1
        elif var_continue=="absences":
            plt.hist(data['absences'])
            plt.title("Histogramme du taux d'absenteisme")
            plt.xlabel("Absences")
            plt.ylabel("Frequence")
            plt.show()
            n=n+1
    return 
#Difficulte rencontree ici : lorsque qu'on execute le script principal un None apparait

#On definit une fonction se nommant diag_qualitatives qui prends en argument une dataframe notee d.
#Elle trace les diagrammes en barres pour les variable qualitatives de d.
#Pour cela, on utilise le module seaborn.      
def diag_qualitatives(d):
    n=0
    while n<12:
        var_qualitative=input("Entrer une variable qualitative : ")
        if var_qualitative=="sex":
            sns.countplot(x="sex", data=d)
            plt.title("Repartition de la variable sexe")
            plt.show()
            n=n+1
        elif var_qualitative=="address":
            sns.countplot(x="address", data=d)
            plt.title("Repartition des personnes habitant a la ville ou la campagne")
            plt.show()
            n=n+1
        elif var_qualitative=="famsize":
            sns.countplot(x="famsize", data=d)
            plt.title("Repartition de la taille des familles")
            plt.show()
            n=n+1
        elif var_qualitative=="Pstatus":
            sns.countplot(x="Pstatus", data=d)
            plt.title("Repartition du statut familial ")
            plt.show()
            n=n+1
        elif var_qualitative=="Medu":
            sns.countplot(x="Medu", data=d)
            plt.title("Repartition du niveau d'education de la mere ")
            plt.show()
            n=n+1
        elif var_qualitative=="Fedu":
            sns.countplot(x="Fedu", data=d)
            plt.title("Repartition du niveau d'education du pere ")
            plt.show()
            n=n+1
        elif var_qualitative=="activities":
            sns.countplot(x="activities", data=d)
            plt.title("Repartition de l'investissement dans des activites extra-scolaire ")
            plt.show()
            n=n+1
        elif var_qualitative=="higher":
            sns.countplot(x="higher", data=d)
            plt.title("Repartition de la volonte de faire des etudes superieur ")
            plt.show()
            n=n+1
        elif var_qualitative=="romantic":
            sns.countplot(x="romantic", data=d)
            plt.title("Repartition du statut amoureux ")
            plt.show()
            n=n+1
        elif var_qualitative=="goout":
            sns.countplot(x="goout", data=d)
            plt.title("Repartition du niveau de sortie avec des amis ")
            plt.show()
            n=n+1
        elif var_qualitative=="Dalc":
            sns.countplot(x="Dalc", data=d)
            plt.title("Repartition du niveau de consommation d'alcool en semaine")
            plt.show()
            n=n+1
        elif var_qualitative=="Walc":
            sns.countplot(x="Walc", data=d)
            plt.title("Repartition du niveau de consommation d'alcool le week-end ")
            plt.show()
            n=n+1
    return 
#Difficulte rencontree ici : lorsque qu'on execute le script principal un None apparait

#On definit la fonction correlations qui a en parametre une dataframe.
#Cette fonction affiche differents graphiques de correlation.
#Pour cela, on utilise plusieurs modules : seaborn, pandas, matplotlib.pyplot.
def correlations(bdd):
    #On decoupe les variables en deux catégories.
    #On copie la base de donnees, en creant un autre dataframe qui se nomme cadre_social grace a l'option deep=True.
    cadre_social=bdd.copy(deep=True)
    del cadre_social['sex']
    del cadre_social['age']
    del cadre_social['studytime']
    del cadre_social['higher']
    del cadre_social['romantic']
    del cadre_social['goout']
    del cadre_social['Walc']
    del cadre_social['Dalc']
    del cadre_social['activities']
    relations_sociales=bdd.copy(deep=True)
    del relations_sociales['address']
    del relations_sociales['famsize']
    del relations_sociales['Pstatus']
    del relations_sociales['Medu']
    del relations_sociales['Fedu']
    del relations_sociales['absences']
    #On affiche le diagramme de correlation pour les deux categories.
    corrmat = cadre_social.corr()
    #Cela definit la taille de la representation: une largeur de 12 et une hauteur de 9. 
        #Les valeurs par défauts sont 6 et 4 ce qui semblait faible compte tenu du nombre de variables. 
    f, ax = plt.subplots(figsize=(12, 9))
    #Vmax correspond à la plage de correlation: elle va de 0 à 0.8. 
    sns.heatmap(corrmat, vmax=.8, square=True)
    corrmat = relations_sociales.corr()
    f, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(corrmat, vmax=.8, square=True)
    return

#On cree une fonction que l'on appelle dans le script principal.
#Elle fait tourner l'ensemble des fonctions qui affichent les graphiques correspondant a la partie des statistiques descriptives sauf les Boxplots.
def graph_stat_desc(bdd):
    #print(boxplot(bdd))
    print(hist_continues(bdd))    
    print(diag_qualitatives(bdd))
    print(correlations(bdd))
    return 
#Difficulte rencontree ici : lorsque qu'on execute le script principal un None apparait

#On cree une fonction que l'on appelle dans le script principal.
    #Difficulte rencontree ici : lorsqu'on veut afficher les boxplots avant les histogrammes, 
    #ils s'affichent dans le graphique de l'histogramme. C'est pourquoi on a definit un fonction a pars que l'on execute apres.
def boxplots(bdd):
    print(boxplot(bdd))
    print(boxplot_sans_une_var(bdd))
    return 







