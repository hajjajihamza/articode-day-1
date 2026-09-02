def calculer_moyenne(notes:list):
    return sum(notes) / len(notes)

def appreciation(moyenne):
    apper = ""
    match moyenne:
        case n if n <= 9.9:
            apper = "Insuffisant"
        case n if n <= 11.9:
            apper = "Passable"
        case n if n <= 15.9:
            apper = "Bien"
        case _:
            apper = "Tres bien"
    return apper
      
notes = [12, 15, 9]
print(calculer_moyenne(notes))  
    
valeurs_test = [9.9, 10.0, 11.9, 12.0, 15.9, 16.0, 20.0]
for i in valeurs_test:
    print(appreciation(i))
      
print('\n')            
etudiants = [
{"nom": "Karim", "notes": [12, 15, 9]},
{"nom": "Sara", "notes": [18, 17, 16]},
{"nom": "Lina", "notes": [6, 8, 5]},
]

meilleur = etudiants[0]
meilleure_moyenne = calculer_moyenne(meilleur["notes"])


moins = etudiants[0]
moins_moyenne = calculer_moyenne(moins["notes"])
for etudiant in etudiants:
    moyenne = calculer_moyenne(etudiant["notes"])

    if moyenne > meilleure_moyenne:
        meilleur = etudiant
        meilleure_moyenne = moyenne
    
    if moyenne < moins_moyenne:
        moins = etudiant
        moins_moyenne = moyenne    
        
    print(f'{etudiant.get("nom")} {moyenne:.2f} {appreciation(moyenne)}')
    
print(f"Le meilleur etudiant est : {meilleur.get('nom')}")    
print(f"Le moins etudiant est : {moins.get('nom')}")  

print('\n')

def calculer_moyenne_ponderee(notes, coefficients):
    moyenne = 0
    for i in range(len(notes)):
        moyenne += notes[i] * coefficients[i]
    return moyenne / sum(coefficients)

notes = [14, 10, 18] # Maths, Francais, Sport
coefficients = [3, 2, 1]
print(f"{calculer_moyenne_ponderee(notes, coefficients):.2f}")


def moyenne_groupe(etudiants):
    moyenne_sum = sum(list(map(lambda e: calculer_moyenne(e.get('notes')), etudiants)))
    try:
        return moyenne_sum / len(etudiants)
    except ZeroDivisionError:
        print('Attention : aucune note fournie.')
        return 0   

etudiants = [
{"nom": "Karim", "notes": [12, 15, 9]},
{"nom": "Sara", "notes": [18, 17, 16]},
{"nom": "Lina", "notes": [6, 8, 5]},
]

print('\n')

print(f"{moyenne_groupe(etudiants):.2f}")

def somme_recursive(notes):
    if (len(notes) == 0):
        return 0
    return notes[0] + somme_recursive(notes[1:]) 


notes = [12, 15, 9, 18]

print('\n')
print(f"{somme_recursive(notes):.2f}")