import json
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent

def load_template(template_name):
    return (ROOT_DIR / 'templates' / template_name).read_text(encoding='utf-8')


def generate_student_card(student):
    return f"""
        <div class="student-card">
            <div class="student-emoji">{student['emoji']}</div>
            <div class="student-info">
                <h3>{student['prenom']} {student['nom']}</h3>
                <p class="student-promo">Promo {student['promo']}</p>
                <p class="student-matiere">Matière préférée : {student['matiere_preferee']}</p>
                <a href="{student['github_page']}" target="_blank" class="student-link">
                    Voir le site →
                </a>
            </div>
        </div>
        """


def generate_html():
    students = json.loads((ROOT_DIR / 'students.json').read_text(encoding='utf-8'))
    students_sorted = sorted(students, key=lambda s: (s['nom'], s['prenom']))

    students_html = ''.join(generate_student_card(s) for s in students_sorted)

    template = load_template('index.html')
    html_content = template.replace('{{ students_cards }}', students_html)
    html_content = html_content.replace('{{ student_count }}', str(len(students)))
    html_content = html_content.replace('{{ student_plural }}', 's' if len(students) > 1 else '')

    (ROOT_DIR / 'index.html').write_text(html_content, encoding='utf-8')
    (ROOT_DIR / 'style.css').write_text(
        (ROOT_DIR / 'templates' / 'static' / 'style.css').read_text(encoding='utf-8'),
        encoding='utf-8'
    )

    print(f"✅ HTML généré avec succès ({len(students)} étudiants)")


if __name__ == '__main__':
    generate_html()