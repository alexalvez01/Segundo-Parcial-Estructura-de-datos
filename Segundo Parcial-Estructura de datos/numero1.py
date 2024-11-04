from pokemontree import PokemonTree

pokemones = [
    ("Bulbasaur", 1, ["planta", "veneno"]),
    ("Ivysaur", 2, ["planta", "veneno"]),
    ("Venusaur", 3, ["planta", "veneno"]),
    ("Charmander", 4, ["fuego"]),
    ("Charmeleon", 5, ["fuego"]),
    ("Charizard", 6, ["fuego", "volador"]),
    ("Squirtle", 7, ["agua"]),
    ("Wartortle", 8, ["agua"]),
    ("Blastoise", 9, ["agua"]),
    ("Pikachu", 25, ["eléctrico"]),
    ("Raichu", 26, ["eléctrico"]),
    ("Jolteon", 135, ["eléctrico"]),
    ("Chikorita", 152, ["planta"]),
    ("Cyndaquil", 155, ["fuego"]),
    ("Totodile", 158, ["agua"]),
    ("Treecko", 252, ["planta"]),
    ("Kommo-o", 784, ["dragón", "lucha"]),
    ("Torchic", 255, ["fuego"]),
    ("Mudkip", 258, ["agua"]),
    ("Turtwig", 387, ["planta"]),
    ("Chimchar", 390, ["fuego"]),
    ("Piplup", 393, ["agua"]),
    ("Snivy", 495, ["planta"]),
    ("Tepig", 498, ["fuego"]),
    ("Oshawott", 501, ["agua"]),
    ("Fennekin", 653, ["fuego"]),
    ("Froakie", 656, ["agua"]),
    ("Rowlet", 722, ["planta", "volador"]),
    ("Litten", 725, ["fuego"]),
    ("Ho-Oh", 250, ["fuego", "volador"]),
    ("Popplio", 728, ["agua"]),
    ("Grookey", 810, ["planta"]),
    ("Scorbunny", 813, ["fuego"]),
    ("Sobble", 816, ["agua"]),
    ("Lycanroc", 745, ["roca"]),
    ("Tyrantrum", 697, ["roca", "dragón"]),
    ("Magnemite", 81, ["eléctrico", "acero"]),
    ("Magneton", 82, ["eléctrico", "acero"]),
    ("Porygon-Z", 474, ["normal"]),
    ("Hakamo-o", 783, ["dragón", "lucha"]),
    ("Tapu-Bulu", 787, ["planta", "hada"]),
]

pokemon_por_nombre = PokemonTree("nombre")
pokemon_por_numero = PokemonTree("numero")
pokemon_por_tipo = PokemonTree("tipo")

for nombre, numero, tipos in pokemones:
    pokemon_por_nombre.insertar(nombre, numero, tipos)
    pokemon_por_numero.insertar(nombre, numero, tipos)
    pokemon_por_tipo.insertar(nombre, numero, tipos)

print("---Datos del pokemon con número 25:")
print(pokemon_por_numero.buscar_por_numero(25))

print("---Datos del pokemon con numero 498:")
print(pokemon_por_numero.buscar_por_numero(498))

print("---Pokemon que contienen 'bul' en su nombre:")
print(pokemon_por_nombre.buscar_por_nombre("bul"))

print("---Pokemones de tipo agua:")
print(pokemon_por_tipo.lista_por_tipo("agua"))

print("---Pokemon en orden ascendente por número:")
print(pokemon_por_numero.in_order())
print("---Pokemon en orden ascendente por nombre:")
print(pokemon_por_nombre.in_order())

print("---Listado de pokemon por nivel:")
print(pokemon_por_nombre.by_level())

print("---Datos de Jolteon:")
print(pokemon_por_nombre.buscar_por_nombre("Jolteon"))
print("---Datos de Lycanroc:")
print(pokemon_por_nombre.buscar_por_nombre("Lycanroc"))
print("---Datos de Tyrantrum:")
print(pokemon_por_nombre.buscar_por_nombre("Tyrantrum"))

print("---Cantidad de pokemones de tipo eléctrico:")
print(len(pokemon_por_tipo.lista_por_tipo("eléctrico")))

print("---Cantidad de pokemones de tipo acero:")
print(len(pokemon_por_tipo.lista_por_tipo("acero")))