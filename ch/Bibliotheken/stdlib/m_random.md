title: random - Pseudo-Zufallsgenerator
stage: alpha
timevalue: 1
difficulty: 2
profiles:
explains:
assumes:
requires:
---

[SECTION::goal::trial]

Ich weiß, wie man zufällige Zahlen generieren oder zufällige Elemente aus einer Menge wählen kann.  

[ENDSECTION]

[SECTION::background::default]

Manche Algorithmen basieren auf zufälligen Eingaben (randomisierte Algorithmen). Aber auch für die Simulation oder die
Generierung von Eingaben zu Testzwecke sind Zufallsgeneratoren nützlich.
[`random`](https://docs.python.org/3/library/random.html#recipes) bietet einen Zufallsgenerator, der für die Generierung
zufälliger Floats, Integer oder die Wahl von Elementen aus Sequenzen verwendet werden kann.

[WARNING]
`random` implementiert einen sogenannten Pseudo-Zufallsgenerator (PRNG). Diese basieren auf deterministischen, und damit
vorhersehbaren Algorithmen. Für viele Anwendungsfälle ist das ausreichend.

In der Kryptografie und anderen sicherheitskritischen Anwendungen können PRNGs aber ein Sicherheitsrisiko darstellen.
Andere Bibliotheken (z.B. [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets)) greifen auf echte
Zufallsgeneratoren (TRNG) zurück, für die dedizierte Hardware notwendig ist.

Hier finden Sie eine [Einführung in das Thema Zufallsgeneratoren](https://www.random.org/randomness/) 
[ENDWARNING]

[ENDSECTION]

[SECTION::instructions::detailed]

- Legen Sie die Datei `m_random.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. Fügen Sie ihre Python
  Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.

### Seed für Random festlegen

Ein Seed ist der "Startwert", mit dem der Zufallsgenerator anfängt, Zahlen zu generieren. Dadurch, dass
wir einen Seed festlegen, erhalten wir beim Ausführen des gleichen Codes immer die gleichen Zufallszahlen. Dadurch wird
das Ergebnis dieser Aufgabe reproduzierbar (und damit leichter zu kontrollieren).  
Wenn Sie keinen Seed angegeben, wird, abhängig vom verwendeten System, eine echte Zufallsvariable oder ein Timestamp
als Seed verwendet. Bei erneuter Ausführung des gleichen Codes erhalten Sie dann auch immer neue Zufallszahlen, was in
vielen Fällen eher das gewünschte Ziel ist.

- Importieren Sie das Modul [`random`](https://docs.python.org/3/library/random.html#recipes) und legen Sie als Seed
  `propra` fest.

### Generierung von Zufallszahlen

- Generieren Sie mithilfe von `random` eine Gleitkommazahl im Bereich von -10 bis 10. Geben Sie das Ergebnis mit
  `print(...)  # Antwort 1` aus.
- Generieren Sie eine 10-elementige Liste von zufälligen ganzen Zahlen im Bereich von -1000 bis 1000. Geben Sie das
  Ergebnis mit `print(...)  # Antwort 2` aus.
- Anstatt gleichverteilte Zufallszahlen zu erhalten, können auch andere vordefinierte Wahrscheinlichkeitsverteilungen
  für die Generierung verwendet werden.  
  Generieren Sie eine Liste von 10 Gleitkommazahlen. Dabei sollen die Zahlen normalverteilt gewählt werden mit einem
  Erwartungswert von 10 und einer Standardabweichung von 5. Geben Sie das Ergebnis mit `print(...)  # Antwort 3` aus.

### Zufälle aus Sequenzen

- Ordnen Sie ihre zuvor erzeugte Liste in einer zufälligen Reihenfolge. Geben Sie das Ergebnis mit
  `print(...)  # Antwort 4` aus.
- Wählen Sie aus dieser Liste zufällig 5 verschiedene Elemente. Geben Sie das Ergebnis mit `print(...)  # Antwort 5` aus.
- Schreiben Sie eine Funktion `throw_dice()`, die k Würfe eines n-seitigen Würfels simuliert. Als Ergebnis soll eine
  Liste mit den geworfenen Zahlen zurückgegeben werden. Verwenden Sie **keine** Schleifen, sondern eine geeignete
  Funktion aus `random`.  
  Simulieren Sie mit ihrer Funktion 10 Mal den Wurf eines 6-seitigen Würfels. Geben Sie das Ergebnis mit
  `print(...)  # Antwort 6` aus.

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_random.py` einmal aus.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `random` machen.

[ENDINSTRUCTOR]
