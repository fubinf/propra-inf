title: Entwicklung eines eigenen Passwortgenerators
stage: draft
timevalue: 0
difficulty: 3
assumes: m_random, m_json1, m_argparse, encoding_and_open
---

TODO_1_ruhe:

- Haben Sie selber diese Aufgabe gelöst? Die Beschreibung klingt nicht so, sie ist
  an recht vielen Stellen vage.
- In dieser Form ist das für den Tutor eine Zumutung: Was sind denn die Kriterien für eine
  akzeptable Lösung? Und wie prüft man die zügig, wenn jeder was ganz verschiedenes baut?
- Ich glaube, wir brauchen eine Spezifikation mit viel weniger Freiheitsgraden bei den
  Anforderungen.
- Und es wäre schön, wenn das Ergebnis praktikabel wäre. Die Regeln für muss-enthalten und
  darf-nicht-enthalten sind aber bei verschiedenen Websites sehr unterschiedlich.
  Ich finde, das Programm sollte die wichtigsten Sorten davon als Auswahltyp abbilden.
- Und eine zufällige Länge scheint mir eine sehr seltsame Idee. Damit will niemand arbeiten.
- Statt `secure` gibt es in der stdlib `secrets`.
- Ein Verweis auf `encoding_and_open` ist auf dem Niveau dieser Aufgabe nicht mehr sinnvoll;
  das ist mit dem assumes erledigt.
- INSTRUCTOR-Teil fehlt.

[SECTION::goal::product]

Ich kann ein Python Programm erstellen, dass mir sichere und zufällige Passwörter ausgibt.

[ENDSECTION]

[SECTION::background::default]

Passwörter sind die Methode, die sich bezüglich Bequemlichkeit und Sicherheit durchgesetzt haben,
um Daten vor unbefugten zu sichern. Leider benötigen häufen sich diese Informationen, die geschützt
werden wollen, weshalb wir immer mehr Passwörter benötigen. Daher möchten wir unsere frisch
erworbenen Programmierfähigkeiten dazu einsetzen, unseren Alltag etwas zu erleichtern und uns gute
Passwörter ausgeben lassen. Nie wieder langweilige und unsichere Passwörter - wir wollen selbst die
Kontrolle über unsere Sicherheit übernehmen!

[ENDSECTION]

[SECTION::instructions::loose]

Im folgenden sollen Sie ein Programm schreiben, dass Ihnen ein Passwort zurück gibt. Dieses Passwort
sollen Sie lokal abspeichern, jederzeit wieder abrufen und bearbeiten können.
Verwenden Sie für die Lösung dieser Entwicklung lediglich die von Python zur Verfügung gestellten
Standardbibliotheken. Sie können zusätzlich die im ProPra kennengelernten Methoden und erweiterten
Pakete verwenden. Sie haben ebenfalls die Möglichkeit von erwähnten Empfehlungen abzuweichen, wenn
andere Lösungen Ihnen gelegener kommen.

### Entwicklung

- [ER] Erstellen Sie einen Passwortgenerator, der folgende Kriterien berücksichtigt:

#### Sicherheit 

- Stellen Sie sicher, dass die generierten Passwörter sicher sind (Passwortrichtlinien)
  - Zeichenklänge zwischen 8 und 20 (zufällig)
  - Mind. 1 Großbuchstabe
  - Mind. 1 Kleinbuchstabe
  - Mind. 1 Zahl
  - Mind. 1 Sonderzeichen aus `.:?!@#$&*`

#### Abrufbarkeit

- Speichern Sie generierte Passwörter (vorerst) unverschlüsselt und lokal in einer
  [PARTREFMANUAL::m_json1::JSON]-Datei.
  - Für die Arbeit mit einer Datei bietet sich die Built-In Funktion
    [PARTREFMANUAL::encoding_and_open::open] an.
- Überlegen Sie sich sich Referenzierung, um das Passwort jederzeit zuordnen zu können.
- Das Passwort soll nur mit einem **Masterpasswort** abrufbar sein, dass Sie (vorerst) fest in den Code
  codieren.

### Bearbeitbar

- ein Abrufbares Passwort soll bearbeitbar sein.

#### Zufälligkeit

- Der Passwortgenerator sollte in der Lage sein, zufällige Passwörter zu generieren, um die Sicherheit
  zu gewährleisten. Die Verwendung von Python's [PARTREFMANUAL::m_random::random]-Modul kann dabei
  hilfreich sein.

[NOTICE]
Zur Generierung von Passwörtern ist `random` in der Praxis keine gute Wahl, da es nicht als sicher
gilt. Eine ALternative zu random ist das Python Modul `secure`. Das Modul ist nicht Bestandteil
des ProPra, kann aber gerne in Eigenrecherche verwendet werden. Hier ein erster Einstieg:
[HREF::https://secure.readthedocs.io/en/latest/]
[ENDNOTICE]

#### Benutzerfreundlichkeit

- Der Passwortgenerator sollte einfach zu bedienen sein und dem Benutzer die Möglichkeit bieten,
  die gewünschte Länge und Komplexität des Passworts anzupassen.
  - Verwenden Sie (optionale) Parameter beim Aufruf des Programms, die:
    - die Mindestlänge vorgibt (default beachten)
    - die Maximale Länge vorgibt (default beachten)
    - eine Referenzierung vorgibt (default aus Ihrer Überlegung)
    - eine Option wäre das Modul [PARTREFMANUAL::m_argparse::argparse]
- Die Bedienung soll trotz der benutzerfreundlichen Entwicklung über die Konsole durchgeführt werden.

#### Wiederverwendbarkeit

- Der Code sollte modular und wiederverwendbar sein, um ihn bei Bedarf in anderen Projekten verwenden
  und leichter erweitern zu können.
- Achten Sie ebenfalls auf ein strukturiertes Datenverzeichnis.

#### Dokumentation

- Dokumentieren Sie den Code, um anderen Entwicklern zu ermöglichen, den Code zu
verstehen und bei Bedarf zu erweitern oder anzupassen.
- Erstellen Sie ein einfaches [PARTREF::changelog]
- Dokumentieren Sie ebenfalls die Anwendung des Passwortgenerators.

### Allgemeiner Ausschluss

- Erstellen Sie keine Tests: dies ist Teil einer anderen Aufgabe.
- Entwickeln Sie keine GUI.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
