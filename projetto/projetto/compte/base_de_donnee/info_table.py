import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


def donnee_user(pseudo):
        
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT pseudo from users
                WHERE pseudo LIKE '%{}%'""".format(pseudo))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste






def donnee_email(email):
        
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT email from users
                WHERE email LIKE '%{}%'""".format(email))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste




def donnee_telephone_portable(portable):
        
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT portable from users
                WHERE portable = {}""".format(portable))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste




































