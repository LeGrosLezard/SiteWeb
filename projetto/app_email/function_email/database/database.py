import psycopg2

from CONFIG import DATABASE
from CONFIG import USER
from CONFIG import HOST
from CONFIG import PASSWORD

def recup_user(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""select id, nom, prenom, lieu_habitation, fixe,
                portable, email from users
                where pseudo = '{}';""".format(pseudo))

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste[0][0], liste[0][1], liste[0][2], liste[0][3],\
           liste[0][4], liste[0][5], liste[0][6]

def recup_message(pseudo):

    id, nom, prenom, lieu_habitation, fixe,\
                portable, email = recup_user(pseudo)


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 


    cur = conn.cursor()

    cur.execute("""select lettre_motivation,
                            lettre_motivation1,
                            lettre_motivation2,
                            lettre_motivation3,
                            lettre_motivation4,
                            lettre_motivation5
                            from message
                            where id_user = {};""".format(id))

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]

    return nom, prenom, lieu_habitation, fixe,\
                portable, email, liste[0][0], liste[0][1],\
                liste[0][2], liste[0][3], liste[0][4], liste[0][5]


def mail_verification(pseudo):

    id_user, _, _, _, _, _, _ = recup_user(pseudo)
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 


    cur = conn.cursor()

    cur.execute("""
                SELECT
                poste_demandee, url
                FROM site_emploie
                where id_user = %s;""", (id_user, ))

    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]

    print(liste)
    return liste

mail_verification("Jbaw")

def mail_stock(pseudo, poste, url, date):

    id_user, _, _, _, _, _, _ = recup_user(pseudo)
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 


    cur = conn.cursor()

    cur.execute("""
                INSERT INTO site_emploie
                (id_user, poste_demandee, url, date)
                VALUES(%s, %s, %s, %s)""", (id_user, poste, url, date))

    conn.commit() 






    
    









