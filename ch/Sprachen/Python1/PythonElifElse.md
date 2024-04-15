title: "Weitere Teile der Fallunterscheidung in Python"
stage: alpha
timevalue: 0.75
difficulty: 2
assumes: PythonStrings, PythonIntegers, PythonBooleans, PythonComments
requires: PythonIf
---

[SECTION::goal::idea]

- Ich habe ein klares Verständnis dafür,
wie Fallunterscheidungsprobleme in Python modelliert werden können.  
- Ich verstehe, wie ich mit einer `if`-`elif`-`else`-Struktur in Python umgehe. 

[ENDSECTION]

[SECTION::background::default]

In [PARTREF::PythonIf] haben Sie bedingte Anweisungen kennengelernt, 
mit denen Sie boolesche Ausdrücke untersuchen können, 
um anhand der Ergebnisse den Ablauf eines Programms zu steuern.

Das Schlüsselwort `if` kümmert sich also in einer Fallunterscheidung um den Teil *"Wenn"*. 
Die Schlüsselwörter `elif` (kurz für "else if") und `else` in Python ermöglichen als Ergänzung
für `if` die Definition von *"sonst wenn"*- und *"sonst"*-Teilen einer Fallunterscheidung.

Damit haben wir die Möglichkeit, in unseren Programmen unterschiedliche Fälle zu behandeln und
entsprechende Aktionen basierend auf den Bedingungen durchzuführen.

[ENDSECTION]

[SECTION::instructions::detailed]

### "Sonst, wenn..": `elif (else if)`

Ganz einfach wird das Schlüsselwort `elif` verwendet, 
um zusätzliche Bedingungen innerhalb einer `if`-Struktur zu prüfen. 
Dabei ist zu beachten, dass eine `elif`-Anweisung nur ausgeführt wird, 
wenn die Bedingung der vorherigen bedingten Anweisung als falsch (`False`) ausgewertet wurde. 
Eine beliebige Anzahl von `elif`-Anweisungen kann nach der `if`-Anweisung folgen. 
Die Ausführung in der `if`-`elif`-Struktur endet, 
sobald eine der Bedingungen als wahr (`True`) ausgewertet wird und 
der zugehörige Codeblock ausgeführt wird.

**Beispiel:**

```python
    x = 10
    # wird geprüft aber nicht ausgeführt, weil der Wert von x kleiner als 20 ist
    if x > 20:
        print('Bedingung von if ist wahr')
    # wird geprüft als nächste Bedingung aber nicht ausgeführt, weil der Wert von x größer als 9 ist
    elif x < 9: 
        print('Bedingung der ersten elif-Anweisung ist wahr')
    # wird geprüft und ausgeführt, weil der Wert von x größer als 5 ist 
    elif x > 5:
        print('Bedingung der zweiten elif-Anweisung ist wahr')
    # wird komplett ignoriert, weil die Bedingung der vorherigen elif-Anweisung bereits wahr war
    elif x == 10: 
        print('Bedingung der dritten elif-Anweisung ist wahr')
```

### "Sonst..": `else`

Das Schlüsselwort `else` wird verwendet, um einen Codeblock auszuführen, 
wenn keine der Bedingungen in der `if`-`elif`-Struktur als wahr ausgewertet wird. 
Es wird immer nach allen `if`- und `elif`-Anweisungen (falls welche existieren) platziert und 
kann optional sein. Wenn also keine der Bedingungen wahr ist, 
wird der Codeblock unter `else` ausgeführt. 
Beachten Sie, dass es nur einen else-Block pro `if`-`elif`-Struktur geben darf.

**Beispiel:**

```python
    x = 10
    # wird geprüft aber nicht ausgeführt, weil der Wert von x kleiner als 20 ist
    if x > 20:
        print('Bedingung von if ist wahr')
    # wird geprüft als nächste Bedingung aber nicht ausgeführt, weil der Wert von x größer als 9 ist
    elif x < 9:
        print('Bedingung der elif-Anweisung ist wahr')
    # Der Inhalt von else-Anweisung benötigt keine Bedingung und wird einfach ausgeführt,
    # falls keine der if-elif-Bedingungen wahr ist
    else:
        print('wird einfach ausgeführt, weil KEINE der oberen Bedingungen True war')
```

[NOTICE]

`elif`- und `else`-Anweisungen sind optional, Sie können also verwendet werden, 
wenn Bedarf besteht. Das hängt immer damit zusammen, 
welche bzw. wie viele Bedingungen Sie überprüfen möchten.

[ENDNOTICE]

---

### Verschachtelungen:

Verschachtelte `if`-`elif`-`else`-Strukturen ermöglichen, 
Bedingungen innerhalb **anderer** Bedingungen zu prüfen, 
was die Erstellung von komplexeren Entscheidungsstrukturen und 
somit vertiefte Untersuchung der betroffenen Daten ermöglicht.

**Beispiel:**

```python
    x = 20
    if x > 35:
        print("x ist größer als 35")
    elif x > 15:
        print("x ist größer als 15, aber nicht größer als 35")
        if x == 20:
            print("x ist gleich 20")
        else:
            print("x ist ungleich 20")
    else:
        print("x ist nicht größer als 15")
```

---

### Übungen:

[ER] Angenommen, ein Student hat die Note 76 in einer der Klausuren erhalten. 
Geben Sie die entsprechende Bewertung ('A', 'B', 'C', 'D' und 'F') basierend auf der Note aus.

- A: Notenbereich von 90 bis 100   
- B: Notenbereich von 80 bis 89  
- C: Notenbereich von 70 bis 79  
- D: Notenbereich von 50 bis 69  
- F: Notenbereich unter 50

[ER] Angenommen, Sie planen einen Ausflug und müssen entscheiden, welche Kleidung Sie tragen möchten. 
Schreiben Sie ein Python-Programm und erstellen Sie eine geeignete Variable für die Temperatur. 
Basierend auf dieser Variable sollte das Programm eine Empfehlung für die passende Kleidung ausgeben. 
Verwenden Sie die folgenden Empfehlungen:

- Ausgabe bei Temperaturen über 25°C:
`"Tragen Sie leichte Kleidung wie T-Shirts und Shorts."`  
- Ausgabe bei Temperaturen zwischen 15°C und 25°C (inklusive):
`"Tragen Sie eine leichte Jacke oder Pullover."`  
- Ausgabe bei Temperaturen unter 15°C:
`"Tragen Sie warme Kleidung wie einen Mantel oder eine dicke Jacke."`  

[ER] Verschachtelte Strukturen können die Lesbarkeit eines Codes beeinträchtigen, 
insbesondere wenn sie übermäßig verwendet werden. 
Recherchieren Sie nach einigen Auswirkungen von Verschachtelungen auf die Lesbarkeit. 
Schreiben Sie Ihre Antwort als Kommentar in Ihrer Python-Datei, die Sie abgeben werden. 

[ER] Versuchen Sie, diese verschachtelte Struktur zu optimieren. 
Sie können dafür überflüssige Bedingungen entfernen und logische Operatoren verwenden, 
die Sie in [PARTREF::PythonBooleans] kennengelernt haben.
 
```python
    x = 10
    if x > 5:
        if x < 15:
            if x <= 11 
                if x == 10:
                    print("x ist gleich 10")
                else:
                    print("x ist nicht gleich 10")
    else:
        print("x ist nicht größer als 5")
``` 

[ENDSECTION]

[SECTION::submission::program]

Bearbeiten Sie die Anforderungen [EREFR::1], [EREFR::2]... 
Erstellen Sie dafür eine geeignete Python-Datei `python_elif_else_abgabe.py` und
geben Sie dann diese Datei ab.

[ENDSECTION]

[INSTRUCTOR::Konzept der Fallunterscheidung]

In den abgegebenen Python-Dateien kann überprüft werden:    
- ob, der Student die Unterschiede zwischen `if`, `elif` und `else` verstanden hat und 
wie diese Anweisungen in Python geschrieben werden können.  
- dass, der Student ein Fallunterscheidungsproblem mithilfe von `if`, `elif` und 
`else` in Python modellieren kann.

[ENDINSTRUCTOR]
