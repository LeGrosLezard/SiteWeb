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



def insertion_part_message(pseudo, part, mode):
    """Here we insert into database the part message."""

    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()


    if mode == "un":

        cur.execute("""UPDATE message
                    SET lettre_motivation = '{1}'
                    WHERE id_user = '{0}';""".format(id_user, part))
                           

        conn.commit() 



    if mode == "deux":

        cur.execute("""UPDATE message
                    SET lettre_motivation1 = '{1}'
                    WHERE id_user = '{0}';""".format(id_user, part))
                           

        conn.commit() 



    if mode == "trois":

        cur.execute("""UPDATE message
                    SET lettre_motivation2 = '{1}'
                    WHERE id_user = '{0}';""".format(id_user, part))
                           

        conn.commit() 



    if mode == "quattre":

        cur.execute("""UPDATE message
                    SET lettre_motivation3 = '{1}'
                    WHERE id_user = '{0}';""".format(id_user, part))
                           

        conn.commit() 



    if mode == "cinq":

        cur.execute("""UPDATE message
                    SET lettre_motivation4 = '{1}'
                    WHERE id_user = '{0}';""".format(id_user, part))
                           

        conn.commit() 



    if mode == "six":

        cur.execute("""UPDATE message
                    SET lettre_motivation5 = '{1}'
                    WHERE id_user = '{0}';""".format(id_user, part))
                           

        conn.commit() 






