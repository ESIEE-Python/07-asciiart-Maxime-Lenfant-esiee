#### Imports et définition des variables globales
"""
encodage Ascii
"""
import sys
sys.setrecursionlimit(5000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    liste=[]
    i=1
    c=s[0]
    for caractere in s[1:]:
        if c==caractere:
            i=i+1
        else:
            tuples=(c,i)
            liste.append(tuples)
            c=caractere
            i=1
    tuples=(c,i)
    liste.append(tuples)
    return liste


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne 
    de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    # votre code ici
    if s=="":
        return []
    compteur =1
    c=s[0]
    while compteur<len(s) and s[compteur]==c:
        compteur+=1
    return [(c,compteur)]+artcode_r(s[compteur:])

#### Fonction principale


def main():
    """
    test du programme
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
