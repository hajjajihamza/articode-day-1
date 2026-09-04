#  3.1 — Intersection, union, différence

atelier_python = ["Ali", "Sara", "Lina", "Karim"]
atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]

atelier_python_set = set(atelier_python)
atelier_java_set = set(atelier_java)

print(atelier_python_set.intersection(atelier_java_set))
print(atelier_python_set.union(atelier_python_set))
print({e for e in atelier_python_set if e not in atelier_java_set})
print('\n')

#  3.2 — a_des_doublons(liste)

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]

def a_des_doublons(liste):
    return len(set(liste)) != len(liste)

print(a_des_doublons(liste_1))
print(a_des_doublons(liste_2))
print('\n')


#  3.3 — Set unique à partir de listes imbriquées

tags_articles = [
    ["python", "web", "api"],
    ["python", "data"],
    ["web", "css"],
]

v_set = set([tech for tag in tags_articles for tech in tag])
print(v_set)
print('\n')


# 3.4 — Limite des sets : éléments non hashables
