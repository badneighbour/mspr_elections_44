import pandas as pd
pd.options.display.width = 200

def traitement_rsa(save=False):

    # Chemin vers le fichier CSV
    df = pd.read_csv('/Users/mickael/Documents/Cours/EPSI/MSPR/Data/Data RSA/RSA par commune.csv', sep=';', encoding='utf-8')

    # Configurations d'affichage pour Pandas
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)

    # Limiter à 10000 lignes
    df = df.head(10000)

    # Colonnes à supprimer
    colonnes_inutiles = ['location']

    def filtrer(nom_colonne):
        for mot in colonnes_inutiles:
            if mot in nom_colonne:
                return True
        return False

    # Trouver les colonnes à supprimer
    columns_to_drop = [col for col in df.columns if filtrer(col)]

    # Supprimer les colonnes inutiles
    df_rsa = df.drop(columns=columns_to_drop)

    # Convertir les colonnes en entiers si nécessaire
    columns_to_convert = ['code_commune', 'nb_benef_rsa']

    for col in columns_to_convert:
        if col in df_rsa.columns:
            # Remplacer les NaN par 0 (ou une autre valeur si nécessaire) avant la conversion
            df_rsa[col] = df_rsa[col].fillna(0).astype(int)

    # Supprimer les lignes avec des valeurs manquantes après la conversion
    df_rsa = df_rsa.dropna()

    # Afficher le résultat final
    print(df_rsa)

    # Chemin vers le fichier CSV de sortie
    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_rsa traité")
        df_rsa.to_csv(output, sep=';', index=False, encoding='utf-8')
