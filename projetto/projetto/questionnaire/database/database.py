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


def insertion_bilan_premiere_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO bilan
                (id_user, bilan)
                VALUES(%s, %s);""", (id_user, bilan))
                       

    conn.commit() 


def insertion_bilan_seconde_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO bilan
                (id_user, bilan1)
                VALUES(%s, %s);""", (id_user, bilan))
                       

    conn.commit() 




def insertion_bilan_troisieme_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO bilan
                (id_user, bilan2)
                VALUES(%s, %s);""", (id_user, bilan))
                       

    conn.commit() 



def insertion_bilan_quatrieme_partie(pseudo, bilan):


    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO bilan
                (id_user, bilan3)
                VALUES(%s, %s);""", (id_user, bilan))
                       

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


    liste = liste[1][0].replace("\n", "!")

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
 


































