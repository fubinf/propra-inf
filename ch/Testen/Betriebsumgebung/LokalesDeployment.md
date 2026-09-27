title: Lokale Bereitstellung des Testobjekts
stage: alpha
timevalue: 0.75
difficulty: 2
explains: SUT
assumes: venv, pip, Shell-Grundlagen, Git101
---

[SECTION::goal::experience]

- Ich kann das Testobjekt lokal starten und im Browser benutzen.

[ENDSECTION]
[SECTION::background::default]

Ein System under Test ([TERMREF::SUT]) ist das System, das bei einem Test geprüft wird.
In den Testaufgaben des ProPra ist das meist das _Testobjekt_, eine einfache Flask-Webanwendung,
die eigens für Übungen zur Testautomatisierung entwickelt wurde.
Damit Sie es testen können, müssen Sie es zunächst auf Ihrem Rechner zum Laufen bringen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Das Testobjekt kennenlernen

<replacement id="LokalesDeployment-SUTCopyRepoLink">
Der Quellcode des Testobjekts liegt im
[GitHub-Repository propra-inf-testobjekt](https://github.com/fubinf/propra-inf-testobjekt).
</replacement>

Lesen Sie dort im `README.md` den Abschnitt "Welche Versionen gibt es" und sehen Sie sich die Versionsverzeichnisse an.

- [EQ] Welche der Versionen enthalten derzeit lauffähigen Code, welche nicht?

Sollten Ihnen später merkwürdige Verhaltensmuster am Testobjekt auffallen, dürfen Sie diese gern
im Repository als Issue melden.
<!-- time estimate: 5 min -->

### Repository klonen

Legen Sie in einer neuen Terminal-Sitzung ein Verzeichnis für das Testobjekt an und klonen Sie
das Repository dorthin:

- [EC] `mkdir ~/ws/sut`
- [EC] `cd ~/ws/sut`
- [EC] `git clone https://github.com/fubinf/propra-inf-testobjekt.git`

[WARNING]
Achten Sie darauf, dass Sie sich beim Klonen **im** Verzeichnis `~/ws/sut` befinden,
sonst landet das Repository woanders.
[ENDWARNING]
<!-- time estimate: 5 min -->

### Umgebung einrichten

Das Testobjekt ist ein Python-Projekt.
Eine aktuelle Python-3-Version genügt.

- [EC] Prüfen Sie Ihre Python-Version mit `python3 --version`.

Die Abhängigkeiten des Testobjekts installieren Sie in eine eigene virtuelle Umgebung,
wie in [PARTREF::venv] beschrieben.
Legen Sie diese außerhalb des Repositorys an, damit sie nicht in `git status` auftaucht:

- [EC] Legen Sie eine virtuelle Umgebung `~/venv/sut` an.
- [EC] Aktivieren Sie diese virtuelle Umgebung.

[HINT::Ich weiß nicht mehr, wie man eine venv anlegt und aktiviert]
Anlegen: `python3 -m venv ~/venv/sut`  
Aktivieren: `source ~/venv/sut/bin/activate`  
Danach sollte Ihr [TERMREF::Prompt] mit `(sut)` beginnen.
[ENDHINT]

Das Testobjekt verwendet das Web-Framework Flask und einige Flask-Erweiterungen.
Diese Abhängigkeiten sind je Version in einer Datei `requirements.txt` im Versionsverzeichnis aufgeführt.
Welche Version Sie verwenden sollen, gibt die jeweilige Aufgabe vor; hier nehmen wir `v1.0.0`.

- [EC] Wechseln Sie in das Verzeichnis `propra-inf-testobjekt/v1.0.0`.
- [EC] Installieren Sie die Abhängigkeiten aus `requirements.txt` mit `pip`.
<!-- time estimate: 10 min -->

### Anwendung starten

Die Hauptdatei der Anwendung heißt `app.py`.

- [EC] Starten Sie die Anwendung, indem Sie `app.py` mit Python ausführen.

Die Anwendung läuft nun im Vordergrund des Terminals, bis Sie sie mit `Strg-C` beenden.
Lassen Sie dieses Terminal also geöffnet.

Lesen Sie die Startmeldung und den Abschnitt
[Debug Mode in der Flask-Dokumentation](https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode).

- [EQ] Laut Startmeldung ist die Anwendung unter `127.0.0.1` erreichbar.
  Was bedeutet diese [TERMREF::IP-Adresse] und könnten andere Rechner die Anwendung aufrufen?
- [EQ] Die Startmeldung sagt `Debugger is active!`.
  Was bewirkt der Debug-Modus und warum darf man ihn nie auf einem öffentlich erreichbaren Server einschalten?

[HINT::`Address already in use` oder der Browser zeigt eine fremde Seite (macOS)]
Unter macOS belegt der AirPlay-Empfänger standardmäßig Port 5000.
Entweder schalten Sie ihn in den Systemeinstellungen unter "Allgemein → AirDrop & Handoff" ab,
oder Sie starten die Anwendung auf einem anderen Port:
`flask --app app run --debug --port 5001`.
Verwenden Sie dann im Folgenden überall `5001` statt `5000`.
[ENDHINT]
<!-- time estimate: 15 min -->

### Anwendung aufrufen

Rufen Sie im Browser `http://127.0.0.1:5000` auf.
Sie sehen eine Anmeldeseite.
Die Benutzernamen stehen in `data/users.json`, das zugehörige Passwort finden Sie in `app.py`
dort, wo die Benutzer angelegt werden.

- [EQ] Melden Sie sich an.
  Mit welchem Benutzernamen und Passwort ist Ihnen das gelungen und was zeigt die Seite danach an?

[HINT::Die Anmeldung schlägt trotz richtigem Passwort fehl]
Möglicherweise wurde das Passwort in der Datenbank geändert.
Rufen Sie `http://127.0.0.1:5000/reset-password` auf; das setzt alle Passwörter auf den Ausgangswert zurück.
[ENDHINT]

Die Startseite können Sie auch auf der Kommandozeile abrufen.
Öffnen Sie dazu ein zweites Terminal (die Anwendung muss im ersten weiterlaufen).
`curl` ruft eine URL ab und gibt die Antwort aus; `-s` unterdrückt dabei die Fortschrittsanzeige.

- [EC] `curl -s http://127.0.0.1:5000 | head -n 10`
<!-- time estimate: 10 min -->

### Warum lokal?

Die Aufgabengruppe [PARTREF::Betriebsumgebung] nennt verschiedene Betriebsumgebungen für Tests.

- [EQ] Welche Vorteile hat es beim Testen, dass jede_r ein eigenes lokales Exemplar des Testobjekts startet,
  statt dass alle gemeinsam einen zentral bereitgestellten Testserver benutzen?
  Nennen Sie mindestens zwei.

Beenden Sie zum Schluss die Anwendung im ersten Terminal mit `Strg-C`.
<!-- time estimate: 5 min -->

[ENDSECTION]
[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
