title: SQL Datenbankprojekt
stage: beta
timevalue: 2
difficulty: 4
assumes: SQLBasic, SQLSelect, SQLJoin
---

[SECTION::goal::product]

Ich kann eine komplexe Datenbankstruktur aufbauen.

[ENDSECTION]

[SECTION::background::default]

Die Softwareentwickler sind auf Sie angewisen, denn eine persistent Speicherung wird für die geplante
Webanwendung benötigt. Hier können Sie zeigen, was Sie in dieser Taskgroup gelernt haben. Bauen Sie
eine Datenbankstruktur auf.

[ENDSECTION]

[SECTION::instructions::tricky]

### Aufbau der Datenbank

Der Datenbankarchitekt hat folgende Tabellen vorgesehen.

Erstellen Sie eine Tabelle mit dem Namen ...

- [EC] ... "students" mit den folgenden Spalten: id (INTEGER, Primärschlüssel), name (TEXT),
  age (INTEGER), major (TEXT).
- [EC] ... "courses" mit den folgenden Spalten: id (INTEGER, Primärschlüssel), name (TEXT),
  teacher (TEXT), credits (INTEGER).
- [EC] ... "enrollments" mit den folgenden Spalten: id (INTEGER, Primärschlüssel),
  student_id (INTEGER, Fremdschlüssel zu "students"), course_id (INTEGER, Fremdschlüssel zu "courses"),
  grade (INTEGER).
- [EC] ... "assignments" mit den folgenden Spalten: id (INTEGER, Primärschlüssel),
  course_id (INTEGER, Fremdschlüssel zu "courses"), name (TEXT), deadline (DATE).
- [EC] ... "grades" mit den folgenden Spalten: id (INTEGER, Primärschlüssel), student_id (INTEGER,
  Fremdschlüssel zu "students"), assignment_id (INTEGER, Fremdschlüssel zu "assignments"), grade (INTEGER).
- [EC] ... "professors" mit den folgenden Spalten: id (INTEGER, Primärschlüssel),
  name (TEXT), department (TEXT).
- [EC] ... "departments" mit den folgenden Spalten: id (INTEGER, Primärschlüssel), name (TEXT),
  location (TEXT).
- [EC] "exams" mit den folgenden Spalten: id (INTEGER, Primärschlüssel),
  course_id (INTEGER, Fremdschlüssel zu "courses"), date (DATE), location (TEXT).
- [EC] ... "attendances" mit den folgenden Spalten: id (INTEGER, Primärschlüssel),
  student_id (INTEGER, Fremdschlüssel zu "students"), exam_id (INTEGER, Fremdschlüssel zu "exams"),
  attendance_status (TEXT).
- [EC] ... "book_reviews" mit den folgenden Spalten: id (INTEGER, Primärschlüssel),
  student_id (INTEGER, Fremdschlüssel zu "students"), course_id (INTEGER, Fremdschlüssel zu "courses"),
  review_text (TEXT), rating (INTEGER).

### Abfragen vorbereiten

Jetzt benötigen die Entwickler Anfragen, die sie in ihren Funktionen verwenden können. Erstellen
Sie folgende Queries:


- [EC] Zeigen Sie alle Kurse an, die von einem bestimmten Professor unterrichtet werden.
- [EC] Zeigen Sie den Namen und das Alter aller Studenten an.
- [EC] Zählen Sie die Anzahl der Studenten in jedem Kurs.
- [EC] Zeigen Sie den Durchschnitt der Noten für alle Aufgaben in einem bestimmten Kurs an.
- [EC] Sortieren Sie die Studenten nach ihrem Alter in absteigender Reihenfolge.
- [EC] Filtern Sie alle Kurse, die mehr als 3 Credits haben.
- [EC] Zeigen Sie den Namen jedes Studenten und die Anzahl der Kurse an, die er belegt.
- [EC] Zeigen Sie den Namen jedes Professors und die Anzahl der Kurse an, die er unterrichtet.
- [EC] Gruppieren Sie die Studenten nach ihrem Hauptfach und zeige die Anzahl der Studenten in jedem
  Hauptfach an.
- [EC] Zeigen Sie den Namen jedes Studenten und die Durchschnittsnote aller seiner Bewertungen an.

### Testdaten einspielen

Nicht nur Entwickler, auch Tester (aber auch andere "Stakeholder") sind an Testdaten interessiert, ohne
die das System nicht einmal begutachtet werden kann. Erstellen Sie daher folgende Testdaten:

- [EC] Erstellen Sie 5 neue Kurse und fügen Sie gleichzeitig 10 neue Einschreibungen von Studenten in diese Kurse ein.
- [EC] Erstellen Sie 3 neue Abteilungen und fügen Sie gleichzeitig 5 neue Professoren in diese Abteilungen ein.
- [EC] Erstellen Sie 3 Prüfungen, die jeweils 5 Teilnehmer haben. (Teilnehmer sind diesem Kurz zugeordnet)

[WARNING]
Sollten Abhängigkeiten fehlen, so sind diese ebenfalls zu erstellen.
[ENDWARNING]

[ENDSECTION]

[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
