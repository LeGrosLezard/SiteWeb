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



def insertion_part_cv(pseudo, part, mode):
    """Here we insert into database the part cv."""

    id_user = recuperation_id_pseudo(pseudo)
    id_user = id_user[0][0]
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()


    if mode == "un":

        cur.execute("""UPDATE cv
                    SET cv = %s
                    WHERE id_user = %s;""",(part, int(id_user)))
                           

        conn.commit() 



    if mode == "deux":

        cur.execute("""UPDATE cv
                    SET cv1 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "trois":


        cur.execute("""UPDATE cv
                    SET cv2 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))                    

        conn.commit() 



    if mode == "quattre":


        cur.execute("""UPDATE cv
                    SET cv3 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))                       

        conn.commit() 



    if mode == "cinq":


        cur.execute("""UPDATE cv
                    SET cv4 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "six_un":


        cur.execute("""UPDATE cv
                    SET cv6_1 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 




    if mode == "six_deux":


        cur.execute("""UPDATE cv
                    SET cv6_2 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "six_trois":


        cur.execute("""UPDATE cv
                    SET cv6_3= %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit()



    if mode == "sept":


        cur.execute("""UPDATE cv
                    SET cv7 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 


    if mode == "metier":

        cur.execute("""UPDATE cv
                    SET metier = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 

    if mode == "formation":


        cur.execute("""UPDATE cv
                    SET formation = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 



    if mode == "poste1":


        cur.execute("""UPDATE cv
                    SET poste1 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 




    if mode == "poste2":


        cur.execute("""UPDATE cv
                    SET poste2 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 


    if mode == "poste3":


        cur.execute("""UPDATE cv
                    SET poste3 = %s
                    WHERE id_user = {0};""".format(id_user), (part, ))
                           

        conn.commit() 










