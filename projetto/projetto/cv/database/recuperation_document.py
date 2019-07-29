import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


def recuperation_id_pseudo(pseudo):
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""select id from users
                WHERE (pseudo = '{0}');""".format(pseudo))
                       

    conn.commit()  

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste[0][0]


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

    username = recuperation_id_pseudo(pseudo)

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT cv, cv1, cv2, cv3, cv4, cv5 FROM cv
                WHERE id_user = '{0}'
                ORDER BY(id_user);""".format(username))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste






def recuperation_bilan(pseudo):

    username = recuperation_id_pseudo(pseudo)

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT bilan FROM bilan
                WHERE id_user = '{0}'
                ORDER BY(id_user);
                """.format(username))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste



def recuperation_motivation(pseudo):

    username = recuperation_id_pseudo(pseudo)

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT lettre_motivation
                FROM motivation
                WHERE id_user = '{0}'
                ORDER BY(id_user);
                """.format(username))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste




def recuperation_message(pseudo):


    username = recuperation_id_pseudo(pseudo)

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT lettre_motivation
                FROM message
                WHERE id_user = '{0}'
                ORDER BY(id_user);
                """.format(username))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    
    return liste









