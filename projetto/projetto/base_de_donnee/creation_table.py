import psycopg2


from CONFIG import DATABASE
from CONFIG import USER
from CONFIG import HOST
from CONFIG import PASSWORD



class Table:


    def creation_table_donnee():
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



        cur.execute("""create table users(
                    id serial PRIMARY KEY,
                    nom VARCHAR(100),
                    prenom VARCHAR(100),
                    date_naissance DATE,
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
                    id_user integer REFERENCES users (id),
                    lettre_motivation TEXT,
                    lettre_motivation1 TEXT,
                    lettre_motivation2 TEXT,
                    lettre_motivation3 TEXT,
                    lettre_motivation4 TEXT,
                    lettre_motivation5 TEXT,
                    code varchar(10),
                    ville varchar(100),
                    poste_moitivation TEXT);""")
        
        conn.commit()





        cur.execute("""create table cv(
                    id serial PRIMARY KEY,
                    id_user integer REFERENCES users (id),
                    metier varchar(100),
                    formation varchar(100),
                    poste1 varchar(100),
                    poste2 varchar(100),
                    poste3 varchar(100),
                    cv TEXT,
                    cv1 TEXT,
                    cv2 TEXT,
                    cv3 TEXT,
                    cv4 TEXT,
                    cv6_1 TEXT,
                    cv6_2 TEXT,
                    cv6_3 TEXT,
                    cv7 TEXT);""")
        
        conn.commit()



        cur.execute("""create table message(
                    id serial PRIMARY KEY,
                    id_user integer REFERENCES users (id),
                    lettre_motivation TEXT,
                    lettre_motivation1 TEXT,
                    lettre_motivation2 TEXT,
                    lettre_motivation3 TEXT,
                    lettre_motivation4 TEXT,
                    lettre_motivation5 TEXT,);""")
        
        conn.commit()



        cur.execute("""create table bilan(
                    id serial PRIMARY KEY,
                    bilan TEXT,
                    bilan1 TEXT,
                    bilan2 TEXT,
                    bilan3 TEXT,
                    id_user integer REFERENCES users (id));""")
        
        conn.commit()



        cur.execute("""create table site_emploie(
                    id serial PRIMARY KEY,
                    id_user integer REFERENCES users (id),
                    poste_demandee VARCHAR(100),
                    date VARCHAR(100));""")
        
        conn.commit()







if __name__ == "__main__":
    
    crea_table = Table.creation_table_donnee()





















