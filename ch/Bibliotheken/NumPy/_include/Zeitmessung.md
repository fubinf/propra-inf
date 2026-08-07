
Um die Laufzeit einer Operation zu messen, bietet Pythons Standardbibliothek das `time`-Modul:
`time.perf_counter()` gibt einen Zeitpunkt in Sekunden zurück, die Differenz zweier Aufrufe ergibt
also die Laufzeit dazwischen.
Eine einzelne Messung schwankt stark, je nachdem was der Rechner sonst gerade tut; deshalb misst man
mehrfach und nimmt die kürzeste Zeit, denn sie ist am wenigsten gestört.
Vergleicht man mehrere Operationen miteinander, misst man sie in derselben Schleife, jede mit ihrer
eigenen Zeitenliste; so treffen Schwankungen der Maschine alle Messungen gleichmäßig.
Mit der in [PARTREF::py-Fstrings] eingeführten f-String-Formatierung mit Präzisionsangabe (`:.5f`)
lässt sich die Ausgabe auf sinnvolle Nachkommastellen begrenzen:

```python
import time

zeiten_a = []
zeiten_b = []
for lauf in range(5):
    start = time.perf_counter()
    # ... erste Operation ...
    zeiten_a.append(time.perf_counter() - start)

    start = time.perf_counter()
    # ... zweite Operation ...
    zeiten_b.append(time.perf_counter() - start)
dauer_a = min(zeiten_a)
dauer_b = min(zeiten_b)
print(f'Kürzeste Dauer der ersten Operation: {dauer_a:.5f} Sekunden')
print(f'Kürzeste Dauer der zweiten Operation: {dauer_b:.5f} Sekunden')
```

Für jede weitere Operation kommt eine weitere Zeitenliste hinzu.
