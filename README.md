# Générateur de Payload avec Interface Graphique

Ce projet propose un générateur simple et efficace de payloads réseau, avec une interface graphique intuitive développée en Python (Tkinter). Il permet de créer facilement des payloads courants comme des reverse shells ou bind shells en quelques clics, sans avoir à se souvenir des commandes exactes.

## Fonctionnalités

- Interface graphique conviviale et légère.
- Génération dynamique de payloads selon l’adresse IP, le port et le type choisi.
- Support des payloads les plus utilisés (bash reverse shell, python reverse shell, netcat bind shell).
- Zone de texte pour afficher et copier facilement le payload généré.
- Validation basique des entrées pour éviter les erreurs communes.

## Utilisation

1. Saisissez l’adresse IP cible.
2. Entrez le port de connexion.
3. Sélectionnez le type de payload souhaité dans la liste déroulante.
4. Cliquez sur **Générer** pour afficher le payload.
5. Copiez le payload pour l’utiliser dans vos tests ou projets.

## Prérequis

- Python 3.x (Tkinter inclus par défaut dans la plupart des installations).

## Installation

Clonez le dépôt et lancez le script Python :

```bash
git clone https://github.com/votre-utilisateur/votre-projet.git
cd votre-projet
python3 payload_generator.py
