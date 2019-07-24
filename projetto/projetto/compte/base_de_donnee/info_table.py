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
    
    cur.execute("""SELECT * from user
                WHERE pseudo LIKE '%%s%'""", (pseudo, ))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste






def donnee_email(email):
        
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT * from user
                WHERE email LIKE '%%s%'""", (email))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste




def donnee_telephone_portable(portable):
        
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""SELECT * from user
                WHERE portable LIKE '%%s%'""", (portable))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste




































