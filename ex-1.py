nom: str = input('Siasser votre nom: ')
prenom = input('Siasser votre prenom: ')
notes=[]
for i in range(3):
    notes.append(int(input(f'Entrer le note {i + 1} : ')))

moyenne = sum(notes) / len(notes)
print(f"{nom} moyenne : {moyenne:.2f}")