title: Vom Fehler, über Defekt, hin zum Versagen
stage: beta
timevalue: 1.5
difficulty: 2
explains: User Story
---

[SECTION::goal::trial]

- Ich kann Fehler, Defekte, Versagen und Akzeptanzkriterien definieren und unterscheiden und 
  kann die Begriffe anwenden.
- Ich kann Versagen erkennen.

[ENDSECTION]

[SECTION::background::default]

In der Qualitätssicherung werden unterschiedliche Begriffe verwendet, die einen Fehlerzustand
beschreiben. Die richtige Verwendung der definierten Begriffe kann nur funktionieren, wenn man die
feinen Unterschiede kennengelernt hat.

[ENDSECTION]

[SECTION::instructions::loose]

### Problemarten

Damit man vernünftig über Testen sprechen und nachdenken kann, muss man ein paar Dinge
sorgfältig auseinanderhalten.
Bitte lesen Sie die folgenden Begriffe im Glossar nach: [TERMREF::Fehler],
[TERMREF::Defekt], [TERMREF::Fehlerzustand], [TERMREF::Versagen].
<replacement id="Fehler-Defekt-Versagen1">(Falls Sie das Modul `Softwaretechnik` besucht haben, 
sind Ihnen die Bergiffe Fehler, Defekt, und Versagen von dort bekannt.)
</replacement>

- [EQ] Diskutieren Sie: Ist jeder Defekt auf eine falsche Programmierung zurückzuführen?
- [EQ] Können Sie sich ein komplexes Programm vorstellen, dass keine Defekte hat?
- [EQ] Warum folgt aus einem Fehler nicht zwangsläufig ein Defekt? Beschreiben Sie ein Beispiel.
- [EQ] Sie haben zwei unterschiedliche Systemumgebungen, auf denen eine Anwendung läuft.
  Die Anwendung hat einen Defekt.
  Ein Versagen tritt jedoch nur auf einer Systemumgebung auf, nicht auf der anderen.
  Spekulieren Sie, warum.

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
- Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen
  für 24 Stunden.
- Nach erfolgreicher Anmeldung wird der Nutzer auf die Nutzer-Profilseite weitergeleitet.

#### Aufgaben zu der User Story

- [EQ] Sind alle Akzeptanzkriterien praktikabel überprüfbar? Wenn nein, formulieren Sie das
  Akzeptanzkriterium entsprechend um.
- [EQ] Welche der folgenden Szenarios ([TERMREF::Testszenario]) beschreiben 
  in Bezug auf obige Akzeptanzkriterien ein [TERMREF::Versagen]?

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

[EQ] Ergänzen Sie mindestens ein weiteres Akzeptanzkriterium, damit es für das letzte Szenario
keine Meinungsverschiedenheiten mehr geben kann.

### Problembericht

Wenn ein Versagen erkannt wurde und nicht sofort beseitigt werden kann, 
sollte es dokumentiert und kommuniziert werden. 
Dazu sind einige Informationen wichtig, um den Bericht zuordnen zu können und um den
Entwickler_innen bestmöglich Informationen zum Debugging und Nachstellen des Problems zu liefern.
Recherchieren Sie, was einen guten Problembericht aus macht: [Problembericht](https://www.guru99.com/de/how-to-write-a-bug-report.html)

- [EQ] Erstellen Sie zu einem der oben entdeckten Versagen einen guten und einen schlechten Problembericht.
- [EQ] Was würden Sie tun, wenn Sie 3 Problemberichte bekommen, die wahrscheinlich vom selben
  Defekt handeln, aber unterschiedlich gut beschrieben sind?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

- [EREFQ::1]: Viele Strukturen werden erst zum Defekt, wenn eine vormals vage Erwartung konkreter wird.
- [EREFQ::2] Ja, aber das kommt selten auf Anhieb vor, da es so viele Möglichkeiten für Defekte gibt.
- [EREFQ::3] Beispiel: beim Ausdruck `f > 0` die Variable `r` mit der 
  hier falschen verwandten Variable `f` verwechselt, 
  die aber größer Null genau dann ist, wenn `r` es auch ist.
- [EREFQ::4]: Die Umgebungen verhalten sich verschieden. Z.B. findet Windows eine Datei,
  auch wenn beim Namen die Groß-/Kleinschreibung falsch ist; 
  bei Linux wird die Datei mit dem gleichen Schreibfehler nicht gefunden.
- [EREFQ::5]: Nr. 5 nicht, da die Wartezeit unzumutbar ist. Reduktion auf 1 Minute Sperre hilft.
- [EREFQ::6]: Nr.1 und 2, denn es ist eine Emailadresse gefordert, nicht ein Benutzername.  
  Nr.4, denn die Weiterleitung ist falsch.  
  Nr.5, da die lange Wartezeit nach den Akzeptanzkriterien nicht zu erwarten und 
  plausiblerweise auch nicht akzeptabel ist.
- [EREFQ::7]: Entgegen Nr. 5 eine nur kurze Wartezeit fordern.
- [EREFQ::8]: ungenaue und sehr genaue Beschreibung sollte hervorstechen
- [EREFQ::9]: verifizieren, dokumentieren, miteinander verlinken und dabei darauf hinweisen,
  welcher die genaueste Beschreibung enthält.  
  Man könnte sie auch zusammenführen, aber das macht viel Arbeit und falls dann doch nicht der gleiche
  Defekt dahintersteckt, hat man sich erst recht keinen Gefallen getan.

[ENDINSTRUCTOR]
