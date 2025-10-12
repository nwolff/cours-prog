import modele_plinko
import modele_receptacle

NOMBRE_DE_JETS = 10_000
TAILLE_PLINKO = 30

if __name__ == "__main__":
    receptacle = modele_receptacle.nouveau_receptacle(TAILLE_PLINKO)
    for _ in range(NOMBRE_DE_JETS):
        trajectoire = modele_plinko.simuler(TAILLE_PLINKO)
        x_de_sortie, _ = trajectoire[-1]
        modele_receptacle.ajouter_au_godet(receptacle, x_de_sortie)

    print(receptacle)
