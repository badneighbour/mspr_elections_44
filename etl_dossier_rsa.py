import pandas as pd

pd.options.display.width = 200
pd.options.display.max_columns = None
pd.options.display.max_colwidth = None


def traitement_rsa(save=False):
    input_path = "input/"
    fichier = input_path + "dossier_complet.csv"

    # Chemin vers le fichier CSV
    df_rsa = pd.read_csv(fichier, sep=';', encoding='utf-8')

    # Colonnes à supprimer
    colonnes_inutiles = ['location']

    def filtrer(nom_colonne):
        for mot in colonnes_inutiles:
            if mot in nom_colonne:
                return True
        return False

    # Trouver les colonnes à supprimer
    columns_to_drop = [col for col in df_rsa.columns if filtrer(col)]

    # Supprimer les colonnes inutiles
    df_rsa.drop(columns=columns_to_drop, inplace=True)

    # Convertir les colonnes en entiers si nécessaire
    columns_to_convert = ['code_commune', 'nb_benef_rsa']

    for col in columns_to_convert:
        if col in df_rsa.columns:
            # Remplacer les NaN par 0 (ou une autre valeur si nécessaire) avant la conversion
            df_rsa[col] = df_rsa[col].fillna(0).astype(int)

    # Supprimer les lignes avec des valeurs manquantes après la conversion
    df_rsa.dropna(inplace=True)

    # Afficher le résultat final
    print(df_rsa)

    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_insee traité")
        df_rsa.to_csv(output, sep=';', index=False, encoding='utf-8')
