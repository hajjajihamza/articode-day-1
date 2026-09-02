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
{"nom": "Nadia", "notes": [12, 15, 9]},
]

etudiants_dict_list = {}

for etudiant in etudiants:
    moyenne = calculer_moyenne(etudiant.get('notes'))
    etudiants_dict_list[etudiant.get('nom')] = {
        'moyenne': moyenne,
        'mention': appreciation(moyenne)
    }
    
print(etudiants_dict_list)   
print('\n')


etudiants_dict_list_tries = sorted(etudiants_dict_list.items(), key=lambda e: e[1].get('moyenne'), reverse=True)
print(etudiants_dict_list_tries)
print('\n')


etudiants_en_echec = [(nom, infos.get("moyenne")) for nom, infos in etudiants_dict_list.items() if infos.get("moyenne") < 10]
# for nom, infos in etudiants_dict_list.items():
#     if infos.get("moyenne") < 10:
#         etudiants_en_echec.append((nom, infos.get("moyenne")))  
        
print(etudiants_en_echec)
print('\n')



#  Défis supplémentaire

regrouper_par_mention = {}

for nom , infos in etudiants_dict_list.items():
    if infos.get('mention') not in regrouper_par_mention:
        regrouper_par_mention[infos.get('mention')] = [nom]
    else:
        regrouper_par_mention[infos.get('mention')].append(nom)
        
print(regrouper_par_mention)
print('\n')

# détection de doublon

noms = ["Karim", "Sara", "Lina", "Karim"]
noms_set = set(noms)
if len(noms) != len(noms_set):
    print('Attention il y a des doublons\n')
    
#  fusion de deux groupes

groupe_a = {
"Karim": {"moyenne": 12.0, "mention": "Bien"},
}
groupe_b = {
"Karim": {"moyenne": 15.0, "mention": "Bien"},
"Sara": {"moyenne": 17.0, "mention": "Tres bien"},
}

fusionner_groupe = {**groupe_a}

for nom, infos in groupe_b.items():
    if nom not in fusionner_groupe:
        fusionner_groupe[nom] = infos
    else:
        print(f'refuser la fusion pour {nom} parce que est doublon')

