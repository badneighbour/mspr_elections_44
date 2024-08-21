from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine('sqlite:///mspr.db')

metadata = MetaData()

metadata.reflect(bind=engine)

# Accéder aux tables spécifiques
communes_table = Table('Communes', metadata, autoload_with=engine)
resultats_2017_t1_table = Table('Resultats_Electoraux_Tour1_2017', metadata, autoload_with=engine)
resultats_2017_t2_table = Table('Resultats_Electoraux_Tour2_2017', metadata, autoload_with=engine)
resultats_2022_t1_table = Table('Resultats_Electoraux_Tour1_2022', metadata, autoload_with=engine)
resultats_2022_t2_table = Table('Resultats_Electoraux_Tour2_2022', metadata, autoload_with=engine)
socio_eco_table = Table('Donnees_SocioEconomiques', metadata, autoload_with=engine)
rsa_table = Table('Donnees_RSA', metadata, autoload_with=engine)
securite_table = Table('Securite', metadata, autoload_with=engine)
associations_table = Table('Associations_Utilite_Publique', metadata, autoload_with=engine)
population_table = Table('Population', metadata, autoload_with=engine)
repertoire_national_table = Table('Repertoire_Asso_National', metadata, autoload_with=engine)

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()

# Lecture des fichiers CSV
data_communes = pd.read_csv('234400034_communes-des-pays-de-la-loire.csv', sep=';', on_bad_lines='skip')
data_socio_eco = pd.read_csv('dares_defm_communales_filtre.csv')
data_resultats_2017_t1 = pd.read_csv('presidentielle2017_T1_filtre.csv')
data_resultats_2017_t2 = pd.read_csv('presidentielle2017_T2_filtre.csv')
data_resultats_2022_t1 = pd.read_csv('presidentielle2022_T1_filtre.csv')
data_resultats_2022_t2 = pd.read_csv('presidentielle2022_T2_filtre.csv')
data_rsa = pd.read_csv('RSA par commune Loire-Atlantique_traitées.csv', sep=';')
data_securite = pd.read_csv('Data sécurité par commune Loire-Atlantique_traitées (1).csv', sep=';')
data_associations = pd.read_csv('filtered_asso_utilite_publique.csv', sep=';', on_bad_lines='skip')
data_population = pd.read_csv('dossier_complet.csv', sep=';')
data_repertoire_national = pd.read_csv('filtred_repertoire_national_asso.csv', sep=';', on_bad_lines='skip')

# Insertion dans la table Communes
for _, row in data_communes.iterrows():
    insert_stmt = communes_table.insert().values(
        Code_Commune=row['INSEE'],
        Libelle_Commune=row['Libellé commune']
    )
    session.execute(insert_stmt)

# Insertion dans la table Donnees_SocioEconomiques
for _, row in data_socio_eco.iterrows():
    insert_stmt = socio_eco_table.insert().values(
        Date=row['Date'],
        Code_Commune=row['Code commune'],
        Libelle_Commune=row['Commune'],
        Sexe=row['Sexe'],
        Tranche_Age=row['Tranche age'],
        Nombre_Demandeurs_Emploi=row['Nombre de demandeurs d_emploi']
    )
    session.execute(insert_stmt)

for col in data_resultats_2017_t1.columns:
    if data_resultats_2017_t1[col].dtype == 'object':  # Vérifier si la colonne est de type chaîne de caractères
        data_resultats_2017_t1[col] = data_resultats_2017_t1[col].str.replace(',', '.').astype(float, errors='ignore')

for _, row in data_resultats_2017_t1.iterrows():
    insert_stmt = resultats_2017_t1_table.insert().values(
        Code_Commune=row['Code de la commune'],
        Code_Departement=row['Code du département'],
        Libelle_Departement=row['Libellé du département'],
        Code_Circonscription=row['Code de la circonscription'],
        Libelle_Circonscription=row['Libellé de la circonscription'],
        Code_Bureau_Vote=row['Code du b.vote'],
        Inscrits=row['Inscrits'],
        Abstentions=row['Abstentions'],
        Pourcentage_Abs_Ins=row['% Abs/Ins'],
        Votants=row['Votants'],
        Pourcentage_Vot_Ins=row['% Vot/Ins'],
        Blancs=row['Blancs'],
        Pourcentage_Blancs_Ins=row['% Blancs/Ins'],
        Pourcentage_Blancs_Vot=row['% Blancs/Vot'],
        Nuls=row['Nuls'],
        Pourcentage_Nuls_Ins=row['% Nuls/Ins'],
        Pourcentage_Nuls_Vot=row['% Nuls/Vot'],
        Exprimes=row['Exprimés'],
        Pourcentage_Exp_Ins=row['% Exp/Ins'],
        Pourcentage_Exp_Vot=row['% Exp/Vot'],
        Nom_Candidat1=row['Nomct1'],
        Prenom_Candidat1=row['Prénomct1'],
        Voix_Candidat1=row['Voixct1'],
        Pourcentage_Voix_Ins_Candidat1=row['% Voix/Insct1'],
        Pourcentage_Voix_Exp_Candidat1=row['% Voix/Expct1'],
        Nom_Candidat2=row['Nomct2'],
        Prenom_Candidat2=row['Prénomct2'],
        Voix_Candidat2=row['Voixct2'],
        Pourcentage_Voix_Ins_Candidat2=row['% Voix/Insct2'],
        Pourcentage_Voix_Exp_Candidat2=row['% Voix/Expct2'],
        Nom_Candidat3=row['Nomct3'],
        Prenom_Candidat3=row['Prénomct3'],
        Voix_Candidat3=row['Voixct3'],
        Pourcentage_Voix_Ins_Candidat3=row['% Voix/Insct3'],
        Pourcentage_Voix_Exp_Candidat3=row['% Voix/Expct3'],
        Nom_Candidat4=row['Nomct4'],
        Prenom_Candidat4=row['Prénomct4'],
        Voix_Candidat4=row['Voixct4'],
        Pourcentage_Voix_Ins_Candidat4=row['% Voix/Insct4'],
        Pourcentage_Voix_Exp_Candidat4=row['% Voix/Expct4'],
        Nom_Candidat5=row['Nomct5'],
        Prenom_Candidat5=row['Prénomct5'],
        Voix_Candidat5=row['Voixct5'],
        Pourcentage_Voix_Ins_Candidat5=row['% Voix/Insct5'],
        Pourcentage_Voix_Exp_Candidat5=row['% Voix/Expct5'],
        Nom_Candidat6=row['Nomct6'],
        Prenom_Candidat6=row['Prénomct6'],
        Voix_Candidat6=row['Voixct6'],
        Pourcentage_Voix_Ins_Candidat6=row['% Voix/Insct6'],
        Pourcentage_Voix_Exp_Candidat6=row['% Voix/Expct6'],
        Nom_Candidat7=row['Nomct7'],
        Prenom_Candidat7=row['Prénomct7'],
        Voix_Candidat7=row['Voixct7'],
        Pourcentage_Voix_Ins_Candidat7=row['% Voix/Insct7'],
        Pourcentage_Voix_Exp_Candidat7=row['% Voix/Expct7'],
        Nom_Candidat8=row['Nomct8'],
        Prenom_Candidat8=row['Prénomct8'],
        Voix_Candidat8=row['Voixct8'],
        Pourcentage_Voix_Ins_Candidat8=row['% Voix/Insct8'],
        Pourcentage_Voix_Exp_Candidat8=row['% Voix/Expct8'],
        Nom_Candidat9=row['Nomct9'],
        Prenom_Candidat9=row['Prénomct9'],
        Voix_Candidat9=row['Voixct9'],
        Pourcentage_Voix_Ins_Candidat9=row['% Voix/Insct9'],
        Pourcentage_Voix_Exp_Candidat9=row['% Voix/Expct9'],
        Nom_Candidat10=row['Nomct10'],
        Prenom_Candidat10=row['Prénomct10'],
        Voix_Candidat10=row['Voixct10'],
        Pourcentage_Voix_Ins_Candidat10=row['% Voix/Insct10'],
        Pourcentage_Voix_Exp_Candidat10=row['% Voix/Expct10'],
        Nom_Candidat11=row['Nomct11'],
        Prenom_Candidat11=row['Prénomct11'],
        Voix_Candidat11=row['Voixct11'],
        Pourcentage_Voix_Ins_Candidat11=row['% Voix/Insct11'],
        Pourcentage_Voix_Exp_Candidat11=row['% Voix/Expct11']
    )
    session.execute(insert_stmt)

for col in data_resultats_2017_t2.columns:
    if data_resultats_2017_t2[col].dtype == 'object':  # Vérifier si la colonne est de type chaîne de caractères
        data_resultats_2017_t2[col] = data_resultats_2017_t2[col].str.replace(',', '.').astype(float, errors='ignore')

# Insertion dans la table Resultats_Electoraux_2017_T2 (Deuxième Tour)
for _, row in data_resultats_2017_t2.iterrows():
    insert_stmt = resultats_2017_t2_table.insert().values(
        Code_Commune=row['Code de la commune'],
        Code_Departement=row['Code du département'],
        Libelle_Departement=row['Libellé du département'],
        Code_Circonscription=row['Code de la circonscription'],
        Libelle_Circonscription=row['Libellé de la circonscription'],
        Code_Bureau_Vote=row['Code du b.vote'],
        Inscrits=row['Inscrits'],
        Abstentions=row['Abstentions'],
        Pourcentage_Abs_Ins=row['% Abs/Ins'],
        Votants=row['Votants'],
        Pourcentage_Vot_Ins=row['% Vot/Ins'],
        Blancs=row['Blancs'],
        Pourcentage_Blancs_Ins=row['% Blancs/Ins'],
        Pourcentage_Blancs_Vot=row['% Blancs/Vot'],
        Nuls=row['Nuls'],
        Pourcentage_Nuls_Ins=row['% Nuls/Ins'],
        Pourcentage_Nuls_Vot=row['% Nuls/Vot'],
        Exprimes=row['Exprimés'],
        Pourcentage_Exp_Ins=row['% Exp/Ins'],
        Pourcentage_Exp_Vot=row['% Exp/Vot'],
        Nom_Candidat1=row['Nomct1'],
        Prenom_Candidat1=row['Prénomct1'],
        Voix_Candidat1=row['Voixct1'],
        Pourcentage_Voix_Ins_Candidat1=row['% Voix/Insct1'],
        Pourcentage_Voix_Exp_Candidat1=row['% Voix/Expct1'],
        Nom_Candidat2=row['Nomct2'],
        Prenom_Candidat2=row['Prénomct2'],
        Voix_Candidat2=row['Voixct2'],
        Pourcentage_Voix_Ins_Candidat2=row['% Voix/Insct2'],
        Pourcentage_Voix_Exp_Candidat2=row['% Voix/Expct2'],
    )
    session.execute(insert_stmt)

# Insertion dans la table Resultats_Electoraux_2022_T1 (Premier Tour)
for _, row in data_resultats_2022_t1.iterrows():
    insert_stmt = resultats_2022_t1_table.insert().values(
        Code_Commune=row['Code de la commune'],
        Code_Departement=row['Code du département'],
        Libelle_Departement=row['Libellé du département'],
        Code_Circonscription=row['Code de la circonscription'],
        Libelle_Circonscription=row['Libellé de la circonscription'],
        Code_Bureau_Vote=row['Code du b.vote'],
        Inscrits=row['Inscrits'],
        Abstentions=row['Abstentions'],
        Pourcentage_Abs_Ins=row['% Abs/Ins'],
        Votants=row['Votants'],
        Pourcentage_Vot_Ins=row['% Vot/Ins'],
        Blancs=row['Blancs'],
        Pourcentage_Blancs_Ins=row['% Blancs/Ins'],
        Pourcentage_Blancs_Vot=row['% Blancs/Vot'],
        Nuls=row['Nuls'],
        Pourcentage_Nuls_Ins=row['% Nuls/Ins'],
        Pourcentage_Nuls_Vot=row['% Nuls/Vot'],
        Exprimes=row['Exprimés'],
        Pourcentage_Exp_Ins=row['% Exp/Ins'],
        Pourcentage_Exp_Vot=row['% Exp/Vot'],
        Nom_Candidat=row['Nom'],
        Prenom_Candidat=row['Prénom'],
        Voix_Candidat=row['Voix'],
        Pourcentage_Voix_Ins_Candidat=row['% Voix/Ins'],
        Pourcentage_Voix_Exp_Candidat=row['% Voix/Exp'],
        Nom_Candidat1=row['Nomct1'],
        Prenom_Candidat1=row['Prénomct1'],
        Voix_Candidat1=row['Voixct1'],
        Pourcentage_Voix_Ins_Candidat1=row['% Voix/Insct1'],
        Pourcentage_Voix_Exp_Candidat1=row['% Voix/Expct1'],
        Nom_Candidat2=row['Nomct2'],
        Prenom_Candidat2=row['Prénomct2'],
        Voix_Candidat2=row['Voixct2'],
        Pourcentage_Voix_Ins_Candidat2=row['% Voix/Insct2'],
        Pourcentage_Voix_Exp_Candidat2=row['% Voix/Expct2'],
        Nom_Candidat3=row['Nomct3'],
        Prenom_Candidat3=row['Prénomct3'],
        Voix_Candidat3=row['Voixct3'],
        Pourcentage_Voix_Ins_Candidat3=row['% Voix/Insct3'],
        Pourcentage_Voix_Exp_Candidat3=row['% Voix/Expct3'],
        Nom_Candidat4=row['Nomct4'],
        Prenom_Candidat4=row['Prénomct4'],
        Voix_Candidat4=row['Voixct4'],
        Pourcentage_Voix_Ins_Candidat4=row['% Voix/Insct4'],
        Pourcentage_Voix_Exp_Candidat4=row['% Voix/Expct4'],
        Nom_Candidat5=row['Nomct5'],
        Prenom_Candidat5=row['Prénomct5'],
        Voix_Candidat5=row['Voixct5'],
        Pourcentage_Voix_Ins_Candidat5=row['% Voix/Insct5'],
        Pourcentage_Voix_Exp_Candidat5=row['% Voix/Expct5'],
        Nom_Candidat6=row['Nomct6'],
        Prenom_Candidat6=row['Prénomct6'],
        Voix_Candidat6=row['Voixct6'],
        Pourcentage_Voix_Ins_Candidat6=row['% Voix/Insct6'],
        Pourcentage_Voix_Exp_Candidat6=row['% Voix/Expct6'],
        Nom_Candidat7=row['Nomct7'],
        Prenom_Candidat7=row['Prénomct7'],
        Voix_Candidat7=row['Voixct7'],
        Pourcentage_Voix_Ins_Candidat7=row['% Voix/Insct7'],
        Pourcentage_Voix_Exp_Candidat7=row['% Voix/Expct7'],
        Nom_Candidat8=row['Nomct8'],
        Prenom_Candidat8=row['Prénomct8'],
        Voix_Candidat8=row['Voixct8'],
        Pourcentage_Voix_Ins_Candidat8=row['% Voix/Insct8'],
        Pourcentage_Voix_Exp_Candidat8=row['% Voix/Expct8'],
        Nom_Candidat9=row['Nomct9'],
        Prenom_Candidat9=row['Prénomct9'],
        Voix_Candidat9=row['Voixct9'],
        Pourcentage_Voix_Ins_Candidat9=row['% Voix/Insct9'],
        Pourcentage_Voix_Exp_Candidat9=row['% Voix/Expct9'],
        Nom_Candidat10=row['Nomct10'],
        Prenom_Candidat10=row['Prénomct10'],
        Voix_Candidat10=row['Voixct10'],
        Pourcentage_Voix_Ins_Candidat10=row['% Voix/Insct10'],
        Pourcentage_Voix_Exp_Candidat10=row['% Voix/Expct10'],
        Nom_Candidat11=row['Nomct11'],
        Prenom_Candidat11=row['Prénomct11'],
        Voix_Candidat11=row['Voixct11'],
        Pourcentage_Voix_Ins_Candidat11=row['% Voix/Insct11'],
        Pourcentage_Voix_Exp_Candidat11=row['% Voix/Expct11']
    )
    session.execute(insert_stmt)

# Insertion dans la table Resultats_Electoraux_2022_T2 (Deuxième Tour)
for _, row in data_resultats_2022_t2.iterrows():
    insert_stmt = resultats_2022_t2_table.insert().values(
        Code_Commune=row['Code de la commune'],
        Code_Departement=row['Code du département'],
        Libelle_Departement=row['Libellé du département'],
        Code_Circonscription=row['Code de la circonscription'],
        Libelle_Circonscription=row['Libellé de la circonscription'],
        Code_Bureau_Vote=row['Code du b.vote'],
        Inscrits=row['Inscrits'],
        Abstentions=row['Abstentions'],
        Pourcentage_Abs_Ins=row['% Abs/Ins'],
        Votants=row['Votants'],
        Pourcentage_Vot_Ins=row['% Vot/Ins'],
        Blancs=row['Blancs'],
        Pourcentage_Blancs_Ins=row['% Blancs/Ins'],
        Pourcentage_Blancs_Vot=row['% Blancs/Vot'],
        Nuls=row['Nuls'],
        Pourcentage_Nuls_Ins=row['% Nuls/Ins'],
        Pourcentage_Nuls_Vot=row['% Nuls/Vot'],
        Exprimes=row['Exprimés'],
        Pourcentage_Exp_Ins=row['% Exp/Ins'],
        Pourcentage_Exp_Vot=row['% Exp/Vot'],
        Nom_Candidat1=row['Nom'],
        Prenom_Candidat1=row['Prénom'],
        Voix_Candidat1=row['Voix'],
        Pourcentage_Voix_Ins_Candidat1=row['% Voix/Ins'],
        Pourcentage_Voix_Exp_Candidat1=row['% Voix/Exp'],
        Nom_Candidat2=row['Nomct1'],
        Prenom_Candidat2=row['Prénomct1'],
        Voix_Candidat2=row['Voixct1'],
        Pourcentage_Voix_Ins_Candidat2=row['% Voix/Insct1'],
        Pourcentage_Voix_Exp_Candidat2=row['% Voix/Expct1']
    )
    session.execute(insert_stmt)

# Insertion dans la table RSA
for _, row in data_rsa.iterrows():
    insert_stmt = rsa_table.insert().values(
        Code_Commune=row['code_commune'],
        Libelle=row['libelle'],
        Nombre_Beneficiaires_RSA=row['nb_benef_rsa'],
        Annee=row['annee']
    )
    session.execute(insert_stmt)

for col in data_securite.columns:
    if data_securite[col].dtype == 'object':
        data_securite[col] = data_securite[col].str.replace(',', '.')
        # Tenter de convertir la colonne en flottant
        try:
            data_securite[col] = data_securite[col].astype(float)
        except ValueError:
            # Remplacer les valeurs non convertibles par NaN
            data_securite[col] = pd.to_numeric(data_securite[col], errors='coerce')

# Insertion dans la table Securite
for _, row in data_securite.iterrows():
    insert_stmt = securite_table.insert().values(
        Code_Commune=row['CODGEO_2024'],
        Annee=row['annee'],
        Classe=row['classe'],
        Unite_De_Compte=row['unité.de.compte'],
        Valeur_Publiee=row['valeur.publiée'],
        Faits=row['faits'],
        Taux_Pour_Mille=row['tauxpourmille'],
        Population=row['POP'],
        Mill_POP=row['millPOP'],
        Logements=row['LOG'],
        Mill_LOG=row['millLOG']
    )
    session.execute(insert_stmt)


# Insertion dans la table Associations
for _, row in data_associations.iterrows():
    insert_stmt = associations_table.insert().values(
        Numero_RNA=row['NUMERO RNA'],
        Nom=row['NOM'],
        Date_Reconnaissance_Utilite_Publique=row["DATE DE RECONNAISSANCE D'UTILITE PUBLIQUE"],
        Date_Derniere_Modification_Statutaire=row["DATE DE DERNIERE MODIFICATION STATUTAIRE"],
        Code_Commune=row['CP'],
        Ville=row['VILLE']
    )
    session.execute(insert_stmt)

# Insertion dans la table Dossier_Complet
for _, row in data_population.iterrows():
    insert_stmt = population_table.insert().values(
        Code_Commune=row['CODGEO'],
        Population_en_2021=row['Population_en_2021'],
        Pop_0_14_ans_en_2021=row['Pop_0_14_ans_en_2021'],
        Pop_15_29_ans_en_2021=row['Pop_15_29_ans_en_2021'],
        Pop_30_44_ans_en_2021=row['Pop_30_44_ans_en_2021'],
        Pop_45_59_ans_en_2021=row['Pop_45_59_ans_en_2021'],
        Pop_60_74_ans_en_2021=row['Pop_60_74_ans_en_2021'],
        Pop_75_89_ans_en_2021=row['Pop_75_89_ans_en_2021'],
        Pop_90_ans_ou_plus_en_2021=row['Pop_90_ans_ou_plus_en_2021'],
        Pop_Hommes_en_2021=row['Pop_Hommes_en_2021'],
        Pop_Femmes_en_2021=row['Pop_Femmes_en_2021'],
        Pop_15_ans_ou_plus_Retraites_en_2021=row['Pop_15_ans_ou_plus_Retraités_en_2021'],
        Population_en_2015=row['Population_en_2015'],
        Pop_0_14_ans_en_2015=row['Pop_0_14_ans_en_2015'],
        Pop_15_29_ans_en_2015=row['Pop_15_29_ans_en_2015'],
        Pop_30_44_ans_en_2015=row['Pop_30_44_ans_en_2015'],
        Pop_45_59_ans_en_2015=row['Pop_45_59_ans_en_2015'],
        Pop_60_74_ans_en_2015=row['Pop_60_74_ans_en_2015'],
        Pop_75_89_ans_en_2015=row['Pop_75_89_ans_en_2015'],
        Pop_90_ans_ou_plus_en_2015=row['Pop_90_ans_ou_plus_en_2015'],
        Pop_Hommes_en_2015=row['Pop_Hommes_en_2015'],
        Pop_Femmes_en_2015=row['Pop_Femmes_en_2015'],
        Pop_15_ans_ou_plus_Retraites_en_2015=row['Pop_15_ans_ou_plus_Retraités_en_2015'],
        Population_en_2010=row['Population_en_2010'],
        Pop_0_14_ans_en_2010=row['Pop_0_14_ans_en_2010'],
        Pop_15_29_ans_en_2010=row['Pop_15_29_ans_en_2010'],
        Pop_30_44_ans_en_2010=row['Pop_30_44_ans_en_2010'],
        Pop_45_59_ans_en_2010=row['Pop_45_59_ans_en_2010'],
        Pop_60_74_ans_en_2010=row['Pop_60_74_ans_en_2010'],
        Pop_Hommes_en_2010=row['Pop_Hommes_en_2010'],
        Pop_Femmes_en_2010=row['Pop_Femmes_en_2010'],
        Pop_15_ans_ou_plus_Retraites_en_2010=row['Pop_15_ans_ou_plus_Retraités__en_2010'],
        Chomeurs_15_64_ans_en_2021=row['Chômeurs_15_64_ans_en_2021'],
        Chomeurs_15_64_ans_en_2015=row['Chômeurs_15_64_ans_en_2015'],
        Chomeurs_15_64_ans_en_2010=row['Chômeurs_15_64_ans_en_2010'],
        Salaire_net_horaire_moyen_en_2021=row['Salaire_net_horaire_moyen_en_2021']
    )
    session.execute(insert_stmt)

# Insertion dans la table Repertoire_National 
for _, row in data_repertoire_national.iterrows():
    insert_stmt = repertoire_national_table.insert().values(
        Date_Creation=row['date_creat'],
        Date_Declaration=row['date_decla'],
        Date_Publication=row['date_publi'],
        Date_Dissolution=row['date_disso'],
        Titre=row['titre'],
        Objet_Social1=row['objet_social1'],
        Objet_Social2=row['objet_social2'],
        Code_Commune=row['adrs_codeinsee'],
        Code_Postal=row['adrs_codepostal'],
        Libelle_Commune=row['adrs_libcommune']
    )
    session.execute(insert_stmt)

# Commit des transactions
session.commit()

# Fermeture de la session
session.close()
