from etl_dossier_insee import *
from etl_dossier_rsa import *
from etl_dossier_securite import *
from etl_dossier_asso_utilite_publique import *
from etl_dossier_subvention_asso import *

def main_funtion():
    print("Main ETL")
    traitement_insee(True)
    traitement_rsa(True)
    traitement_securite(True)
    traitement_asso_utilite_publique(True)
    traitement_subvention_asso(True)


if __name__ == "__main__":
    main_funtion()
