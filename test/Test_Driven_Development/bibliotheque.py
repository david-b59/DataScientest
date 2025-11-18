class Livre:

    def __init__(self, titre: str, auteur: str) -> None:

        self.titre = titre

        self.auteur = auteur



class Bibliotheque:

    def __init__(self) -> None:

        # On stocke les objets Livre dans une liste

        self._livres = []


    def ajouter_livre(self, livre: Livre) -> None:

        """Ajoute un livre dans la bibliothèque."""

        self._livres.append(livre)


    def supprimer_livre(self, titre: str) -> None:

        """

        Supprime un livre à partir de son titre.

        Si plusieurs livres ont le même titre, on supprime le premier trouvé.

        """

        self._livres = [livre for livre in self._livres if livre.titre != titre]


    def lister_livres(self):

        """

        Retourne la liste des livres sous forme de liste de tuples (titre, auteur),

        comme attendu par les tests.

        """

        return [(livre.titre, livre.auteur) for livre in self._livres]


    def rechercher_livres_par_auteur(self, auteur: str):

        """

        Retourne uniquement les livres écrits par l'auteur donné,

        sous forme de liste de tuples (titre, auteur).

        """

        return [

            (livre.titre, livre.auteur)

            for livre in self._livres

            if livre.auteur == auteur

        ]


    def generer_statistiques(self):

        """

        Retourne un dictionnaire contenant :

        - le nombre total de livres

        - l'ensemble des auteurs uniques

        """

        auteurs = {livre.auteur for livre in self._livres}

        return {

            "nombre_livres": len(self._livres),

            "auteurs_uniques": auteurs,

        }

