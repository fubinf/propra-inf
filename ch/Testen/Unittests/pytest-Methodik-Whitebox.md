title: Whitebox-Testing - Testmethodik und Anwendung mit pytest
stage: alpha
timevalue: 1.0
difficulty: 3
assumes: m_pytest, pytest-Methodik-Blackbox
---

[SECTION::goal::idea]

Ich verstehe die Idee von Whitebox-Testing.

Ich kann Whitebox-Tests mit pytest schreiben.
Ich erkenne die Unterschiede zwischen strukturellen Testkriterien (Statement, Condition, Branch, Path).

[ENDSECTION]
[SECTION::background::default]

Blackbox-Testing testet nur die sichtbaren Eingaben und Ausgaben – dabei übersieht man leicht
interne Logik, Sonderfälle oder seltene Zweige.
Whitebox-Testing hilft, diese verborgenen Aspekte gezielt zu prüfen und sorgt für eine höhere
Testabdeckung.
Besonders nützlich ist Whitebox-Testing, wenn keine vollständige Spezifikation vorliegt:
Die Analyse des Codes selbst zeigt, welche zusätzlichen Tests sinnvoll oder notwendig sind.

[ENDSECTION]

[SECTION::instructions::detailed]

### Einführung in die Whitebox-Testmethodik

Whitebox-Tests – auch strukturelle Tests genannt – analysieren die interne Logik und den Aufbau des
Codes.
Im Gegensatz dazu konzentrieren sich Blackbox-Tests ausschließlich auf die Eingaben und Ausgaben
eines Systems, ohne Kenntnis der zugrunde liegenden Implementierung.
Während Blackbox-Testmethoden wie Äquivalenzklassen- und Grenzwertanalyse ein Mindestmaß an
sinnvollen Testfällen definieren, bleibt der Raum möglicher weiterer Testfälle groß und potenziell
unbegrenzt.
Whitebox-Testing hingegen erlaubt es uns, anhand der sichtbaren Code-Struktur genau zu bestimmen,
was und wie viel wir testen müssen – z. B. durch Kriterien wie Anweisungs- oder Schleifenüberdeckung.

Whitebox-Tests sind besonders nützlich, um sicherzustellen, dass der Code aus Sicht des Entwicklers
_robust_ ist und keine ungetesteten Bereiche enthält.
Das Ganze basiert auf der Analyse möglicher 'Wege', 'Stationen' und Werte die im Laufe der
Codeausführung durchlaufen werden können.

Typische Whitebox-Testkriterien:

- **Anweisungsüberdeckung** (statement coverage, C₀): **Jede einzelne ausführbare Codezeile** wird mindestens einmal durchlaufen.
  
  *Beispiel:* 
  ```python
  def check_age(age):          # Zeile 1: Nicht ausführbar (nur Definition)
      if age >= 18:            # Zeile 2: Ausführbar (Bedingung wird geprüft)  
          return "adult"       # Zeile 3: Ausführbar (return-Statement)
      return "minor"           # Zeile 4: Ausführbar (return-Statement)
  ```
  **Ein** Test mit `age=20` erreicht bereits 100% Anweisungsüberdeckung (alle ausführbaren Zeilen durchlaufen).
- **Bedingungsüberdeckung** (condition coverage, C₁): **Jede atomare (unteilbare) Teilbedingung** wird sowohl True als auch False.
  
  **Wichtig - "atomar" bedeutet:** Bei `if age >= 18 and income > 30000:` gibt es **zwei** atomare Bedingungen:
  - `age >= 18` muss einmal True und einmal False werden  
  - `income > 30000` muss einmal True und einmal False werden
  
  **Vier** Tests nötig: `(age=20, income=40000)`, `(age=20, income=20000)`, `(age=16, income=40000)`, `(age=16, income=20000)`
  
  **Häufiger Fehler:** Die gesamte Bedingung `age >= 18 and income > 30000` als eine Einheit zu betrachten!
- **Zweigüberdeckung** (branch coverage): **Jeder mögliche Ausgang einer Entscheidung** wird mindestens einmal genommen.
  
  **Was ist ein "Zweig"?** Ein Zweig ist ein möglicher **Ausführungspfad** nach einer Entscheidung:
  ```python
  if condition:        # ← Entscheidung mit ZWEI Zweigen
      do_something()   # ← True-Zweig (expliziter Code)
  # impliziter else   # ← False-Zweig (auch ohne 'else'!)
  next_statement()
  ```
  
  **Wichtig:** Auch `if` ohne `else` hat **zwei** Zweige!
  - **True-Zweig:** Bedingung erfüllt → Code im if-Block wird ausgeführt
  - **False-Zweig:** Bedingung nicht erfüllt → if-Block wird übersprungen
  
  _Beispiel:_ Bei `if age >= 18:` gibt es **zwei** Ausgänge/Zweige:
  - **True-Zweig:** Code wird ausgeführt, wenn Bedingung erfüllt ist (`return "adult"`)
  - **False-Zweig:** Code wird ausgeführt, wenn Bedingung nicht erfüllt ist (`return "minor"`)
  
  **Zwei** Tests nötig: `age=20` (True-Zweig) und `age=16` (False-Zweig)
  
  **Unterschied zur Bedingungsüberdeckung:** Zweigüberdeckung fragt "Welche Wege werden genommen?", 
  Bedingungsüberdeckung fragt "Welche Teilbedingungen werden wahr/falsch?"
- **Schleifenüberdeckung** (loop coverage): **Alle wichtigen Iterationszustände** einer Schleife werden getestet.
  
  _Typische Testfälle:_ **Null** Durchläufe, **ein** Durchlauf, **mehrere** Durchläufe:
  ```python
  def sum_positive(numbers):
      total = 0
      for num in numbers:  # ← Diese Schleife testen
          if num > 0:
              total += num
      return total
  ```
  **Drei Tests für Schleifenüberdeckung:**
  - `sum_positive([])` → 0 Durchläufe (Edge Case)
  - `sum_positive([5])` → 1 Durchlauf (Normalfall minimal) 
  - `sum_positive([1, -2, 3, 4])` → 4 Durchläufe (Normalfall mehrfach)
  
  **Besonders wichtig:** Test mit **0 Durchläufen** deckt oft Initialisierungsdefekte auf!
- **Pfadüberdeckung** (path coverage): **Jede mögliche Kombination von Entscheidungen** durch den gesamten Code wird getestet.
  
  _Beispiel Verzweigungen:_ Bei zwei aufeinanderfolgenden if-Anweisungen entstehen **vier** verschiedene Pfade:
  ```python
  def example(a, b):
      if a > 0:     # Entscheidung 1: True oder False
          x = 1
      if b > 0:     # Entscheidung 2: True oder False  
          y = 1
      return x, y
  ```
  **Vier Pfade:** (True,True), (True,False), (False,True), (False,False) → **4 Tests** erforderlich.
  
  **Schleifen-Problematik:** Schleifen sind besonders **fehleranfällig** und erfordern spezielle Behandlung:
  ```python
  def process_items(items, threshold):
      count = 0
      for item in items:  # ← Schleife: Wie viele Durchläufe?
          if item > threshold:
              count += 1
      return count
  ```
  **Drei kritische Pfade für Schleifen:**
  - **0 Durchläufe:** `process_items([], 5)` → Leere Liste (Initialisierung testen)
  - **1 Durchlauf:** `process_items([3], 5)` → Minimaler Fall (Schleifenkörper einmal)  
  - **>1 Durchläufe:** `process_items([3, 7, 2, 8], 5)` → Typischer Fall (mehrfache Iteration)
  
  **Exponentielles Wachstum:** Bei n Entscheidungen entstehen 2ⁿ Pfade! 
  Bei Schleifen wird es noch extremer: Eine Schleife mit 0-10 Durchläufen = 11 Pfade.
  **Verschachtelte Schleifen** führen schnell zu hunderten möglichen Pfaden → Pfadüberdeckung wird unpraktikabel!
- **Datenflusskriterien**: Hierbei werden die möglichen Belegungen und Verwendungen von Variablen
  getestet (z.B. „def-use“-Paare). Das ist ein fortgeschrittenes Thema und für Einsteiger meist komplex
  - dennoch wagen wir einen kleinen Blick in das Thema.

[NOTICE]
Methoden geben vor, wie Sie beim Testen vorgehen sollen.
Kriterien für die Testqualität zeigen Ihnen, wie vollständig Ihre Tests sind.
Die Auswahl und das Ausdenken der konkreten Testfälle bleibt jedoch weiterhin Ihre Aufgabe –
auch wenn es dafür Hilfestellungen gibt.
[ENDNOTICE]

### Vorbereitung

Die folgenden Aufgaben basieren auf dem echten Open-Source-Projekt
[keon/algorithms](https://github.com/keon/algorithms), das über 24.000 Sterne hat und eine
umfassende Sammlung von Python-Algorithmus-Implementierungen enthält.
Die verwendeten Funktionen stammen konkret aus den Dateien `algorithms/search/binary_search.py` und
`algorithms/sort/cocktail_shaker_sort.py`.
Sie arbeiten mit realen Algorithmen, die in der Praxis verwendet werden – inklusive echter Defekte,
die durch systematische Whitebox-Testverfahren aufgedeckt werden können.

- Legen Sie die Datei `whitebox.py` mit folgendem Inhalt an:

```python
def binary_search_recur(array, low, high, val):
    """
    Rekursive Binärsuche in einem sortierten Array.
    Quelle: Adaptiert von github.com/keon/algorithms
    
    Args:
        array: Sortiertes Array zum Durchsuchen
        low: Startindex
        high: Endindex
        val: Zu suchender Wert
    
    Returns:
        Index des gefundenen Werts oder -1 wenn nicht gefunden
    """
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    
    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    elif val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    else:
        return mid


def cocktail_shaker_sort(arr):
    """
    Cocktail Shaker Sort - bidirektionale Bubble Sort Variante.
    Quelle: Adaptiert von github.com/keon/algorithms
    
    Bug: Enthält einen subtilen Defekt im Algorithmus!
    
    Args:
        arr: Zu sortierendes Array
        
    Returns:
        Sortiertes Array
    """
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    n = len(arr)
    swapped = True
    
    while swapped:
        swapped = False
        
        # Vorwärts durchlaufen
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
        
        if not swapped:  # Bug: Frühzeitiger Exit verhindert Rückwärtslauf
            return arr
            
        swapped = False
        
        # Rückwärts durchlaufen  
        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                
    return arr
```

Diese Algorithmen aus einer realen Open-Source-Bibliothek bieten komplexere Kontrollstrukturen und
echte Defekte, die durch systematische Whitebox-Testverfahren aufgedeckt werden können.

Legen Sie für die folgenden Aufgaben die Datei `test_whitebox.py` an.

### Anweisungsüberdeckung

Diese Methode prüft, ob jede einzelne Anweisung (z. B. `if`, `return`, `raise`, Zuweisungen) im Code
mindestens einmal während der Testausführung ausgeführt wird.
Ziel ist es, „tote“ oder nie ausgeführte Codezeilen zu identifizieren.

**Anwendung** Man analysiert den Code und erstellt gezielte Testfälle, um sicherzustellen, dass jede
Zeile mindestens einmal erreicht wird – unabhängig davon, ob alle möglichen Bedingungen oder Pfade
getestet wurden.
Dies ist die einfachste Form der strukturellen Testabdeckung.

**Beispiel** Bei einer Funktion mit mehreren `if`-Blöcken sollten die Tests so gestaltet sein, dass
für jeden Block mindestens ein Fall zutrifft und ausgeführt wird.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_statement_coverage_binary_search()`, die sicherstellt,
  dass jede Anweisung in der Funktion `binary_search_recur(..)` mindestens einmal ausgeführt wird.

[HINT::Anweisungen in binary_search_recur() identifizieren]
Schauen Sie sich die `binary_search_recur()` Funktion genau an. Sie enthält folgende ausführbare Anweisungen:

- `if low > high:` (Basisfall-Bedingung)
- `return -1` (Nicht gefunden)
- `mid = low + (high - low) // 2` (Mittelwert berechnen)
- `if val < array[mid]:` (Wert kleiner als Mitte)
- `return binary_search_recur(array, low, mid - 1, val)` (Linke Hälfte)
- `elif val > array[mid]:` (Wert größer als Mitte)  
- `return binary_search_recur(array, mid + 1, high, val)` (Rechte Hälfte)
- `return mid` (Wert gefunden)

Jede dieser Zeilen muss durch mindestens einen Testfall ausgeführt werden.
[ENDHINT]

### Bedingungsüberdeckung

Diese Methode stellt sicher, dass alle atomaren Bedingungen im Code sowohl den Wert `True` als auch
`False` annehmen – unabhängig davon, ob dies in Kombination mit anderen Bedingungen passiert oder
nicht.

**Anwendung** Zerlegen Sie zusammengesetzte Bedingungen (z. B. `if` `a > 10 and b < 5`) in ihre Einzelteile
`(a > 10, b < 5)` und erstellen Sie Testfälle, sodass jede davon einmal `True` und einmal `False` ergibt.
Hilfreich zur Erkennung von falsch gesetzten oder überflüssigen Bedingungen.

**Beispiel** Wenn eine Funktion prüft `if price > 100`, brauchen Sie Testfälle für `price > 100` und
`price <= 100`.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_condition_coverage_binary_search()`, die sicherstellt, dass
  alle Bedingungen in der Funktion `binary_search_recur(..)` sowohl `True` als auch `False` sind.

### Zweigüberdeckung

Diese Methode verlangt, dass jeder mögliche Zweig einer Entscheidung (`if`, `else`, `elif`, `try/except`)
mindestens einmal ausgeführt wird – also jede Richtung, nicht nur jede Bedingung (!).

**Anwendung** Man analysiert die Entscheidungsstellen im Code und erstellt für jede `if`-
oder `else`-Richtung einen passenden Testfall.
So kann man sicherstellen, dass sowohl der positive als auch der negative Pfad tatsächlich getestet
wurde.

**Beispiel** Für `if is_member:` brauchst du Testfälle mit `is_member = True` und `is_member = False`.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_branch_coverage_cocktail_sort()`, die sicherstellt, dass
  jede Verzweigung in der Funktion `cocktail_shaker_sort(..)` mindestens einmal durchlaufen wird.

### Pfadüberdeckung

Hier wird überprüft, ob alle möglichen Ausführungspfade im Code getestet wurden – also alle
Kombinationen von Entscheidungswegen, von Start bis Ende der Funktion.

**Anwendung** Man erstellt für jeden einzigartigen Ablaufweg durch den Code einen eigenen Testfall.
Je komplexer der Code (z. B. mit vielen verschachtelten `if`-Anweisungen), desto schwieriger wird
die vollständige Pfadüberdeckung.
Hilfreich für sicherheitskritische oder sehr fehleranfällige Funktionen.

**Beispiel** Die Funktion `binary_search_recur(..)` hat verschiedene logische Pfade je nach Vergleichsergebnis
und Rekursionstiefe.
Jeder Pfad sollte durch einen Testfall abgedeckt werden.

- [ER] Schreiben Sie eine pytest-Testfunktion `test_path_coverage_binary_search()`, die alle möglichen
  Ausführungspfade in der Funktion `binary_search_recur(..)` testet.

[HINT::Die Pfade in binary_search_recur() analysieren]
Die `binary_search_recur()` Funktion hat diese möglichen Ausführungspfade:

1. **Pfad 1**: `low > high` → Rückgabe -1 (Element nicht gefunden)
2. **Pfad 2**: `low <= high` UND `val < array[mid]` → Rekursion in linker Hälfte
3. **Pfad 3**: `low <= high` UND `val > array[mid]` → Rekursion in rechter Hälfte  
4. **Pfad 4**: `low <= high` UND `val == array[mid]` → Rückgabe mid (Element gefunden)

Beachten Sie, dass durch die Rekursion zusätzliche Pfadkombinationen entstehen können.
Erstellen Sie Testfälle, die diese verschiedenen Szenarien abdecken.
[ENDHINT]

### Datenflusskriterium

Diese Methode untersucht, ob alle Definitionen und Verwendungen von Variablen im Code abgedeckt sind.
Sie achtet darauf, ob eine Variable nach ihrer Zuweisung tatsächlich verwendet oder überschrieben wird.

**Anwendung** Man identifiziert alle Stellen, an denen Variablen gesetzt („definiert“) und
anschließend verwendet werden.
Testfälle sollen sicherstellen, dass es keine „toten“ Variablen gibt und dass Werte konsistent über
den Kontrollfluss hinweg verwendet werden.
Dies hilft besonders bei der Fehlersuche in komplexer Logik.

**Grundbegriffe der Datenflussanalyse:**

- **Definition (def)**: Eine Variable wird mit einem Wert belegt (z.B. `x = 5`, `result = calculate()`)
- **Verwendung (use)**: Eine Variable wird gelesen/verwendet (z.B. `return x`, `if x > 0`)
- **Def-Use-Pfad**: Ein Pfad von der Definition einer Variable zu ihrer Verwendung
- **Kill**: Eine Variable wird überschrieben/neu definiert, wodurch der alte Wert "getötet" wird

**Typische Datenfluss-Testkriterien:**

- **All-Defs**: Jede Definition einer Variable wird mindestens einmal verwendet
- **All-Uses**: Jede Verwendung einer Variable wird mindestens einmal von jeder möglichen Definition erreicht
- **All-Def-Use-Paths**: Alle möglichen Pfade von Definitionen zu Verwendungen werden getestet

**Beispiel** In der Funktion `discount(...)` wird price mehrfach geprüft und verwendet.
Ziel ist es sicherzustellen, dass jede Zuweisung (z. B. über Rückgabewerte) auch getestet und
genutzt wurde.

- [ER] Analysieren Sie die Variablen in beiden Funktionen und erstellen Sie:
  - `test_dataflow_bonus()` für die Analyse des Datenflusses in der `bonus` Funktion
  - `test_dataflow_discount()` für die Analyse des Datenflusses in der `discount` Funktion

[HINT::Vereinfachte Datenflussanalyse]
Für Einsteiger ist es oft ausreichend, zu testen, dass:

**Für `binary_search_recur`:**
- Parameter (`array`, `low`, `high`, `val`) werden in verschiedenen Konstellationen verwendet
- Variable `mid` wird korrekt berechnet und in Vergleichen verwendet
- Rekursive Aufrufe verwenden modifizierte Parameter (`mid-1`, `mid+1`)

**Für `cocktail_shaker_sort`:**
- Parameter `arr` wird modifiziert und zurückgegeben
- Variablen `n`, `swapped` werden definiert und in Schleifen verwendet
- Vertauschen von Elementen via `swap()` wird getestet

Konzentrieren Sie sich auf die wichtigsten Def-Use-Paare, anstatt alle theoretisch möglichen Pfade abzudecken.
[ENDHINT]

### Coverage-Kriterien und ihre relative Schärfe

Ein wichtiger Aspekt beim Whitebox-Testing ist das Verständnis, wann ein Testkriterium **schärfer** 
(strenger) ist als ein anderes. Ein Kriterium A ist schärfer als Kriterium B, wenn jede Testsuite, 
die A erfüllt, automatisch auch B erfüllt – aber nicht umgekehrt.

#### Hierarchie der Coverage-Kriterien

- [EQ] **Anweisungsüberdeckung vs. Bedingungsüberdeckung**: Betrachten Sie folgenden Code:
  ```python
  def check_eligibility(age, income):
      if age >= 18 and income > 30000:
          return "eligible"
      return "not eligible"
  ```
  
  Erstellen Sie Testfälle, die:
  1. 100% Anweisungsüberdeckung erreichen
  2. 100% Bedingungsüberdeckung erreichen
  
  Welches Kriterium ist schärfer? Warum können Sie mit nur einem Test alle Anweisungen abdecken, 
  benötigen aber mehrere Tests für alle Bedingungen?

[HINT::Anweisungs- vs. Bedingungsüberdeckung]
**Anweisungsüberdeckung** erfordert nur, dass jede Zeile mindestens einmal ausgeführt wird. 
Ein Test mit `age=20, income=40000` würde beide Anweisungen abdecken.

**Bedingungsüberdeckung** erfordert, dass jede atomare Bedingung sowohl `True` als auch `False` wird:
- `age >= 18`: einmal True, einmal False
- `income > 30000`: einmal True, einmal False

Das bedeutet mindestens 4 verschiedene Testfälle sind nötig!
Bedingungsüberdeckung ist daher schärfer als Anweisungsüberdeckung.
[ENDHINT]

- [EQ] **Bedingungsüberdeckung vs. Zweigüberdeckung**: Analysieren Sie diesen Code:
  ```python
  def complex_check(a, b, c):
      if (a > 0 and b > 0) or c > 10:
          return "pass"
      return "fail"
  ```
  
  Können Sie Testfälle finden, die 100% Bedingungsüberdeckung, aber nicht 100% Zweigüberdeckung 
  erreichen? Oder umgekehrt? Was bedeutet das für die relative Schärfe?

[HINT::Bedingung vs. Zweig - Unabhängigkeit]
Hier zeigt sich ein interessantes Phänomen: **Bedingungsüberdeckung und Zweigüberdeckung sind 
unvergleichbar** - keines ist generell schärfer als das andere!

**Szenario 1**: Bedingungsüberdeckung ohne vollständige Zweigüberdeckung:
- `a=1, b=1, c=5` → erste Bedingung True, zweite False, Zweig "pass"
- `a=-1, b=-1, c=15` → erste Bedingung False, zweite True, Zweig "pass"

Alle Bedingungen werden True/False, aber der "fail"-Zweig wird nie erreicht!

**Szenario 2**: Zweigüberdeckung ohne vollständige Bedingungsüberdeckung:
- `a=1, b=1, c=15` → "pass" Zweig  
- `a=-1, b=-1, c=5` → "fail" Zweig

Beide Zweige erreicht, aber `b > 0` wurde nie als True getestet!
[ENDHINT]

- [EQ] **Zweigüberdeckung vs. Pfadüberdeckung**: Betrachten Sie die `cocktail_shaker_sort` Funktion.
  Wie viele verschiedene Zweige gibt es? Wie viele verschiedene Pfade durch die verschachtelten 
  Schleifen? Warum ist Pfadüberdeckung hier praktisch unmöglich?

[HINT::Pfad-Explosion]
Die Anzahl der Pfade wächst **exponentiell** mit der Anzahl der Entscheidungspunkte:
- 2 if-Anweisungen → 4 mögliche Pfade
- 3 if-Anweisungen → 8 mögliche Pfade
- n if-Anweisungen → 2ⁿ mögliche Pfade

Bei Schleifen wird es noch schlimmer: Eine Schleife, die 0-10 mal läuft, erzeugt bereits 11 verschiedene 
Pfade. Zwei verschachtelte Schleifen → 11×11 = 121 Pfade!

**Pfadüberdeckung ist daher das schärfste, aber auch das unpraktischste Kriterium.**
[ENDHINT]

#### Praktische Anwendung der Kriterien-Hierarchie

- [EQ] **Rekursive Funktionen**: Bei der `binary_search_recur` Funktion - welches Coverage-Kriterium 
  hilft am besten dabei, den rekursiven Aufruf in verschiedenen Tiefen zu testen? Warum reicht 
  Anweisungsüberdeckung hier nicht aus?

- [EQ] **Kostenabwägung**: Ordnen Sie die Coverage-Kriterien nach ihrem Aufwand-Nutzen-Verhältnis 
  für typische Geschäftslogik. Begründen Sie Ihre Entscheidung anhand konkreter Beispiele.

[HINT::Praktische Coverage-Strategien]
**Typische Reihenfolge nach Aufwand-Nutzen-Verhältnis:**

1. **Zweigüberdeckung** (85-95% aller Bugs) - Bester Kompromiss
2. **Anweisungsüberdeckung** (60-70% aller Bugs) - Minimum für Produktionscode
3. **Bedingungsüberdeckung** (90-95% aller Bugs) - Für kritische Algorithmen
4. **Pfadüberdeckung** (95-99% aller Bugs) - Nur für sicherheitskritische Systeme
5. **Datenflusskriterien** - Für komplexe Zustandslogik

**Faustregel**: Beginnen Sie mit Zweigüberdeckung, fügen Sie Bedingungsüberdeckung für komplexe 
Entscheidungslogik hinzu.
[ENDHINT]

### Reflektieren Sie

- [EQ] Welche Herausforderungen haben Sie bei der Testfallerstellung für die Algorithmus-Funktionen erkannt?
  Wie schwierig war es, Tests für rekursive Funktionen wie `binary_search_recur` zu erstellen?
- [EQ] Konnten Sie den Defekt in `cocktail_shaker_sort` durch Ihre Whitebox-Tests identifizieren?
  Welche Coverage-Methode hat dabei geholfen?
- [EQ] Ist es stets sinnvoll oder möglich, alle Whitebox-Testkriterien auf jede Funktion anzuwenden?
- [EQ] Welche der Coverage-Arten (Statement, Condition, Branch, Path) bietet das beste
  Verhältnis zwischen Aufwand und Nutzen für typische Algorithmus-Implementierungen?

[NOTICE]
**Automatisierte Coverage-Messung:** In der Praxis würden Sie Tools wie `pytest-cov` verwenden, 
um automatisch zu messen, welche Codezeilen durch Ihre Tests abgedeckt werden. 
Solche Tools können Ihnen zeigen, ob Ihre manuell entwickelten Testfälle tatsächlich alle 
gewünschten Coverage-Kriterien erfüllen.

Das Thema Coverage-Tools ist ebenfalls Bestandteil in diesem Kurs und kann im Anschluss gerne hier
[PARTREF::pytest_plugin_testcoverage] oder hier [PARTREF::testcoverage] angepackt werden.
[ENDNOTICE]

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
