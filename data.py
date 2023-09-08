from connexion import Connexion


class Data:

    @staticmethod
    def get_total_don():
        cursor = Connexion.connecter()
        request = "SELECT SUM(donation) FROM contributor"
        cursor.execute(request)
        result = cursor.fetchone()
        if result is not None and len(result) > 0:
            total_don = round(result[0])
        else:
            total_don = 0
        Connexion.deconnecter()
        return total_don

    def save_entry(nom, prenom, email, donation):
        cursor = Connexion.connecter()
        query = f"INSERT INTO ipa_donate.contributor(nom, prenom, adress_mail, donation) VALUES('{nom}', '{prenom}', '{email}', {donation})"
        cursor.execute(query)
        Connexion.deconnecter()
        return True

    @staticmethod
    def get_thx():
        cursor = Connexion.connecter()
        request = "SELECT nom, donation FROM contributor;"
        cursor.execute(request)
        personnes = []
        for info in cursor:
            personnes.append(info)

        Connexion.deconnecter()

        return personnes


# print(Data.get_total_don())


    # def set_don():
    #     cursor = Connexion.connecter()
    #     querry = " INSERT INTO ipa_donate.contributor (nom, prenom, adress_mail, donation) VALUES (%s, %s, %s, %s) "
    #     cursor.execute(querry)
    #     personnes = []
    #
    #     for info in cursor:
    #         personnes.append(info)
    #
    #     Connexion.deconnecter()
    #
    #     return personnes


# print(Data.get_don())

# Data.save_entry('test', 'test', 'test@test.com', 10000)