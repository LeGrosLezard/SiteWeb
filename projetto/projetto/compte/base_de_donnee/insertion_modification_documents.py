import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


def insertion_cv(pseudo, password, cv):
    """On verifie le cv de l'utilisateur"""
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO cv
                (id_user, cv)
                VALUES SELECT users.id
                FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}', '{2}'""".format(pseudo, password, cv))
                       

    conn.commit() 






def insertion_motivation(pseudo, password, motivation):
    """On verifie la lettre de motivation de l'utilisateur"""

    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    
    cur.execute("""INSERT INTO motivation
                (id_user, lettre_motivation)
                VALUES SELECT users.id
                FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}', '{2}'""".format(pseudo, password, motivation))
                       

    conn.commit() 







def insertion_message(pseudo, password, motivation):
    """On verifie le message aux recruteurs de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO message
                (id_user, lettre_motivation)
                VALUES SELECT users.id
                FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}', '{2}'""".format(pseudo, password, motivation))
                       

    conn.commit() 





def insertion_bilan(pseudo, password, bilan):
    """On verifie les bilans de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO bilan
                (id_user, bilan)
                VALUES SELECT users.id
                FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}', '{2}'""".format(pseudo, password, bilan))
                       

    conn.commit() 




def insertion_site(pseudo, password, poste_demandee, date):
    """On verifie les bilans de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO site_emploie
                (id_user, poste_demandee, date)
                VALUES SELECT users.id
                FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}', '{2}', '{3}'""".format(pseudo,
                                                  password, poste_demandee, date))
                       

    conn.commit() 




#A FAIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIRE
def modification_cv(pseudo, password):
    """On verifie le cv de l'utilisateur"""
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT * FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}'""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]




def modification_motivation(pseudo, password):
    """On verifie la lettre de motivation de l'utilisateur"""
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT * FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}'""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]





def modification_message(pseudo, password):
    """On verifie le message aux recruteurs de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT * FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}'""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]




def modification_bilan(pseudo, password):
    """On verifie les bilans de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT * FROM users
                WHERE pseudo = '{0}' AND
                password = '{1}'""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]














