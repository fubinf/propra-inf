title: Klassen und Prototypen – Strukturierte Logik in JavaScript
stage: alpha
timevalue: 1.0
difficulty: 2
requires: js-DOM-Einführung
---

[SECTION::goal::idea]

- Ich kann in JavaScript eigene Klassen definieren und Instanzen davon erstellen.  
- Ich kann Methoden und Vererbung einsetzen, um wiederverwendbare Strukturen aufzubauen.  
- Ich verstehe den Zusammenhang zwischen Klassen und Prototypen in JavaScript.  
- Ich kann Gemeinsamkeiten und Unterschiede zu Python-Klassen benennen. 
[ENDSECTION]


[SECTION::background::default]
Mit Klassen können wir Code strukturieren, wiederverwenden und leichter verstehen.  
Statt verstreute Funktionen und Daten getrennt zu behandeln, bündeln wir beides in klaren Bausteinen.  
So lassen sich auch größere Programme übersichtlich aufbauen. 
[ENDSECTION]


[SECTION::instructions::loose]

### Eigene Klassen mit `class` und `constructor`

In Python kennen wir bereits Klassen, die mit `class` eingeführt und mit der speziellen Methode `__init__` initialisiert werden.  
In JavaScript gibt es seit ES6 ebenfalls eine `class`-Syntax, sie sieht ähnlich aus, funktioniert aber intern etwas anders.  
JavaScript basiert nicht auf „echten“ Klassen wie Python, sondern auf Prototypen (dazu gleich mehr).  
Das Prinzip ist jedoch gleich: Man bündelt Daten (Attribute) und Funktionen (Methoden) in einer wiederverwendbaren Struktur.

Beispiel in Python:

```python
class TodoItem:
    def __init__(self, text):
        self.text = text
        self.erledigt = False

    def erledigen(self):
        self.erledigt = True

    def anzeigen(self):
        return "✔️ " + self.text if self.erledigt else self.text

aufgabe = TodoItem("Kapitel 4 lesen")
print(aufgabe.anzeigen())   # Kapitel 4 lesen
aufgabe.erledigen()
print(aufgabe.anzeigen())   # ✔️ Kapitel 4 lesen
```

Das gleiche Prinzip in JavaScript:

```js
class TodoItem {
  constructor(text) {
    this.text = text;
    this.erledigt = false;
  }

  erledigen() {
    this.erledigt = true;
  }

  anzeigen() {
    return this.erledigt ? "✔️ " + this.text : this.text;
  }
}

const aufgabe = new TodoItem("Kapitel 4 lesen");
console.log(aufgabe.anzeigen()); // "Kapitel 4 lesen"
aufgabe.erledigen();
console.log(aufgabe.anzeigen()); // "✔️ Kapitel 4 lesen"
```

#### Parallelen:

Sowohl in Python als auch in JavaScript definiert man Klassen mit dem Schlüsselwort `class`.  
In Python übernimmt die spezielle Methode `__init__` die Rolle des Konstruktors, während in JavaScript dafür die Methode `constructor` vorgesehen ist.  
Auch der Verweis auf das aktuelle Objekt ist vergleichbar: In Python geschieht das über `self`, in JavaScript über `this`.  
Methoden werden in beiden Sprachen direkt innerhalb der Klassendefinition notiert, sodass die grundlegende Struktur von Klassen in Python und JavaScript auf den ersten Blick sehr ähnlich wirkt.

[ER] Erstellen Sie eine Klasse `Produkt`, die Name und Preis im Konstruktor entgegennimmt.  
Fügen Sie eine Methode `beschreibung()` hinzu, die beides als String zurückgibt.


### Was bedeutet „Prototyp“?

In JavaScript hat jedes Objekt intern einen Prototyp, ein anderes Objekt, von dem es Eigenschaften erben kann.  
Klassen (`class`) sind also eigentlich nur eine modernere und übersichtlichere Schreibweise für diese Prototyp-Verkettung.

Beispiel mit Prototypen (ohne class):

```js
function Tier(name) {
  this.name = name;
}

Tier.prototype.sprechen = function() {
  console.log(this.name + " macht ein Geräusch.");
};

const hund = new Tier("Bello");
hund.sprechen(); // "Bello macht ein Geräusch."
```

Die moderne class-Syntax:

```js
class Tier {
  constructor(name) {
    this.name = name;
  }

  sprechen() {
    console.log(this.name + " macht ein Geräusch.");
  }
}
```

Beide Varianten tun dasselbe, nur die Syntax unterscheidet sich.

[ER] Prototyp statt class:  

1. Erstellen Sie eine Konstruktorfunktion `Auto(marke, baujahr)`.  
2. Ergänzen Sie eine Methode `alter()` über `Auto.prototype`, die das Alter des Autos aus dem aktuellen Jahr berechnet.  
3. Erzeugen Sie zwei Auto-Objekte und geben Sie für beide mit `console.log` Marke und Alter aus.


### Vererbung mit `extends`

Genauso wie in Python kann man in JavaScript Klassen von anderen Klassen ableiten.  
Das bedeutet: Eine Unterklasse übernimmt Eigenschaften und Methoden der Elternklasse und kann neue hinzufügen oder bestehende überschreiben.  
So vermeiden wir doppelten Code und können gemeinsame Logik an einer zentralen Stelle definieren.

In Python sieht das z. B. so aus:

```python
class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

    def beschreibung(self):
        return f"{self.name}: {self.preis} €"

class PremiumProdukt(Produkt):
    def __init__(self, name, preis, rabatt):
        super().__init__(name, preis)
        self.rabatt = rabatt

    def endpreis(self):
        return self.preis * (1 - self.rabatt)

buch = PremiumProdukt("JS-Handbuch", 30, 0.2)
print(buch.beschreibung())  # "JS-Handbuch: 30 €"
print(buch.endpreis())      # 24.0
```

Und in JavaScript funktioniert es sehr ähnlich, nur mit dem Schlüsselwort `extends`:

```js
class Produkt {
  constructor(name, preis) {
    this.name = name;
    this.preis = preis;
  }

  beschreibung() {
    return this.name + ": " + this.preis + " €";
  }
}

class PremiumProdukt extends Produkt {
  constructor(name, preis, rabatt) {
    super(name, preis);  // ruft den Konstruktor der Elternklasse auf
    this.rabatt = rabatt;
  }

  endpreis() {
    return this.preis * (1 - this.rabatt);
  }
}

const buch = new PremiumProdukt("JS-Handbuch", 30, 0.2);
console.log(buch.beschreibung()); // "JS-Handbuch: 30 €"
console.log(buch.endpreis());     // 24
```

#### Wichtige Gemeinsamkeiten und Unterschiede

`super()`:  
- Python: ruft den Konstruktor der Elternklasse auf.  
- JavaScript: genau dasselbe – nur Pflicht, wenn man im Konstruktor von `extends`-Klassen auf `this` zugreifen will.

Syntax:  
- Python: `class Kind(Eltern)`:  
- JavaScript: `class Kind extends Eltern { ... }`

Intern:  
- Python: "echte" Klassenhierarchie.  
- JavaScript: Prototyp-Ketten, die durch `extends` gebildet werden.  


[ER] Leiten Sie eine Klasse `DigitalProdukt` von `Produkt` ab.  
Sie soll:  
- zusätzlich eine Eigenschaft `downloadLink` im Konstruktor setzen,  
- eine Methode `info()` besitzen, die Name und Link kombiniert zurückgibt.

Beispiel:

```js
const ebook = new DigitalProdukt("JavaScript Basics", 15, "http://download/ebook");
console.log(ebook.beschreibung()); // "JavaScript Basics: 15 €"
console.log(ebook.info());         // "JavaScript Basics → Download: http://download/ebook"
```


### Prototypische Vererbung verstehen

Bisher haben wir Vererbung mit `extends` genutzt.  
Jetzt schauen wir uns an, wie JavaScript das intern umsetzt: über Prototyp-Ketten.  
Gehen wir jetzt einen Schritt weiter und schauen uns an, wie die Vererbung konkret funktioniert.  
Jedes Objekt in JavaScript hat eine interne Referenz auf ein anderes Objekt, seinen Prototypen.   
Wenn man auf eine Eigenschaft oder Methode zugreift, die im aktuellen Objekt nicht vorhanden ist, 
sucht JavaScript automatisch im Prototyp weiter.  
Bei Vererbung ergibt sich daraus eine ganze Prototyp-Kette.

Beispiel mit einer Konstruktorfunktion:

```js
function Tier(name) {
  this.name = name;
}

Tier.prototype.sprechen = function() {
  console.log(this.name + " macht ein Geräusch.");
};

const hund = new Tier("Bello");
hund.sprechen(); // "Bello macht ein Geräusch."
```

Hier passiert intern Folgendes:  
1. JavaScript sucht bei `hund.sprechen()` nach einer Methode `sprechen` im Objekt `hund`. 
2. Sie wird dort nicht gefunden → also schaut die Engine im Prototyp (`Tier.prototype`) nach.  
3. Dort gibt es `sprechen` → die Methode wird ausgeführt.


#### Verbindung zu `class` und `extends`

Die moderne `class`-Syntax setzt diese Prototyp-Ketten für uns auf.  
Das heißt, wenn wir mit `extends` arbeiten, wird intern einfach die Prototyp-Referenz so gesetzt, 
dass die Kindklasse auf die Methoden und sonstigen Attribute der Elternklasse zugreifen kann.

Darum gilt:  

- `class` = lesbarere Syntax  
- Prototypen = das eigentliche System dahinter

[ER] Die Prototyp-Kette untersuchen  
1. Definieren Sie eine Klasse `Tier` und leiten Sie davon die Klasse `Hund` ab.  
2. Erzeugen Sie eine Instanz von `Hund`.  
3. Verwenden Sie `Object.getPrototypeOf()`, um Ihnen Schritt für Schritt die Kette anzeigen zu lassen:  
- von der Instanz (`hund`) → `Hund.prototype`  
- von `Hund.prototype` → `Tier.prototype`  
- und schließlich bis `Object.prototype`.  

[EQ] Erklären Sie anhand Ihrer Ausgabe, wie JavaScript bei einem Methodenaufruf (z. B. `hund.sprechen()`) 
durch diese Kette wandert, bis es die passende Methode findet:
Welche Attribute von welchen Objekten werden der Reihe nach benutzt?
Welcher Wert kommt dabei jeweils heraus?
[ENDSECTION]


[SECTION::submission::reflection,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
