title: "Go-Standardbibliothek: context"
stage: draft
timevalue: 2
difficulty: 2
---

Src: https://www.digitalocean.com/community/tutorials/how-to-use-contexts-in-go

### `context` [Dokumentation](https://pkg.go.dev/context)

Beispiel:

```go
var dataChan chan []byte

// struct{} ist ein zero-byte Typ, bequem für Kommunikation der Art "guck mal hier, es ist was passiert"
var cancelChan chan struct{}

...
for {
    select {
    case data := <-dataChan:
        processData(data)
    case <-cancelChan:
        // wir interessieren uns nicht dafür, _was_ empfangen wurde
        // das Empfagen selbst ist das Signal
        return
    }
}
```

[FOLDOUT::Wo kommt der `cancelChan` her?]

Einen solchen Kanal können Sie natürlich selbstständig erzeugen und benutzen.
Meistens kommt er jedoch als Teil eines _Kontexts_.

Das Paket `context` gehört zur Standardbibliothek und bietet Werkzeuge zur Übertragung von Abbruchsignalen oder anfragespezifischen Werten.

Beispiele:

```go
// so wird ein Kontext erzeugt; in 10 Sekunden kommt ein Abbruchsignal
ctx, _ := context.WithTimeout(context.Background(), 10 * time.Second)
```

```go
func doWork(ctx context.Context, ch chan int) {
    for {
        select {
            case newInt := <- ch {
                // do work...
            }
            // ctx.Done() gibt einen Kanal zurück, der geschlossen wird, wenn die Ausführung abgebrochen werden soll
            // dieses Ereignis wird hier im select-Block abgefangen
            case <- ctx.Done() {
                return
            }
        }
    }
}
```
[ENDFOLDOUT]

Das Paket `context` bietet Mechanismen zur Übertragung von anfragespezifischen Werten, Abbruchsignalen und Fristen.

Das Hauptobjekt des Pakets ist das Interface `Context`:

```go
type Context interface {
    Deadline() (deadline time.Time, ok bool)
    Done() <-chan struct{}
    Err() error
    Value(key any) any
}
```

Diese Methoden haben folgende Funktionen:

- `Deadline()` — Gibt den Zeitpunkt zurück, zu dem der Kontext abgebrochen wird (falls vorhanden);
- `Done()` — Gibt einen Kanal zurück, der geschlossen wird, wenn der Kontext abgebrochen wird;
- `Err()` — Gibt einen Fehler zurück, der erklärt, warum der Kontext abgebrochen wurde;
- `Value(key any)` — Ruft einen mit einem bestimmten Schlüssel verknüpften Wert ab.

#### So erzeugt man einen `context`

* `context.Background() context.Context`
  — Hintergrundkontext, welcher nie abgebrochen wird.
  Dieser Kontext wird in der Regel in der `main`-Funktion erzeugt;
* `context.TODO() context.Context`
  — ein leerer Kontext, welcher beim Entwickeln als Platzhalter benutzt wird.
  Besonders nützlich während Migrationen von älteren Go-Projekten;
* `context.WithCancel(parent context.Context) (context.Context, context.CancelFunc)`
  — neben dem Kontext selbst wird eine Funktion zurückgegeben, mithilfe deren dieser Kontext abgebrochen werden kann.
  Der neue Kontext übernimmt alle Werte und Fristen des `parent`-Kontexts und wird abgebrochen, sobald der `parent`-Kontext abgebrochen wird;
* `context.WithDeadline(parent context.Context, deadline time.Time) (context.Context, context.CancelFunc)`
  — ähnlich wie `context.WithCancel()`.
  Dieser Kontext wird abgebrochen, sobald die Frist (`deadline`) abläuft oder `cancelFunc` aufgerufen wird
  (Zeitstempel-basiert);
* `context.WithTimeout(parent context.Context, timeout time.Duration) (context.Context, context.CancelFunc)`
  — ähnlich wie `context.WithCancel()`.
  Dieser Kontext wird entweder in `timeout` (beispielsweise `3*time.Second`) oder nach dem Aufruf von `cancelFunc` abgebrochen, je nachdem, was als Erstes stattfindet
  (Dauer-basiert);
* `context.WithoutCancel(parent context.Context) context.Context`
  — ein Kontext, der alle Werte des `parent`-Kontexts übernimmt, kann aber nicht abgebrochen werden.
  Ein solcher Kontext kann in HTTP-Handlern benutzt werden, wo der Request bereits abgebrochen wurde, aber alle wichtigen Daten noch gespeichert werden müssen.
  Cleanup-Operationen können auch unter dem `context.WithoutCancel()` durchgeführt werden.

