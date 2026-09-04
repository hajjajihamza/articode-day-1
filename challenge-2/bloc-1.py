# 1.1 — Max/min sans fonctions natives

def min(lst:list):
    min_index = 0
    for i in range(len(lst)):
        if lst[min_index] > lst[i]:
            min_index = i
            
    return lst[min_index]

def max(lst:list):
    max_index = 0
    for i in range(len(lst)):
        if lst[max_index] < lst[i]:
            max_index = i
            
    return lst[max_index]

notes = [12, 18, 7, 15, 9, 20, 3, 14]

print(f"Note min : {min(notes)}")
print(f"Note max : {max(notes)}\n")

# 1.2 — notes_au_dessus(notes, seuil)

notes = [8, 14, 6, 17, 11, 20]
seuil = 12

def notes_au_dessus(notes, seuil):
    return [n for n in notes if n >= seuil]
    
print(notes_au_dessus(notes, seuil))
print('\n')

# 1.3 — Comptage d’occurrences

from collections import defaultdict

fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]

occurrences = defaultdict(dict)

for f in fruits:
    occurrences[f] = occurrences.get(f, 0) + 1

for key, value in occurrences.items():
    print(f"{key} : {value}")
print('\n')

# 1.4 — Inversion manuelle

liste = [1, 2, 3, 4, 5]

new_index = 0
for i in range(len(liste) - 1, len(liste) // 2, -1):
    old_value = liste[i]
    liste[i] = liste[new_index]
    liste[new_index] = old_value
    new_index += 1
   
print(liste)
print('\n')

# 1.5 — Fusion de deux listes triées
liste_a = [1, 4, 7]
liste_b = [2, 3, 8, 9]

fusion_lit = [*liste_a, *liste_b]

for i in range(len(fusion_lit)):
    for j in range(i + 1, len(fusion_lit), 1):
        if fusion_lit[i] > fusion_lit[j]:
            old_value = fusion_lit[i]
            fusion_lit[i] = fusion_lit[j]
            fusion_lit[j] = old_value
            
print(fusion_lit)
print('\n')

# 1.6 — Compréhension de liste

nombres = [3, 12, 7, 25, 8, 19, 2]

print([(n * n) for n in nombres if n%2 == 0])
print('\n')