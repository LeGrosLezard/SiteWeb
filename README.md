# SiteWeb

-------------------------------------------------------

cv -> dire de dézoomé au pire le mec met le sien

faut faire les mise en database de ce qui a été fait pour ne pas spam (emploi + adresse mail du genre dev python ref 18498498456456498 mail == dawan ne pas lui envoyer mais si ref dzadazddazdaz envoyer

les textes des tests

----------------------------------------

remplacer tous les path par celui du serveur



-----------------------------------------

----------------------------------------------------

database non spam

les tests

faire les tiens (bien sur j'ai le droit de tricher c mon site)


--------------------------------------------------------

# QUI ?

Jeune developpeur web sortant de la formation OpenClassrooms 

# Quoi ?

Projetto est un site en logne qui permet aux chercheurs d'emploi de trouver un travail plus rapidement et plus efficacement.

Projetto aide aussi les personnes ne sachant pas faire de CV, de lettre de motivation en leur proposant un tutoriel.

Enfin, Projetto envoie tous ces éléments aux différentes entreprises cherchant un salarié via un scrappage de Pole emploi.



# COMMENT ?

Nous nous basons sur la technique de scrap. Nous prenons les informations du site pole emploi. Essayons dans un premier temps de prendre l'information mail et dans le cas échéant le nom de l'entreprise qui parfois apparait en bas de page ou sur la page "description".

Si aucunes de ces informations n'est présente, nous nous dirigeons alors vers le site partenaire. Une fois sur ce site, nous essayons de trouver le nom de l'entreprise. 

Pour cela, nous avons défini plusieurs conditions selon le site (careerbuilder, carriereonline, talentplug, stepstone, monster, joboolo,
inzejob). 

Ensuite une fois le nom de l'entreprise nous allons chercher une adresse mail sur google.

Bien sur des fois la nombre d'email n'est pas tres grand (métier rare, petite ville) 

# COMPLEMENTS

Afin de ne pas spammer nous mettons en database les sites et référence de la demande en database.

Nous effectuons cela via une tache cron depuis un serveur hébergé par digital océan car notre site web est sur heroku qui impose un time out d'au maximum 30 secondes. Notre opération de mail peut prendre plusieurs minutes





# ARCHITECTURE

la meme des fois je comprend pas et les erreurs faut les cherchers dans 4 trucks différents ^^ mais jadore comme ca

Le site est codé de cette facon:

views -> views_functions -> fichier de traitement -> database

On apel la database, on traite la réponse, on combine toutes ces réponses pour l'appeler dans la views ou recevoir l'apel



# ALGORYTHME

Afin de séduire le client nous ne le feront pas venir chaque jour demandé d'envoyer des émails. C'est pour cela que nous effectuons une tache cron. Chaque jour nous enverrons des emails à de nouvelles annonces. Un système de non spam à été mis en oeuvre

a faire + vidéo


# LES DOCUMENTS SE SITUENT DANS DOCUMENT

- docuemnt truk fonctionnel

- technique

- zooning

- truk balade site ect




#si quelqu'un à vus ce projet et que tu veux l'essayer envoie moi un msg a jb26400@hotmail.fr pcque aucunes taches cron ne sera mise en place sans utilisateur je lance le script pour moi mais je vais pas le faire chaque jour enfete et du coup je mettrai une tache cron pour toi
