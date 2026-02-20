title: Die Testpyramide verstehen
stage: draft
timevalue: 0
difficulty: 1
---

TODO_2_ruhe:

Diese Aufgabe funktioniert so nicht, fürchte ich.
Ich sehe zwei Hauptprobleme:

- Der Artikel setzt viel Wissen voraus, dass unsere Studis an dieser Stelle nicht haben.
  (Außerdem widerspricht er sich teilweise verwirrend selbst, z.B. bei Wieso Pyramide?)
- Das ist für ProPra zu theoretisch.  
  Mindestens sollte man sich ein reales Beispielprojekt angucken, das alle drei Sorten hat,
  alle drei Sorten nachzählen, alle drei Sorten laufenlassen und die Zeiten beobachten,
  für alle drei Sorten in der git-Historie stöbern und nachvollziehen, dass welche
  Sorten wie oft weswegen geändert werden.  
  Dann wäre das eine supertolle Aufgabe! Allerdings auch eine sehr umfangreiche und
  sehr schwierige.  
  Und der Aufwand, sie zu bauen, ist auch riesig. Allein, ein solches Projekt auszusuchen...

- Die "kleine" Lösung für Problem 2 wäre, ein Projekt zu finden, das solche Statistiken schon
  öffentlich bereit hält und die dann nur zu studieren. Ich kenne auf Anhieb keins.
- Eine andere kleine Lösung könnte sein, in einem Projekt nur je zwei Exemplare von
  Unittest, Integrationstest und E2E-Test genauer anzusehen: Wie viel Code ist das?
  Wie viele Einzelteile werden benutzt? Wie viel Funktionalität deckt das ab?
  Wie oft ist es korrigiert worden? etc.
- In jedem Fall ergibt die Aufgabe erst Sinn, wenn das Vorwissen über die Testarten da ist.
  Und da nach meinem Eindruck kaum jemand Unittests von Integrationstests klar unterscheidet,
  wenn beide mit einem "Unit"test-Framework gebaut sind, ist das alles in der Praxis unübersichtlich.

[SECTION::goal::idea]

- Ich kann die Ebenen einer Testpyramide von Unittest bis Abnahmetest erklären
- Ich kann Vor- und Nachteile einer jeweiligen Ebene erkennen

[ENDSECTION]

[SECTION::background::default]

Eine Testebene kann von Unittest bis hin zu Abnahmetests betrachtet werden. Zusätzlich gibt es noch
Systemtest, Integrationstest und E2E Test, die eingeordnet werden wollen und ob wir die Pyramide von
oben, oder unten betrachten.

[ENDSECTION]

[SECTION::instructions::loose]
<!-- @LINK_SPEC: status=403 -->
Zu erste sollten Sie sich einen Verständnis über das Thema Testpyramide entwickeln. Anschließend
reflektieren Sie das neu erworbene Wissen. Lesen Sie dazu den kurzen aber informativen Beitrag des
[Austrian Testing Board - Testpyramide](https://www.austriantestingboard.at/die-testautomationspyramide-ein-einfaches-gebilde-voller-missverstaendnisse/), um die folgenden
Fragen zu beantworten.

### Verständnisfragen

- [EQ] Was versteht man unter einer Testpyramide?
- [EQ] Gibt es eine einheitliche Definition einer Testpyramide? Wenn nein, welche Unterschiede gibt es?
- [EQ] Wie unterscheiden sich die Ebenen der Testpyramide hinsichtlich der Kosten, der Geschwindigkeit,
  der Komplexität und der Testanzahl?
- [EQ] Welchen Bezug hat die Testautomatisierung zu der jeweiligen Testebene?
- [EQ] Diskutieren Sie alternative Ansätze und wie diese sich von der Testpyramide unterscheiden.

### Reflektion

- [EQ] Können Sie sich ein Projekt vorstellen, in dem tatsächlich streng nach der dreistufigen
  Pyramide getestet wird?
- [EQ] Können Sie sich vorstellen **alle** Testfälle auf der obersten Ebene zu automatisieren?
- [EQ] Sollten Tester auf der untersten Ebene (ganz oder teilweise) Testfälle erstellen?
- [EQ] Sollten Entwickler auf der obersten Ebene (ganz oder teilweise) Testfälle erstellen?

### Zuordnung von Tests

Im Folgenden werden eine Reihe von Szenarien beschrieben. Sortieren Sie diese in eine der
kennengelernten Ebenen ein (gerne auch in mehrere). Beschreiben Sie jedoch, warum ein Test auf
dieser Ebene sinnvoll ist.

- [EQ] Auf welcher Ebene würden Sie den / die Test vorsehen?

Sie sollen testen, ob ...

1. der Datenbankserver erreichbar ist.
2. der Button "Abbrechen" seine definierte Funktion erfüllt.
3. die neu implementierte [TERMREF::API]-Schnittstelle alle [TERMREF::Akzeptanzkriterien]
   erfüllt.
4. die Methode "calculate()" das erwartete Ergebnis zurück gibt.
5. sich jeder definierte Nutzerrolle korrekte Berechtigungen besitzt.

[ENDSECTION]

[SECTION::submission::trace,reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

- [EREFQ::1]: Ein Konzept aus drei Ebenen (Unit-, Integrations- und Systemtestebene)
- [EREFQ::2]: Nein, zB die umgedrehte Testpyramide.
- [EREFQ::3]: Kosten: unten gering, oben hoch; Geschwindigkeit: unten hoch, oben langsam; Komplexität:
  unten gering, oben hoch; (kann anders herum sein für nicht Entwickler) Testanzahl: unten hoch, oben gering(er)
- [EREFQ::4]: Unittest: vollautomatisiert, Integrations- und Systemtest: automatisiert/manuell
- [EREFQ::5]: Z.B. die umgedrehte Testpyramide: Fokus auf mehr E-2-E/Systemtests oder Abnahmetest,
  als auf Unit- oder Integrationstests
- [EREFQ::10]: Unittests: 1., 4., (5.), Integrationstests: 1., 3. (5.), Systemtest: 2., 5.

[ENDINSTRUCTOR]
