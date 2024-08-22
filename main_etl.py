from etl_dossier_insee import *
from etl_dossier_rsa import *
from etl_dossier_securite import *
from etl_dossier_asso_utilite_publique import *
from etl_dossier_subvention_asso import *
from etl_epci_44 import *



def main_funtion(save=False):
    print("Main ETL")
    traitement_insee(save)
    # traitement_rsa(save)
    # traitement_securite(save)
    # traitement_asso_utilite_publique(save)
    # traitement_subvention_asso(save)
    # traitement_epci_44(save)


if __name__ == "__main__":
    main_funtion()
