import bibliotheque



def test_ajouter_livre():

    lib = bibliotheque.Bibliotheque()

    livre = bibliotheque.Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")

    lib.ajouter_livre(livre)

    assert lib.lister_livres() == [(livre.titre, livre.auteur)]



def test_supprimer_livre():

    lib = bibliotheque.Bibliotheque()

    livre = bibliotheque.Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")

    lib.ajouter_livre(livre)

    lib.supprimer_livre(livre.titre)

    assert lib.lister_livres() == []



def test_rechercher_livres_par_auteur():

    lib = bibliotheque.Bibliotheque()

    livre1 = bibliotheque.Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")

    livre2 = bibliotheque.Livre("Harry Potter", "J.K. Rowling")

    lib.ajouter_livre(livre1)

    lib.ajouter_livre(livre2)

    livres = lib.rechercher_livres_par_auteur("J.R.R. Tolkien")

    assert livres == [(livre1.titre, livre1.auteur)]



def test_statistiques_bibliotheque():

    lib = bibliotheque.Bibliotheque()

    livre1 = bibliotheque.Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")

    livre2 = bibliotheque.Livre("Harry Potter", "J.K. Rowling")

    lib.ajouter_livre(livre1)

    lib.ajouter_livre(livre2)

    stats = lib.generer_statistiques()

    assert stats == {

        "nombre_livres": 2,

        "auteurs_uniques": {"J.R.R. Tolkien", "J.K. Rowling"},

    }

