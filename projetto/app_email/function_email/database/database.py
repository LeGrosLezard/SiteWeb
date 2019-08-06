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

    cur.execute("""select pseudo, nom, prenom, addresse, from users;""")

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]


def recup_message(pseudo):

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""select * from users;""")

    conn.commit() 

    rows = cur.fetchall()
    liste = [i for i in rows]
