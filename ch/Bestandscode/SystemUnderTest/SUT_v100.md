title: Einführung in das SUT v1.0.0
stage: alpha
timevalue: 1
difficulty: 3
explains: SUT
---

[SECTION::goal::idea]

Ich verstehe den Aufbau des SUT v1.0.0.

[ENDSECTION]

[SECTION::background::default]

Es gibt verschiedene Möglichkeiten, um Ihre Programmierfähigkeiten zu verbessern: Sie können Ihren
eigenen Code erstellen, testen und zum Laufen bringen, oder Sie können vorhandenen Code verwenden,
um Ihr Können weiter zu vertiefen. In Ihrer aktuellen Aufgabe beziehen Sie sich auf den bestehenden
Codezustand `SUT v1.0.0`, an dem Sie nicht aktiv mitgewirkt haben. Für bevorstehende Aufgaben sollen
Sie jedoch entweder an der Entwicklung, am Testen oder an anderen Verbesserungen teilnehmen. Um Sie
dabei optimal zu unterstützen, erhalten Sie hier einen kurzen Überblick über die bisherige
Entwicklung dieses Codes.

[ENDSECTION]

[SECTION::instructions::detailed]

### Wo finde ich das SUT?

Das SUT v1.0.0 ist eine eigenentwicklung, mit dem Ziel, das Entwickeln und Testen im ProPra
praktisch zu unterstützen. Daher wurde der Entwicklungstsand im "Freie Universität Berlin, Institut
für Informatik"-GitHub Profil unter `propra-inf-testobjekt` abgelegt und ist
[hier](https://github.com/fubinf/propra-inf-testobjekt) verlinkt.

- [EQ] Sehen Sie die unterschiedlich bereitgestellten Versionen im Repository?
- [EQ] Ohne den Inhalt zu kennen: Wie unterschiedlich schätzen Sie die Versionen ein?

### Aufbau des SUT

Lesen Sie die im Repository hinterlegte `README.md` Datei. Darin erhalten Sie einen Überblick über
die Aufgabe des SUT.

- [EQ] Welche Begriffe, die in der README.md aufgeführt sind, bereiten Ihnen Schwierigkeiten beim
  Verständnis?
- [EQ] Finden Sie den technologischen Ansatz eher komplex, oder überrascht er Sie gar nicht?
- [EQ] Angenommen, Sie wollen mit dem SUT Aufgaben anhand der implementierten User Stories bearbeiten:
  Finden Sie die implementierte User Story Übersicht eher hilfreich, oder störend?

### User Storie Übersicht

Betrachten Sie die User Stories unter `v1.0.0/data/user_stories.json`.

- [EQ] Sind diese User Stories für Sie verständlich formuliert?
- [EQ] Finden Sie die Anzahl der User Stories für eine Version 1.0.0 angemessen?

### Nutzer Übersicht

Betrachten Sie die Nutzer unter `v1.0.0/data/users.json`.

- [EQ] Welche Nutzer können sich einloggen und wie ist das jeweilige Passwort zu den Nutzern?

### Python Code

Der auf Python basierende Entwicklungscode ist unter `v1.0.0/app.py`.

- [EQ] Welche Funktion verbirgt sich hinter dem [TERMREF::Dekorator] `@app.route('/')`?
- [EQ] Was für eine Funktion sollte nach dieser Zeile folgen?

### Frontend Anteil

Das Frontend für die schicke GUI ist sowohl unter `v1.0.0/static` für den Styleaufbau, als auch unter
`v1.0.0/templates` für den wiederverwendbaren HTML Anteil untergebracht.  

- [EQ] Warum finden Sie unter `templates` die Dateien `base.html`, `login.html` und `profile.html`
  wieder?

### Datenbank

Die hinterlegten Informationen, die Sie verarbeiten wollen, sollen nach einem deployment persistent
sein. Daher wird eine kleine Datenbank verwenden, die Sie unter `v1.0.0/instance` finden.
Diese Datei können Sie jedoch nicht im Browser können, aber in einem DB Unterstützendem Tool, das
Sie unter [PARTREF::IDE] einrichten können. Wenn Sie neugierig sind, wie eine Datenbank funktioniert,
können Sie den Teil [PARTREF::SQL] durcharbeiten.

### Unittests

Zu jeder guten Entwicklung gehören auch Unnittests. Diese finden Sie unter `v1.0.0/tests/*`.

- [EQ] Wie viele Test finden Sie und welche davon sind Ihrer Meinung nach warum nicht sinnvoll?

### Requirements

Das SUT hat Abhängigkeiten. Um diese schnellstmöglich zu identifizieren, ist eine Datei
`requirements.txt` hinterlegt. Mit dieser Datei können Sie unkompliziert die Abhängigkeiten
installieren.

Nachdem Sie sich einen Überblick über die Version 1.0.0 verschafft haben, sollten Sie problemlos
bereit sein, mit dieser Version zu arbeiten.

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Hinweise]

- [EREFQ::1] Drei Versionen v1.0.0, v1.1.0 und v3.0.0 mit Stand 13. Juli 2024
- [EREFQ::2] Idealer Weise wird auf die einzelnen Sektionen der Versionsnummer eingegenagen:
  Hauptversion.Unterversion.Patchversion-Ergänzung - Die Ergänzung ist hier kein Bestandteil.
  Mit der Erhöhung der Hauptvesion sollte eine größere Änderung erwartet werden, als mit der
  Erhöhung der Unterversion.
- [EREFQ::3] - [EREFQ::4] Interessant für den Tutor, um eine kleimne Einschätzung der Erfahrungen
  des Studenten zu erhalten.
- [EREFQ::5] Erste Berührungspunkt mit dem Thema Useability und User Experience (UX). Der Student soll
  beim Kennenlernen des SUT lediglich über den Aufbau reflektieren.
- [EREFQ::6] Idealer Weise ja, da die wesentlichen Punkte beschrieben sind.
- [EREFQ::7] Für Anfänger: ja, Fortgeschrittene: nein
- [EREFQ::8] Die JSON verrät: Nutzer: Alice, Bob und Charlie. Das PW ist in der User Story 1 mit
  'password' definiert (Beim initialen Start - Passwort könnte vom Studenten geändert werden. DB löschen
  initialisiert die Nutzer neu.)
- [EREFQ::9] Im Python-Framework Flask ist der Dekorator @app.route('/') eine Methode, um Routen für
  die Webanwendung zu definieren. Der Eintrag / gibt das Stammverzeichnis der Anwendung an.
- [EREFQ::10] Anschließend kommt das gewünschte Verhalten, nachdem diese Seite gezielt aufgerufen wurde.
  Z.B. Darstellung der Login-Seite.
- [EREFQ::11] Flask nutzt diese Standardkonvention um eine Trennung von Logik und Darstellung der
  Anwendung zu ermöglichen. Hier kommen demnach HTML Dateien hinein.

[ENDINSTRUCTOR]
