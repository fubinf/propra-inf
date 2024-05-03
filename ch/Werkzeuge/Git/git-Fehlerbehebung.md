title: Fehler beheben im git Repository
stage: alpha
timevalue: 2.0
difficulty: 1
assumes: git-Funktionsweise
requires: git-Zweitrepo
---
TODO_1_hüster:

- Das ist eine Aufgabe für ein Kommandoprotokoll!
  Einfacher für alle Beteiligten.
  Ein paar zusätzliche Fragen in Markdown gehen trotzdem, wenn an die braucht.
- F4: "Beschreiben Sie, wie Sie mit git restore eine Datei aus einem ungepushten Commit entfernen können."
  Gar nicht. Da haben Sie was falsch verstanden oder falsch formuliert.
- Das ist nie im Leben difficulty 1, machen Sie 2 draus.
- F5: "Beschreiben Sie, wie Sie mit git restore den Zustand einer Datei zurück 
  auf den letzten Commit zurücksetzen können."  
  Hier (und an allen ähnlichen Stellen) wünsche ich mir mehr sprachliche Genauigkeit, 
  um das Verständnis zu erleichtern, den wer git-Denke nicht gewohnt ist, für den ist das
  alles ziemlich anpruchsvoll:  
  "...zurück auf ihren Zustand im letzten Commit setzen können."
- Huch, unten wird ja schon ein Kommandoprotokoll verlangt. Das wäre also leer.
- Die Zwischenüberschriften im Tutorenteil finde ich Overkill.
  Die Fx-Marker reichen zum Finden völlig aus.
- Hingegen ist "heading" keine sehr aussagekräftige Überschrift.
  Ich habe in meinen Aufgaben da immer so eine Art Generalklausel stehen:
  Worauf der Fokus der Korrektur liegt.

[SECTION::goal::experience]

Ich lerne verschiedene Fehlerarten für das Arbeiten mit git kennen und wie ich diese behebe.

[ENDSECTION]
[SECTION::background::default]

Im Laufe des Programmierpraktikums und auch danach werden wir mit ziemlich großer Sicherheit 
Fehler beim Bedienen von git machen, daher ist es natürlich hilfreich diese Fehler einfach mal 
in einer kontrollierten Testumgebung zu machen und dabei auch direkt wieder zu lernen wie man 
Sie rückgängig machen bzw. beheben kann.

[ENDSECTION]
[SECTION::instructions::loose]

Zuallererst lesen wir wieder einmal eine Seite aus dem Git Buch. Diesmal geht es darum wie wir 
[Dinge rückgängig machen](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) können.

[WARNING]
Lesen Sie die Seite gründlich durch! Viele der hier gelernten Befehle können Änderungen 
verursachen, welche **nicht** ohne weiteres rückgängig gemacht werden können.
[ENDWARNING]

Nun machen wir uns daran, das gelesene selbst auszuprobieren.

### Änderungen an einen bestehenden Commit anhängen

Erstellen Sie in ihrem zweiten Git-Repo eine neue Datei mit beliebigem Inhalt, fügen diese einem 
neuen Commit hinzu. Danach nehmen Sie wieder Änderungen an dieser Datei vor und fügen diese dann 
dem bestehenden Commit hinzu.

[EQ] Mit welchem Befehl haben Sie die Änderungen an den bestehenden Commit angehangen und wie 
funktioniert das Ändern des Commits eigentlich genau?

### Eine Datei(-änderung) aus einem ungepushten Commit entfernen/unstagen

Entfernen Sie die Datei aus der vorherigen Aufgabe aus dem jetzt noch ungepushten Commit zurück 
in die Working-Directory.

[EQ] Schreiben Sie den verwendeten Befehl auf und beschreiben Sie die Vorgehensweise.

### Änderungen an einer Datei rückgängig machen

Für diesen Teil der Aufgabe benötigen wir zwei neue Commits und ein paar Änderungen an der Datei.
Zunächst fügen wir den Status Quo der Datei einem neuen Commit *A* zu. Danach nehmen wir wieder 
beliebige Änderungen vor, sodass wir danach einen neuen Commit *B* mit diesen Änderungen erstellen 
können. Zuallerletzt machen wir die letzten Änderungen rückgängig in dem wir Sie auf den Zustand 
von Commit *A* zurücksetzen.

[EQ] Beschreiben Sie ihre vorgehensweise und die benutzten Befehle.

### Wie man git restore benutzt

Einige der vorherigen Aufgaben lassen sich auch, ab git version 2.23.0, mit git restore 
umsetzen. Gehen Sie dafür die vorherigen Beiden aufgaben durch und lösen Sie diese exklusiv mit 
git restore.

- [EQ] Beschreiben Sie, wie Sie mit `git restore` eine Datei aus einem ungepushten Commit 
  entfernen können.
- [EQ] Beschreiben Sie, wie Sie mit `git restore` den Zustand einer Datei zurück auf den 
  letzten Commit zurücksetzen können.

[NOTICE]
Falls Sie in den vorherigen Aufgaben bereits `git restore` verwendet haben. Gehen Sie diese noch 
einmal durch und überlegen Sie wie Sie die Aufgaben vielleicht noch lösen könnten.
[ENDNOTICE]

[ENDSECTION]
[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::heading]

### Änderungen an einen bestehenden Commit anhängen

- [EREFQ::1] `git commit --ammend`

### Eine Datei(-änderung) aus einem ungepushten Commit entfernen/unstagen

- [EREFQ::2] `git reset HEAD filename`

### Änderungen an einer Datei rückgängig machen

- [EREFQ::3] `git checkout -- filename`

### Wie man git restore benutzt

- [EREFQ::4] `git restore --stage filename`
- [EREFQ::5] `git restore filename`

[ENDINSTRUCTOR]
