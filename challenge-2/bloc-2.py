# 2.1 — vendre(stock, produit, quantite)

def vendre(stock, produit, quantite):
    quantite_actuail = stock.get(produit)
    if quantite_actuail < quantite:
        print(f"Stock insuffisant pour {produit} (disponible : {quantite_actuail}).")
        return
    stock[produit] -= quantite
    print(f'Vente enregistree : {quantite} {produit}.')

stock = {"pommes": 50, "bananes": 30, "oranges": 0}
vendre(stock, "pommes", 20)
vendre(stock, "oranges", 5)
print('Etat final de stock: ')
print(stock)
print('\n')

# 2.2 — produits_epuises(stock)

def produits_epuises(stock):
    return [fruit for fruit, quantiter in stock.items() if quantiter == 0]

stock = {"pommes": 30, "bananes": 0, "oranges": 0, "kiwis": 12}

print(produits_epuises(stock))
print('\n')

# 2.3 — Total par client

from collections import defaultdict

def total_par_client(commandes):
    result = defaultdict(int)
    
    for command in commandes:
        client = command.get('client')
        
        result[client] = result[client] + command.get('quantite')
        
    return dict(result)
    
commandes = [
    {"client": "Ali", "produit": "pommes", "quantite": 5},
    {"client": "Sara", "produit": "bananes", "quantite": 10},
    {"client": "Ali", "produit": "oranges", "quantite": 2},
]

print(total_par_client(commandes))
print('\n')

# 2.4 — Inversion d’un dictionnaire

d = {"a": 1, "b": 2, "c": 3}

print({value: key for key,value in d.items()})
print('\n')

# 2.5 — Compréhension de dictionnaire

mots = ["chat", "elephant", "abeille", "riz"]

print({mot: len(mot) for mot in mots})
print('\n')

# 2.6 — Dictionnaires imbriqués

entreprises = {
    "IT": ["Ali", "Sara", "Omar"],
    "RH": ["Lina"],
    "Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
}

for entreprise, employers in entreprises.items():
    print(f'{entreprise} : {len(employers)} employe(s)')
print('\n')

