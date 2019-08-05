import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD

from .CONFIG import CV1
from .CONFIG import CV2
from .CONFIG import CV3
from .CONFIG import CV4
from .CONFIG import CV5
from .CONFIG import CV6_1
from .CONFIG import CV6_2
from .CONFIG import CV6_3
from .CONFIG import CV7
from .CONFIG import METIER
from .CONFIG import FORMATION
from .CONFIG import POSTE1
from .CONFIG import POSTE2
from .CONFIG import POSTE3

from .CONFIG import MOTIVATION1
from .CONFIG import MOTIVATION2
from .CONFIG import MOTIVATION3
from .CONFIG import MOTIVATION4
from .CONFIG import MOTIVATION5
from .CONFIG import MOTIVATION6
from .CONFIG import CODE
from .CONFIG import VILLE
from .CONFIG import POSTE_MOTIVATION




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
    
    print(user)
    cur.execute("""INSERT INTO cv
                (id_user, cv, cv1, cv2, cv3, cv4,
                cv6_1, cv6_2, cv6_3, cv7, metier, formation, poste1,
                poste2, poste3)
                values(%s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s);""",(user,
                                                        CV1,
                                                        CV2,
                                                        CV3,
                                                        CV4,
                                                        CV5,
                                                        CV6_1,
                                                        CV6_2,
                                                        CV6_3,
                                                        CV7,
                                                        METIER,
                                                        FORMATION,
                                                        POSTE1,
                                                        POSTE2,
                                                        POSTE3))

    conn.commit()



    cur.execute("""INSERT INTO motivation
                (id_user,
                lettre_motivation,
                lettre_motivation1,
                lettre_motivation2,
                lettre_motivation3,
                lettre_motivation4,
                lettre_motivation5,
                code,
                ville,
                poste_moitivation)
                values(%s, %s, %s, %s, %s, %s, %s, 26400, 'Ville',
                'Serveur le caffé la ristourne');""",(user,
                                                    MOTIVATION1,
                                                    MOTIVATION2,
                                                    MOTIVATION3,
                                                    MOTIVATION4,
                                                    MOTIVATION5,
                                                    MOTIVATION6))

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












