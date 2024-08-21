CREATE TABLE Communes (
    Code_Commune TEXT PRIMARY KEY,
    Libelle_Commune TEXT
);

CREATE TABLE Resultats_Electoraux_Tour1_2017 (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code_Commune TEXT,
    Code_Departement TEXT,
    Libelle_Departement TEXT,
    Code_Circonscription TEXT,
    Libelle_Circonscription TEXT,
    Code_Bureau_Vote TEXT,
    Inscrits INTEGER,
    Abstentions INTEGER,
    Pourcentage_Abs_Ins REAL,
    Votants INTEGER,
    Pourcentage_Vot_Ins REAL,
    Blancs INTEGER,
    Pourcentage_Blancs_Ins REAL,
    Pourcentage_Blancs_Vot REAL,
    Nuls INTEGER,
    Pourcentage_Nuls_Ins REAL,
    Pourcentage_Nuls_Vot REAL,
    Exprimes INTEGER,
    Pourcentage_Exp_Ins REAL,
    Pourcentage_Exp_Vot REAL,
    Nom_Candidat TEXT,
    Prenom_Candidat TEXT,
    Voix_Candidat INTEGER,
    Pourcentage_Voix_Ins_Candidat REAL,
    Pourcentage_Voix_Exp_Candidat REAL,
    Nom_Candidat1 TEXT,
    Prenom_Candidat1 TEXT,
    Voix_Candidat1 INTEGER,
    Pourcentage_Voix_Ins_Candidat1 REAL,
    Pourcentage_Voix_Exp_Candidat1 REAL,
    Nom_Candidat2 TEXT,
    Prenom_Candidat2 TEXT,
    Voix_Candidat2 INTEGER,
    Pourcentage_Voix_Ins_Candidat2 REAL,
    Pourcentage_Voix_Exp_Candidat2 REAL,
    Nom_Candidat3 TEXT,
    Prenom_Candidat3 TEXT,
    Voix_Candidat3 INTEGER,
    Pourcentage_Voix_Ins_Candidat3 REAL,
    Pourcentage_Voix_Exp_Candidat3 REAL,
    Nom_Candidat4 TEXT,
    Prenom_Candidat4 TEXT,
    Voix_Candidat4 INTEGER,
    Pourcentage_Voix_Ins_Candidat4 REAL,
    Pourcentage_Voix_Exp_Candidat4 REAL,
    Nom_Candidat5 TEXT,
    Prenom_Candidat5 TEXT,
    Voix_Candidat5 INTEGER,
    Pourcentage_Voix_Ins_Candidat5 REAL,
    Pourcentage_Voix_Exp_Candidat5 REAL,
    Nom_Candidat6 TEXT,
    Prenom_Candidat6 TEXT,
    Voix_Candidat6 INTEGER,
    Pourcentage_Voix_Ins_Candidat6 REAL,
    Pourcentage_Voix_Exp_Candidat6 REAL,
    Nom_Candidat7 TEXT,
    Prenom_Candidat7 TEXT,
    Voix_Candidat7 INTEGER,
    Pourcentage_Voix_Ins_Candidat7 REAL,
    Pourcentage_Voix_Exp_Candidat7 REAL,
    Nom_Candidat8 TEXT,
    Prenom_Candidat8 TEXT,
    Voix_Candidat8 INTEGER,
    Pourcentage_Voix_Ins_Candidat8 REAL,
    Pourcentage_Voix_Exp_Candidat8 REAL,
    Nom_Candidat9 TEXT,
    Prenom_Candidat9 TEXT,
    Voix_Candidat9 INTEGER,
    Pourcentage_Voix_Ins_Candidat9 REAL,
    Pourcentage_Voix_Exp_Candidat9 REAL,
    Nom_Candidat10 TEXT,
    Prenom_Candidat10 TEXT,
    Voix_Candidat10 INTEGER,
    Pourcentage_Voix_Ins_Candidat10 REAL,
    Pourcentage_Voix_Exp_Candidat10 REAL,
    Nom_Candidat11 TEXT,
    Prenom_Candidat11 TEXT,
    Voix_Candidat11 INTEGER,
    Pourcentage_Voix_Ins_Candidat11 REAL,
    Pourcentage_Voix_Exp_Candidat11 REAL,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Resultats_Electoraux_Tour2_2017 (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code_Commune TEXT,
    Code_Departement TEXT,
    Libelle_Departement TEXT,
    Code_Circonscription TEXT,
    Libelle_Circonscription TEXT,
    Code_Bureau_Vote TEXT,
    Inscrits INTEGER,
    Abstentions INTEGER,
    Pourcentage_Abs_Ins REAL,
    Votants INTEGER,
    Pourcentage_Vot_Ins REAL,
    Blancs INTEGER,
    Pourcentage_Blancs_Ins REAL,
    Pourcentage_Blancs_Vot REAL,
    Nuls INTEGER,
    Pourcentage_Nuls_Ins REAL,
    Pourcentage_Nuls_Vot REAL,
    Exprimes INTEGER,
    Pourcentage_Exp_Ins REAL,
    Pourcentage_Exp_Vot REAL,
    Nom_Candidat1 TEXT,
    Prenom_Candidat1 TEXT,
    Voix_Candidat1 INTEGER,
    Pourcentage_Voix_Ins_Candidat1 REAL,
    Pourcentage_Voix_Exp_Candidat1 REAL,
    Nom_Candidat2 TEXT,
    Prenom_Candidat2 TEXT,
    Voix_Candidat2 INTEGER,
    Pourcentage_Voix_Ins_Candidat2 REAL,
    Pourcentage_Voix_Exp_Candidat2 REAL,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Resultats_Electoraux_Tour1_2022 (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code_Commune TEXT,
    Code_Departement TEXT,
    Libelle_Departement TEXT,
    Code_Circonscription TEXT,
    Libelle_Circonscription TEXT,
    Code_Bureau_Vote TEXT,
    Inscrits INTEGER,
    Abstentions INTEGER,
    Pourcentage_Abs_Ins REAL,
    Votants INTEGER,
    Pourcentage_Vot_Ins REAL,
    Blancs INTEGER,
    Pourcentage_Blancs_Ins REAL,
    Pourcentage_Blancs_Vot REAL,
    Nuls INTEGER,
    Pourcentage_Nuls_Ins REAL,
    Pourcentage_Nuls_Vot REAL,
    Exprimes INTEGER,
    Pourcentage_Exp_Ins REAL,
    Pourcentage_Exp_Vot REAL,
    Nom_Candidat TEXT,
    Prenom_Candidat TEXT,
    Voix_Candidat INTEGER,
    Pourcentage_Voix_Ins_Candidat REAL,
    Pourcentage_Voix_Exp_Candidat REAL,
    Nom_Candidat1 TEXT,
    Prenom_Candidat1 TEXT,
    Voix_Candidat1 INTEGER,
    Pourcentage_Voix_Ins_Candidat1 REAL,
    Pourcentage_Voix_Exp_Candidat1 REAL,
    Nom_Candidat2 TEXT,
    Prenom_Candidat2 TEXT,
    Voix_Candidat2 INTEGER,
    Pourcentage_Voix_Ins_Candidat2 REAL,
    Pourcentage_Voix_Exp_Candidat2 REAL,
    Nom_Candidat3 TEXT,
    Prenom_Candidat3 TEXT,
    Voix_Candidat3 INTEGER,
    Pourcentage_Voix_Ins_Candidat3 REAL,
    Pourcentage_Voix_Exp_Candidat3 REAL,
    Nom_Candidat4 TEXT,
    Prenom_Candidat4 TEXT,
    Voix_Candidat4 INTEGER,
    Pourcentage_Voix_Ins_Candidat4 REAL,
    Pourcentage_Voix_Exp_Candidat4 REAL,
    Nom_Candidat5 TEXT,
    Prenom_Candidat5 TEXT,
    Voix_Candidat5 INTEGER,
    Pourcentage_Voix_Ins_Candidat5 REAL,
    Pourcentage_Voix_Exp_Candidat5 REAL,
    Nom_Candidat6 TEXT,
    Prenom_Candidat6 TEXT,
    Voix_Candidat6 INTEGER,
    Pourcentage_Voix_Ins_Candidat6 REAL,
    Pourcentage_Voix_Exp_Candidat6 REAL,
    Nom_Candidat7 TEXT,
    Prenom_Candidat7 TEXT,
    Voix_Candidat7 INTEGER,
    Pourcentage_Voix_Ins_Candidat7 REAL,
    Pourcentage_Voix_Exp_Candidat7 REAL,
    Nom_Candidat8 TEXT,
    Prenom_Candidat8 TEXT,
    Voix_Candidat8 INTEGER,
    Pourcentage_Voix_Ins_Candidat8 REAL,
    Pourcentage_Voix_Exp_Candidat8 REAL,
    Nom_Candidat9 TEXT,
    Prenom_Candidat9 TEXT,
    Voix_Candidat9 INTEGER,
    Pourcentage_Voix_Ins_Candidat9 REAL,
    Pourcentage_Voix_Exp_Candidat9 REAL,
    Nom_Candidat10 TEXT,
    Prenom_Candidat10 TEXT,
    Voix_Candidat10 INTEGER,
    Pourcentage_Voix_Ins_Candidat10 REAL,
    Pourcentage_Voix_Exp_Candidat10 REAL,
    Nom_Candidat11 TEXT,
    Prenom_Candidat11 TEXT,
    Voix_Candidat11 INTEGER,
    Pourcentage_Voix_Ins_Candidat11 REAL,
    Pourcentage_Voix_Exp_Candidat11 REAL,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Resultats_Electoraux_Tour2_2022 (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code_Commune TEXT,
    Code_Departement TEXT,
    Libelle_Departement TEXT,
    Code_Circonscription TEXT,
    Libelle_Circonscription TEXT,
    Code_Bureau_Vote TEXT,
    Inscrits INTEGER,
    Abstentions INTEGER,
    Pourcentage_Abs_Ins REAL,
    Votants INTEGER,
    Pourcentage_Vot_Ins REAL,
    Blancs INTEGER,
    Pourcentage_Blancs_Ins REAL,
    Pourcentage_Blancs_Vot REAL,
    Nuls INTEGER,
    Pourcentage_Nuls_Ins REAL,
    Pourcentage_Nuls_Vot REAL,
    Exprimes INTEGER,
    Pourcentage_Exp_Ins REAL,
    Pourcentage_Exp_Vot REAL,
    Nom_Candidat1 TEXT,
    Prenom_Candidat1 TEXT,
    Voix_Candidat1 INTEGER,
    Pourcentage_Voix_Ins_Candidat1 REAL,
    Pourcentage_Voix_Exp_Candidat1 REAL,
    Nom_Candidat2 TEXT,
    Prenom_Candidat2 TEXT,
    Voix_Candidat2 INTEGER,
    Pourcentage_Voix_Ins_Candidat2 REAL,
    Pourcentage_Voix_Exp_Candidat2 REAL,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Donnees_SocioEconomiques (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date TEXT,
    Code_Departement TEXT,
    Libelle_Departement TEXT,
    Code_Commune TEXT,
    Libelle_Commune TEXT,
    Sexe TEXT,
    Tranche_Age TEXT,
    Nombre_Demandeurs_Emploi INTEGER,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Donnees_RSA (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Annee INTEGER,
    Libelle_Commune TEXT,
    Code_Commune TEXT,
    Nombre_Beneficiaires_RSA INTEGER,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Population (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code_Commune TEXT,
    Population_en_2021 REAL,
    Pop_0_14_ans_en_2021 REAL,
    Pop_15_29_ans_en_2021 REAL,
    Pop_30_44_ans_en_2021 REAL,
    Pop_45_59_ans_en_2021 REAL,
    Pop_60_74_ans_en_2021 REAL,
    Pop_75_89_ans_en_2021 REAL,
    Pop_90_ans_ou_plus_en_2021 REAL,
    Pop_Hommes_en_2021 REAL,
    Pop_Femmes_en_2021 REAL,
    Pop_15_ans_ou_plus_Retraites_en_2021 REAL,
    Population_en_2015 REAL,
    Pop_0_14_ans_en_2015 REAL,
    Pop_15_29_ans_en_2015 REAL,
    Pop_30_44_ans_en_2015 REAL,
    Pop_45_59_ans_en_2015 REAL,
    Pop_60_74_ans_en_2015 REAL,
    Pop_75_89_ans_en_2015 REAL,
    Pop_90_ans_ou_plus_en_2015 REAL,
    Pop_Hommes_en_2015 REAL,
    Pop_Femmes_en_2015 REAL,
    Pop_15_ans_ou_plus_Retraites_en_2015 REAL,
    Population_en_2010 REAL,
    Pop_0_14_ans_en_2010 REAL,
    Pop_15_29_ans_en_2010 REAL,
    Pop_30_44_ans_en_2010 REAL,
    Pop_45_59_ans_en_2010 REAL,
    Pop_60_74_ans_en_2010 REAL,
    Pop_75_89_ans_en_2010 REAL,
    Pop_Hommes_en_2010 REAL,
    Pop_Femmes_en_2010 REAL,
    Pop_15_ans_ou_plus_Retraites_en_2010 REAL,
    Chomeurs_15_64_ans_en_2021 REAL,
    Chomeurs_15_64_ans_en_2015 REAL,
    Chomeurs_15_64_ans_en_2010 REAL,
    Salaire_net_horaire_moyen_en_2021 REAL,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Securite (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code_Commune TEXT,
    Annee INTEGER,
    Classe TEXT,
    Unite_De_Compte TEXT,
    Valeur_Publiee REAL,
    Faits INTEGER,
    Taux_Pour_Mille REAL,
    Population REAL,
    Mill_POP REAL,
    Logements REAL,
    Mill_LOG REAL,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Associations_Utilite_Publique (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Numero_RNA TEXT,
    Nom TEXT,
    Date_Reconnaissance_Utilite_Publique TEXT,
    Date_Derniere_Modification_Statutaire TEXT,
    Code_Commune TEXT,
    Ville TEXT,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);

CREATE TABLE Repertoire_Asso_National (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date_Creation TEXT,
    Date_Declaration TEXT,
    Date_Publication TEXT,
    Date_Dissolution TEXT,
    Titre TEXT,
    Objet_Social1 TEXT,
    Objet_Social2 TEXT,
    Code_Commune TEXT,
    Code_Postal TEXT,
    Libelle_Commune TEXT,
    FOREIGN KEY (Code_Commune) REFERENCES Communes(Code_Commune)
);



