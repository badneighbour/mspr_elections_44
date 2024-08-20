import pandas as pd

pd.options.display.width = 200
pd.options.display.max_columns = None
pd.options.display.max_colwidth = None


def traitement_subvention_asso(save=False):
    input_path = "input/"
    fichier = input_path + "dossier_complet.csv"

    df_subvention_asso = pd.read_csv(fichier, sep=';', encoding='UTF-8')

    colonnes_inutiles = [
        'objet', 'conditionsversement', 'dateconvention', 'nature', 'detailavantagesnature',
        'estimationavantagesnature', 'referencedecision', 'notificationue', 'idrae'
    ]

    # Filtrer les colonnes inutiles
    columns_to_drop = [col for col in df_subvention_asso.columns if
                       col in colonnes_inutiles or col.startswith('montant')]
    df_subvention_asso = df_subvention_asso.drop(columns=columns_to_drop)

    # Afficher les 100 premières lignes du DataFrame nettoyé (optionnel)
    print(df_subvention_asso.head(100))

    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde du fichier filtré")
        df_subvention_asso.to_csv(output, sep=';', index=False)
