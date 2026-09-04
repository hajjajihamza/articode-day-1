#  1.1 — Erreur de syntaxe ou exception ?
try:
    print('bonjour')
    resultat = 10 / 0
    
    valeurs = [1, 2, 3]
    print(valeurs[5])
except SyntaxError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
    
#  1.2 — division_securisee(a, b)

def division_securisee(a, b):
    if b == 0:
        raise ZeroDivisionError('division par zero impossible.')
    return a / b
        
    
try:
    division_securisee(10, 2)
    division_securisee(10, 0)
except Exception as error:
    print(f'Error : {error}')
    
# 1.3 — convertir_entier(valeur)

def convertir_entier(valeur):
    try:
        print(int(valeur))
    except:
        print(f'Erreur : "{valeur}" n’est pas un entier valide.')

convertir_entier("42")
convertir_entier("abc")

#  1.4 — acceder_element(liste, index)

def acceder_element(liste, index):
    try:
        return liste[index]
    except IndexError:
        print(f'Erreur : index {index} hors limites (taille de la liste : 3).')

notes = [12, 15, 9]
acceder_element(notes, 1)
acceder_element(notes, 10)

#  1.5 — acceder_cle(dictionnaire, cle)

def acceder_cle(dictionnaire, cle):
    try:
        return dictionnaire[cle]
    except KeyError:
        print(f'Erreur : la cle "{cle}" n’existe pas.')
    
    
eleve = {"nom": "Sara", "age": 20}
acceder_cle(eleve, "nom")
acceder_cle(eleve, "email")

# 1.6 — try / except / else / finally

def traiter_valeur(value):
    try:
        converted_value = int(value)
    except ValueError:
        print(f"Erreur : '{value}' n’est pas convertible")
    else:
        print(f"Conversion reussie : {converted_value}")
    finally:
        print("Traitement termine.")
        
traiter_valeur("8")
traiter_valeur("x")

