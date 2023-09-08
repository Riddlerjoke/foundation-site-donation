from flask import Flask, render_template, request
from data import Data

from connexion import Connexion

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/a-propos')
def about():
    return render_template('about.html')


@app.route('/don')
def donate():
    return render_template('donate.html')


@app.route('/givers', methods=['GET'])
def donateurs():
        donateurs = Data.get_thx()
        total_des_fonds = Data.get_total_don()
        return render_template('givers.html', donateurs=donateurs, total_des_fonds=total_des_fonds)


@app.route('/confirmation')
def confirmation():
    donation = ()
    print(donation)
    montant = int
    print(montant)
    for donateur in donation:
        montant += donateur[2]
    return render_template('confirmation.html')


@app.route('/confirmation', methods=['POST'])
def sauvegarder_don():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    email = request.form.get('adress_mail')
    montant_don = int(request.form.get('donation'))
    Data.save_entry(nom, prenom, email, montant_don)
    return render_template('confirmation.html', nom=nom, montant_don=montant_don)





































# from flask import Flask, render_template,request
# from models.connexion import Connexion
#
#
# app = Flask(__name__)
#
# # Page d'accueil
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Page À Propos
# @app.route('/')
# def about():
#     return render_template('about.html')
#
# @app.route('/donnateur')
# def donator():
#     # Se connecter à la base de données
#     cursor = Connexion.connecter()
#
#     # Exécuter une requête pour récupérer les données des donateurs (exemple)
#     cursor.execute("SELECT nom, donation FROM mecene")
#     donateurs = cursor.fetchall()
#
#     # Fermer la connexion
#     Connexion.deconnecter()
#
#     # Passer les données récupérées à la template donate.html
#     return render_template('givers.html', donateurs=donateurs)
#
#
# @app.route('/formulaire', methods=['GET', 'POST'])
# def formulaire():
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.form['nom']
#         prenom = request.form['prenom']
#         email = request.form['email']
#         donation = request.form['montant']
#
#         # Se connecter à la base de données
#         cursor = Connexion.connecter()
#
#         # Exécuter une requête pour insérer le person_who_donate dans la table "donateurs"
#         query = "INSERT INTO donateurs (nom, prenom, adress_mail, donation) VALUES (%s, %s, %s, %s)"
#         values = (nom, prenom, email, donation)
#         cursor.execute(query, values)
#         Connexion.bdd.commit()
#
#         # Fermer la connexion
#         Connexion.deconnecter()
#
#         # Rediriger vers une page de confirmation (vous pouvez créer une page spécifique pour cela)
#         return render_template('confirmation.html', nom=nom, montant_don=montant_don)
#
# @app.route('/sauvegarder_don', methods=['POST'])
# def sauvegarder_don():
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.form['nom']
#         prenom = request.form['prenom']
#         email = request.form['adresse mail']
#         donation = request.form['montant don']
#
#         # Se connecter à la base de données
#         cursor = Connexion.connecter()
#
#         # Exécuter une requête pour insérer le don dans la table "donateurs"
#         query = "INSERT INTO donateurs (nom, prenom, adress_mail, donation) VALUES (%s, %s, %s, %s)"
#         values = (nom, prenom, email, donation)
#         cursor.execute(query, values)
#         Connexion.bdd.commit()
#
#         # Fermer la connexion
#         Connexion.deconnecter()
#
#         # Rediriger vers une page de confirmation (vous pouvez créer une page spécifique pour cela)
#         return render_template('confirmation.html', nom=nom, donation=donation)
#
#     return render_template('donate.html')
# if __name__ == '__main__':
#     app.run(debug=True)