title: Linting mit black
stage: draft
timevalue: 0
difficulty: 2
explains: Linter
assumes: venv, flake8
---

TODO_1_ruhe:

Ich stelle mir (gegeben die Aufgaben PEP8 und flake8) den Rest so vor:  
Aufgabe black:

- Die gleichen Dateien wieder benutzen wie bei flake8, aber nochmal die Fassung auschecken,
  die vor flake8 vorlag.
- black drüberlaufen lassen und gucken, a) ob was Wichtiges am Format kaputt gegangen ist (Kommentare)
  und b) wo mir das Resultat zusagt (gut oder akzeptabel) und wo vielleicht nicht
- flake8 auf das Ergebnis laufen lassen. Das sollte doch jetzt still sein? Ist es nicht!
- Verstehen, woher die Abweichungen kommen (nämlich: a) flake8-Meldungen, die gar nicht auf das
  Format abheben, das black verändert; b) flake8-Meldungen, wo ein anderes Format erwartet wird
  als die Defaults von black vorsehen).
- black-Einstellungen so vornehmen, dass die Meldungen aus Kategorie b) verschwinden.
- Reflektieren, wie mir selektives manuelles Korrigieren gefällt (wie in der flake8-Aufgabe) im Vergleich zum
  totalen automatischen Korrigieren durch black.

Aufgabe Lint-PyCharm:

- Die gleichen Dateien wieder benutzen wie bei flake8, aber nochmal die Fassung auschecken,
  die vor flake8 vorlag.
- Die immer vorhandenen Linter-Meldungen in PyCharm erkunden: oben rechts im Editorfenster anklicken.
- Die Leute in der JetBrains-Doku herausfinden lassen, was das alles enthält
  (bei Python mindestens die Ausgaben von flake8 und vom pypy-Typchecker; Querverweis (ohne assumes)
  zur noch nicht existenten Aufgabe über Typdeklarationen machen, die Herr Alrwasheda in Python2 anlegen sollte)
- Für mindestens eine Datei alle Meldungen bearbeiten und lösen
- EQ: Reflektieren, wie mir das im Vergleich zum manuellen Aufruf von flake8 gefällt? Warum? (vermutlich sehr
  viel besser, denn es ist recht komfortabel).
- Diese Anzeige für die flake8-Meldungen so konfigurieren wie in der Aufgabe flake8
  und dann noch darüber hinaus so, dass nur noch Meldungen erscheinen, die ich auch lösenswert finde.
- EQ: Wenn ich die nun gelöschten Meldungen mittels nur 2-4 Kategorien beschreiben möchte,
  welche Kategorien wären das dann. Mit anderen Worten: Was sind meine Kriterien dafür, welche
  Meldungen ich haben will und welche nicht? Warum?
- Jetzt auch noch die black-Formatierung in PyCharm einschalten.
- Nochmal die Fassung der benutzten Python-Quellen auschecken,
  die vor flake8 vorlag. black anwenden. Jetzt wieder die Meldungen anschauen.
  Vermutlich weniger als eben?
- EQ: Da ich nun die bequemsten technischen Mittel dafür kenne:
  Wie gründlich möchte ich meinen Code bezüglich PEP8 säubern?
  Falls nicht komplett: Warum nicht?
  Will ich dafür black nutzen oder es lieber manuell machen? Warum?
  (Z.B.: Falls ich den Anspruch habe, es gleich richtig einzutippen, liefert eine manuelle Korrektur
  wünschenswerte Rückmeldung darüber, wie gut das klappt.)

Aufgabe flake8_SUT:

- Ergibt die jetzt noch Sinn? Vermutlich streichen?


[SECTION::goal::trial]

- Ich kann black auf einen Python Code ausführen
- Ich kann black konfigurieren, um nach meinem Bedarf die Codeformatierung vorzunehmen

[ENDSECTION]
[SECTION::background::default]

Black ist ein leistungsstarker Python-Codeformatter, der entwickelt wurde, um die manuelle
Formatierung von Python-Code überflüssig zu machen. Anders als traditionelle Linter wie
[PARTREF::flake8], die nur Stilrichtlinien überprüfen, formatiert Black den Code automatisch gemäß
einem festgelegten Satz von Regeln. Dies führt zu einem konsistenten und einheitlichen Codestil im
gesamten Projekt.

[ENDSECTION]
[SECTION::instructions::loose]

### Black Überblick

Machen Sie sich mit der offiziellen Dokumentation von [black](https://black.readthedocs.io/en/stable/)
vertraut und beantworten Sie die folgenden Fragen.

- [EQ] Was ist black und wofür wird es in der Python-Entwicklung verwendet?
- [EQ] Steht black in Verbindung zu [TERMREF::PEP 8]?
- [EQ] Welche Formatierungen kann black am Code vornehmen?
- [EQ] Welche Funktionen bietet black zur Verbesserung der Codequalität und -lesbarkeit?
- [EQ] Welche Ressourcen stehen zur Verfügung, um black zu erlernen und effektiv einzusetzen,
  wie z.B. Dokumentation, Tutorials oder Beispiele?
- [EQ] Gehört black zu den aktiven oder passiven Lintern?

### Black installieren

- [ER] Installieren Sie black in einer neuen Virtuellen Umgebung.

### Black verwenden

Im Folgenden ist ein Codeabschnitt gegeben. Kopieren Sie diesen Teil in eine Datei und verwenden Sie
black, um diesen Code zu analysieren.

```Python
import math,sys

def func(  x ) :
    print( "foo" ,x ) 

def calculate_circle_area (radius ) :
    area = math.pi*radius**2
    return area 

def print_circle_info (radius ) :
    area = calculate_circle_area(radius)
    print("Kreis mit Radius:",radius)
print("Fläche:",area)


if __name__ == "__main__" :
    print_circle_info(5)
```

- [ER] Verbessern Sie den gegebenen Code mit black.
- [EQ] Welche Verbesserungen werden auf welcher Zeile durchgeführt?
- [EQ] Angenommen, Sie wollen eine projektdefinierte Zeilenlänge von 120 Zeichen festsetzen. Wie
  definieren Sie das mit black?

### Reflexion

- [EQ] Können Sie sich vorstellen, diesen Codeverbesserer in einem Projekt einzusetzen?
  Diskutieren Sie Ihre Antwort.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]
