import urllib.request as ur
import parse as ps

##12/02 : En lien annexe, mettre peut être quelques artciles qui sont les plus consultés :
##Difficultés : Header Python --> anglais : noms de champs différents : analyse en anglais
##d'un article en français

sujet = "France"
url = "https://fr.wikipedia.org/wiki/" + sujet
stats = "https://tools.wmflabs.org/pageviews/?project=fr.wikipedia.org&platform=all-access&agent=user&range=latest-20&pages=" + sujet

# Récupération des données
req = ur.urlopen(url)
result = open("test2.html",'wb')
result.write(req.read())
result.close()

#Traitement des données
result = open("test2.html",'rb')
data = result.read().decode()
data_splitted = data.split('\n')
for line in data_splitted:
    ps.title_principal(line)
    ps.paragraphe(line)

##Etude statistique
#Récupération des données
req = ur.urlopen(stats)
result = open("test2_stats.html",'wb')
result.write(req.read())
result.close()

#Traitement des données
result = open("test2_stats.html",'rb')
data = result.read().decode()
data_splitted = data.split('\n')
for line in data_splitted:
    ps.relevant(line)