import pandas as pd
import sqlite3
from sklearn.preprocessing import LabelEncoder

# Connexion à la base de données SQLite
conn = sqlite3.connect('mspr.db')

# Récupérer les données de la table Communes et filtrer celles qui commencent par '44'
communes_df = pd.read_sql_query("SELECT * FROM Communes", conn)
communes_df = communes_df.dropna(subset=['Code_Commune'])
communes_df = communes_df[communes_df['Code_Commune'].str.startswith('44')]
communes_df['Code_Commune'] = communes_df['Code_Commune'].astype(str)

# Récupérer les données de la table Population pour l'année 2021
population_df = pd.read_sql_query(
    """
    SELECT Code_Commune, Population_en_2021, Pop_0_14_ans_en_2021, 
           Pop_15_29_ans_en_2021, Pop_30_44_ans_en_2021, 
           Pop_45_59_ans_en_2021, Pop_60_74_ans_en_2021, 
           Pop_75_89_ans_en_2021, Pop_90_ans_ou_plus_en_2021, 
           Pop_Hommes_en_2021, Pop_Femmes_en_2021, 
           Pop_15_ans_ou_plus_Retraites_en_2021,
           Chomeurs_15_64_ans_en_2021, Salaire_net_horaire_moyen_en_2021
    FROM Population
    """, conn)
population_df['Code_Commune'] = population_df['Code_Commune'].astype(str)

# Calculer la médiane pour le salaire net horaire moyen en 2021
median_salaire = population_df['Salaire_net_horaire_moyen_en_2021'].median()

# Remplacer les valeurs manquantes par la médiane
population_df['Salaire_net_horaire_moyen_en_2021'] = population_df['Salaire_net_horaire_moyen_en_2021'].fillna(median_salaire)

print(f"Médiane du Salaire net horaire moyen en 2021 : {median_salaire}")

# Charger les données de sécurité depuis le fichier CSV
securite_csv_df = pd.read_csv('Data sécurité par commune Loire-Atlantique_traitées (1).csv', sep= ';')

# Vérifier si la colonne 'CODGEO_2024' existe et la renommer en 'Code_Commune'
if 'CODGEO_2024' in securite_csv_df.columns:
    securite_csv_df.rename(columns={'CODGEO_2024': 'Code_Commune'}, inplace=True)
else:
    raise KeyError("La colonne 'CODGEO_2024' n'a pas été trouvée dans le fichier CSV.")

# Ajouter .0 à la fin des Code_Commune et s'assurer que le type est 'str'
securite_csv_df['Code_Commune'] = securite_csv_df['Code_Commune'].astype(str) + '.0'

# Filtrer les données pour l'année 2021
securite_2021_df = securite_csv_df[securite_csv_df['annee'] == 21]

# Sélection des classes pertinentes
elements_pertinents = ['Vols avec armes', 'Cambriolages de logement', 'Trafic de stupéfiants']

# Filtrer les données pour ne conserver que ces trois éléments
securite_pertinent_df = securite_2021_df[securite_2021_df['classe'].isin(elements_pertinents)]

# Créer un tableau croisé dynamique (pivot table) avec 'tauxpourmille' en valeurs pour les classes pertinentes
pivot_df = securite_pertinent_df.pivot_table(
    index='Code_Commune', 
    columns='classe', 
    values='tauxpourmille', 
    aggfunc='sum', 
    fill_value=0
)
pivot_df.reset_index(inplace=True)
pivot_df['Code_Commune'] = pivot_df['Code_Commune'].astype(str)

# Fusionner le pivot avec le DataFrame principal
merged_df = communes_df.merge(population_df, on='Code_Commune', how='left')
merged_df = merged_df.merge(pivot_df, on='Code_Commune', how='left')

# Récupérer les données des résultats électoraux pour le tour 1 de 2022
resultats_2022_t1_df = pd.read_sql_query(
    """
    SELECT Code_Commune, 
           Nom_Candidat1, Voix_Candidat1, 
           Nom_Candidat2, Voix_Candidat2,
           Nom_Candidat3, Voix_Candidat3,
           Nom_Candidat4, Voix_Candidat4,
           Nom_Candidat5, Voix_Candidat5,
           Nom_Candidat6, Voix_Candidat6,
           Nom_Candidat7, Voix_Candidat7,
           Nom_Candidat8, Voix_Candidat8,
           Nom_Candidat9, Voix_Candidat9,
           Nom_Candidat10, Voix_Candidat10,
           Nom_Candidat11, Voix_Candidat11
    FROM Resultats_Electoraux_Tour1_2022
    """, conn)
resultats_2022_t1_df = resultats_2022_t1_df.drop_duplicates(subset=['Code_Commune'])
resultats_2022_t1_df['Code_Commune'] = resultats_2022_t1_df['Code_Commune'].astype(str) + '.0'

# Fonction pour obtenir le candidat avec le plus de voix
def get_max_candidate(row):
    voix_columns = ['Voix_Candidat1', 'Voix_Candidat2', 'Voix_Candidat3', 
                    'Voix_Candidat4', 'Voix_Candidat5', 'Voix_Candidat6', 
                    'Voix_Candidat7', 'Voix_Candidat8', 'Voix_Candidat9', 
                    'Voix_Candidat10', 'Voix_Candidat11']
    
    candidats = ['Nom_Candidat1', 'Nom_Candidat2', 'Nom_Candidat3', 
                 'Nom_Candidat4', 'Nom_Candidat5', 'Nom_Candidat6', 
                 'Nom_Candidat7', 'Nom_Candidat8', 'Nom_Candidat9', 
                 'Nom_Candidat10', 'Nom_Candidat11']
    
    max_voix_index = row[voix_columns].idxmax()
    max_candidat = row[candidats[voix_columns.index(max_voix_index)]]
    max_voix = row[max_voix_index]
    
    return pd.Series([max_candidat, max_voix], index=['Candidat_Max_Voix_T1_2022', 'Nombre_Voix_Max_T1_2022'])

# Appliquer la fonction à chaque ligne pour obtenir le nom du candidat et le nombre de voix maximum
resultats_2022_t1_df[['Candidat_Max_Voix_T1_2022', 'Nombre_Voix_Max_T1_2022']] = resultats_2022_t1_df.apply(get_max_candidate, axis=1)

# Encoder le nom des candidats
label_encoder = LabelEncoder()
resultats_2022_t1_df['Candidat_Max_Voix_T1_2022_Encoded'] = label_encoder.fit_transform(resultats_2022_t1_df['Candidat_Max_Voix_T1_2022'])

# Vérifier les encodages
print("Encodage des noms des candidats :")
print(resultats_2022_t1_df[['Candidat_Max_Voix_T1_2022', 'Candidat_Max_Voix_T1_2022_Encoded']].head())

# Fusionner les résultats du premier tour avec le DataFrame principal
merged_df = merged_df.merge(resultats_2022_t1_df[['Code_Commune', 'Candidat_Max_Voix_T1_2022_Encoded', 'Nombre_Voix_Max_T1_2022']], on='Code_Commune', how='left')

# Supprimer les colonnes qui sont complètement vides (toutes les valeurs sont NaN)
merged_df = merged_df.dropna(axis=1, how='all')

# S'assurer qu'il n'y a qu'une seule ligne par Code_Commune
merged_df = merged_df.drop_duplicates(subset=['Code_Commune'])

# Exporter le DataFrame fusionné en un fichier CSV
merged_df.to_csv('dataset_modele_ia_2021.csv', index=False, encoding='utf-8')

print("Data exportée avec succès dans dataset_modele_ia_2021.csv")

# Fermer la connexion à la base de données
conn.close()
