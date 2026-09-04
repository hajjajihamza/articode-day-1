# 4.1 — lire_fichier_securise(chemin)
from pathlib import Path
from statistics import quantiles


def lire_fichier_securise(chemin):
    try:
        ficher_chemin = Path(chemin)

        if not ficher_chemin.exists():
            raise FileNotFoundError('le fichier "inexistant.txt" n’existe pas.')

        with ficher_chemin.open('r', encoding='utf-8'):
             print('Contenu du fichier renvoye sous forme de liste de lignes.')
    except:
        raise

# lire_fichier_securise("courses.txt")
# lire_fichier_securise("inexistant.txt")


# 4.2 — Import CSV : calculer_moyenne_csv(chemin)

import csv

def calculer_moyenne_csv(chemin):
    summe = 0
    count_note = 0
    try:
        ficher_chemin = Path(chemin)
        if not ficher_chemin.exists():
            raise FileNotFoundError(f'le fichier "{chemin}" n’existe pas.')
        with ficher_chemin.open('r', encoding='utf-8') as ficher:
            reader = csv.DictReader(ficher)
            for row in reader:
                try:
                    if not row['note'].isdigit():
                        raise ValueError(f'Attention : note invalide pour "{row["nom"]}" ("{row["note"]}"), ligne ignoree.')
                    summe += int(row['note'])
                    count_note += 1
                except ValueError as error:
                    print(error)
    except Exception as message:
        print(message)
        raise

    print(f'Moyenne calculee ({count_note} notes valides) : {(summe / count_note):.2f}')


# calculer_moyenne_csv('notes.csv')

# 4.3 — Mini-challenge final : journal de commandes

stock = {"pommes": 20, "bananes": 4, "oranges": 15}
commandes_brutes = [
    "pommes,5",
    "bananes,10",
    "kiwis,2",
    "oranges,abc",
    "oranges,5",
]

from io import TextIOWrapper

def log(file_path: TextIOWrapper, status: str, message: str):
    file_path.write(f"[{status}] {message}\n")

try:
    FILE_PATH = Path('journal.txt')
    if not FILE_PATH.exists():
        raise FileNotFoundError(f'le fichier "journal.txt" n’existe pas.')

    with FILE_PATH.open('a') as ficher:
        for commande in commandes_brutes:
            produit, quntite = commande.split(',')
            if produit not in stock.keys():
                log(ficher, 'ERREUR', f'{produit} : produit inconnu')
            elif not quntite.isdigit():
                log(ficher, 'ERREUR', f'{produit} : quantite invalide ("{quntite}")')
            elif int(quntite) > stock[produit]:
                log(ficher, 'ERREUR', f'{produit} : stock insuffisant (demande {quntite}, dispo {stock[produit]})')
            else:
                log(ficher, 'OK', f'{produit} : -{quntite} (reste {stock[produit] - int(quntite)})')

except FileNotFoundError as message:
    print(message)