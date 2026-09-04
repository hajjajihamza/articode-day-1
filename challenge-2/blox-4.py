#  4.1 — Analyse des ventes

from collections import defaultdict

ventes = [
    {"produit": "pommes", "montant": 120},
    {"produit": "bananes", "montant": 80},
    {"produit": "pommes", "montant": 45},
    {"produit": "oranges", "montant": 60},
    {"produit": "bananes", "montant": 30},
]

total_par_produit = defaultdict(int)

for v in ventes:
    produit = v.get('produit')
    total_par_produit[produit] = total_par_produit[produit] + v.get('montant')

total_par_produit = dict(total_par_produit)
print('Total par produit :', total_par_produit)


total_par_produit_list = list(total_par_produit.items())
meilleur_produit = total_par_produit_list[0]
for p, t in total_par_produit_list:
    if t > meilleur_produit[1]:
        meilleur_produit = [p, t]
print(f"Meilleur produit : {meilleur_produit[0]}")

produits_distincts = set(map(lambda v: list(v.items())[0][1], ventes))
print(f"Meilleur produit : {produits_distincts}")
print('\n')

# 4.2 — fusionner_inventaires(inv1, inv2)

inv1 = {"pommes": 20, "bananes": 15}
inv2 = {"bananes": 10, "kiwis": 5}

def fusionner_inventaires(inv1, inv2):
    fusionner =  defaultdict(int)
    liste =  [*list(inv1.items()), *list(inv2.items())]
    for t in liste:
        produit = t[0]
        fusionner[produit] = fusionner[produit] + t[1]
    print(dict(fusionner))
    print('\n')
    
fusionner_inventaires(inv1, inv2)

# 4.3 — Mini-challenge final

etudiants = [
    {"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
    {"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
    {"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
]

print('Moyenne par etudiant :')

for e in etudiants:
    matieres_note = e.get('matieres').values()
    print(f'{e.get('nom')} : {sum(matieres_note) / len(matieres_note):.2f}')
    
print('\n')
print("Matieres enseignees (set) :")

matieres = [i for e in etudiants for i in e.get('matieres').keys()]
print(set(matieres))
print('\n')


notes_par_matiere = defaultdict(list)

for e in etudiants:
    for m , n in e['matieres'].items():
        notes_par_matiere[m].append(n)
    
print("Notes par matiere :")
for m, n in dict(notes_par_matiere).items():
    print(m, n)
print('\n')


moyennes =  [[m,sum(n)/len(n)] for m,n in dict(notes_par_matiere).items()]

meilleure_matiere = moyennes[0]

for matiere, moyenne in moyennes:
    if moyenne > meilleure_matiere[1]:
        meilleure_matiere = [matiere, moyenne]

print(f"Meilleure matiere (moyenne globale) : {meilleure_matiere[0]} ({meilleure_matiere[1]})")
