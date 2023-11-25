description: >
  Wie schreibt man automatisierte Tests, die viel Zutrauen bringen
  ohne einen Wahnsinns-Aufwand für Erstellung und Pflege zu benötigen?
---

Softwaretesten ist ein umfassendes Thema, das verschiedene Bereiche und Aspekte abdeckt. Es gibt verschiedene
Teststrategien und -ansätze, die in der Softwareentwicklung verwendet werden, um sicherzustellen, dass eine Anwendung
(fehlerfrei und) gem. den Anforderungen funktioniert.

**Manuelles Testen** ist ein wesentlicher Bestandteil des Softwaretestprozesses und umfasst verschiedene Aspekte wie
Funktionalitätsprüfung, exploratives Testen, Usability-Tests, Akzeptanztests und Regressionstests. Hierbei werden
Testfälle von menschlichen Testern manuell ausgeführt, um sicherzustellen, dass die Software den funktionalen
Anforderungen entspricht, Benutzerfreundlich ist und/oder den Akzeptanzkriterien gerecht wird.

**Automatisiertes Testen** ist ein effizienter Ansatz, der die Verwendung von Skripten und Tools zur automatisierten
Ausführung von Testfällen beinhaltet. Zu den Hauptbereichen gehören Unit Testing, Integrationstests, Regressionstests
und Leistungstests. Dieser Ansatz trägt dazu bei, den Testprozess zu beschleunigen, die Konsistenz der Testergebnisse
sicherzustellen und ermöglicht auch die Durchführung umfangreicher Last- und Leistungstests.

Die effektive Organisation und Steuerung des gesamten Testprozesses erfordert **Testmanagement**, was die Planung,
Testfallerstellung, Testausführung, Fehlerverwaltung, Berichterstellung, Testautomatisierung und die Verwaltung von
Testumgebung und -daten einschließt. Ein gutes Testmanagement gewährleistet die Ordnungsmäßigkeit und
Nachvollziehbarkeit der Tests sowie die effiziente Zusammenarbeit zwischen den Testteams und anderen Stakeholdern.

Die verschiedenen **Testarten und -ziele** spielen eine entscheidende Rolle beim Testen der Software. Hierbei werden
Funktionalitätstests durchgeführt, um sicherzustellen, dass die Software die funktionalen Anforderungen erfüllt.
Nicht-funktionale Tests konzentrieren sich auf Aspekte wie Leistung, Sicherheit und Benutzerfreundlichkeit.
Sicherheitstests decken Schwachstellen und Sicherheitslücken auf, während Usability-Tests die Benutzerfreundlichkeit
bewerten. Kompatibilitätstests stellen sicher, dass die Software auf verschiedenen Plattformen und Geräten
ordnungsgemäß funktioniert, und Performance- und Leistungstests prüfen die Software unter verschiedenen Belastungen
und Bedingungen.

In diesem Kapitel geht es um die Qualität der Software, die durch Testmanager, Test Leiter, Test Analysten,
Testautomatisierer und Test Architekten (allg. Tester) optimiert werden kann. Hier betrachten wir den Nutzen des
Testens (Return On Invest), erlenen die Grundlagen des Testens, betrachten Konzeptionen und lassen den Spaß, das
Programmieren, definitiv im Thema Testautomatisierung nicht außen vor.

```mermaid
graph TD
    A[Softwaretesten] -->|enthält| B[Basiswissen]
    B --> BA[Übung: Fehler, Defekt, Fehlerart]
    B --> BB[Übung: Testen, Debuggen, Qualitätssicherung]
    B --> BC[Übung: Testfall, Testsammlung, Testplan, Testdaten]

    A -->|enthält| C[SuT]
    C --> CA[Vorstellung des SuT]
    CA --> CA1[Bestandscode v1.0.0]
    CA1 -.-> CA2[Bestandscode v1.1.0]
    CA2 -.-> CA3[Bestandscode v3.0.0]
    CA --> CB[Übung: Implementierung]
    CB --> CB1[Übung: IDE]
    CB --> CB2[Übung: GitHub Action]

    A -->|enthält| D[Manuelles Testen]
    D --> DA[Übung: Testfälle erstellen]
    DA -.-> DB[Übung: Fehlerberichterstattung]

    A -->|enthält| E[Automatisiertes Testen]
    E --> EA[Testautomatisierungstools]
    EA --> EA1[Übung: Pytest]
    EA --> EA2[Übung: Robot Framework]
    EA --> EA3[Übung: Cypress]
    EA --> EA4[Übung: Cycumber mit Cypress]
    EA --> EA5[Übung: Locust]
    EA --> EA6[Übung: JMeter]
    EA --> EA7[Übung: SonarQube]
    EA --> EA8[Übung: Nessus]

    E --> EB[Testarten]
    EB --> EB1[Übung: Unittests / TDD]
    EB --> EB2[Übung: Integrationstests]
    EB --> EB3[Übung: Systemtests]
    EB --> EB4[Übung: Last- und Performance Tests]
    EB --> EB5[Übung: Sicherheitstests]
    EB --> EB6[Übung: Linter]

    A -->|enthält| F[Testdatenmanagement]
    F --> FA[Übung: Statischer TF]
    FA -.-> FB[Übung: Generischer TF]

    A -->|enthält| G[Übung: Testabdeckung]

    style B fill:#9BCD9B
    style B color:Black
    style BA fill:#9BCD9B
    style BA color:Black
    style BB fill:#9BCD9B
    style BB color:Black
    style BC fill:#9BCD9B
    style BC color:Black

    style CA1 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style CB1 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5 
    style CB2 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5 
    style CB stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5 
    style DA stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style DB stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA1 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA2 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA3 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA4 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA5 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA6 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA7 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EA8 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EB1 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EB2 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EB3 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EB4 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EB5 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style EB6 stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style FA stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5
    style G stroke:#ff6347,stroke-width:2px,stroke-dasharray:5,5

    style CA2 stroke:#00FFFF,stroke-width:2px,stroke-dasharray:5,5
    style FB stroke:#00FFFF,stroke-width:2px,stroke-dasharray:5,5

    style CA3 stroke:#AAAA55,stroke-width:2px,stroke-dasharray:5,5
```
