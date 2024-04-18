title: Fehler beheben im git Repository
stage: alpha
timevalue: 2.0
difficulty: 1
assumes: git-Funktionsweise
requires: git-Zweitrepo
---

[SECTION::goal::experience]

Wir lernen verschiedene Fehlerszenarien in git kennen und lernen wie man diese beheben kann.

[ENDSECTION]
[SECTION::background::default]

Auch wenn einem git vieles in der Versionsverwaltung einfacher macht stößt man doch hin und 
wieder auf Hindernisse. So kann es z.B. sein, dass man eine bereits eingecheckte Datei wieder 
entfernen, oder einen Commit rückgängig machen möchte. Manchmal möchte man auch mehrere Commits 
vor dem Pushen zusammenführen oder vielleicht will man auch die Commit-Nachricht noch einmal 
anpassen.

[ENDSECTION]
[SECTION::instructions::loose]

Zuallererst lesen wir wieder einmal eine Seite aus dem Git Buch. Diesmal geht es darum wie wir 
[Dinge rückgängig machen](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) können.

[WARNING]
Lesen Sie die Seite gründlich durch! Viele der hier gelernten Befehle können Änderungen 
verursachen, welche **nicht** rückgängig gemacht werden können.
[ENDWARNING]

Bearbeiten Sie die folgenden Aufgaben. Dokumentieren Sie dabei die vorgenommenen Arbeitsschritte 
und schreiben Sie auf welche Kommandos Sie verwendet haben.

### Änderungen an einen bestehenden Commit anhängen

1. Erstellen Sie in ihrem git-Repo eine neue Datei mit beliebigem Inhalt.  
2. Fügen Sie diese Datei einem neuen Commit hinzu.
3. Nehmen Sie nun beliebige Änderungen an dieser Datei vor.
4. Fügen Sie diese Änderungen dem existierenden Commit hinzu.

[EQ] Mit welchem Befehl haben Sie die Änderungen an den bestehenden Commit angehangen und wie 
funktioniert dieser Befehl genau?

### Eine Datei(-änderung) aus einem ungepushten Commit entfernen/unstagen

1. Wir benutzen die Datei aus dem vorherigen Commit.
2. Entfernen Sie nun die Datei aus dem vorherigen Commit zurück in die Working-Area.

[EQ] Mit welchem Befehl haben Sie die Datei aus dem Commit entfernt?

### Änderungen an einer Datei rückgängig machen

1. Wir öffnen wieder die Datei aus dem vorherigen Commit und nehmen an ihr beliebige Änderungen vor.
2. Nun setzen Sie mithilfe von git die Datei auf den Stand vom vorherigen Commit zurück.

[EQ] Mit welchem Befehl haben Sie den Zustand der Datei zurückgesetzt?

### Wie man git restore benutzt

Einige der vorherigen Aufgaben lassen sich auch, ab git version 2.23.0 einfacher mit git restore 
umsetzen.

- [EQ] Entfernen Sie mit `git restore` eine Datei aus einem ungepushten Commit.
- [EQ] Setzen Sie mit `git restore` den Zustand einer Datei zurück auf den letzten Commit.

[ENDSECTION]
[SECTION::submission::reflection]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

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
