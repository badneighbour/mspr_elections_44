import pandas as pd
pd.options.display.width = 200

def traitement_epci_44(save=False):

    #Expression régulière (REGEX) pour sélectionner toutes les communes de Loire Atlantique (code insee qui commence par 44)
    regex_code_insee = "^44[0-9]{3}$"

    input_path = "input/"
    fichier = input_path + "georef-france-epci.csv"

    df_epci = pd.read_csv(fichier, sep=";")

    print(df_epci.head())
