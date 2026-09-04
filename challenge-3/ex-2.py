#  2.1 — verifier_age(age) avec raise
def verifier_age(age):
    try:
        if age < 1:
            raise ValueError(f'ValueError: l’age ne peut pas etre negatif ({age}).')
        print(f'Valide age : ({age})')
    except ValueError as error:
        print(error)
    
# verifier_age(25)
# verifier_age(-3)

#  2.2 — Relancer une exception (raise sans argument)

def traiter_liste_de_valeurs(liste):
    try:
        [int(i) for i in liste]
    except ValueError:
        print('Error')
        raise

# traiter_liste_de_valeurs(["3", "9", "x", "5"])


#  2.3 / 2.4 — Exception personnalisée StockInsuffisantError

class StockInsuffisantError(Exception):
    pass


def retirer_stock(stock, produit, quantite):
    try:
        if stock[produit] < quantite:
            raise StockInsuffisantError(f'stock insuffisant pour "{produit}" (demande : {quantite}, disponible : {stock[produit]})')
    except:
        raise
        
stock = {"pommes": 20, "bananes": 4}
retirer_stock(stock, "pommes", 5)
retirer_stock(stock, "bananes", 10)

