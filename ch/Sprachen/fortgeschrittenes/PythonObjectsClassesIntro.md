title: "Einführung in Klassen und Objekte in Python"
stage: alpha
timevalue: 1
difficulty: 2
assumes: PythonStrings, PythonComments
---

[SECTION::goal::idea]

- Ich habe gutes Verständnis von grundlegenden Konzepten objektorientierter Programmierung.  
- Ich kann in Python eine einfache objektorientierte Darstellung von Daten implementieren.  

[ENDSECTION]

[SECTION::instructions::loose]

Betrachten Sie den folgenden [Artikel](https://www.w3schools.com/python/python_classes.asp). Sie werden Schritt für Schritt bestimmte Abschnitte in dem Artikel lesen und anhand dessen kleine Aufgaben bearbeiten:

### Klassen:

**Lesen Sie zuerst den kleinen Einführungsabschnitt *"Python Classes/Objects"* und danach *nur* den ersten Artikelabschnitt *"Create a Class"*.**

- [ER]

Legen Sie eine neue Python-Datei `propra_objects_classes_intro.py` an und definieren Sie innerhalb dieser Datei, wie im Beispiel des Abschnitts, eine Klasse namens `ProPraTeilnehmer` mit folgenden "Attributen":

- `matrikelnummer = # str: Ihre eigene Matrikelnummer`  
- `vorname = # str: Ihr eigener Vorname`  
- `nachname = # str: Ihr eigener Nachname`  

Ihre Python-Datei `propra_objects_classes_intro.py` soll bis zu diesem Punkt wie folgt aussehen:

```python
    # Definition der Klasse ProPraTeilnehmer: (Schlüsselwort class + Klassenname + :)
        # Attribute 1: matrikelnummer
        # Attribute 2: vorname
        # Attribute 3: nachname
```

---

### Objekte:

**Lesen Sie jetzt *nur* den zweiten Artikelabschnitt *"Create Object"*.**

- [ER]

Erstellen Sie, wie im Artikel, zwei Objekte `teilnehmer1` und `teilnehmer2` aus der Klasse `ProPraTeilnehmer` unter der Klassendefinition in Ihrer Datei `propra_objects_classes_intro.py`. Überprüfen Sie mithilfe der `print()`-Funktion die Ausgaben, wenn Sie auf die drei Attribute jeweils mithilfe der beiden erstellten Objekte zugreifen. 

Ihre Python-Datei `propra_objects_classes_intro.py` soll nach diesem Schritt wie folgt aussehen:

```python
    # Definition der Klasse ProPraTeilnehmer:
        # Attribute 1: matrikelnummer
        # Attribute 2: vorname
        # Attribute 3: nachname

    # Erstellung vom ersten Objekt teilnehmer1
    # Erstellung vom zweiten Objekt teilnehmer2

    # print(teilnehmer1.matrikelnummer)
    # print(...)
    # print(...)

    # print(teilnehmer2.matrikelnummer)
    # print(...)
    # print(...)
```

- [EQ] Gibt es Unterschiede zwischen den Ausgaben? Bspw. zwischen `teilnehmer1.matrikelnummer` und `teilnehmer2.matrikelnummer`?


---

### `__init__()`:

**Lesen Sie jetzt den dritten Abschnitt *"The `__init__()` Function"*.**

- [ER]

Löschen Sie die drei Variablen (`matrikelnummer`, `vorname`, `nachname`), die Sie in [EREFR::1] erstellt haben. Nutzen Sie jetzt die `__init__()`-Funktion mit den drei Variablen, um diese Variablen allen Objekten, die aus dieser Klasse erstellt werden, zuweisen zu können. Bearbeiten Sie dafür jetzt die Stellen, wo Sie die beiden Objekte `teilnehmer1` und `teilnehmer2` erstellt haben, sodass jedes Objekt eigene beliebige Werte für die drei Variablen hat.

[WARNING]

Vergessen Sie hierbei nicht den ersten Parameter `self`! In weiteren Abschnitten des Artikels ist das bereits erklärt. Im Allgemeinen ist aber wichtig zu verstehen, dass `self` kein [TERMREF::Schlüsselwort] ist, sondern eine Konvention für die Refernzierung auf das Objekt, das die Methode aufruft. In vielen anderen Programmiersprachen findet man das gleiche Konzept mithilfe von Schlüsselwörtern, bspw. `this`. Sie werden ohnehin dieses Konzept in [PARTREF::PythonObjectsClassesPractice] vertieft üben können. 

[ENDWARNING]

Nach diesem Schritt soll Ihre Python-Datei `propra_objects_classes_intro.py` wie folgt aussehen:

```python
    # Definition der Klasse ProPraTeilnehmer:
        # Nutzung von __init__() mit den drei Variablen matrikelnummer, vorname und nachname

    # Erstellung vom ersten Objekt teilnehmer1 mit eignen Werten für: matrikelnummer, vorname, nachname
    # Erstellung vom zweiten Objekt teilnehmer2 mit eignen Werten für: matrikelnummer, vorname, nachname

    # print(teilnehmer1.matrikelnummer)
    # print(...)
    # print(...)

    # print(teilnehmer2.matrikelnummer)
    # print(...)
    # print(...)
```

- [EQ] Was ist genau die `__init__()`-Funktion und wie nennt man diese Funktion? Welche Rolle hat solche Funktion in objektorientierter Programmierung?

- [EQ] In [EREFR::1] haben Sie mit drei Variablen gearbeitet, diese nennt man **"Klassenattribute"**. In [EREFR::2] haben Sie festgestellt, dass der Zugriff auf diese drei Klassenattribute über beide Objekte zu identischen Werten führt. Begründen Sie dieses Verhalten in Ihrem Code.

- [EQ] In [EREFR::3] haben Sie mithilfe von `__init__()` jedem der Objekte verschiedene Werte für die drei Variablen (`matrikelnummer`, `vorname`, `nachname`) zugewiesen. Sie konnten auch feststellen, dass die Ausgaben diesmal unterschiedlich waren. Solche Variablen, die einem Objekt zugehören, nennt man Attribute für das Objekt. Was ist aber der Unterschied zwischen Klassen- und Objektattributen?


[HINT::Klassenattribute]

Recherchieren Sie, was Klassenattribute sind und wie sie sich von Objektattributen unterscheiden. 
Zur Hilfe können Sie diesen kleinen [Artikel](https://www.educative.io/answers/what-is-a-python-class-attribute) lesen.

[ENDHINT]

---

### Zusammenfassung:

- [EQ] Beschreiben Sie in eigenen Worten, was eine *"Klasse"* und ein *"Objekt"* in der objektorientierten Programmierung sind und wie sie miteinander interagieren.  

- [EQ] Den *"Klassenkonstruktor"* haben Sie im Rahmen von [EREFR::2] und [EREFR::3] kennengelernt. Führen Sie folgende Code-Abschnitte in Ihrer eigenen Programmierumgebung aus. Erklären Sie danach das Verhalten und den Unterschied. Beantworten Sie dafür folgende Fragen:

    - a) Sind die ersten zwei Beispiele gleich? Warum und was passiert genau, wenn das Objekt `obj = A()` erstellt wird?  
    - b) `obj = A()` im 3. Beispiel führt zu Fehler. Wie lautet dieser Fehler und warum entsteht er? Recherchieren Sie hierfür nach *"impliziten"* und *"expliziten"* Konstruktoren in Python.   
    - c) In welchem der drei Beispiele ist ein impliziter bzw. expliziter Klassenkonstruktor zu finden?   
    - d) Was passiert mit dem impliziten Konstruktor, wenn wir einen expliziten definieren? Kann der implizite weiterhin verwendet werden, wenn ein expliziter bereits definiert ist?  

**Beispiel 1:**

```python
    class A:
        pass

    obj = A()
    print(obj) # Um hier die Ausgabe zu verstehen, lesen Sie den Artikelabschnitt "The __str__() Function"
```

**Beispiel 2:**

```python
    class A:
        def __init__(self):
            pass
            
    obj = A()
    print(obj)
```

**Beispiel 3:**

```python
    class A:
        def __init__(self, x):
            self.x = x

    obj = A()
    print(obj)
```

[ENDSECTION]

[SECTION::submission::program]

Bearbeiten Sie die Anforderungen [EREFR::1], [EREFR::2], ... Am Ende sollte eine Python-Datei `propra_objects_classes_intro.py` abgegeben werden. Der Zustand Ihrer Abgabedatei sollte etwa dem in [EREFR::3] beschriebenen Zustand entsprechen. 

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]


[INSTRUCTOR::Syntax und Konzepte]

In den abgegebenen Python-Dateien könnte überprüft werden, ob man die Syntax für den Umgang mit Klassen und Objekten, wie im verlinkten "w3schools"-Artikel, verstanden hat.

Bei schriftlichen Markdown-Abgaben bitte überprüfen, ob die grundlegenden OOP-Konzepte verstanden wurden:  
- Klassen und Objekten und Verhältnis dazwischen  
- Rolle von Konstruktoren  
- Impliziter und expliziter Konstruktor  
- Unterschied zwischen Klassen- und Objektattributen  

[ENDINSTRUCTOR]