# LLM_CONTINUUM

Projet réalisé par une étudiante de l'ENSC [ROCHE Eléa](https://github.com/elroche)
Un powerpoint expliquant l'objectif du projet ainsi qu'une explication du code proposé est disponible au [lien suivant](https://github.com/elroche/IA_oso_player/blob/main/Rapport_IA_Perret_Roche.pdf).

## Installations
### Installation Python
Assurez-vous que Python est installé sur votre système. Si ce n'est pas le cas, téléchargez et installez Python à partir du site officiel : [Télécharger Python](https://www.python.org/downloads/).

### Installation de l'IDE (VSCode)
Téléchargez et installez Visual Studio Code (VSCode) à partir du site officiel : [Télécharger VSCode](https://code.visualstudio.com/).

### Installation d'Ollama
Suivez les instructions fournies sur le site pour installer Ollama sur votre système à partir de [l'adresse suivante](https://ollama.com/).

## Exécution de Ollama
Exécutez la commande suivante pour lancer Ollama :
```console
ollama run llama2
```

## Configuration de l'environnement virtuel
Installez virtualenv en exécutant la commande suivante :
```console
pip install virtualenv
```

Créez un nouvel environnement virtuel en exécutant la commande suivante :
```console
virtualenv venv
```

Activez l'environnement virtuel en exécutant la commande suivante (pour Windows) :
```console
venv\Scripts\activate
```

## Dependances
### Installation des dépendances
Installez les dépendances à partir du fichier requirements.txt en exécutant la commande suivante :
```console
pip install -r requirements.txt
```

### Sauvegarde des dépendances
Si vous installez de nouvelles dépendances, assurez-vous de mettre à jour le fichier requirements.txt en exécutant la commande suivante  : 
```console
pip freeze > requirements.txt
```