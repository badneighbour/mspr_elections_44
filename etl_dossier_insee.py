from sqlalchemy import create_engine
import pandas as pd
pd.options.display.width = 200

def traitement_insee(save=False):

    #Expression régulière (REGEX) pour sélectionner toutes les communes de Loire Atlantique (code insee qui commence par 44)
    regex_code_insee = "^44[0-9]{3}$"

    input_path = "input/"
    fichier = input_path + "dossier_complet.csv"
    fichier_metadata = input_path + "meta_dossier_complet.csv"

    df_insee = pd.read_csv(fichier, sep=";")
    df_metadata = pd.read_csv(fichier_metadata, sep=";")

    df_insee["CODGEO"] = df_insee["CODGEO"].apply(str)
    print(df_insee.shape)
    print(df_metadata.shape)

    df_insee = df_insee[df_insee["CODGEO"].str.contains(regex_code_insee, regex=True)]

    df_insee = df_insee.filter(regex=r"^(P(21|15|10)_(POP(H|F|0014|1529|3044|4559|6074|7589|90P)?|CHOM1564)|C(21|15|10)_POP15P_CS7|CODGEO|SNHM21)$")
    df_metadata = df_metadata[(df_metadata["COD_VAR"] != "CODGEO") & (df_metadata["COD_VAR"].isin(df_insee.columns))]

    #On renomme les colonnes du dossier complet par des noms explicites
    df_metadata["LIB_VAR"] = df_metadata["LIB_VAR"].str.split('(').str[0].str.strip().str.replace(" |-", "_", regex=True)
    df_insee.rename(columns=df_metadata.set_index("COD_VAR")["LIB_VAR"], inplace=True)

    print(df_insee.head())
    print(df_insee.shape)

    print(df_metadata.head())
    print(df_metadata.shape)
    i = 0
    for column in df_insee.columns:
        i+=1
        print(column, end=", ")
        if i == 10:
            i = 0
            print()

    output_path = "output/"
    output = output_path + "dossier_complet.csv"
    output_metadata = output_path + "meta_dossier_complet.csv"

    if save:
        print("Sauvegarde dossier complet df_insee traité")
        df_insee.to_csv(output, sep=";", index=False)
        df_metadata.to_csv(output_metadata, sep=";", index=False)

def insee_to_db():
    print("insee_to_db")
    output_path = "output/"
    output = output_path + "dossier_complet.csv"
    engine = create_engine('sqlite:///data/msprdb')
