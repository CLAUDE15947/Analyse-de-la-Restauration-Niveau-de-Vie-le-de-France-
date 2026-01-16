import pandas as pd
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': '91.208.207.108',  # L'adresse du serveur
    'database': 'bm9z2tdd0hqv6jryavlp',                 # Le nom de la base
    'user': 'uhsw7eak8bqyelua',                            # L'identifiant
    'password': 'l9HNxYoWsCzH2RcNDrR4',                    # Le mot de passe
    'port': 3306,

    'use_pure': True,       
    'ssl_disabled': True   
}


FILE_CSV = r"C:\Users\YANNIS\Documents\projet ennglobant\restaurants_paris_sql_ready.csv"

try:
    print("1. Connexion à la base de données...")
    connection = mysql.connector.connect(**DB_CONFIG)
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        print(f"2. Lecture du fichier {FILE_CSV}...")
        df = pd.read_csv(FILE_CSV)
        
        # Remplacement des NaN par None (NULL en SQL)
        df = df.where(pd.notnull(df), None)

        # Préparation de la requête
        print("3. Préparation de l'insertion...")
        
        # On récupère les colonnes du CSV qui doivent correspondre EXACTEMENT à celles de la table SQL
        cols = ",".join(df.columns.tolist())
        
        # On crée des placeholders (%s, %s, %s...)
        wildcards = ",".join(["%s"] * len(df.columns))
        
        sql_insert = f"INSERT INTO restaurants_paris ({cols}) VALUES ({wildcards})"
        
        # Transformation des données en liste de tuples pour MySQL
        data_to_insert = [tuple(x) for x in df.to_numpy()]
        
        print(f"4. Envoi de {len(data_to_insert)} lignes vers le Cloud...")
        cursor.executemany(sql_insert, data_to_insert)
        connection.commit()
        
        print(f"SUCCÈS ! {cursor.rowcount} restaurants ont été importés.")

except Error as e:
    print(f"ERREUR : {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée.")