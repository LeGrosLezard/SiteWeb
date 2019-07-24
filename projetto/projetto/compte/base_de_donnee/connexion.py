import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD



def verifier_connexion(pseudo, password):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT pseudo, password FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}'""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste


def connexion_database(pseudo, password, GLOBAL_CONNEXION):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO connexion
                (pseudo, password)
                values(%s, %s);""",
                (pseudo, password))
                       

    conn.commit()



def user_connected(GLOBAL_CONNEXION):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT pseudo, password FROM connexion
                WHERE pseudo = '{0}' AND
                password = '{1}'""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste























def deconnexion_database(pseudo, password):

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










    
