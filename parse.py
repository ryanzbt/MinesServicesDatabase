def unbaliser(html, balise):
    end = end_balise(html)
    balise_end = "</" + balise + ">"
    return html[end:].split(balise_end)[0]

def end_baliser(nom_balise):
    balise_end = "</" + nom_balise + ">"
    return balise_end

def title_principal(string):
    if end_baliser("h1") in string:
        result = "Titre : " + unbaliser(string, "h1")
        print(result)
        return result

def paragraphe(string):
    if end_baliser("p") in string:
        result = "Un paragraphe : " + unbaliser(string, "p")
        print(result)
        return result


"""Comme les balises contiennent plusieurs paramètres, fonction retournant l'indice
du caracètre '>' de fin de la balise"""
def end_balise(string):
    indice = 0
    while string[indice] != ">" and indice<len(string):
        indice+=1
    return indice + 1


## Statistiques
def relevant(string):
    if "Moyenne" in "Moyenne":
        print(string)
    return 0