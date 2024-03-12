title: Linting mit flake8
stage: alpha
timevalue: 1.5
difficulty: 2
profiles: TEST
explains: Linter
assumes: venv
---

[SECTION::goal::trial]

- Ich kann flake8 auf einen Python Code ausführen
- Ich kann flake8 konfigurieren, um gefundene Meldungen auszublenden

[ENDSECTION]
[SECTION::background::default]

In der Softwareentwicklung ist es wichtig, [TERMREF::Linter]-Werkzeuge einzusetzen, um eine hohe
**Codequalität** zu gewährleisten. Durch die kontinuierliche Überprüfung auf **Syntaxfehler** und
potenzielle Fehler hilft flake8 Entwicklern, Probleme frühzeitig im Entwicklungsprozess zu erkennen
und zu beheben, was letztendlich zu **stabileren** und zuverlässigeren Anwendungen führt.
zusätzlich trägt die Einhaltung von **Coding-Standards**, die flake8 ermöglicht, zur Schaffung von
konsistent formatiertem Code bei, was die **Lesbarkeit** erhöht und die **Wartbarkeit** erleichtert.

Diese erwähnten Eigenschaften sind für ein Softwareprojekt wichtig, weshalb flake8 in einem Python
Projekt eine gute Möglichkeit bietet, diese Ziele zu erreichen.

[ENDSECTION]
[SECTION::instructions::loose]

### Flake8 Überblick

Machen Sie sich mit der offiziellen Dokumentation von [flake8](https://flake8.pycqa.org/en/latest/)
vertraut und beantworten Sie die folgenden Fragen.

- [EQ] Was ist flake8 und wofür wird es in der Python-Entwicklung verwendet?
- [EQ] Steht flake8 in Verbindung zu [TERMREF::PEP 8]?
- [EQ] Welche Funktionen bietet flake8 zur Verbesserung der Codequalität und -lesbarkeit?
- [EQ] Warum ist es wichtig, Syntaxfehler und Stilprobleme im Code frühzeitig zu erkennen?
- [EQ] Wie kann flake8 in den Entwicklungsworkflow integriert werden, um den Linting-Prozess zu
  automatisieren?
- [EQ] Welche Vorteile bietet die Einhaltung von Coding-Standards, die durch flake8 unterstützt
  werden?
- [EQ] Welche Ressourcen stehen zur Verfügung, um flake8 zu erlernen und effektiv einzusetzen,
  wie z.B. Dokumentation, Tutorials oder Beispiele?
- [EQ] Wofür steht der Fehlercode F401 in flake8?

### Flake8 installieren

- [ER] Installieren Sie flake8 in einer neuen Virtuellen Umgebung.

### Flake8 verwenden

Im Folgenden ist ein Codeabschnitt gegeben. Kopieren Sie diesen Teil in eine Datei und verwenden Sie
flake8, um diesen Code zu analysieren.

```Python
def main():
    print("Hallo Welt")
    x=5   

    if x == 5:
        print("x ist gleich 5")
    else:
        print("x ist nicht gleich 5")
    
    for i in range(5):
        print(i)
    print(i)

    print("Dies ist eine lange Zeile, die die maximale Zeilenlänge von 79 Zeichen in PEP 8 überschreitet. Dies sollte vermieden werden, um die Lesbarkeit des Codes zu verbessern.")

if __name__ == "__main__":
    main()
```

- [ER] Analysieren Sie den gegebenen Code mit flake8.
- [EQ] Welche Fehler werden zu welcher Zeile ausgegeben?
- [ER] Korrigieren Sie den Code so, dass keine Fehlermeldungen ausgegeben werden.
- [EQ] Angenommen, Sie wollen / können den Code nicht anpassen. Wie können Sie diese Fehlermeldungen
  unterdrücken? (Beschreiben Sie zwei Wege)
- [ER] Verwenden Sie den gegebenen Code und **konfigurieren** Sie flake8 so, dass keine
  Fehlermeldung ausgegeben wird.

### Reflexion

- [EQ] Können Sie sich vorstellen, diesen Linter in einem Projekt einzusetzen? Diskutieren Sie Ihre
  Antwort.
- [EQ] Gibt es aus Ihrer Sicht Fehlercodes, die weniger kritisch zu betrachten sind und in Projekten
  gegebenenfalls aus-konfiguriert werden können? Diskutieren Sie.


[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
