import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


def insertion_bilan(pseudo, password, bilan):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO bilan
                (bilan, id_user)
                VALUES ('{2}')
                SELECT users.id from users
                WHERE users.pseudo = '{0}'
                password = '{1}'""".format(pseudo, password, bilan))
                       

    conn.commit() 



