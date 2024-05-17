title: Vom Fehler, über Defekt, hin zum Versagen
stage: alpha
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::trial]

- Ich kann Fehlerbegriffe definieren
- Ich kann Versagen erkennen

[ENDSECTION]

[SECTION::background::default]

In der Qualitätssicherung werden unterschiedliche Begriffe verwendet, die einen Fehlerzustand
beschreiben. Die richtige Verwendung der definierten Begriffe kann nur funktionieren, wenn man die
feinen Unterschiede kennengelernt hat.

[ENDSECTION]

[SECTION::instructions::loose]

### Fehlerarten

Wenn Sie das Modul `Softwaretechnik` besucht haben, sind Ihnen die Bergiffe Fehler, Defekt,
Fehlerzustand und Versagen sicherlich noch bekannt. Falls nein, hier ein kleiner Refresher:

Lesen Sie zu aller erst die folgenden Begriffe im Glassar nach: [TERMREF::Fehler],
[TERMREF::Defekt], [TERMREF::Fehlerzustand], [TERMREF::Versagen]

- [EQ] Diskutieren Sie: Ist jeder Defekt auf eine 'falsche' Programmierung zurückzuführen?
- [EQ] Können Sie sich ein komplexes Programm vorstellen, dass keine Defekte hat?
- [EQ] Warum folgt aus einem Fehler nicht zwangsläufig ein Defekt? Beschreiben Sie ein Beispiel.
- [EQ] Welche Funktionalität könnte aus Ihrer Sicht zu 100% selbst bei einer einfachen Testabdeckung
  keinen Defekt beinhalten? (Beschreibung oder Pseudocode reicht aus)
- [EQ] Sie haben zwei unterschiedliche Systemumgebungen, auf denen eine Anwendung, die einen Defekt aufweist,
  läuft. Dieser Defekt ist jedoch nur auf einer Systemumgebung reproduzierbar. Spekulieren Sie, warum.

Nachdem Sie nun wissen, was ein Fehler definiert, sollen Sie auch lernen diesen zu erkennen. Dazu
verwenden wir als Grundlage dieser Übung folgende [TERMREF::User Story]:

### Praktische Anwendung

#### User Story

Als registrierter Benutzer möchte ich mich im Portal anmelden können, damit ich auf meine
Kontoinformationen zugreifen kann.

##### [TERMREF::Akzeptanzkriterien] (AKs):

- Ein registrierter und aktiver Benutzer kann sich mit einer gültigen E-Mail-Adresse und seinem
  zugehörigen Passwort anmelden.
- Das System zeigt eine Fehlermeldung, wenn die E-Mail-Adresse ungültig ist.
- Das System zeigt eine Fehlermeldung, wenn das Passwort zu kurz ist.
- Ein aktiver Benutzer kann sein Passwort auf der Anmeldeseite neu vergeben.
- Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen.
- Nach erfolgreicher Anmeldung wird der Nutzer auf die Nutzer-Profilseite weitergeleitet.

#### Aufgabenn zu der User Story

- [EQ] Sind alle Akzeptanzkriterien für einen Menschen prüfbar? Wenn nein, formulieren Sie das
  Akzeptanzkriterium entsprechend um.
- [EQ] Welche der folgenden Testbeschreibungen ([TERMREF::Testszenario]) führen zu einem [TERMREF::Versagen]?

Vorbedingung: Ein Benutzer befindet sich auf der Login Seite eines Portals.

1. Hier gibt der Nutzer seinen **validen** Benutzernamen und sein **gültiges** Passwort in die
vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden. Das Portal leitet
den Benutzer auf die Seite seines Nutzer-Profils weiter.

2. Hier gibt der Nutzer seinen **validen** Benutzernamen und ein **ungültiges** Passwort in
die vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal gibt eine Fehlermeldung aus und leitet den Benutzer nicht weiter.

3. Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **gültiges** Passwort in die
vorgesehenen Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal leitet den Benutzer auf die Seite seines Nutzer-Profils weiter.

4. Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **gültiges** Passwort in die
Eingabemasken ein. Anschließend klickt der Benutzer auf Anmelden.
Das Portal leitet den Benutzer auf die Seite des Portal-Administrators weiter.

5. Hier gibt der Nutzer seine **valide** E-Mail-Adresse und sein **gültiges** Passwort in die
Eingabemasken ein. Anschließend wartet der Nutzer 100 Jahre, bis er angemeldet ist.

[EQ] Ergänzen Sie mindestens ein weiteres Akzeptanzkriterium.

### Ferhlerbericht

Wenn ein Defekt vorliegt, sollte dieser auch Dokumentiert und Kommuniziert werden. Dazu sind einige
Informationen wichtig, um sowohl diesen Defektbericht eindeutig zuordnen zu können, aber auch dem
Entwickler / Bug-Fixer bestmöglich Informationen zum Debugging und Nachstellen des Problems zu liefern.
Recherchieren Sie, was einen guten Defektbericht aus macht: [Defektbericht](https://www.guru99.com/de/how-to-write-a-bug-report.html)

- [EQ] Erstellen Sie zu einem entdeckten Defekt einen guten udn einen schlechten Defektbericht
- [EQ] Was würden Sie tun, wenn Sie 3 Fehlerberichte bekommen haben, die durch einen und den selben
  Fehler ausgelöst werden, aber alle unterschiedlich gut in der Erzwingung der Fehlerwirkung und der
  verwendeten Daten beschrieben sind?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

- [EREFQ::1]: hier sollte ein nein argumentiert werden, da u.a. Missverständnisse oder inkonsistente
  Architekturen Gründe sein können
- [EREFQ::2] nein, da eine 100% Testabdeckung bei komplexen Systemen nahezu unmöglich ist (Aufwand und Testdaten)
- [EREFQ::3] Seiteneffekte: Ein Fehler hebt einen anderen Fehler auf; Ein Fehler tritt sehr
  unwahrscheinlich ein (zB. bei 0,0001% aller Fälle)
- [EREFQ::4]: Da Systemarchitektur, -konfiguration oder abhängige Versionierungen anders sind;
  das verhindert die Erkennung des Defekt oder der Defekt ist dadurch obsolet
- [EREFQ::5]: hier sollte etwas triviales beschrieben werden (z.B.: 1+1=2)
- 
- [EREFQ::6]: Nr. 5 nicht, da die Wartezeit unzumutbar ist.
- [EREFQ::7]: Nr.1-2: E-Mail, kein Benutzername ist gefordert; Nr.4: Falsche Weiterleitung;
  Nr.5: blockiert, da in keiner angemessenen Zeit testbar
- [EREFQ::8]: hier kann auf eines weiteren Akzeptanzkriterien eingegangen werden, die in der User
  Story aufgelistet sind
- [EREFQ::9]: ungenaue und sehr genaue Beschreibung sollte hervorstechen
- [EREFQ::10]: verifizieren, dokumentieren und miteinander verknüpfen/verlinken

[ENDINSTRUCTOR]
