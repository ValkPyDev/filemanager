# 📂 filemanager

Une bibliothèque Python ultra-légère et robuste pour gérer simplement vos fichiers JSON sans vous soucier des fichiers manquants ou corrompus.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Site Web](https://img.shields.io/badge/Site_Web-blue.svg?logo=org&logoColor=white)](https://valk-solutions.fr/projets/valk-filemanager/)

## ✨ Fonctionnalités

- **Auto-Réparation :** Si un fichier JSON est corrompu ou mal formé, la bibliothèque le détecte et le réinitialise proprement pour éviter le crash de votre application.
- **Sécurité :** Création automatique des fichiers s'ils n'existent pas lors d'une tentative de lecture ou d'écriture.
- **Simplicité :** Enregistrez une clé et une valeur en une seule ligne de code sans charger tout le fichier manuellement.

## 🚀 Installation

Installez directement depuis PyPI:

```bash
pip install filemanager
```

## 🛠️ Utilisation

```py
from filemanager import load_data, save_data, save_key, exist, create_json
filename = "config.json"

# 1. Vérifier si le fichier existe
print(exist(filename)) # Retourne False ou True

# 2. Sauvegarder des données complètes (Crée le fichier automatiquement s'il n'existe pas)
data_utilisateurs = {
    "pseudo": "Valk",
    "premium": True
}
save_data(filename, data_utilisateurs)

# 3. Ajouter ou modifier une clé spécifique facilement
save_key(filename, "version", "1.0.2")

# 4. Charger les données du fichier
config = load_data(filename)
print(config)
# Résultat : {'pseudo': 'Valk', 'premium': True, 'version': '1.0.2'}

# 5. Créer un json avec un dictionnaire initial ou non
create_json(filename)
# Créer un JSON avec un dictionnaire vide: {}

create_json(filename, {"valeur_de_base": True})
# Créer un JSON avec un dictionnaire: {"valeur_de_base": True}
```