import psycopg2


from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD



class Table:


    def creation_table_donnee(self):
        """un mec a ses info sur lui
        sa lettre de motivation,
        son cv,
        son bilan,
        les sites a qui on a envoyé les demandes"""



        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()



        cur.execute("""create table user(
                    id serial PRIMARY KEY,
                    nom VARCHAR(100),
                    prenom VARCHAR(100),
                    prenom1 VARCHAR(100),
                    prenom2 VARCHAR(100),
                    prenom3 VARCHAR(100),
                    date_naissance INT,
                    sexe VARCHAR(10),
                    email VARCHAR(100),
                    fixe INT,
                    portable INT,
                    password VARCHAR(100),
                    pseudo VARCHAR(100),
                    lieu_habitation VARCHAR(100));""")
        
        conn.commit()





        cur.execute("""create table motivation(
                    id serial PRIMARY KEY,
                    id_user integer REFERENCES user (id),
                    lettre_motivation TEXT);""")
        
        conn.commit()





        cur.execute("""create table cv(
                    id serial PRIMARY KEY,
                    id_user integer REFERENCES user (id),
                    cv TEXT);""")
        
        conn.commit()





        cur.execute("""create table bilan(
                    id serial PRIMARY KEY,
                    bilan TEXT,
                    id_user integer REFERENCES user (id));""")
        
        conn.commit()





        cur.execute("""create table site_emploie(
                    id serial PRIMARY KEY,
                    id_user integer REFERENCES user (id),
                    poste_demandee VARCHAR(100));""")
        
        conn.commit()







if __name__ == "__main__":
    
    crea_table = Table.creation_table_donnee()




















