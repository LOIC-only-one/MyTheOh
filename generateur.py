from cProfile import label
import csv
import matplotlib.pyplot as plt
from pylab import *
import statistics


#MD5 : 27afe1a11426e341002d254d200b456e

def recupData(fichierCSV):
    """
    Permet de récuperer les données dans une liste
    """
    Datas = []

    with open(fichierCSV, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            Datas.append(row)
    return Datas

def recupListe(nom,numero):
    """
    Récuperation des données d'une liste de liste vers une liste
    """
    lst = []

    #Temperature Exterieure
    if numero == 1:
        lst = data[1]
        a = lst.pop(0)
        return lst
    #Humidité Exterieure
    elif numero == 2:
        lst = data[2]
        a = lst.pop(0)
        return lst
    #Vent
    elif numero == 3:
        lst = data[3]
        a = lst.pop(0)
        return lst
    #Pluie
    elif numero == 4:
        lst = data[4]
        a = lst.pop(0)
        return lst

def minMax(liste):
    """
    Informations d'une liste + formatage de la liste
    """
    Min = min(liste)
    Max = max(liste)
    Mean = mean(liste) 
    return Min,Max,Mean


def cumulPrecipitation(liste):
    cumul = sum(liste)*0.1
    return cumul

def genImagePlot(liste,titreDuGraphique,nomFichierImage,moyenne,Valmoyenne): ############################### ATTENTION RAJOUTER LES LABELS
    """
    Génération des images #Soucis ligne transformé par abcisse
    """
    axeX = [j for j in range(0,len(liste))]
    moyGraph = [moyenne for j in range(0,300)]
    a = round(Valmoyenne)
    plt.title(titreDuGraphique)
    plt.plot(axeX, liste)
    plt.plot(axeX, moyGraph)
    plt.legend([titreDuGraphique, f'Moyenne {titreDuGraphique} = {a}'])
    plt.savefig(nomFichierImage)
    plt.clf()

def genImageBarre(liste,cumul,titreDuGraphique,nomFichierImage):
    axeX = [j for j in range(0,len(liste))]
    cumGraph = [cumul for j in range(0,300)]
    a = round(cumul)
    plt.title(titreDuGraphique)
    plt.bar(axeX, liste)
    plt.legend([f'Précipitation = {a} mm'])
    plt.savefig(nomFichierImage)
    plt.clf()

#Programme Principale :
entry = int(input('Nom de fichier .csv : ')
data = recupData(entry)

#Récuperation des tuples et transformation des les tuples en liste
tempExt = list(recupListe(data,1))
humExt = list(recupListe(data,2))
vent = list(recupListe(data,3))
pluie = list(recupListe(data,4))

#List en float

float_temp = [float(item) for item in tempExt]
float_hum = [float(item) for item in humExt]
float_vent = [float(item) for item in vent]
float_pluie = [float(item) for item in pluie]

#Résultat des températures

tempMeta = list(minMax(float_temp))
tempMini, tempMaxi, tempMoyenne = tempMeta[0],tempMeta[1],tempMeta[2]
humMeta = list(minMax(float_hum))
humMini, humMaxi, humMoyenne = humMeta[0], humMeta[1], humMeta[2]
ventMeta = list(minMax(float_vent))
ventMini, ventMaxi, ventMoyenne = ventMeta[0], ventMeta[1], ventMeta[2]
#Résultat des pluies
a = round(cumulPrecipitation(float_pluie)) #=11.6 round to 12 int

#Génération des images

genImagePlot(float_temp,"Température","tempExt.png",tempMoyenne,tempMoyenne)
genImagePlot(float_hum,"Humidité","humExt.png",humMoyenne,humMoyenne)
genImagePlot(float_vent,"Vent","vent.png",ventMoyenne,ventMoyenne)
genImageBarre(float_pluie,cumulPrecipitation(float_pluie),"Précipitation","pluie.png")
