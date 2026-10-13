# 🤖 Kutiwa DevOps Agent

Bienvenue dans le **Kutiwa DevOps Agent**, un assistant intelligent et chaleureux propulsé par l'IA, conçu pour automatiser et simplifier vos tâches DevOps directement via WhatsApp.

## 🌟 Description du Projet

Le **Kutiwa Agent** agit comme un copilote DevOps personnel. Il peut :
- 📝 Rédiger et mettre à jour votre documentation (README, CHANGELOG, etc.).
- 🚀 Déployer des changements directement sur GitHub.
- 🐳 Gérer des conteneurs Docker.
- 📊 Analyser des logs et suggérer des corrections.

L'agent est capable de comprendre le contexte de votre dépôt et d'appliquer les changements avec précision, tout en maintenant un ton professionnel et amical.

## 🏗️ Architecture Technique

Le projet repose sur une architecture modulaire et scalable :

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   WhatsApp  │◄─────►│    N8n      │◄─────►│   LLM / AI  │
│   (Waha)    │       │ (Orchestrateur)│      │  (Brain)    │
└─────────────┘       └──────┬──────┘       └─────────────┘
                             │
                             ▼
                      ┌─────────────┐
                      │   GitHub    │
                      │  (Actions)  │
                      └─────────────┘
```

1.  **Waha (WhatsApp)** : Sert de pont entre l'utilisateur et le système. Il gère la réception des messages WhatsApp et l'envoi des réponses de l'agent.
2.  **N8n (Automation)** : Le cœur de la logique. Il orchestre le flux de travail :
    - Reçoit le message de Waha.
    - Interroge le modèle d'IA.
    - Exécute les actions (ex: script de déploiement, lecture de fichiers).
    - Envoie le résultat final à Waha.
3.  **Docker Compose** : Permet de déployer l'ensemble du stack (Waha, N8n, et les services nécessaires) en une seule commande, garantissant un environnement reproductible.

## 🚀 Guide de Démarrage Rapide

### Prérequis
- [Docker](https://www.docker.com/) et Docker Compose installés.
- Un compte GitHub avec accès au dépôt.
- Un token WhatsApp (via la API Business ou un service de bridge comme Waha).

### Installation

1.  **Cloner le dépôt** :
    ```bash
    git clone https://github.com/Tanguy-coder/kutiwa-n8n-challenge.git
    cd kutiwa-n8n-challenge
    ```

2.  **Configurer les variables d'environnement** :
    Creer un fichier `.env` à la racine du projet :
    ```env
    # Variables Waha
    WAHA_API_KEY=your_waha_api_key
    WAHA_INSTANCE_ID=your_instance_id

    # Variables N8n
    N8N_ENCRYPTION_KEY=your_secure_encryption_key

    # Variables GitHub
    GITHUB_TOKEN=your_github_pat
    GITHUB_REPO=Tanguy-coder/kutiwa-n8n-challenge
    ```

3.  **Lancer le stack** :
    ```bash
    docker-compose up -d
    ```

4.  **Vérifier les services** :
    - N8n : `http://localhost:5678`
    - Waha : Selon votre configuration (souvent sur le port 3000+).

### Utilisation

Une fois le stack lancé, envoyez un message à votre numéro WhatsApp lié à l'instance Waha.
Exemple : *"Peux-tu mettre à jour le README en ajoutant une section sur les tests ?"*

L'agent répondra avec un aperçu et vous demandera confirmation pour pousser les changements.

## 📄 Licence

Ce projet est sous licence MIT. N'hésitez pas à le fork et à l'améliorer !
