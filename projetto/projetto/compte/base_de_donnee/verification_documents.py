import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


def verifier_cv(pseudo, password):
    """On verifie le cv de l'utilisateur"""
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""select cv.cv from cv, users
                where pseudo = '{0}' AND
                password = '{1}' AND
                users.id = cv.id_user""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]




def verifier_motivation(pseudo, password):
    """On verifie la lettre de motivation de l'utilisateur"""
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""select motivation.lettre_motivation
                from motivation, users
                where pseudo = '{0}' AND
                password = '{1}' AND
                users.id = motivation.id_user""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]





def verifier_message(pseudo, password):
    """On verifie le message aux recruteurs de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""select message.lettre_motivation
                from message, users
                where pseudo = '{0}' AND
                password = '{1}' AND
                users.id = message.id_user""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]




def verifier_bilan(pseudo, password):
    """On verifie les bilans de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""select bilan.bilan
                from bilan, users
                where pseudo = '{0}' AND
                password = '{1}' AND
                users.id = bilan.id_user""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]




def verifier_site_demandee(pseudo, password):
    """On verifie les demande deja fait de l'utilisateur"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""select site_emploie.poste_demandee
                from site_emploie, users
                where pseudo = '{0}' AND
                password = '{1}' AND
                users.id = site_emploie.id_user""".format(pseudo, password))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]













