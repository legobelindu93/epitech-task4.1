
# Nombres à traiter
nombres = [12.24, 424242.8412]

for n in nombres:
    # On transforme le nombre en chaîne pour extraire la partie après la virgule
    decimal_str = str(n).split(".")[1]  # tout ce qui est après le '.'
    print("Nombre :", n)
    print("Partie décimale :", decimal_str)
    print("-----")
