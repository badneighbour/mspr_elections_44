import pandas as pd

def traitement_asso_utilite_publique(save=False):

    # Chemin vers le fichier CSV
    df = pd.read_csv('/Users/mickael/Documents/Cours/EPSI/MSPR/Data/Data Associations/Liste associations reconnues d_utilité publique - avril 2021.csv', sep=';', encoding='latin1')

    # Configurations d'affichage pour Pandas
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)

    # Liste des colonnes à supprimer
    colonnes_inutiles = [
        'OBJET', 'ADRESSE'
    ]

    # Filtrer les colonnes inutiles
    columns_to_drop = [col for col in df.columns if col in colonnes_inutiles or col.startswith('Unnamed')]
    df_cleaned = df.drop(columns=columns_to_drop)

    # Afficher les 100 premières lignes du DataFrame nettoyé (optionnel)
    # print(df_cleaned.head(100))

    # Filtrer les données où la colonne 'CP' commence par '44'
    if 'CP' in df_cleaned.columns:
        df_asso_utilite_publique = df_cleaned[df_cleaned['CP'].astype(str).str.startswith('44')]
    else:
        print("La colonne 'CP' n'existe pas dans le DataFrame.")

    # Afficher les données filtrées
    print(df_asso_utilite_publique)

    # Chemin vers le fichier CSV de sortie (si vous souhaitez sauvegarder les résultats filtrés)
    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_asso_utilite_publique traité")
        df_asso_utilite_publique.to_csv(output, sep=';', index=False)
