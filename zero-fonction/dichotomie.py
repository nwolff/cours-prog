#!/usr/bin/env python

from icecream import ic

from fonctions import f1 as f

ic.configureOutput(prefix="", includeContext=True)


def methode_dichotomie(a, b, tol, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError(
            "Les valeurs de la fonction aux extrémités de l'intervalle doivent avoir des signes opposés."
        )

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        point_milieu = (a + b) / 2
        ic(iteration, a, f(a), b, f(b), point_milieu, f(point_milieu))
        print()
        if f(point_milieu) == 0:
            return point_milieu  # Trouvé la racine exacte
        elif f(point_milieu) * f(a) < 0:
            b = point_milieu
        else:
            a = point_milieu

        iteration += 1
    return (a + b) / 2


# Exemple d'utilisation :
a = 0.0
b = 32.0
tolerance = 0.001

racine = methode_dichotomie(a, b, tolerance)

print(f"Une racine de la fonction est approximativement : {racine}")
