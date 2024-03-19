# GES calendar

Fork du projet [ges-calendar](https://github.com/Florent-COMPAGNONI/ges-calendar) de [@Florent-COMPAGNONI](https://github.com/Florent-COMPAGNONI).

Ges calendar est une application python permettant de récupérer son planning [myGES](https://myges.fr) et de créer un fichier .ics, permettant ainsi de l'importer sur sur n'importe quel agenda.


## Installation


Pré-requis:
- [python 3.10](https://www.python.org/downloads/) ou version ultérieure
- vos identifiants myGES

Lancer les commandes suivantes pour récupérer le projet et installer les paquets.
```
git clone https://github.com/Florent-COMPAGNONI/ges_calendar.git
pip install -r ./requirements.txt
```


Créer un fichier **.env** à la racine du projet en se basant sur le fichier [.env_template](./.env_template)


## Utilisation


Pour lancer le script:


```
python ./main.py
```


Par défaut un fichier .ics est créé à la racine du projet avec tous les événements du mois en cours, il est possible de spécifier les dates de début et de fin.


```
python ./main.py --start-date=2023-09-11 --end-date=2023-09-17
```


