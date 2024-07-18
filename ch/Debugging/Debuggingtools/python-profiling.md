title: Performanceprobleme mit Python Profiling aufdecken
stage: draft
timevalue: 1
difficulty: 2
---

[SECTION::goal::experience]

Ich verstehe wie ich Profiler nutzen kann, um Performanceprobleme in meinem Python Code zu 
entdecken.

[ENDSECTION]

[SECTION::background::default]

Wenn man längere Zeit an einem Projekt arbeitet, kann es vorkommen, dass das Projekt irgendwann 
so groß bzw. unübersichtlich wird, dass man bei Performanceproblemen nicht mehr ohne weiteres 
durch das Durchschauen des Codes die Ursache finden kann.

Glücklicherweise gibt es Werkzeuge, welche uns bei dieser Arbeit unterstützen können. Eines davon 
ist ein sogenannter Profiler. Dieser erlaubt uns, die Laufzeiten unseres Codes während der 
Ausführung aufzuzeichnen und gibt uns danach Aufschluss darüber, welche Teile des Codes am 
meisten Zeit bzw. Performance kosten.

[ENDSECTION]

[SECTION::instructions::loose]

Python selbst bietet eine sehr ausführliche Dokumentation über die Hauseigenen Profiler an.
Diese finden sie hier: https://docs.python.org/3/library/profile.html

Dort wird beschrieben was ein Profiler ist, wofür er genutzt wird und vor allem *wie* er genutzt 
wird. U.a. kann man ein Python skript einfach mit dem Profiler als Argument aufrufen und sich 
die Ausgabe direkt in eine Datei schreiben lassen.

Jetzt wollen wir aber selbst auch mal einen Profiler über ein Python-Skript laufen lassen.
Dazu haben wir hier ein kleines Beispielprogramm vorbereitet. 
Dieses Programm erstellt zuerst eine Datenbank und eine Tabelle in dieser Datenbank und 
schreibt danach zur Laufzeit generierte Namen in die zuvor erstellte Tabelle.

Wenn Sie das Programm ausführen, werden Sie natürlich merken, dass es sich hier trotz alledem nur 
um wenige Sekunden Laufzeit handelt. Allerdings ist hier trotzdem noch einiges an 
Optimierungspotential vorhanden.

```python
import sqlite3
import random

def create_table():
    conn = sqlite3.connect('profile.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS profile')
    c.execute('CREATE TABLE profile (name TEXT, age INTEGER)')
    conn.commit()
    conn.close()

def generate_first_names():
    return ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

def generate_last_names():
    return ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown']

def generate_middle_initials():
    return ['A', 'B', 'C', 'D', 'E']

def generate_full_names():
    first_names = generate_first_names()
    last_names = generate_last_names()
    middle_initials = generate_middle_initials()
    names = []
    for first_name in first_names:
        for last_name in last_names:
            for middle_initial in middle_initials:
                name = first_name + ' ' + middle_initial + '. ' + last_name
                names.append(name)
    return names
    

def profile_this():
    names = generate_full_names()

    for name in names:
        conn = sqlite3.connect('profile.db')
        c = conn.cursor()
        age = random.randint(18, 65)
        c.execute('INSERT INTO profile VALUES (?, ?)', (name, age))
        conn.commit()
        conn.close()


def main():
    create_table()
    profile_this()


if __name__ == '__main__':
    main()
```

[EQ] Erklären Sie kurz was ein Profiler ist und wozu er eingesetzt wird.
[ER] Verwenden Sie einen geeigneten Python Profiler um den Flaschenhals im Skript zu entfernen.
[ER] Passen Sie das Skript entsprechend an um den Flaschenhals zu entfernen.
[EC] Geben Sie jeweils die Ausgabe des Profilers, vor und nach ihren Anpassungen am Skript, ab.

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Nutzung und Verständnis von Profilern]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
