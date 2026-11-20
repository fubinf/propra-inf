title: SciPy Grundlagen verstehen und anwenden
stage: beta
timevalue: 0.5
difficulty: 2
assumes: np-Einführung, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann SciPy installieren und die Installation überprüfen.
- Ich kann ausgewählte SciPy-Module dieser Aufgabengruppe ihren Anwendungsbereichen zuordnen.
- Ich kann mit `scipy.constants` mathematische und physikalische Konstanten abrufen und die beiden
  Zugriffswege des Moduls unterscheiden.
[ENDSECTION]


[SECTION::background::default]
SciPys Funktionsumfang ist auf spezialisierte Module verteilt, von denen jedes ein eigenes
Anwendungsgebiet abdeckt.
Wer ein Problem mit SciPy lösen will, muss deshalb zuerst entscheiden, in welches Modul es gehört;
erst danach lohnt es sich, dort nach einer passenden Funktion zu suchen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorwissen

Für [EREFQ::1] nötiges Vorwissen, falls es fehlt:

- [Integralrechnung (Wikipedia)](https://de.wikipedia.org/wiki/Integralrechnung):
  Bedeutung des bestimmten Integrals
- [Gewöhnliche Differentialgleichung (Wikipedia)](https://de.wikipedia.org/wiki/Gew%C3%B6hnliche_Differentialgleichung):
  Begriff und Anfangswertproblem
- [Nullstelle (Wikipedia)](https://de.wikipedia.org/wiki/Nullstelle):
  Begriff der Nullstelle einer Funktion
- [Methode der kleinsten Quadrate (Wikipedia)](https://de.wikipedia.org/wiki/Methode_der_kleinsten_Quadrate):
  Grundidee der Ausgleichsrechnung


### SciPy installieren

[EC] Installieren Sie SciPy mit `pip`:

```bash
pip install "scipy==1.18.*"
```
<!-- TODO_3: ggf. ändern und Aufgaben anpassen -->

Die Versionsangabe legt die Minor-Version fest, auf die alle Aufgaben dieser Gruppe abgestimmt
sind.

[EC] Überprüfen Sie, welche SciPy-Version Sie tatsächlich benutzen:

```bash
python -c "import scipy; print(scipy.__version__)"
```

<!-- time estimate: 5 min -->


### SciPy-Module: Überblick und Anwendungsbereiche

Die folgende Auswahl umfasst nur die Module dieser Aufgabengruppe; die vollständige Liste steht
in der
[SciPy API Reference](https://docs.scipy.org/doc/scipy/reference/index.html):

- `scipy.optimize`: Optimierung (vertieft in [PARTREF::sp-optimize])
- `scipy.integrate`: Numerische Integration (vertieft in [PARTREF::sp-integrate])
- `scipy.linalg`: Erweiterte lineare Algebra (vertieft in [PARTREF::sp-linalg])
- `scipy.stats`: Statistische Funktionen und Verteilungen (vertieft in [PARTREF::sp-stats])
- `scipy.interpolate`: Interpolation zwischen Stützstellen (vertieft in [PARTREF::sp-interpolate])
- `scipy.sparse`: Operationen auf dünnbesetzten (sparse) Matrizen (vertieft in [PARTREF::sp-sparse])
- `scipy.constants`: Mathematische und physikalische Konstanten (Thema dieser Aufgabe)

[EQ] Welches SciPy-Modul würden Sie für folgende Problemstellungen verwenden?
Begründen Sie Ihre Auswahl:

- Berechnung des zurückgelegten Wegs aus einer gemessenen Geschwindigkeitskurve
- Finden einer Nullstelle einer Funktion
- Lösen einer gewöhnlichen Differentialgleichung
- Anpassung einer Modellfunktion an eine Messreihe

Die Liste oben nennt für jedes Modul nur sein Hauptgebiet; was ein Modul darüber hinaus abdeckt,
zeigt die Überschrift seiner Seite in der SciPy API Reference.

<!-- time estimate: 10 min -->


### Mathematische und physikalische Konstanten mit `scipy.constants`

`scipy.constants` stellt wenige mathematische und viele physikalische Konstanten bereit.
Der Nutzen liegt dabei weniger bei `pi`, das es auch in `math` gibt, als bei den physikalischen
Konstanten.

```python
from scipy import constants

print(constants.pi)      # 3.141592653589793 (Kreiszahl π)
print(constants.golden)  # 1.618033988749895 (Goldener Schnitt)
print(constants.g)       # 9.80665 (Normfallbeschleunigung in m/s²)
```

Außerdem enthält `scipy.constants` das Dictionary `physical_constants`, dessen Einträge jeweils ein
Tripel (ein Tupel mit drei Elementen) aus Wert, Einheit und Unsicherheit sind.
Die Unsicherheit gibt an, wie genau der Wert bekannt ist.
Werte, Einheiten und Unsicherheiten stammen aus den
[CODATA-Konstanten beim NIST](https://physics.nist.gov/cuu/Constants/).
Ein Eintrag wird so ausgelesen:

```python
from scipy import constants

value, unit, uncertainty = constants.physical_constants['speed of light in vacuum']
print(f"Wert: {value} {unit} (Unsicherheit: {uncertainty})")
```

[ER] Geben Sie auf diese Weise Wert, Einheit und Unsicherheit für diese drei Konstanten aus:
`'Boltzmann constant'`, die Elektronenmasse und `'Newtonian constant of gravitation'`.
Den genauen Schlüssel der Elektronenmasse ermitteln Sie im Programm mit
[`constants.find()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.constants.find.html),
das alle Schlüssel liefert, die eine gegebene Zeichenkette enthalten; geben Sie die Treffer aus und
wählen Sie den passenden aus.
Geben Sie danach in einer weiteren Zeile das Modulattribut `constants.Boltzmann` und den Wert aus
dem Tripel von `'Boltzmann constant'` direkt nebeneinander aus.

[EQ] Nennen Sie zwei technische Gründe, warum `scipy.constants` sowohl Modulattribute als auch
das Dictionary `physical_constants` anbietet.
Ziehen Sie dafür Ihre eigene Ausgabe aus [EREFR::1] heran: die beiden nebeneinander
ausgegebenen Zahlen, die drei Unsicherheiten und die ausgeschriebenen Schlüsselnamen.
Man könnte erwarten, dass ein Eintrag ohne echte Messunsicherheit nur aus Wert und Einheit
besteht.
Erklären Sie, warum das Tripel trotzdem für alle Einträge dieselbe Form hat.

<!-- time estimate: 15 min -->
[ENDSECTION]


[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]

### Kommandoprotokoll
[PROT::ALT:sp-Einführung.prot]


### Fragen und Python-Dateien
[INCLUDE::ALT:sp-Einführung.md]
[ENDINSTRUCTOR]
