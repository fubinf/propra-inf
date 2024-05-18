title: Die Testpyramide verstehen
stage: alpha
timevalue: 1.5
difficulty: 1
---

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
