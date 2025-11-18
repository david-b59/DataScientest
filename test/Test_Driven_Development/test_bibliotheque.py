import bibliotheque

def test_ajouter_livre():
	lib = bibliotheque.Bibliotheque()
	livre = bibliotheque.Livre("Harry Potter", "J. K. Rowling")
	lib.ajouter_livre(livre)
	assert lib.lister_livres() == [(livre.titre, livre.auteur)]

def test_supprimer_livre():
        lib = bibliotheque.Bibliotheque()
        livre = bibliotheque.Livre("Harry Potter", "J. K. Rowling")
	lib.ajouter_livre(livre)  
        lib.supprimer_livre(livre.titre)
        assert lib.lister_livres() == []

def test_rechercher_livres_par_auteur():
        lib = bibliotheque.Bibliotheque()
        livre1 = bibliotheque.Livre("Harry Potter", "J. K. Rowling")
	livre2 = bibliotheque.Livre("Le Sorceleur", "Andrzej Sapkowski")   
        lib.ajouter_livre(livre1)
	lib.ajouter_livre(livre2)
	livres = lib.rechercher_livres_par_auteur("J. K. Rowling")
        assert livres == [(livre1.titre, livre1.auteur)]

def test_generation_stat():
	lib = bibliotheque.Bibliotheque()
        livre1 = bibliotheque.Livre("Harry Potter", "J. K. Rowling")  
        livre2 = bibliotheque.Livre("Le Sorceleur", "Andrzej Sapkowski")   
        lib.ajouter_livre(livre1)
        lib.ajouter_livre(livre2)
	stats = lib.generer_stat()
	assert stats == {
		'nombre_livres' : 2,
		'auteur_uniques' : {'J. K.Rowling', 'Andrzej Sapkowski'},
	}
