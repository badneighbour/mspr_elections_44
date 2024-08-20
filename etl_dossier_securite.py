import pandas as pd
pd.options.display.width = 200
pd.options.display.max_columns = None
pd.options.display.max_colwidth = None

def traitement_securite(save=False):

    # Chemin vers le fichier CSV
    file_path = "/Users/mickael/Documents/Cours/EPSI/MSPR/Data/Data sécurité/Base statistique communale de la délinquance enregistrée par la police et la gendarmerie nationales.csv"

    # Lire le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path, sep=';', encoding='utf-8')

    # Ajouter 2000 à la colonne "annee"
    df["annee"] = df["annee"] + 2000

    # Remplacer les valeurs "NA" de la colonne "tauxpourmille" par les valeurs de la colonne "complementinfotaux"
    df["tauxpourmille"] = df["tauxpourmille"].where(df["tauxpourmille"] != "NA", df["complementinfotaux"])

    # Supprimer la colonne "complementinfotaux"
    df = df.drop(columns=["complementinfotaux"])

    # Remplacer les valeurs "NA" dans la colonne "faits" par les valeurs de "complementinfoval"
    df["faits"] = df["faits"].where(df["faits"] != "NA", df["complementinfoval"])

    # Supprimer la colonne "complementinfoval"
    df = df.drop(columns=["complementinfoval"])

    # Filtrer les lignes où la colonne Code.département est égale à 44
    df_securite = df[
        (df["CODGEO_2024"].astype(str).str.startswith("44")) &
        (df["annee"] < 2023) &
        ((df["faits"] != 0) | (df["faits"].notna()))
        ]

    # Échantillonner 20% des données filtrées
    df_sample = df_securite.sample(frac=0.2, random_state=42)

    # Afficher les résultats filtrés et échantillonnés
    print(df_sample.head(1000))

    output_path = "output/"
    output = output_path + "dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_securite traité")
        df_securite.to_csv(output, sep=';', index=False, encoding='utf-8')
