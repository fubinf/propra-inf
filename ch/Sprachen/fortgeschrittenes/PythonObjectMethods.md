title: "Objektmethoden in Python"
stage: draft
timevalue: 0.75
difficulty: 2
requires: PythonObjectsClassesIntro, PythonFunctions
assumes: PythonStrings, PythonIntegers, PythonBooleans, PythonComments, PythonCasting, PythonConditionalstatements
---

[SECTION::goal::idea]

- Ich verstehe, was Objektmethoden sind und wie ich damit arbeite.

[ENDSECTION]

[SECTION::instructions::loose]

Lesen Sie den folgenden kleinen [Artikel](https://www.w3schools.com/python/gloss_python_object_methods.asp). Sie haben in [PARTREF::PythonObjectsClassesIntro] Objekte kennengelernt. Sie haben auch gelernt, dass Objekte Attribute haben können und diese Attribute bei der Objekterstellung beliebig gesetzt werden können. 

[EQ] Was haben Sie von dem kleinen Artikel verstanden? Was sind diese Methoden, die wir innerhalb der Klasse angeben, um damit später über erstellte Objekte arbeiten zu können? 

[EQ] Welchen Aspekt von einem Objekt beschreiben diese Methoden, wenn Sie wissen würden, dass die Attribute die **Eigenschaften** von einem Objekt darstellen. 

[EQ] Wie kann auf die Objektattribute innerhalb dieser Objektmethoden zugegriffen werden?

[EQ] was ist der Unterscheid zwischen einer *"Methode"* und einer *"Funktion"* in Python?


### Übung: Einfaches Bibliotheksverwaltungssystem

Betrachten Sie folgende Klassendefinition:

```python
    class Buch:
        def __init__(self, titel, autor_innen, seitenzahl):
            self.titel = titel # str
            self.autor_innen = autor_innen # str
            self.seitenzahl = seitenzahl # int
            self.verfuegbar = True # bool
        
        def info(self):
            print('Buchtitel: ', self.titel)
            '''
            Folgendes muss noch ausgegeben werden:
            - Ausgabe der Autor_innen
            - Ausgabe der Seitenzahl
            - Ausgabe der Verfügbarkeit
            '''
            

        def ausleihen(self):
            '''
            Erst Überprüfen, ob das Buch verfügbar ist:
            - Falls ja, 'Das Buch "<Titel-des-Buches>" wurde erfolgreich ausgeliehen!' ausgeben.
            - Falls nein, 'Das Buch "<Titel-des-Buches>" ist gerade nicht verfügbar' ausgeben.
            
            Fall das Buch verfügbar war und ausgeliehen wurde,
            dann muss das Buch demzufolge nicht mehr verfügbar gemacht werden. (entsprechendes Attribut aktualisieren)
            '''
        
        def zurueckgeben(self):
            '''
            Ausgabe: 'Das Buch "<Titel-des-Buches>" wurde erfolgreich zurückgegeben!'

            Nach der Ausgabe muss das Buch wieder verfügbar sein. (entsprechendes Attribut aktualisieren)
            '''



    # Beispiel:
    buch1 = Buch('Der Herr der Ringe', 'John Ronald Reuel Tolkien', 1296)
    buch2 = Buch('Der pragmatische Programmierer', 'Andrew Hunt and David Thomas', 321)

    buch1.info()
    buch1.ausleihen()
    print(buch1.titel + ' ist verfügbar: ' + str(buch1.verfuegbar))
    buch1.zurueckgeben()
    print(buch1.titel + ' ist verfügbar: ' + str(buch1.verfuegbar))

    print('-----------------------')

    buch2.info()
    print(buch2.titel + ' ist verfügbar: ' + str(buch2.verfuegbar))
    buch2.ausleihen()
    print(buch2.titel + ' ist verfügbar: ' + str(buch2.verfuegbar))
```

[ER] Erstellen Sie zuerst eine geeignete Python-Datei und kopieren Sie dann den gesamten Code hinein. Ergänzen Sie danach die drei Objektmethoden `info()`, `ausleihen()` und `zurueckgeben()` anhand der Kommentare, die die Ausgaben jeder Methode beschreiben.

[ER] Testen Sie Ihre Implementierungen mithilfe des Beispiels der beiden zur Verfügung gestellten Bücher-Objekte `buch1` und `buch2` und schreiben Sie die Ausgaben als Kommentare an passende Stellen im Code.

[EQ] In der Definition der `__init__()`-Funktion habe wir das Attribut `verfuegbar` auf `True` gesetzt. Wir haben dabei also angenommen, dass jedes Buch am Anfang immer verfügbar ist. Wie Sie wahrscheinlich gemerkt haben, muss dieses Attribut bei der Erstellung von Ojekten nicht als Parameter für den Konstruktor angegeben werden. Wie würde man solche Attribute nennen und wann sind sie hilfreich?

[ENDSECTION]

[SECTION::submission::program]

Bearbeiten Sie die Anforderungen [EREFR::1], [EREFR::2]. Am Ende sollte eine Python-Datei abgegeben werden.

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]


[INSTRUCTOR::Syntax und Konzepte]

In den abgegebenen Python-Dateien könnte überprüft werden, ob man die Syntax für den Umgang mit Objektattributen und Objektmethoden verstanden hat.

Bei schriftlichen Markdown-Abgaben bitte überprüfen:  
- ob, der Student verstanden hat, was eine Objektmethode ist.  
- ob, der Student mit den Objektattributen innerhalb der Methoden arbeiten kann.  
- ob, der Student Default-Attribute versteht, die für alle Objekte der Klasse gleiche Werte haben sollten.  

[ENDINSTRUCTOR]