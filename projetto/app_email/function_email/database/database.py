import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD

def recup_user(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""select id, nom, prenom, lieu_habitation, fixe,
                portable, email from users;""")

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]
    return liste

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

    return id, nom, prenom, lieu_habitation, fixe,\
                portable, email, liste[0], liste[1],\
                liste[2], liste[3], liste[4], liste[5]















