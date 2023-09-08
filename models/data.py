from models.connexion import Connexion
from models.site import Site
from models.personne import Personne


class Data:
    def client_BDD(self):
        sites = [] 

        cursor = Connexion.connecter()
        request = "SELECT * FROM client;"
        cursor.execute(request)

        for site_lu in cursor:
            sites.append(Site(site_lu[0], site_lu[1]))

        Connexion.deconnecter()
        return sites

    def lister_personne_par_site(self, site_id):
        personnes = []

        cursor = Connexion.connecter()
        request = f"SELECT * FROM utilisateurs WHERE site = {site_id}"
        cursor.execute(request)

        for personne in cursor :
            personnes.append(Personne(personne[1], personne[2]))

        Connexion.deconnecter()

        return personnes