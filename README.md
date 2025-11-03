# Portfolio TNAH

> ### [Annuaire collaboratif](https://segolene-albouy.github.io/Portfolio-TNAH/) des promotions du Master Technologies numériques appliquées à l'histoire de l'École des chartes.

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
        "matiere_preferee": "Git",
        "emoji": "🐱"
      }
    ```
4. Valider vos modifications avec un message de commit clair
5. Pousser vos modifications sur GitHub
6. Retournez sur la page de votre fork
7. Cliquez sur **Contribute** > **Open pull request**
8. Soumettez une _Pull Request_ avec un contenu détaillé

### Code review entre camarades

En binôme, validez mutuellement vos _Pull Requests_ avant de les merger :
1. Allez sur l'onglet "_Pull Requests_"
2. Ouvrez la PR à reviewer
3. Cliquez sur "_Files changed_"
4. Vérifiez :
   - [ ] Le JSON est bien formaté (virgules, accolades)
   - [ ] Tous les champs sont présents
   - [ ] L'URL du site GitHub Pages est correcte
   - [ ] Pas de doublons
5. Laissez un commentaire
6. Approuvez ou demandez des changements
7. Si approuvée, venir me voir pour merger la PR

### Magie 🪄

GitHub Actions va automatiquement :
1. **Valider** le format du JSON
2. **Générer** une page HTML à partir des données
3. **Déployer** automatiquement sur GitHub Pages

Votre profil apparaîtra sur le portfolio dans ~2 minutes !

Ce workflow automatique, définit dans `.github/workflows/build.yml`, s'exécute à chaque push sur `main`.
Si la validation échoue, la PR ne peut pas être mergée.

## 🧪 Tester localement

Si vous voulez tester avant de push :

```bash
# Valider le JSON
python scripts/validate_json.py

# Générer le HTML
python scripts/generate_html.py

# Ouvrir index.html dans votre navigateur
```
