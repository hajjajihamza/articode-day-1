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
    
print(f"\nLe meilleur etudiant est : {meilleur.get('nom')}")    
print(f"\nLe moins etudiant est : {moins.get('nom')}")  