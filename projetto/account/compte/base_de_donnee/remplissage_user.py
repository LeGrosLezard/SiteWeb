import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD



def insertion_user(nom, prenom, date, sexe, email, fixe, password,
                   pseudo, lieu_habitation, portable):


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO users
                (nom, prenom, date_naissance, sexe, email,
                fixe, password, pseudo, lieu_habitation, portable)
                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                (nom, prenom, date, sexe, email, fixe,
                 password, pseudo, lieu_habitation, portable))
                       

    conn.commit() 































