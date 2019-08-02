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



def insertion_part_motivation(pseudo, part, mode):
    """Here we insert into database the part cv."""

    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()


    if mode == "un":
        print(id_user)
        cur.execute("""UPDATE motivation
                    SET lettre_motivation = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "deux":

        cur.execute("""UPDATE motivation
                    SET lettre_motivation1 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "trois":

        cur.execute("""UPDATE motivation
                    SET lettre_motivation2 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "quattre":

        cur.execute("""UPDATE motivation
                    SET lettre_motivation3 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "cinq":

        cur.execute("""UPDATE motivation
                    SET lettre_motivation4 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "six":

        cur.execute("""UPDATE motivation
                    SET lettre_motivation5 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 

    if mode == "poste_motivation":

        cur.execute("""UPDATE motivation
                    SET poste_moitivation = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 

    if mode == "code":

        cur.execute("""UPDATE motivation
                    SET code = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 

    if mode == "ville":

        cur.execute("""UPDATE motivation
                    SET ville = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 
