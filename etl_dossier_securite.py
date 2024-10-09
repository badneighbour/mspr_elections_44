import pandas as pd

pd.options.display.width = 200
pd.options.display.max_columns = None
pd.options.display.max_colwidth = None

def traitement_securite(save=False):

    input_path = "input/"
    fichier = input_path + "dossier_complet.csv"

    # Lire le fichier CSV dans un DataFrame
    df_securite = pd.read_csv(fichier, sep=';', encoding='utf-8', low_memory=False)

    # Filtrer les lignes où la colonne Code.département est égale à 44
    df_securite_filtered = df_securite[df_securite['CODGEO_2024'].str.startswith('44')].copy()

    # Ajouter 2000 à la colonne "annee"
    df_securite_filtered.loc[:, "annee"] = df_securite_filtered["annee"] + 2000

    df_securite_filtered['complementinfotaux'] = df_securite_filtered['complementinfotaux'].str.replace(',', '.').astype(float)

    # Remplacer les valeurs "NaN" dans la colonne "tauxpourmille" par les valeurs de la colonne "complementinfotaux"
    df_securite_filtered.loc[:, 'tauxpourmille'] = df_securite_filtered['tauxpourmille'].fillna(df_securite_filtered['complementinfotaux'])

    # Supprimer la colonne "complementinfotaux"
    df_securite_filtered.drop(columns=['complementinfotaux'], inplace=True)

    # Remplacer les virgules par des points dans la colonne 'complementinfoval'
    df_securite_filtered['complementinfoval'] = df_securite_filtered['complementinfoval'].str.replace(',', '.').astype(float)

    # Remplacer les valeurs "NaN" dans la colonne "faits" par les valeurs de "complementinfoval"
    df_securite_filtered.loc[:, 'faits'] = df_securite_filtered['faits'].fillna(df_securite_filtered['complementinfoval'])

    # Supprimer la colonne "complementinfoval"
    df_securite_filtered.drop(columns=['complementinfoval'], inplace=True)

    # Échantillonner 20% des données filtrées
    #df_sampled = df_securite_filtered.sample(frac=0.2, random_state=42)

    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_securite traité")
        df_securite_filtered.to_csv(output_path, sep=';', index=False, encoding='utf-8')

# Appel de la fonction
traitement_securite(save=True)