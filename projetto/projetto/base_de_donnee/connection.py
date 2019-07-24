import psycopg2

from CONFIG import DATABASE
from CONFIG import USER
from CONFIG import HOST
from CONFIG import PASSWORD


class Table:

    def creation_table_connexion():


        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()



        cur.execute("""create table connexion(
                    id serial PRIMARY KEY,
                    pseudo VARCHAR(100),
                    password VARCHAR(100));""")
        
        conn.commit()




if __name__ == "__main__":
    
    crea_table = Table.creation_table_connexion()
