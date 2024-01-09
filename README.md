# Snake Game

Ce projet consiste en un jeu Snake développé en Python utilisant le module Turtle et la programmation orientée objet.

## Présentation du jeu

Le jeu Snake est un jeu classique où un serpent se déplace sur l'écran pour manger de la nourriture et grandir. Le but est de maintenir le serpent en mouvement et d'éviter qu'il ne se heurte aux murs ou à son propre corps.

## Contenu du projet

### Fichiers inclus :

- `main.py`: Le fichier principal du jeu qui initialise l'interface graphique, crée les éléments du jeu (serpent, nourriture, score) et gère la logique du jeu.
- `snake.py`: Ce fichier définit la classe Snake qui gère le serpent, sa taille, ses déplacements et ses contrôles.
- `scoreboard.py`: Ce fichier contient la classe Scoreboard qui gère l'affichage du score et du meilleur score, ainsi que la sauvegarde du meilleur score dans un fichier externe.
- `food.py`: Le fichier contient la classe Food qui représente la nourriture que le serpent doit manger pour grandir.
- `data.txt`: Ce fichier contient le meilleur score obtenu par le joueur. Il est mis à jour à chaque nouveau meilleur score obtenu.

## Comment jouer ?

Exécutez le fichier `main.py` pour démarrer le jeu.
Les contrôles du serpent sont les suivants :
- Haut : Flèche vers le haut
- Bas : Flèche vers le bas
- Droite : Flèche vers la droite
- Gauche : Flèche vers la gauche

Le jeu continue tant que le serpent ne se heurte pas aux murs ou à lui-même.

![Game Screenshot](/assets/playground.png)

(Insérez une capture d'écran de l'interface du jeu ici)

### Remarques

- Assurez-vous d'avoir Python installé sur votre machine pour exécuter le jeu.
- Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
