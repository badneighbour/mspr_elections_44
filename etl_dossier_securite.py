import pandas as pd

pd.options.display.width = 200
pd.options.display.max_columns = None
pd.options.display.max_colwidth = None


def traitement_securite(save=False):
    input_path = "input/"
    fichier = input_path + "dossier_complet.csv"

    # Lire le fichier CSV dans un DataFrame
    df_securite = pd.read_csv(fichier, sep=';', encoding='utf-8')

    # Ajouter 2000 à la colonne "annee"
    df_securite["annee"] = df_securite["annee"] + 2000

    # Remplacer les valeurs "NA" de la colonne "tauxpourmille" par les valeurs de la colonne "complementinfotaux"
    df_securite["tauxpourmille"] = df_securite["tauxpourmille"].where(df_securite["tauxpourmille"] != "NA",
                                                                      df_securite["complementinfotaux"])

    # Supprimer la colonne "complementinfotaux"
    df_securite = df_securite.drop(columns=["complementinfotaux"])

    # Remplacer les valeurs "NA" dans la colonne "faits" par les valeurs de "complementinfoval"
    df_securite["faits"] = df_securite["faits"].where(df_securite["faits"] != "NA", df_securite["complementinfoval"])

    # Supprimer la colonne "complementinfoval"
    df_securite = df_securite.drop(columns=["complementinfoval"])
    df_securite = df_securite.drop(columns=["valeur.publiée"])

    # Filtrer les lignes où la colonne Code.département est égale à 44
    df_securite = df_securite[
        (df_securite["CODGEO_2024"].astype(str).str.startswith("44")) &
        (df_securite["annee"] < 2023) &
        ((df_securite["faits"] != 0) | (df_securite["faits"].notna()))
        ]

    # Échantillonner 20% des données filtrées
    df_securite.sample(frac=0.2, random_state=42)

    # Afficher les résultats filtrés et échantillonnés
    print(df_securite.head(1000))

    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_securite traité")
        df_securite.to_csv(output, sep=';', index=False, encoding='utf-8')
