import pandas as pd
def traitement_repertoire_assso(save=False):

    # Chemin vers le fichier CSV
    df = pd.read_csv('/Users/mickael/Documents/Cours/EPSI/MSPR/Data/Data Associations/rna_waldec_20220101_dpt_44.csv', sep=';', encoding='latin1')

    # Configurations d'affichage pour Pandas
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)

    # Liste des colonnes à supprimer
    colonnes_inutiles = [
        'id_ex', 'siret', 'rup_mi', 'gestion', 'groupement', 'objet_social',
        'maj_time', 'siteweb', 'publiweb', 'dir_civilite', 'telephone', 'adrg',
        'nature', 'objet','adrs_complement','adrs_numvoie','adrs_repetition',
        'adrs_typevoie','adrs_libvoie','adrs_distrib', 'observation','position',
        'titre_court'
    ]

    # Filtrer les colonnes inutiles
    columns_to_drop = [col for col in df.columns if col in colonnes_inutiles or col.startswith('adrg')]
    df_repertoire_asso = df.drop(columns=columns_to_drop)

    # Facultatif : Afficher les 100 premières lignes du DataFrame nettoyé
    print(df_repertoire_asso.head(100))

    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_insee traité")
        df_repertoire_asso.to_csv(output, sep=';', index=False)
