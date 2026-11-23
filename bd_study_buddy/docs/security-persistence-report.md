
# Study Buddy
## Rapport de sécurité et de persistance des données

### 1. Présentation du projet

Study Buddy est une application backend développée
avec FastAPI permettant aux utilisateurs de créer
des conversations privées et d'échanger des messages
avec un assistant intelligent.

L'objectif est de garantir la persistance des données
et la confidentialité des conversations.

### 2. Architecture technique

Technologies utilisées :

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- JWT
- Redis (cache facultatif)

### 3. Schéma de la base de données

La base de données contient trois tables principales.

#### Table Users

- id : identifiant unique
- email : adresse e-mail unique
- password_hash : mot de passe haché
- created_at : date de création

#### Table Conversations

- id : identifiant unique
- title : titre de la conversation
- user_id : identifiant du propriétaire
- created_at : date de création

Chaque conversation appartient à un utilisateur.

#### Table Messages

- id : identifiant unique
- conversation_id : conversation associée
- role : user ou assistant
- content : contenu du message
- tokens_used : nombre de tokens utilisés
- created_at : date de création

Chaque message appartient à une conversation.

### 4. Flux d'authentification

1. L'utilisateur s'inscrit avec son e-mail
   et son mot de passe.
2. Le mot de passe est haché avant stockage.
3. L'utilisateur se connecte avec ses identifiants.
4. Le backend vérifie le mot de passe.
5. Un JWT est généré après authentification.
6. Le client transmet le JWT dans ses requêtes.
7. FastAPI vérifie le token et identifie
   l'utilisateur actuel.

### 5. Protection des données privées

Chaque conversation est associée à un utilisateur
grâce au champ user_id.

Lorsqu'un utilisateur consulte une conversation,
le backend vérifie simultanément :

- L'identifiant de la conversation.
- L'identifiant de l'utilisateur connecté.

Un utilisateur ne peut donc consulter ou modifier
que ses propres conversations.

Les accès non autorisés retournent une erreur 404.

### 6. Persistance des messages

Les messages utilisateur et assistant sont enregistrés
dans la table Messages.

L'historique est conservé dans SQLite et peut être
consulté ultérieurement.

### 7. Cache temporaire

Redis peut être utilisé pour conserver temporairement
les résultats IA non sensibles.

Une durée d'expiration est définie pour chaque résultat.

Contrairement à SQLite, le cache est temporaire
et ses données peuvent être supprimées ou expirer.

Les données privées des utilisateurs ne sont pas
stockées dans un cache partagé.

### 8. Tests de sécurité

Les tests suivants doivent être réalisés :

- Inscription d'un utilisateur.
- Connexion avec des identifiants valides.
- Refus des mauvais identifiants.
- Refus d'un JWT invalide.
- Création d'une conversation.
- Enregistrement des messages.
- Consultation de son propre historique.
- Refus d'accès à la conversation d'un autre utilisateur.
- Refus d'ajout de messages dans une conversation
  appartenant à un autre utilisateur.

### 9. Conclusion

Le backend Study Buddy met en place un système
d'authentification JWT, une base de données SQLite,
la persistance des conversations et des messages,
ainsi qu'une vérification de propriété des données.

Ces mécanismes permettent de renforcer la sécurité
et la confidentialité des échanges entre utilisateurs.
