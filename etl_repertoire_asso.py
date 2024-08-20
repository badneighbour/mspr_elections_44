import pandas as pd
pd.options.display.width = 200
pd.options.display.max_columns = None
pd.options.display.max_colwidth = None


def traitement_repertoire_assso(save=False):

    input_path = "input/"
    fichier = input_path + "dossier_complet.csv"

    df_repertoire_asso = pd.read_csv(fichier, sep=';', encoding='latin1')

    # Liste des colonnes à supprimer
    colonnes_inutiles = [
        'id_ex', 'siret', 'rup_mi', 'gestion', 'groupement', 'objet_social',
        'maj_time', 'siteweb', 'publiweb', 'dir_civilite', 'telephone', 'adrg',
        'nature', 'objet', 'adrs_complement', 'adrs_numvoie', 'adrs_repetition',
        'adrs_typevoie', 'adrs_libvoie', 'adrs_distrib', 'observation', 'position',
        'titre_court'
    ]

    # Filtrer les colonnes inutiles
    columns_to_drop = [col for col in df_repertoire_asso.columns if col in colonnes_inutiles or col.startswith('adrg')]
    df_repertoire_asso = df_repertoire_asso.drop(columns=columns_to_drop)

    # Facultatif : Afficher les 100 premières lignes du DataFrame nettoyé
    print(df_repertoire_asso.head(100))

    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_insee traité")
        df_repertoire_asso.to_csv(output, sep=';', index=False)
