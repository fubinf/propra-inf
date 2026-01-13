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
JavaScript verwendet intern keine Klassenhierarchie wie Python, sondern ein prototypbasiertes Objektmodell (dazu gleich mehr).  
Die `class`-Syntax ist lediglich eine alternative Schreibweise für dieses Prototyp-System.

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

Das gleiche in JavaScript:

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
In Python übernimmt die spezielle Methode `__init__` die Rolle des Konstruktors, 
während in JavaScript dafür die Methode `constructor` vorgesehen ist.  
Auch der Verweis auf das aktuelle Objekt ist vergleichbar: 
In Python geschieht das über `self`, in JavaScript über `this`.  
Methoden werden in beiden Sprachen direkt innerhalb der Klassendefinition notiert, 
sodass die grundlegende Struktur von Klassen in Python und JavaScript auf den ersten Blick sehr ähnlich wirkt.

[ER] Erstellen Sie eine Klasse `Produkt`, die Name und Preis im Konstruktor entgegennimmt.  
Fügen Sie eine Methode `beschreibung()` hinzu, die beides als String zurückgibt.


### Was bedeutet „Prototyp“?

In JavaScript besitzt jedes Objekt intern einen Verweis auf ein anderes Objekt, seinen Prototyp.  
Wenn auf eine Eigenschaft zugegriffen wird, die im Objekt selbst nicht existiert, wird im Prototyp weitergesucht.
Klassen (`class`) sind nur eine modernere und übersichtlichere Schreibweise für diese Prototyp-Verkettung.

Beispiel mit Prototypen (ohne `class`):

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

Die moderne `class`-Syntax:

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

Beide Varianten erzeugen dieselbe Struktur:  
Eine Konstruktorfunktion, deren `prototype`-Objekt die Methode `sprechen` enthält.  
Der Unterschied liegt nur in der Schreibweise.

[ER] Prototyp statt `class`:  

1. Erstellen Sie eine Konstruktorfunktion `Auto(marke, baujahr)`, die die übergebenen Werte als Eigenschaften speichert.  
2. Ergänzen Sie eine Methode `alter(aktuellesJahr)` über `Auto.prototype`.  
Die Methode soll das Alter des Autos als Differenz aus `aktuellesJahr` und dem gespeicherten Baujahr berechnen und zurückgeben.  
3. Erzeugen Sie zwei Auto-Objekte, legen Sie ein aktuelles Jahr in einer Variablen fest  
und geben Sie für beide mit `console.log` Marke und Alter aus.


### Vererbung mit `extends`

Genauso wie in Python kann man in JavaScript Klassen von anderen Klassen ableiten.  
Das bedeutet: Eine Unterklasse kann auf Eigenschaften und Methoden der Elternklasse zugreifen,  
weil ihre Instanzen über eine Prototyp-Kette mit der Elternklasse verbunden sind.  
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

`super`:  
- Python: `super()` liefert ein Proxy-Objekt, über das Methoden/Attribute der Elternklasse aufgerufen werden können  
(z. B. `super().__init__(...)`). Es ist nicht „die Elternklasse selbst“, sondern ein spezieller Zugriff darauf.    
- JavaScript: `super` ist ein spezielles Schlüsselwort für Zugriffe auf den Prototyp der Elternklasse.  
`super(...)` ruft im Konstruktor den Konstruktor der Elternklasse auf.  
`super.methode()` ruft eine Methode der Elternklasse auf.

Wichtig in JavaScript:  
In einer abgeleiteten Klasse (`extends`) muss im `constructor` zuerst `super(...)` aufgerufen werden,  
bevor `this` verwendet werden darf.  
Wenn Sie keinen eigenen `constructor` definieren, fügt JavaScript automatisch einen ein, der `super(...)` aufruft.

Syntax:  
- Python: `class Kind(Eltern)`
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
Jedes Objekt in JavaScript hat eine interne Referenz auf ein anderes Objekt, seinen Prototypen.   
Wenn man auf eine Eigenschaft oder Methode zugreift, die im aktuellen Objekt nicht vorhanden ist, 
sucht JavaScript im Prototyp weiter.  
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

Die moderne `class`-Syntax übernimmt für uns genau die Schritte,  
die wir zuvor manuell mit Konstruktorfunktionen und Prototypen durchführen würden.

Wenn eine Klasse `B` mit `extends A` von einer anderen Klasse erbt,  
setzt JavaScript intern zwei wichtige Verknüpfungen:

1. Das Prototyp-Objekt der Kindklasse wird mit dem Prototyp-Objekt der Elternklasse verbunden:  
`B.prototype` erhält als Prototyp `A.prototype`.  
2. Der Konstruktor der Kindklasse wird mit dem Konstruktor der Elternklasse verbunden,  
sodass `super(...)` im Konstruktor von `B` den Konstruktor von `A` aufrufen kann.

Dadurch entsteht eine Prototyp-Kette:  
Instanzen von `B` → `B.prototype` → `A.prototype` → `Object.prototype`.

Die `class`-Syntax ist damit lediglich eine lesbarere Schreibweise für diese Prototyp-Verknüpfungen.

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
