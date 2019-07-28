import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD




def recuperation_nom(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT nom, prenom FROM users
                WHERE pseudo = '{0}' """.format(pseudo))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]


def recuperation_cv(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT nom, prenom FROM users
                WHERE pseudo = '{0}' """.format(pseudo))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste[0][0], liste[0][1]






def recuperation_bilan(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT bilan.bilan FROM bilan, users
                WHERE users.pseudo = '{0}' AND
                bilan.id_user = users.id
                """.format(pseudo))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste



def recuperation_motivation(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT motivation.lettre_motivation
                FROM motivation, users
                WHERE users.pseudo = '{0}' AND
                motivation.id_user = users.id
                """.format(pseudo))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste




def recuperation_motivation(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT motivation.lettre_motivation
                FROM motivation, users
                WHERE users.pseudo = '{0}' AND
                motivation.id_user = users.id
                """.format(pseudo))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste









