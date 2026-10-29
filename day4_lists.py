films = [
    "Runner in the labirint 1",
    "Jymanji",
    "Rembo",
    "Best of the best",
    "Big mom"
]

films.append("Runner in the labirint 2")
films.append("Divergent 1")
films.remove("Big mom")
print(len(films))

films.sort()
print(films)
print(films[:3])

for i, film in enumerate(films, start=1):
    print(f"{i}. {film}")