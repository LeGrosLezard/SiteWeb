import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


def insertion_bilan_premiere_partie(pseudo, bilan):


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""UPDATE bilan
                set bilan = %s
                WHERE id_user = {0};""".format(user, (bilan, )))
                       

    conn.commit() 



