import os
import json
from typing import Any

def create_json(filename: str, data = {}) -> None:
    """Créer un fichier JSON vide contenant un dictionnaire initial.

    Args:
        filename (str): Le chemin ou le nom du fichier à créer.
        data (dict) (optionnel): Un dictionnaire écrit dans le fichier.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"[ERREUR] Impossible de créer le fichier '{filename}' | {e}")


def exist(filename: str) -> bool:
    """Vérifier si un fichier existe sur le disque.

    Args:
        filename (str): Le chemin ou le nom du fichier.

    Returns:
        bool: True si le fichier existe, False sinon.
    """
    return os.path.exists(filename)

def check_file(filename: str) -> bool:
    """Vérifier la validité d'un fichier JSON et le réparer s'il est corrompu.

    Si le fichier n'existe pas ou s'il est illisible/corrompu, il est automatiquement
    réinitialisé avec un dictionnaire vide `{}`.

    Args:
        filename (str): Le chemin ou le nom du fichier.

    Returns:
        bool: True si le fichier est valide ou a été réparé avec succès, False en cas d'erreur d'écriture.
    """
    if not exist(filename):
        create_json(filename)
        return exist(filename)

    try:
        with open(filename, "r", encoding="utf-8") as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        print(f"[ATTENTION] Le fichier '{filename}' est corrompu. Réinitialisation.")
        create_json(filename)
        return exist(filename)

def load_data(filename: str) -> dict:
    """Charger les données d'un fichier JSON sous forme de dictionnaire.

    Args:
        filename (str): Le chemin ou le nom du fichier à lire.

    Returns:
        dict: Le contenu du fichier JSON, ou un dictionnaire vide en cas d'erreur.
    """
    if not check_file(filename):
        return {}
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERREUR] Impossible de lire le fichier '{filename}' | {e}")
        return {}
        
def save_data(filename: str, data: dict) -> None:
    """Sauvegarder un dictionnaire complet dans un fichier JSON.

    Args:
        filename (str): Le chemin ou le nom du fichier.
        data (dict): Les données à sauvegarder.
    """
    if not check_file(filename):
        return

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"[ERREUR] Impossible d'écrire dans le fichier '{filename}' | {e}")
        
def save_key(filename: str, key: str, value: Any) -> None:
    """Ajouter ou mettre à jour une clé spécifique dans le fichier JSON.

    Args:
        filename (str): Le chemin ou le nom du fichier.
        key (str): La clé à modifier ou créer.
        value (Any): La valeur à associer à la clé.
    """

    data = load_data(filename)
    data[key] = value
    save_data(filename, data)