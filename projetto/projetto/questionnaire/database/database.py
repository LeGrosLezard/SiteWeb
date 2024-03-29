"""Database for documents + test"""

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


    return liste



def accord(pseudo, mode):

    #We recup id user from users
    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 
    cur = conn.cursor()


    liste = ["un", "deux", "trois", "quattre"]
    for i in liste:
        if mode == i:
            
            cur.execute("""SELECT {} FROM {}
                        WHERE (id_user = {});""".format(str(i), "bilan", id_user))
            conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste[0][0]







def insertion_bilan_premiere_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""UPDATE bilan
                SET bilan = %s
                WHERE id_user = {0};""".format(id_user), (bilan, ))
                       

    conn.commit() 


    cur.execute("""UPDATE bilan
                SET un = %s
                WHERE id_user = {0};""".format(id_user), (1, ))
                       

    conn.commit() 


def insertion_bilan_seconde_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""UPDATE bilan
                SET bilan1 = %s
                WHERE id_user = {0};""".format(id_user), (bilan, ))
                       

    conn.commit() 

    cur.execute("""UPDATE bilan
                SET deux = %s
                WHERE id_user = {0};""".format(id_user), (1, ))
                       

    conn.commit() 


def insertion_bilan_troisieme_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""UPDATE bilan
                SET bilan2 = %s
                WHERE id_user = {0};""".format(id_user), (bilan, ))
                       

    conn.commit() 

    cur.execute("""UPDATE bilan
                SET trois = %s
                WHERE id_user = {0};""".format(id_user), (1, ))
                       

    conn.commit()

    


def insertion_bilan_quatrieme_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""UPDATE bilan
                SET bilan3 = %s
                WHERE id_user = {0};""".format(id_user), (bilan, ))
                       

    conn.commit() 

    cur.execute("""UPDATE bilan
                SET quattre = %s
                WHERE id_user = {0};""".format(id_user), (1, ))
                       

    conn.commit() 



#--------------------SECONDE PARTIE------------------------------------
#----------------RECUPERATION DES BILANS-------------------------------


def recuperation_info_perso(pseudo):
    
    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""select nom, prenom from users
                WHERE (pseudo = '{0}');""".format(pseudo))
                       

    conn.commit()  

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste[0][0], liste[0][1]





def récupération_psycho(pseudo):

    
    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    print(id_user)

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT bilan FROM bilan
                WHERE id_user = %s;""", (id_user, ))
                       

    conn.commit() 



    rows = cur.fetchall()
    liste = [i for i in rows]


    liste = liste[0][0].replace("\n", "!")

    resume = []

    phrase = ""

    c = 0
    for i in liste:
        if i == "!":
            resume.append([phrase])
            phrase = ""

        else:
            phrase += i

            
    return resume
 



def recuperation_dictee(pseudo):

    
    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT bilan1 FROM bilan
                WHERE id_user = %s;""", (id_user, ))
                       

    conn.commit() 



    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste[0][0]



def recuperation_flexi(pseudo):

    
    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT bilan2 FROM bilan
                WHERE id_user = %s;""", (id_user, ))
                       

    conn.commit() 



    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste[0][0]



def recuperation_memoire(pseudo):

    
    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT bilan3 FROM bilan
                WHERE id_user = %s;""", (id_user, ))
                       

    conn.commit() 



    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste[0][0]

















