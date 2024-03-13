title: Linting mit black
stage: alpha
timevalue: 1.0
difficulty: 2
profiles: TEST
explains: Linter
assumes: venv, flake8
---

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
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
[ENDSECTION]
