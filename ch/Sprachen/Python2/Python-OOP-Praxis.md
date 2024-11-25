title: "Grundlagen von objektorientierter Programmierung in Python: Eine praktische Übung"
stage: alpha
timevalue: 3
difficulty: 3
requires: Python-OOP-Intro, Python-OOP-Methods, Python-OOP-Inheritance
---

[SECTION::goal::product]

- Ich kann eine komplexe Struktur von Entitäten mithilfe von objektorientiertem Ansatz erstellen und
Relationen dazwischen modellieren.

[ENDSECTION]

[SECTION::instructions::tricky]

In dieser Aufgabe simulieren wir teilweise das Programmierpraktikum "ProPra". 
Sie werden die Hauptakteure und die Interaktionen dazwischen durch Klassen modellieren.

Legen Sie dabei Ihren Fokus nicht auf die Qualität des Endprodukts, 
sondern darauf, 
wie Sie die Kommunikation und Interaktion zwischen den Klassen und deren Instanzen modellieren können.

Die Logik der Feinheiten ist hierbei zweitrangig.
Machen Sie Ihr Bestes und genießen Sie dabei das neue Wissen die Reise.
Sie dürfen alle sinnvollen Anpassungen selbst machen -- 
ein kurzer erklärender Kommentar wäre allerdings hilfreich.

Versuchen Sie so gut wie möglich, die folgenden Klassen zu implementieren:

[ER] Die Klasse `ProPra`: Davon erstellen wir Instanzen des Programmierpraktikums.

Sie hat folgende Instanzattribute:

- `project_manager`: Jedes Programmierpraktikum-Projekt soll einen Verwalter haben
- `roles`: Wir betrachten folgende Teilnehmerrollen:
    - `author`: Autor, der die Aufgaben verfasst
    - `instructor`: Tutor, der die Studierenden leitet und die Aufgaben korrigiert
    - `reviewer`: Prüft die Aufgaben, die die Autoren schreiben
    - `student`: Bearbeitet die Aufgaben
Dazu noch folgende Instanzattribute, die Sie bspw. als Listen darstellen können:
- `authors`: Alle Autoren
- `instructors`: Alle Tutoren
- `reviewers`: Alle Prüfer
- `students`: Alle Studierenden, die am Projekt teilnehmen
- `chapters`: Alle Aufgabengruppen bzw. Kapitel
- `tasks`: Alle Aufgaben im Projekt

Instanzmethoden:

- `add_member(self, new_member_instance)`: aktualisiert die entsprechende Teilnehmerliste, 
damit wir ständig im Blick haben können, welche Teilnehmer im gesamten Projekt sind.

---

[ER] Die Klasse `ProPraUser`:

Ober- bzw. Basisklasse und hat folgende Instanzattribute:

- `first_name`: Vorname
- `last_name`: Nachname
- `email`: E-Mail-Adresse
- `role`: `'author'`, `'instructor'`, `'reviewer'` oder `'student'`

Hierfür brauchen wir keine Methoden.

---

[ER] Die Klasse `ProPraManager`: Er ist der einzige Verwalter in jeder `ProPra`-Instanz.

Er fügt neue Teilnehmer zu seinem `ProPra`-Projekt hinzu, 
pupliziert geprüfte Aufgaben mit Stage `beta` und löscht Aufgaben, 
die bspw. nicht mehr gültig sind oder Aktualisierung benötigen.

Instanzattribute:

- `first_name`
- `last_name`
- `tasks_to_publish`: Liste geprüfter Aufgaben mit Stage `beta`, dient als Todo-Queue, 
aus der der Manager die Aufgaben nimmt und veröffentlicht, damit die Studierenden daran arbeiten.

Instanzmethoden:

- `add_member(self, propra_instance, new_member_instance)`: 
ruft über `propra_instance` die Methode `add_member` der Klasse `ProPra` auf, 
um die entsprechende Teilnehmerliste aktualisieren zu lassen. 
- `publish_task(self, propra_instance, task_instance)`:
Falls die übergebene Aufgabe `task_instance` in der Warteliste der zu veröffentlichenden Aufgaben
`tasks_to_publish` existiert, wird die Aufgabenliste `tasks` der `ProPra`-Instanz dadurch aktualisiert,
indem die neue Aufgabe `task_instance` hinzugefügt wird --
am Ende ist diese Aufgabenliste die Quelle, aus der die Studierenden Aufgaben zur Bearbeitung nehmen.  
Dazu wird auch die Liste der Aufgabengruppen `chapters` der `ProPra`-Instanz, 
auch über `propra_instance`, aktualisiert. Jede Aufgabe gehört nämlich zu einer Aufgabengruppe. 
Hierbei ist zu beachten, dass die zugehörige Aufgabengruppe bei der Aufgabeninstanz gespeichert wird,
das sehen Sie in der Klasse `ProPraTask`. 
Das heißt, dass dabei eine Aufgabengruppe nicht doppelt gespeichert werden soll.
- `remove_task(self, propra_instance, task_instance)`:
Entfernt über `propra_instance` die übergebene Aufgabe aus der Aufgabenliste `tasks` der `ProPra`-Instanz.

---

[ER] Die Klasse `ProPraAuthor`: Unterklasse der Klasse `ProPraUser`.

Die persönlichen Daten bekommt ein `ProPraAuthor` von der Oberklasse mithilfe von `super()`,
seine Rolle als `author` übergeben wir gleich auch in diesem Schritt an `super()`.

Zusätzliche Instanzattribute:

- `rejected_tasks`: Eine Liste der vom Prüfer abgelehnten Aufgaben. 
Ein Prüfer prüft den verfassten Inhalt und kann die Aufgabe ablehnen bzw. an den Autor zur
Ausarbeitung zurückschicken. 
Die Aufgaben in dieser Liste korrigiert der Autor gemäß dem Feedback des Prüfers und 
leitet sie anschließend erneut an denselben Prüfer weiter.
- `accepted_tasks`: Eine Liste der vom Prüfer akzeptierten Aufgaben. 
Diese Aufgaben werden dann mit Stage `beta` vom Prüfer an den Manager zur Veröffentlichung weitergeleitet, 
indem sie später in der Liste `tasks_to_publish` beim Manager gespeichert werden.

Methoden:

- `submit_task(self, reviewer_instance, task_instance)`: Markiert erstmal eine geschriebene
Aufgabe, die übrigens anfangs immer Stage `draft` hat, mit Stage `alpha` bzw. "bereit zur Prüfung". 
Sie speichert danach bei der Aufgabeninstanz den Prüfer `reviewer_instance`,
damit wir immer wissen, bei welchem Prüfer sich die Aufgabe befindet, 
da das Projekt mehrere Prüfer haben könnte.  
Damit außerdem ein Author einem Prüfer sagt, dass eine Aufgabe geprüft werden kann, 
speichern wir in dieser Methode auch die zu prüfende Aufgabe `task_instance` in die Liste 
der zu prüfenden Aufgaben `tasks_to_review`, die ein Prüfer der Klasse `ProPraReviewer` hat.
- `update_task(self, rejected_task_instance, **kwargs)`: 
In einer abgelehnten Aufgabe sollte meistens kleinen Teil korrigiert bzw. optimiert werden, 
vielleicht hat nur der Title der Aufgabe dem Prüfer nicht gefallen.
Daher lässt diese Methode mithilfe vom übergebenen Schlüsselwort-Argument `**kwargs`
(s.b. [PARTREF::Python-Function-Arguments-Advanced]) beliebige Änderungen der Attribute der 
abgelehnten Aufgabe `rejected_task_instance` zu. 
Gültige Attribute werden also entsprechend bei der Aufgabe aktualisiert.  
Abschließend schickt der Author die Aufgabe mit der gemachten Korrektor zurück an denselben Prüfer,
indem er die Aufgabe wieder in die Prüfersliste der zu prüfenden Aufgaben `tasks_to_review` speichert
und aus der eignen Liste der abgelehnten Aufgaben `rejected_tasks` entfernt.
Machen Sie dabei von der vorherigen Methode `submit_task` Gebrauch.

---

[ER] Die Klasse `ProPraReviewer`: Unterklasse der Klasse `ProPraUser`.

Die persönlichen Daten bekommt ein `ProPraReviewer` ebenso von der Oberklasse `ProPraUser`,
seine Rolle als `reviewer` übergeben wir an `super()` auch in diesem Schritt.

Seine zusätzlichen Instanzattribute sind `tasks_to_review` und `reviewed_tasks`.
Den Nutzen von `tasks_to_review` haben wir bereits klargemacht. 
`reviewed_tasks` hilft einem Prüfer dabei, zu wissen, was bzw. wie viel er im Projekt geleistet hat.

Methoden:

- `accept_task(self, propra_instance, task_instance)`:
Zuerst aktualisieren wir hier den Stage der Aufgabe von `alpha` zu `beta`. 
Danach speichern wir die akzeptierte Aufgabe beim Autor in seiner Liste `accepted_tasks`,
damit er auch im Blick behält, welche Aufgaben von ihm weitergelassen wurden.  
Anschließend sagen wir dem Manager des Projekts mithilfe von `propra_instance.project_manager`, 
dass diese akzeptierte Aufgabe veröffentlicht werden kann, 
indem wir die Aufgabe in seiner Liste `tasks_to_publish` speichern.  
Am Ende aktualisieren wir als Reviewer unsere eigene Liste der geprüften Aufgaben `reviewed_tasks`
und speichern die akzeptierte Aufgabe darin.
- `reject_task(self, task_instance)`: Die Aufgabe, die wir vom Autor mit Stage `alpha` bekamen,
aber nicht passend fanden, markieren wir zuerst wieder als `draft` und schicken sie mithilfe
von `task_instance.author` wieder an denselben Autor zurück, 
indem wir sie in seiner Liste der abgelehnten Aufgaben `rejected_tasks` speichern.  
Abschließend aktualisieren wir auch die eigene Liste der geprüften Aufgaben `reviewed_tasks`.

---

[ER] Die Klasse `ProPraStudent`: Unterklasse der Klasse `ProPraUser`.

Die persönlichen Daten bekommt ein `ProPraStudent` von der Oberklasse `ProPraUser`,
seine Rolle als `student` übergeben wir gleich an `super()` auch in diesem Schritt.

Ein Klassenattribut für alle teilnehmenden Studierenden ist `required_time_value_to_pass`, 
mit dem Wert 150.  
Dadurch ist der minimale Stundenaufwand von Aufgaben zum Bestehen des Projekts repräsentiert --
jede Aufgabe `ProPraTask` hat ja ein `time_value` Attribut, welches den Bearbeitungsaufwand in Stunden darstellt.

Seine zusätzlichen Instanzattribute sind:

- `total_time_value_of_finished_tasks`: anfangs 0, 
wird um den Wert von `time_value` einer vom Tutor bzw. 
`ProPraInstructor` akzeptierten Aufgabe inkrementiert.
- `instructor`: Aufgabenlösungen von Studenten prüft der zuständige Tutor. 
Dieses Attribut können Sie gleich dem Konstruktor als `instructor_instance` übergeben.
- `rejected_solutions`: Liste aller vom zuständigen Tutor abgelehnten Lösungen.

Methoden:

- `submit_solution(self, propra_instance, solution_instance)`:
Zuerst schauen wir nach, ob die abzugebende Lösung bereits abgelehnt war.
Falls ja, dann löschen wir diese Lösung aus `rejected_solutions` erst, 
bevor wir sie an unseren Tutor zur Korrektor weiterleiten, 
indem wir seine Liste `solutions_to_check` um diese Lösung erweitern. 

---

[ER] Die Klasse `ProPraInstructor`: Unterklasse von `ProPraUser`.

Die persönlichen Daten bekommt ein `ProPraInstructor` von `ProPraUser`,
seine Rolle als `instructor` übergeben wir gleich an `super()` auch in diesem Schritt.

Ein `ProPraInstructor` hat ein zusätzliches Instanzattribut, 
und zwar die bereits besprochene Liste der zu korrigierenden Aufgabenlösungen `solutions_to_check`,
die anfangs logischerweise leer ist.

Methoden:

- `accept_solution(self, solution_instance)`:
Wenn wir als Tutor eine Lösung akzeptieren, müssen wir nur dem Studenten den entsprechenden
Zeitaufwand `time_value` der zugehörigen Aufgabe gutschreiben, 
indem wir sein `total_time_value_of_finished_tasks` aktualisieren.
Dieses erriechen wir über `solution_instance.student.total_time_value_of_finished_tasks`, da
wir, wie Sie in der Klasse `ProPraTaskSolution` sehen, jede Lösung einem bestimmten Studenten
zuweisen.
- `reject_solution(self, solution_instance)`: 
Hier kommt die Studentenliste der abgelehnten Aufgabenlösungen `rejected_solutions` zum Einsatz.
Wir aktualisieren ganz einfach diese List und addieren die Lösung `solution_instance` darin, 
damit der Student später diese Lösung erneut bearbeitet und mit seiner Methode `submit_solution`
    an uns als Tutor zur erneuten Korrektor zurückgibt. 

---

[ER] Die Klasse `ProPraTask`: Repräsentiert die Aufgaben.

Instanzattribute: 

- `chapter_instance`: 
Nutzen wir, um eine Aufgabe einer entsprechenden Aufgabengruppe der Klasse `ProPraChapter` zuzuweisen.
Die Liste `tasks` einer solchen `ProPraChapter`-Instanz aktualisieren wir im Konstruktor auch.
- `title`
- `time_value`: Bearbeitungsaufwand in Stunden, einfach als natürliche Zahl
- `difficulty`: Schwierigkeitsgrad einer Aufgabe. Aufsteigend als 1, 2, 3 oder 4 
- `stage`: Anfangs hat den Wert `draft`
    - `draft`: Aufgabe in Bearbeitung beim Autor
    - `alpha`: Aufgabe im Review beim Prüfer
    - `beta`: Aufgabe bereit zur Veröffentlichung vom Manager bzw. Bearbeitung von Studenten
- `content`: Der Inhalt der Aufgabe. 
Dieser kann eine Referenz zu einer Datei beinhalten, bspw. zu einer `.md`-Datei. 
Der Einfachheit halber allerdings kann dieses Attribut einen einfachen Text-String beinhalten.
- `author`: Jede Aufgabe wird von einem einzigen Autor geschrieben.
- `reviewer`: Jede Aufgabe wird von einem einzigen Prüfer geprüft. 
Anfangs hat eine Aufgabe gar keinen Prüfer. 
Diesen setzen wir erst, wenn der Autor die Aufgabe an einen bestimmten Prüfer zum Review schickt,
indem er dafür seine Methode `submit_task` nutzt.

Hierfür brauchen wir keine Methoden.

---

[ER] Die Klasse `ProPraTaskSolution`: Repräsentiert die Lösung einer Aufgabe.

Instanzattribute:

- `student`: Jede Lösung wird von einem einzigen Student geschrieben.
- `task`: Jede Lösung gehört einer einzigen Aufgabe.
- `commit_id`: Wir nehmen an, dass der Student die Lösungen auf Github hochlädt.

Hierfür brauchen wir keine Methoden.

---

[ER] Die Klasse `ProPraChapter`: Repräsentiert eine Gruppe bzw. ein Kapitel von Aufgaben aus einem Themenbereich.

Instanzattribute:

- `tasks`: Liste alle zugehörenden Aufgaben

Hierfür brauchen wir keine Methoden.

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösung]
Anpassungen jederart sind auch akzeptabel, sofern die Struktur, 
die Syntax und die Funktionalität sinnvoll sind.

[INCLUDE::ALT:]
[ENDINSTRUCTOR]