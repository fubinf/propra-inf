title: Zeiger
stage: draft
timevalue: 1
difficulty: 2
requires: GoIDE, GoVariablesAndPrimitives, GoFunctions, GoStructs
---

[SECTION::goal::idea]
Ich verstehe, was Zeiger sind und wo ich sie benutzen soll.

[ENDSECTION]

### Was ist ein Zeiger?

Rudimentär gesehen ist ein Zeiger nichts anderes, als die Nummer (Adresse) von der Speicherzelle, wo sich der Wert befindet.
Zeiger in Go sind einigermaßen sicher, da sie keine Zeigerarithmetik unterstützen (sie ist zwar möglich, aber umständlich).

Zwei wichtige Operationen:

* `&` kann als "Adresse von" gelesen werden. `&x` - "Adresse von x"
* `*` kann als "Wert an/von" gelesen werden. `*addr` - "Wert an Adresse `addr`"

Mithilfe von diesen zwei Operatoren können wir die Werte verändern, ohne auf die Variable selbst zuzugreifen.

Ein Beispiel:
```go
x := 10
addrX := &x         // "addrX" beinhaltet "Adresse von x"
*addrX = 20
fmt.Println(x)      // 20
```

Zeiger sind eine Datentyp-Familie. Ein solcher Typ besteht aus dem Datentypen, auf den "gezeigt" wird, mit dem `*`-Sternchen vorne:
```go
var intPtr *int
var stringPtr *string
var userPtr *User
```

### Wo soll man Zeiger benutzen?

Der beste Anwendungsfall für die Zeiger hängt mit dem Thema "pass-by-reference" zusammen. Betrachten Sie das folgende Beispiel:
```go
type User struct {
    accountName string
    email       string
}

func updateAccountName(user User, newName string) {
    user.accountName = newName
}

func main() {
    user := User{
        accountName: "defaultName",
        email: "defaultEmail@me.com",      
    }
    
    fmt.Println(user)                       // {defaultName defaultEmail@me.com}
    updateAccountName(user, "newName")
    fmt.Println(user)                       // {defaultName defaultEmail@me.com}
}
```

Was ist passiert? Die Funktion `updateAccountName()` hat nur eine Kopie der ursprünglichen Struktur bekommen. 
Das nennt sich "pass-by-value". Wenn wir die Struktur mutieren wollen, müssen wir der Funktion einen Zeiger auf die Struktur übergeben.
Das ist ebenfalls "pass-by-value". In dem Fall wird jedoch __die Adresse__ kopiert, was in Ordnung ist.

```go
type User struct {
    accountName string
    email       string
}

func updateAccountName(user *User, newName string) {
    user.accountName = newName
}

func main() {
    user := User{
        accountName: "defaultName",
        email: "defaultEmail@me.com",      
    }
    
    fmt.Println(user)                       // {defaultName defaultEmail@me.com}
    updateAccountName(&user, "newName")
    fmt.Println(user)                       // {newName defaultEmail@me.com}
}
```

Eine verbreitete Praxis ist es, solche Strukturen gleich bei dem Initialisieren zu Zeigern umzuwandeln:
```go
user := &User{
    ...
}
```

[SECTION::submission::snippet]
[ENDSECTION]

[INSTRUCTOR::Lösungen]

[ENDINSTRUCTOR]
