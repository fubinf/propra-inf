title: Performanceprobleme mit Python Profiling aufdecken
stage: draft
timevalue: 1
difficulty: 2
---

TODO_1_hüster:

- _Sehr_ schönes Anwendungsbeispiel!
- Leider braucht es entscheidendes Vorwissen, dass wir nicht voraussetzen können.
  Wir brauchen erst eine sqlite3-Aufgabe, die dann hier _assumed_ wäre.  
  (Der entscheidende Hinweis steht aktuell zwar in der Aufgabenstellung, aber wir dürfen die Leute
  nicht dazu erziehen, ohne Verständnis der Semantik solche Änderungen zu machen.)
- Ich habe die Arbeitsmenge des Programms so weit erhöht, dass man die Verbesserung
  auch deutlich fühlen kann, nicht nur ausrechnen.
  So hat die Aufgabe einen Wow!-Effekt, der eher in Erinnerung bleibt.
- Wir sollten den Leuten lieber beibringen, gezielt eine Routine des Programms zu profilieren,
  denn das ist weitaus flexibler als nur ein Aufruf des Gesamtprogramms.
  Ich habe die Anleitung entsprechend modifiziert.
- Der Einleitungstext war recht geschwätzig; bitte knapp halten (und das Diff anschauen).
- Der Anleitungsteil war für 'leicht' viel zu ungenau. Bitte auch hierzu das Diff anschauen.
- Auch bei der Musterlösung sollte man den Text eher knapp halten; auf ein schnell überschaubares
  Layout kommt es an.
- Ich war insgesamt etwas enttäuscht, wie wenig Ihre Aufgabe aus der tollen Aufgabenidee gemacht hat.

[SECTION::goal::experience]

Ich verstehe wie ich Profiler nutzen kann, um Performanceprobleme in meinem Python Code zu 
lokalisieren.

[ENDSECTION]

[SECTION::background::default]

Wenn ein Programm etwas größer wird, 
versteht man meist nur noch schlecht, welche Teile davon wie viel Laufzeit benötigen.

Glücklicherweise gibt dafür _Profiler_. 
Ein Profiler (genauer: Laufzeitprofiler; es gibt auch Speicherprofiler)
sagt uns, welche Teile unseres Codes wie viel Laufzeit gebraucht haben.

[ENDSECTION]

[SECTION::instructions::loose]

Python hat Profiler eingebaut und bietet ausführliche Dokumentation dazu an:
[HREF::https://docs.python.org/3/library/profile.html].

Z.B. kann man ein Pythonskript einfach mit dem Profiler aufrufen und sich 
die Ausgabe direkt in eine Datei schreiben lassen.
Das probieren wir nun aus.

Das nachfolgende Programm erstellt zuerst eine SQL-Datenbank, 
dann eine Tabelle in dieser Datenbank und 
schreibt dannn zur Laufzeit generierte Namen in diese Tabelle.

Das Programm hat nur wenige Sekunden Laufzeit, besitzt aber ein gewaltiges Optimierungspotential.

```python
import os
import sqlite3
import random

DBNAME = 'profile.db'


def create_table(dbfile: str):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS profile')
    c.execute('CREATE TABLE profile (name TEXT, age INTEGER)')
    conn.commit()
    conn.close()


def generate_first_names():
    return ['Alice', 'Bob', 'Carla', 'David', 'Eve', 'Ford', 'Gotthilf', 'Hermione', 'Ira', 
            'Jolande', 'Kermit', 'Lady']


def generate_last_names():
    return ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Prefect', 'Gaga', 'Lastname']


def generate_middle_initials():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']


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


def profile_this(dbfile: str):
    names = generate_full_names()

    for name in names:
        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        age = random.randint(18, 65)
        c.execute('INSERT INTO profile VALUES (?, ?)', (name, age))
        conn.commit()
        conn.close()


def main():
    create_table(DBNAME)
    profile_this(DBNAME)
    os.unlink(DBNAME)


if __name__ == '__main__':
    main()
```

[EC] Speichern Sie das obige Programm in eine Datei und machen Sie einen Commit.

[EC] Lassen Sie es einmal laufen und messen Sie die Laufzeit:
`time python-profiling.py`.

[ER] Verwenden Sie die obige Dokumentation, um das Programm minimal so zu ergänzen, 
dass es den `cProfile`-Profiler startet, um `main()` auszuführen.
Machen Sie einen Commit.

[EC] Lassen Sie es erneut laufen: `time python-profiling.py`.

[EQ] Profilierung ist nicht gratis. Um wie viel Prozent hat sich die Laufzeit erhöht?

[EQ] Studieren Sie mithilfe der Dokumentation die Profiling-Ausgabe.
Welche drei Programmzeilen (bitte deren Text angeben) verbrauchen den Bärenanteil der Laufzeit?

[ER] Diese Aufrufe müssten alle nicht in der Schleife stehen.
Passen Sie das Skript entsprechend an, um den Flaschenhals zu entfernen.

[EC] Lassen Sie das optimierte Skript erneut laufen: `time python-profiling.py`.

[EQ] Um welchen Faktor hat sich die Laufzeit reduziert? (Cool, oder?)

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Nutzung und Verständnis von Profilern]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
