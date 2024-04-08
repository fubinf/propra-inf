title: random - Pseudo-Zufallsgenerator
stage: beta
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::trial]

Ich weiß, wie man zufällige Zahlen generieren oder zufällige Elemente aus einer Menge wählen kann.  

[ENDSECTION]
[SECTION::background::default]

Manche Algorithmen basieren auf zufälligen Eingaben (randomisierte Algorithmen). Aber auch für die Simulation oder die
Generierung von Eingaben zu Testzwecke sind Zufallsgeneratoren nützlich.
[`random`](https://docs.python.org/3/library/random.html#recipes) bietet einen Zufallsgenerator, der für die Generierung
zufälliger Floats, Integer oder die Wahl von Elementen aus Sequenzen verwendet werden kann.

`random` implementiert einen sogenannten Pseudo-Zufallsgenerator (PRNG). Diese basieren auf deterministischen, und damit
vorhersehbaren Algorithmen. Für viele Anwendungsfälle ist das wünschenswert.
In der Kryptografie und anderen sicherheitskritischen Anwendungen kann Vorhersehbarkeit aber 
ein Sicherheitsrisiko darstellen.
Andere Bibliotheken (z.B. [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets)) greifen auf echte
Zufallsgeneratoren (TRNG) zurück, für die dedizierte Hardware notwendig ist.

Bei Interesse lesen Sie eine [Einführung in das Thema Zufallsgeneratoren](https://www.random.org/randomness/) 

[ENDSECTION]
[SECTION::instructions::detailed]

- [ER] Legen Sie die Datei `m_random.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.

### Seed für Random festlegen

Ein Seed ist der "Startwert", mit dem der Zufallsgenerator anfängt, Zahlen zu generieren. 
Dadurch, dass wir einen Seed festlegen, erhalten wir beim Ausführen des gleichen Codes 
immer die gleichen Zufallszahlen und das Ergebnis wird reproduzierbar.  

Wenn Sie keinen Seed angegeben, wird eine echte Zufallsvariable oder ein Timestamp
als Seed verwendet. 
Sie erhalten also bei jeder Ausführung neue Zufallszahlen, was oft erwünscht ist.

- [ER] Importieren Sie das Modul [`random`](https://docs.python.org/3/library/random.html) 
  und legen Sie als Seed `propra` fest.

### Zufallszahlen erzeugen

- [ER] Erzeugen Sie mithilfe von `random` eine Gleitkommazahl im Bereich von -10 bis 10. 
  Geben Sie das Ergebnis mit `print("[-10,10]:\t", ...)` aus.
- [ER] Erzeugen Sie eine 4-elementige Liste von zufälligen ganzen Zahlen im Bereich von -1000 bis 1000. 
  Geben Sie das Ergebnis mit `print("-1000..1000:\t", ...)` aus.
- [ER] Erzeugen Sie eine Liste von 5 normalverteilten Gleitkommazahlen mit 
  Erwartungswert 10 und Standardabweichung 3. 
  Geben Sie das Ergebnis mit `print("normalverteilt:\t", ...)` aus.

### Auswahl aus Sequenzen

- [ER] Ordnen Sie ihre zuvor erzeugte Liste in einer zufälligen Reihenfolge. Geben Sie das Ergebnis mit
  `print("permutiert:\t", ...)` aus.
- [ER] Wählen Sie aus dieser Liste zufällig 2 verschiedene Elemente. 
  Geben Sie das Ergebnis mit `print("davon 2:\t", ...)` aus.
- [ER] Schreiben Sie eine Funktion `throw_dice()`, die k Würfe eines n-seitigen, gleichverteilten "Würfels" simuliert.
  Als Ergebnis soll eine Liste mit den geworfenen Zahlen zurückgegeben werden. 
  Verwenden Sie **keine** Schleife, sondern eine geeignete Funktion aus `random`.  
- [ER] Simulieren Sie mit ihrer Funktion 10 Mal den Wurf eines 6-seitigen Würfels. 
  Geben Sie das Ergebnis mit `print("Würfeln:\t", ...)` aus.

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_random.py` einmal aus.

[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell grob auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `random` machen.

[ENDINSTRUCTOR]
