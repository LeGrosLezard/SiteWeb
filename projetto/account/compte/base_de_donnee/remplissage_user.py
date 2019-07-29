import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD



def insertion_user(nom, prenom, date, sexe, email, fixe, password,
                   pseudo, lieu_habitation, portable):


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


    
    cur.execute("""SELECT id FROM users
                where pseudo='{0}' """.format(pseudo))
                       

    conn.commit() 

    rows = cur.fetchall()
    user = [i for i in rows]
    user = user[0][0]
    

    cur.execute("""INSERT INTO cv
                (id_user, cv, cv1, cv2, cv3, cv4, cv5)
                values(%s, '', '', '', '', '', '');""",(user, ))

    conn.commit()



    cur.execute("""INSERT INTO motivation
                (id_user, lettre_motivation,
                lettre_motivation1,
                lettre_motivation2,
                lettre_motivation3,
                lettre_motivation4,
                lettre_motivation5)
                values(%s, '', '', '', '', '', '');""",(user, ))

    conn.commit()

    cur.execute("""INSERT INTO message
                (id_user, lettre_motivation,
                lettre_motivation1,
                lettre_motivation2,
                lettre_motivation3,
                lettre_motivation4,
                lettre_motivation5)
                values(%s, '', '', '', '', '', '');""",(user, ))

    conn.commit()












