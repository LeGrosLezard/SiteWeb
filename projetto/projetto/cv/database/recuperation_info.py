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


def recuperation_info(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT nom, prenom, lieu_habitation, fixe,
                portable, email FROM users
                WHERE pseudo = '{0}' """.format(pseudo))
                       

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    print(liste)
    return liste[0][0], liste[0][1], liste[0][2],\
           liste[0][3], liste[0][4], liste[0][5]
