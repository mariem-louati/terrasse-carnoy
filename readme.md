# ☕ La Terrasse Carnoy

Application web de commande en ligne pour le salon de thé **La Terrasse Carnoy**.

🌐 **Site en production** : [terrasse-carnoy.onrender.com](https://terrasse-carnoy.onrender.com)

---

## 📋 Description

La Terrasse Carnoy est une application web complète permettant aux clients de consulter le menu, parcourir les catégories et commander en ligne. Le projet a été développé avec Django et déployé sur Render avec une base de données PostgreSQL et un stockage d'images via Cloudinary.

---

## ✨ Fonctionnalités

- 🍽️ **Menu par catégories** — Cafés, thés, jus, pâtisseries, sandwichs...
- 🛒 **Panier d'achat** — Ajout, modification, suppression et calcul automatique du total
- 🖼️ **Photos des produits** — Images stockées et servies via Cloudinary CDN
- 👨‍💼 **Interface Admin** — Gestion complète des produits et catégories via Django Admin
- 📱 **Design responsive** — Interface adaptée mobile, tablette et desktop
- 🎬 **Vidéo Hero Banner** — Page d'accueil avec vidéo en arrière-plan
- 💰 **Gestion des promotions** — Prix promo et badges nouveauté

---

## 🏗️ Architecture Technique

| Composant | Technologie |
|-----------|-------------|
| Backend | Django 6.0 (Python) |
| Base de données | PostgreSQL |
| Stockage images | Cloudinary |
| Fichiers statiques | WhiteNoise |
| Déploiement | Render |
| CI/CD | GitHub Actions |

---

## 🚀 Installation locale

### Prérequis
- Python 3.14+
- pip

### Étapes

```bash
# 1. Cloner le projet
git clone https://github.com/mariem-louati/terrasse-carnoy.git
cd terrasse-carnoy

# 2. Créer un environnement virtuel
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Créer le fichier .env
cp .env.example .env
# Remplir les variables dans .env

# 5. Lancer les migrations
python manage.py migrate

# 6. Créer un superutilisateur
python manage.py createsuperuser

# 7. Lancer le serveur
python manage.py runserver
```

### Variables d'environnement (.env)

```env
SECRET_KEY=votre_secret_key
DEBUG=True
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=votre_api_key
CLOUDINARY_API_SECRET=votre_api_secret
DATABASE_URL=postgresql://...  # optionnel en local
```

---

## 📁 Structure du projet

```
terrasse-carnoy/
├── blogproject/
│   ├── settings.py       # Configuration Django
│   ├── urls.py           # URLs principales
│   └── wsgi.py
├── shop/
│   ├── models.py         # Modèles : Product, Category, Order
│   ├── views.py          # Vues : liste produits, panier...
│   ├── urls.py           # URLs de l'application
│   ├── admin.py          # Interface admin
│   ├── templates/        # Templates HTML
│   └── static/           # CSS, JS, images statiques
├── media/                # Images en local (dev)
├── requirements.txt
├── manage.py
└── Procfile              # Configuration Render
```

---

## 🌐 Déploiement sur Render

Le projet est configuré pour un déploiement automatique sur Render :

1. **Build** : `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic`
2. **Start** : `gunicorn blogproject.wsgi`

Variables d'environnement à configurer sur Render :
- `SECRET_KEY`
- `DEBUG=False`
- `DATABASE_URL`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`
- `DJANGO_SETTINGS_MODULE=blogproject.settings`

---

## 🔧 Défis techniques résolus

- **Images Cloudinary** — Résolution du problème d'affichage en production avec la nouvelle API `STORAGES` de Django 6.0
- **Persistance des données** — Migration de SQLite vers PostgreSQL pour éviter la perte de données lors des redéploiements
- **Variables d'environnement** — Configuration via `python-decouple` pour séparer les environnements dev/prod

---

## 👩‍💻 Auteur

**Mariem** — Développeuse Full Stack  
🌐 [terrasse-carnoy.onrender.com](https://terrasse-carnoy.onrender.com)