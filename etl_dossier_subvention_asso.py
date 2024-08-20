import pandas as pd

def traitement_subvention_asso(save=False):

    # Chemin vers le fichier CSV
    df = pd.read_csv('/Users/mickael/Documents/Cours/EPSI/MSPR/Data/Data Associations/Subventions aux associations versées par le Département de Loire-Atlantique.csv', sep=';', encoding='UTF-8')

    # Configurations d'affichage pour Pandas
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)

    # Liste des colonnes à supprimer
    colonnes_inutiles = [
        'objet', 'conditionsversement','dateconvention','nature','detailavantagesnature',
        'estimationavantagesnature', 'referencedecision','notificationue','idrae'
    ]

    # Filtrer les colonnes inutiles
    columns_to_drop = [col for col in df.columns if col in colonnes_inutiles or col.startswith('montant')]
    df_subvention_asso = df.drop(columns=columns_to_drop)

    # Afficher les 100 premières lignes du DataFrame nettoyé (optionnel)
    print(df_subvention_asso.head(100))


    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_insee traité")
        df_subvention_asso.to_csv(output, sep=';', index=False)
