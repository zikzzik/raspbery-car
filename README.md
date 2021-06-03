# raspbery-car

Remarque : Il est nécessaire d'avoir le seveur, le client et la commande sur le même réseau.

Les étapes à suivre pour lancer le voiture (seveur, client, commande) :

1. Installer un environement Python 3, ainsi que le fichier requirement.txt.

2. Sur le serveur :
  - Paramétrer le fichier main_serveur.py (ip et port)
  - Exécuter la commande python3 main_serveur.py
  
3. Sur la commande :  
  - Paraméter le fichier main_command.py (ip, port et nom de la voiture)
  - Exécuter la commande  python3 main_command.py
  
4. Sur la voiture :
  - Paramétrer le fichier main_voiture.py (ip, port et nom de la voiture)
  - Exécuter la commande python3 main_serveur.py

