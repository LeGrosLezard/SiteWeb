import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD



def insertion_user(nom, prenom, prenom1, prenom2, prenom3,
                   date, sexe, email, fixe, password,
                   pseudo, lieu_habitation, portable):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO user
                WHERE nom LIKE '%%s%' AND
                nom LIKE '%%s%' AND
                prenom LIKE '%%s%' AND
                prenom1 LIKE '%%s%' AND
                prenom2 LIKE '%%s%' AND
                prenom3 LIKE '%%s%' AND
                date LIKE '%%s%' AND
                sexe LIKE '%%s%' AND
                fixe LIKE '%%s%' AND
                password LIKE '%%s%' AND
                pseudo LIKE '%%s%' AND
                lieu_habitation LIKE '%%s%' AND
                portable LIKE '%%s%'""",
                (nom,
                 prenom,
                 prenom1,
                 prenom2,
                 prenom3,
                 date,
                 sexe,
                 fixe,
                 password,
                 pseudo,
                 lieu_habitation,
                 portable)
                )
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste

