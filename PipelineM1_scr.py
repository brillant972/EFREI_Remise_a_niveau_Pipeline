import pymysql  # Importe la bibliothèque pour MySQL

# Connexion à la bdd
def connect_to_db():
    conn = pymysql.connect(
        host="localhost",   
        user="root",        
        password="root",    
        database="ecole"  
    )
    return conn

# Récup les données d'une table
def fetch_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

# Fonction main
def main():
    conn = connect_to_db()  # Connexion
    cursor = conn.cursor() 

    # Obtenir les données des tables "etudiants" et "enseignants"
    etudiants = fetch_data(cursor, "etudiants")
    enseignants = fetch_data(cursor, "enseignants")

    # Trouver les associations élèves-enseignants
    associations = [(e[1], e[2], p[1], p[2]) for e in etudiants for p in enseignants if e[7] == p[8]]
    print("""\tAssociations élèves - enseignants :
------------------------------------------""")
    for asso in associations:
        print(f"- L'élève : {asso[0]} {asso[1]} a pour enseignant : {asso[2]} {asso[3]}")
    print("------------------------------------------")
    # Compter les élèves par enseignant
    compteur_enseignants = {f"{p[1]} {p[2]}": 0 for p in enseignants}
    for e in etudiants:
        for p in enseignants:
            if e[7] == p[8]:
                compteur_enseignants[f"{p[1]} {p[2]}"] += 1

    # Afficher les comptes par enseignant
    print("""\n\n\tNombre d'élèves par enseignant :
------------------------------------------""")
    for prof, count in compteur_enseignants.items():
        print(f"- L'enseignant {prof} a {count} élève(s).")
    print("------------------------------------------")

    # Ferme la connexion
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
