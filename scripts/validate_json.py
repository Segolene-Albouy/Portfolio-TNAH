import json
import sys
from urllib.parse import urlparse


def validate_students_json():
    errors = []

    try:
        with open('students.json', 'r', encoding='utf-8') as f:
            students = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de format JSON : {e}")
        return False
    except FileNotFoundError:
        print("❌ Fichier students.json introuvable")
        return False

    if not isinstance(students, list):
        print("❌ Le fichier JSON doit contenir une liste d'étudiants")
        return False

    if len(students) == 0:
        print("❌ La liste d'étudiants est vide")
        return False

    required_fields = ['prenom', 'nom', 'promo', 'github_page', 'matiere_preferee', 'emoji']

    for i, student in enumerate(students):
        if not isinstance(student, dict):
            errors.append(f"Étudiant #{i + 1} : doit être un objet")
            continue

        for field in required_fields:
            if field not in student:
                errors.append(f"Étudiant #{i + 1} : champ '{field}' manquant")

        if 'prenom' in student and not student['prenom'].strip():
            errors.append(f"Étudiant #{i + 1} : le prénom ne peut pas être vide")

        if 'nom' in student and not student['nom'].strip():
            errors.append(f"Étudiant #{i + 1} : le nom ne peut pas être vide")

        if 'promo' in student:
            if not isinstance(student['promo'], int):
                errors.append(f"Étudiant #{i + 1} : la promo doit être un nombre")
            elif student['promo'] < 2010:
                errors.append(f"Étudiant #{i + 1} : année de promo invalide ({student['promo']})")

        if 'github_page' in student:
            url = student['github_page']
            if not url.startswith('https://') and not url.startswith('http://'):
                errors.append(f"Étudiant #{i + 1} : l'URL doit commencer par https:// ou http://")
            parsed = urlparse(url)
            if not parsed.netloc:
                errors.append(f"Étudiant #{i + 1} : URL invalide ({url})")

    first_last_names = set()
    for i, student in enumerate(students):
        if 'prenom' in student and 'nom' in student:
            student_name = (student['prenom'].lower(), student['nom'].lower())
            if student_name in first_last_names:
                errors.append(f"Étudiant #{i + 1} : doublon détecté ({student['prenom']} {student['nom']})")
            first_last_names.add(student_name)

    if errors:
        print("❌ Erreurs de validation :\n")
        for error in errors:
            print(f"  • {error}")
        return False

    print(f"✅ Validation réussie : {len(students)} étudiant(s) valide(s)")
    return True


if __name__ == '__main__':
    if not validate_students_json():
        sys.exit(1)