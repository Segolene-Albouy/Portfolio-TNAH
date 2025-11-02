# Portfolio TNAH

[Annuaire collaboratif](https://portfolio-promo-2025.github.io) des sites personnels des promotions TNAH.

## Contribuer au portfolio

### Créer une _Pull Request_ à partir d'un _fork_
1. Créer un **_fork_** de ce _repository_
2. Cloner le _fork_ en local
3. Modifier le fichier `students.json` pour ajouter vos informations à la fin de la liste
    ```json
      {
        "prenom": "Votre Prénom",
        "nom": "Votre Nom",
        "promo": 2025,
        "github_page": "https://votre-username.github.io",
        "matiere_preferee": "Python",
        "emoji": "🚀"
      }
    ```
4. Valider vos modifications avec un message de commit clair
5. Pousser vos modifications sur GitHub
6. Retournez sur la page de votre fork
7. Cliquez sur **Contribute** > **Open pull request**
8. Soummettez une _Pull Request_ avec un contenu détaillé

### Code review entre camarades

En binôme, validez mutuellement vos Pull Requests avant de les merger :
- Vérifier que votre JSON est valide
- Ajouter un commentaire dans la PR
- La merger dans le _repository_ principal

### Étape 6 : Magie ✨

GitHub Actions va automatiquement :
1. Valider votre JSON
2. Générer la nouvelle page HTML
3. Déployer le site mis à jour

Votre profil apparaîtra sur le portfolio dans ~2 minutes !

## 🔍 Comment faire une code review ?

Quand vous devez reviewer la PR d'un camarade :

1. **Allez sur l'onglet "Pull Requests"**
2. **Ouvrez la PR à reviewer**
3. **Cliquez sur "Files changed"**
4. **Vérifiez** :
   - [ ] Le JSON est bien formaté (virgules, accolades)
   - [ ] Tous les champs sont présents
   - [ ] L'URL du site GitHub Pages est correcte
   - [ ] Pas de doublons
5. **Laissez un commentaire** :
   - Si tout est bon : "LGTM ! ✅" (Looks Good To Me)
   - Sinon : expliquez ce qui doit être corrigé
6. **Approuvez ou demandez des changements**
7. **Si approuvé : Merge la PR**

## 🛠️ Structure du projet

```
portfolio-promo/
├── students.json           # Fichier à modifier pour s'ajouter
├── generate_html.py        # Script qui génère le HTML
├── validate_json.py        # Script qui valide le JSON
├── .github/
│   └── workflows/
│       └── build.yml       # GitHub Action automatique
└── README.md               # Ce fichier
```

## 🤖 GitHub Actions

Le workflow automatique `.github/workflows/build.yml` s'exécute à chaque push sur `main` et :

1. **Valide** le format du JSON
2. **Génère** la page HTML à partir des données
3. **Déploie** automatiquement sur GitHub Pages

Si la validation échoue, la PR ne peut pas être mergée.

## 📊 Format du JSON

Chaque étudiant doit avoir ces champs :

| Champ | Type | Exemple | Requis |
|-------|------|---------|--------|
| `prenom` | string | "Alice" | ✅ |
| `nom` | string | "Dupont" | ✅ |
| `promo` | number | 2025 | ✅ |
| `github_page` | string | "https://alice.github.io" | ✅ |
| `matiere_preferee` | string | "Python" | ✅ |
| `emoji` | string | "🐍" | ✅ |

## 🧪 Tester localement

Si vous voulez tester avant de push :

```bash
# Valider le JSON
python validate_json.py

# Générer le HTML
python generate_html.py

# Ouvrir index.html dans votre navigateur
```

## ❓ FAQ

**Mon JSON est refusé, pourquoi ?**
- Vérifiez les virgules entre les éléments
- Vérifiez que tous les champs sont présents
- Vérifiez que l'URL commence par `https://`

**Je me suis trompé dans ma PR, que faire ?**
- Vous pouvez modifier les fichiers dans votre fork
- Les changements seront automatiquement ajoutés à votre PR

**Combien de temps avant que mon profil apparaisse ?**
- GitHub Actions prend ~2 minutes pour valider, générer et déployer

**Je n'ai pas encore de site GitHub Pages**
- Créez d'abord votre site personnel avec le template fourni
- Publiez-le sur GitHub Pages
- Puis ajoutez-vous au portfolio

## 💡 Conseils

- Faites des commits clairs : `[add] Prénom Nom`
- Testez votre JSON localement avant de push
- Soyez bienveillants dans vos code reviews
- N'hésitez pas à demander de l'aide

## 🎉 Bon courage !

Vous apprenez les vraies pratiques de collaboration en équipe utilisées dans l'industrie : fork, pull request, code review, et CI/CD automatisé !

---

*Généré automatiquement • Promo 2025*