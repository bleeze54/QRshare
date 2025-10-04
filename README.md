# QRshare

**QRshare** est une application permettant de **générer, partager et scanner des codes QR** de manière simple et efficace. Idéal pour échanger des liens, des textes ou des informations rapidement via un format universel.

---

## 📌 Fonctionnalités

| Fonctionnalité               | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **Scan de QR codes**         | Utilise la caméra de ton appareil pour partager des QR codes en temps réel.    |
| **Personnalisation**         | Partage les avec le monde entier     |

---

## 🛠 Technologies Utilisées

| Outil/Langage  | Rôle                          |
|----------------|---------------------------------------|
| **Python**     | Langage principal (backend/logique).  |
| **Django**     | Framework web.                        |
| **OpenCV**     | Traitement d'images pour le scanning. |
| **Pillow**     | Génération et manipulation d'images.  |
| **HTML/CSS/JS**| Interface utilisateur (frontend).     |

---

## 🚀 Installation

### Prérequis
- Python 3.8+
- Pip (pour les dépendances)

### Étapes
1. Clone le dépôt :
   ```bash
   git clone https://github.com/bleeze54/QRshare.git
   cd QRshare
   ```

2. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Lance l'application :
   ```bash
   python manage.py runserver 8000
   ```

4. Ouvre ton navigateur à l'adresse :
   ```
   http://localhost:8000
   ```

---

## 📂 Structure du Projet

```
QRshare/
├── manage.py               # Point d'entrée principal
├── requirements.txt        # Dépendances Python
├── static/                 # Fichiers statiques (CSS, JS, images)
├── templates/              # Fichiers HTML
└── app/                    # Fonctions utilitaires (génération/scan QR)
```

---

## 🎯 Utilisation

### Scanner un QR code
1. Clique sur **"📷 Scanner un QR Code"**.
2. Autorise l'accès à ta caméra.
3. Rentre ton pseudo ou un nom pour le QR code dans l'input.
4. Pointe ton appareil vers un QR code.
5. Quand le QR code aura été scanné, les données de ce dernier s'afficheront en dessous de la zone de scan.
6. Les QR codes sont supprimés toutes les 3 secondes (choix de conception).

### Voir les QR codes
1. Clique sur **"📋 Voir les QR Codes"**.
2. Tu verras les QR codes scannés en direct, du plus récent au plus ancien, avec la data et la date en dessous.

---

## 🔧 Configuration
- Modifie `settings.py` pour ajuster les paramètres (tailles, couleurs, fonctionnalités, etc.).
- Pour une utilisation en production, configure un serveur WSGI comme **Gunicorn** ou **uWSGI**.

---

## 🤝 Contribuer
Les contributions sont les bienvenues ! Pour participer (bien que je ne regarde pas souvent) :
1. Fork le projet.
2. Crée une branche (`git checkout -b feature/ma-fonctionnalite`).
3. Commit tes changements (`git commit -m "Ajout de X"`).
4. Push et ouvre une **Pull Request**.

---

## 📜 Licence
[MIT](LICENCE) – Libre d'utilisation, modification et distribution.

---

## ⚠️ Avertissements et Mentions Légales

### Avertissements
- Ce projet a été créé à l'aide de l'IA.
- Ce projet est **personnel** et n'a pas pour but d'avoir une qualité professionnelle.

### 📜 Conditions Générales d'Utilisation (CGU)

En utilisant QRshare, vous acceptez les conditions suivantes :

1. **Utilisation Responsable** :
   - QRshare est conçu pour le **partage de QR codes publics et en libre accès**.
   - Toute utilisation **illicite** (contenu frauduleux, illégal, ou contraire à l'éthique) est strictement interdite.
   - Nous nous désolidariserons totalement de toute donnée partagée à des fins illégales.

2. **Responsabilité** :
   - Nous ne sommes pas responsables des **contenus partagés** par les utilisateurs.
   - En cas de **poursuite judiciaire**, nous nous réservons le droit de fournir les informations enregistrées conformément à la **Loi pour la Confiance dans l’Économie Numérique (LCEN, 2004)**.

3. **Modifications** :
   - Nous nous réservons le droit de modifier ces CGU à tout moment. Les changements seront affichés ici.

---

### 🔒 Politique de Confidentialité

Conformément à la **Loi pour la Confiance dans l’Économie Numérique (LCEN, 2004)** et au **RGPD** :

1. **Données Collectées** :
   - **Adresse IP** : Conservée pendant **1 an** pour les QR codes publics (obligation légale, Article 6-I-7 de la LCEN).
   - **Données des QR codes** : La data brute, la date et l'IP sont conservées pendant **1 an**.
   - **Pseudos** : Si vous en utilisez un, il sera associé à vos QR codes.

2. **Utilisation des Données** :
   - Les données sont utilisées uniquement pour le fonctionnement du service et pour répondre aux obligations légales.
   - Nous ne partageons pas vos données avec des tiers, sauf en cas de **réquisition judiciaire**.

3. **Vos Droits** :
   - Vous pouvez demander l'accès, la modification ou la suppression de vos données en nous contactant à **estebanfourage29@gmail.com**.
   - Pour les données soumises à une obligation légale (comme les IP), la suppression ne sera effective qu'après le délai légal de conservation (1 an).

4. **Sécurité** :
   - Les données sont stockées de manière sécurisée, mais aucun système n'est infaillible. Nous mettons en place des mesures raisonnables pour protéger vos informations.

---

## 📬 Contact
Pour toute question ou suggestion :
- **GitHub** : [@bleeze54](https://github.com/bleeze54)
- **Email** : estebanfourage29@gmail.com
