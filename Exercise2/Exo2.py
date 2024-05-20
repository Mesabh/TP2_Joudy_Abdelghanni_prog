import csv
pokemon_data = {}


with open("pokemon.csv", "r") as f:
    data = csv.reader(f)
    for ligne in data:
        nom = ligne[0]
        stats = list(map(int, ligne[1:]))
        pokemon_data[nom] = stats

for nom, stats in pokemon_data.items():
    print(f"{nom}: {stats}")

print(isinstance(pokemon_data, dict))
print(isinstance(pokemon_data["Pikachu"], list))
print(isinstance(pokemon_data["Pikachu"][0], int))
