---
description: Begutachte eine Task oder eine Taskgroup-Indexseite
---

# Aufgaben-Review

Reviewe die in $ARGUMENTS angegebene Aufgabendatei (oder Taskgroup-Indexseite).
Lies zuerst die Datei, dann wende die untenstehenden Heuristiken an.
Gib die Ergebnisse in GitHub-Markdown-Syntax in zwei Listen aus 
(schwerwiegend, geringfügig, je mit H3-Überschrift, durchgehend wie eine einzige Liste nummeriert),
mit gerade genug Erläuterung, um das Problem zu verstehen.
Nenne bei jedem Befund die Zeilennummer(n).
Beginne jeden Satz auf einer neuen Zeile und packe den ganzen Satz auf diese Zeile.
Setze technische Syntax in Backquotes.

Falls ein URL mit angegeben ist, sollte das die zur Aufgabe gehörige Issue sein.
Rufe diese ab und prüfe, ob die ggf. dort behaupteten letzten Nachbesserungsschritte
passend erfolgt sind.
Weise auf Kritikpunkte aus einem ggf. früheren Review nur dann erneut hin,
wenn sie bei der Überarbeitung gar nicht beachtet wurden oder grob unzureichend
korrigiert worden sind -- wir wollen eine "im Wesentlichen gute" Aufgabenqualität erreichen,
nicht eine perfekte. 
Ein Vergleich der Aufgabe mit früheren Dateirevisionen in git sollte i.d.R. nicht nötig sein.

---

## A. Inhaltliche Probleme

### A1. Schwierigkeitsgrad und Anleitung

**A1.1 Schwierigkeitsgrad muss zu den tatsächlichen Anforderungen passen.**
Prüfe, ob der deklarierte `difficulty`-Wert zum Umfang der Anleitung, zur Anzahl neuer Konzepte
und zur Komplexität passt.
Schwierigkeitsgrad 2 ("leicht") bedeutet schrittweise Anleitung mit Dokumentationsverweisen
und [HINT]-Blöcken für schwierigere Schritte.
Wenn die Aufgabe eigenständiges Problemlösen erfordert, kann sie nicht Schwierigkeitsgrad 2 sein.

**A1.2 Leichte Aufgaben müssen schrittweise anleiten.**
Bei Schwierigkeitsgrad 2 erwarten Studierende, "mit einem wohlgeformten Löffel gefüttert" zu werden.
Jedes neue Syntaxelement, jeder API-Aufruf und jedes Konzept muss gezeigt oder verlinkt werden.
Nicht davon ausgehen, dass Studierende Nicht-Triviales selbst herausfinden können.
Falls ein Schritt schwächere Studierende blockieren könnte, einen [HINT] hinzufügen.

**A1.3 HINT-Blöcke für nicht-offensichtliche Schritte.**
Jeden Arbeitsschritt prüfen: Könnte eine schwächere Person hier hängenbleiben?
Falls ja, gibt es einen [HINT]?
HINT-Titel sollten das Symptom der Studierenden beschreiben
(z.B. "Ich verstehe nicht, was X bedeutet"), nicht Themenbezeichnungen sein.

**A1.4 Stoffmenge muss zum Schwierigkeitsgrad passen.**
Bei leichten Aufgaben den Umfang auf die wichtigsten und gebräuchlichsten Punkte beschränken.
Erschöpfende Listen überfordern Studierende und verwässern den Fokus.

### A2. Konzeptuelle Klarheit und Korrektheit

**A2.1 Technische Aussagen müssen sachlich korrekt sein.**
Definitionen, Erklärungen und technische Aussagen auf Präzision und Richtigkeit prüfen.
Häufige Fehler: Wert mit Variable verwechseln, Methode mit Funktion, Ausdruck mit Befehl;
Aussagen, die der Sprachspezifikation widersprechen; invertierte API-Beziehungen.
Was überraschend klingt, nachschlagen.

**A2.2 Jedes neue Konzept muss vor der Verwendung eingeführt werden.**
Kein Fachbegriff, Schlüsselwort oder Konzept darf unerklärt auftauchen.
Falls es nicht durch eine Voraussetzungs-Aufgabe (`assumes`/`requires`) abgedeckt ist,
muss es hier erklärt oder ein Dokumentationslink angegeben werden.
Die gesamte assumes/requires-Kette prüfen.

**A2.3 Halb eingeführte Konzepte erzeugen kognitiven Stress.**
Kein fortgeschrittenes Konzept beiläufig erwähnen ("Sie lernen mehr über X später"),
ohne es hinreichend zu erklären.
Entweder ausreichend erklären oder die Erwähnung ganz entfernen.

**A2.4 Unerklärte Notation in Codebeispielen.**
Codebeispiele auf Notation prüfen, die Anfänger nicht kennen könnten
(z.B. printf-Formatspezifizierer, Regex-Syntax, fortgeschrittene Kurzschreibweisen).
Solche Notation muss erklärt oder auf Dokumentation verlinkt werden.

**A2.5 Korrekte Fachterminologie.**
Auf unpräzise Sprache prüfen: "Methode" vs. "Funktion", "Ausdruck" vs. "Befehl",
"Eigenschaft" vs. "Methode".
Unpräzision beschädigt mentale Modelle.

**A2.6 Definitionen und Erklärungen müssen präzise sein, nicht schwammig.**
Vage Erklärungen, die ein falsches Verständnisgefühl erzeugen, sind schlimmer als keine.
Wenn ein Konzept erklärt wird, muss die Erklärung einer sorgfältigen Prüfung
auf dem gewählten Detailniveau standhalten.

**A2.7 Externe Quellen dürfen keine irreführenden Aussagen enthalten.**
Beim Verlinken von Blogposts oder Artikeln prüfen, ob die Quelle zweifelhafte Aussagen enthält.
Falls problematisch, entweder die Quelle ersetzen oder als Übung zum kritischen Lesen umrahmen.

### A3. Aufgabenstruktur und Didaktik

**A3.1 Praxis vor Theorie (in einem Praktikum).**
Wenn eine Aufgabe Theorie und Praxis umfasst, erwägen, ob Praxis-zuerst motivierender wäre.
Studierende experimentieren erst, dann verstehen sie.
Lange Theorieblöcke vor jeder Praxis sind demotivierend.

**A3.2 Übungen zwischen erklärenden Text einstreuen.**
Lange Textstrecken (> ~1 Seite) ohne [EQ]-, [EC]- oder [ER]-Marker vermeiden.
Übungen sollten bald nach Einführung des zugehörigen Konzepts erscheinen.

**A3.3 Fragen müssen echtes Lernen bewirken.**
Jedes [EQ] sollte die Lernziele voranbringen und echtes Nachdenken erfordern.
Fragen nach trivialen Fakten oder mit Antworten direkt im vorhergehenden Text
sind Beschäftigungstherapie.

**A3.4 Klausurartige Fragen sind für das ProPra ungeeignet.**
In einem Praktikum sollten Fragen aus dem Tun entstehen, nicht aus Auswendiglernen.
Fragen bevorzugen, bei denen Studierende erst etwas ausprobieren
und dann über das Geschehene reflektieren.

**A3.5 Aufgaben müssen praktische Relevanz zeigen.**
Beim Einführen eines Konzepts erklären, warum es die Studierenden interessieren sollte.
Einen motivierenden Anwendungsfall oder praktischen Nutzen zeigen, nicht nur Mechanik.

**A3.6 Übungen müssen den Effekt des gelehrten Features sichtbar machen.**
Beim Lehren einer Kommandozeilenoption, API-Funktion oder Technik müssen die Übungsdaten
so gewählt sein, dass die Verwendung des Features sichtbar andere Ergebnisse liefert
als die Nichtverwendung.
Triviale Beispiele ohne beobachtbaren Effekt sind nutzlos.

**A3.7 Motivierende Szenarien müssen realistisch sein.**
Wenn eine Aufgabe ein Szenario als Rahmen für Übungen nutzt, muss es plausibel sein.
Unrealistische oder weit hergeholte Szenarien verwirren statt zu motivieren.

**A3.8 Beispiele müssen komplex genug sein, um das Konzept zu motivieren.**
Bei Testmethoden, Entwurfsmustern oder Analysetechniken muss das Beispiel
reichhaltig genug sein, um den Wert des Konzepts zu demonstrieren.
Trivial korrekte Beispiele untergraben das "Warum".

**A3.9 Sprachübergreifende Vergleiche müssen eingerahmt werden.**
Beim Ziehen von Parallelen zu einer anderen Sprache den Vergleich klar ankündigen.
Unbeschrifteter Code in einer anderen Sprache verwirrt.
Vergleiche ggf. in einem FOLDOUT platzieren.

**A3.10 Codebeispiele: Werte vermeiden, die mit Indizes zusammenfallen.**
In Array-/Listenbeispielen markante Werte verwenden (10, 20, 30), nicht (0, 1, 2, 3),
um Mehrdeutigkeit zwischen Werten und Indizes zu vermeiden.

### A4. Aufgabenumfang und Abhängigkeiten

**A4.1 Aufgabe muss beim angekündigten Thema bleiben.**
Eine Aufgabe sollte nicht stillschweigend umfangreiche Konzepte einführen,
die in eine eigene Aufgabe gehören.
Bei Themenausweitung entweder aufteilen oder umbenennen.

**A4.2 Zu groß gewordene Aufgaben sollten aufgeteilt werden.**
Wenn timevalue > ~1,5h oder die Aufgabe mehr als 2–3 verschiedene Konzepte abdeckt,
Aufteilung erwägen. Jede Aufgabe sollte ein zusammenhängendes Thema haben.

**A4.3 Fortgeschrittenes Material gehört nicht in Grundlagenaufgaben.**
Zu fortgeschrittenes Material für die Zielstufe sollte in eine eigene Folgeaufgabe
verschoben werden.

**A4.4 Stoff, der zu einer anderen Aufgabe gehört, muss dorthin verlagert werden.**
Grundlegende Konzepte, die Voraussetzung für mehrere Aufgaben sind,
sollten in der passenden Grundlagenaufgabe gelehrt werden,
nicht hastig als Randbemerkung abgehandelt.

**A4.5 `assumes` und `requires` korrekt unterscheiden.**
`requires` = Studierende bauen auf Artefakten der Voraussetzung auf.
`assumes` = Studierende brauchen das Wissen, aber nicht die Artefakte.
Prüfen, ob die Klassifikation zur tatsächlichen Verwendung passt.

**A4.6 Stoff aus Voraussetzungsaufgaben nicht erneut erklären.**
Wenn Material durch eine Aufgabe in `assumes`/`requires` abgedeckt ist,
nicht wiederholen. Ein kurzer Verweis genügt.

**A4.7 Fachwissenschaft nicht in einem Programmierkurs lehren.**
Aufgaben über Bibliotheken sollten lehren, wie man die Bibliothek benutzt,
nicht den zugrundeliegenden Fachbereich (Statistik, Physik, Mathematik).
Für fachlichen Hintergrund auf externe Ressourcen verlinken.

### A5. Dokumentation und Lesereferenzen

**A5.1 Dokumentationsverweise müssen spezifisch sein.**
"Lesen Sie die Dokumentation" ist unzureichend.
Jeder Verweis muss eine bestimmte Seite, einen Abschnitt oder eine Funktion nennen.
Bei Schwierigkeitsgrad 2 genaue Koordinaten angeben.
Bei Schwierigkeitsgrad 3 genügt ein Hinweis, wie man den richtigen Abschnitt findet.

**A5.2 "Lesen Sie diesen Artikel" braucht eine fokussierte Frage.**
Studierende nicht zum Lesen eines Artikels schicken ohne Leitfrage.
"Finden Sie heraus, was X bedeutet" statt nur "Lesen Sie dies."

**A5.3 Lesehinweise sollten vor der ersten Aufgabe stehen, die das Wissen erfordert.**
Studierende bei Schwierigkeitsgrad 2 müssen gesagt bekommen, was sie lesen sollen,
bevor sie etwas damit tun sollen.

**A5.4 Dokumentationslinks sollten auf stabile Versionen zeigen.**
Stable-/Release-URLs verwenden, nicht Dev-/Nightly-Versionen, die sich ändern können.

**A5.5 Verweise auf andere Aufgaben müssen [PARTREF::...] verwenden.**
Das Makro verwenden, nicht fest codierte URLs oder vage Formulierungen wie
"in der vorherigen Aufgabe".
Studierende arbeiten Aufgaben möglicherweise nicht in der erwarteten Reihenfolge.

### A6. Übungen und Einreichungen

**A6.1 Markertypen ([EC], [EQ], [ER]) müssen zur Übung passen.**
[EC] = Befehle für Befehlsprotokoll, [EQ] = Fragen für Markdown, [ER] = Codeanforderungen für Quellcode.
Falsche Marker verwirren Studierende und das Einreichungssystem.

**A6.2 Einreichungsabschnitt muss zu den tatsächlich verwendeten Markern passen.**
Nur INCLUDE-Dateien einbinden, die zu tatsächlich in der Aufgabe verwendeten Markern gehören.

**A6.3 Programmierübungen müssen Randfall-Verhalten spezifizieren.**
Alle relevanten Fälle müssen spezifiziert werden, einschließlich Randfälle.
Mehrdeutigkeit führt zu Verwirrung.

**A6.4 Fragen im Fließtext müssen mit [EQ] markiert oder entfernt werden.**
Wenn der Text eine Frage stellt, muss sie einen [EQ]-Marker haben
oder als rhetorische Passage umformuliert werden.

**A6.5 Keine ungültigen Artefakte erzeugen lassen.**
Studierende sollten nicht aufgefordert werden, Dateien zu erstellen,
die in der Zielsprache/dem Zielwerkzeug ungültig sind.
Das widerspricht den Lernzielen.

**A6.6 Leichte Aufgaben: Variablennamen vorgeben, um die Prüfung zu erleichtern.**
Bei Schwierigkeitsgrad 2 erleichtern vorgegebene Variablennamen
die Überprüfung durch Lehrende erheblich.

**A6.7 Leichte Aufgaben: Rückmeldung zur Korrektheit ermöglichen.**
Wenn Studierende Code schreiben, aber keine Möglichkeit haben, Ergebnisse zu überprüfen
(keine erwartete Ausgabe, keine Assertion), können sie stillschweigend falsche Ergebnisse produzieren.

**A6.8 Unnötige Wahlmöglichkeiten erschweren die Bewertung.**
Wenn "Mache A oder B" zu divergierenden Pfaden führt, einen Ansatz für alle wählen,
es sei denn, die Wahlfreiheit ist selbst didaktisch wertvoll.

### A7. Instruktorenabschnitt

**A7.1 Instruktorenabschnitt muss existieren und nützlich sein.**
Jede Aufgabe braucht einen [INSTRUCTOR]-Abschnitt mit Frage-/Aufgabenlabels (F1, A1 usw.),
kurzen erwarteten Antworten und Review-Prioritäten.
Den Tutoren sagen, worauf sie sich konzentrieren sollen.

**A7.2 Offene Fragen brauchen klare Erwartungen.**
Angeben, was eine minimal akzeptable Antwort ausmacht.
Auf die zentrale Lernerkenntnis fokussieren.

**A7.3 Musterlösungen müssen instruktorenorientiert sein.**
Nicht einfach Code abladen.
Schlüsselaspekte, minimal akzeptable Lösungen und häufige Fehler hervorheben.
Marker/Annotationen verwenden.

**A7.4 Instruktorenabschnitt muss nach Überarbeitungen aktuell bleiben.**
Nach dem Bearbeiten von Aufgabenstellungen den Instruktorenabschnitt aktualisieren:
Nummerierung, Musterlösungen, Review-Hinweise.

**A7.5 Musterlösungen gehören ins altdir, nicht in die öffentliche Datei.**
Instruktorenlösungen kommen in das `altdir`-Submodul.
Die öffentliche Datei sollte nur eine INCLUDE-Direktive haben.

---

## B. Formale Probleme

### B1. Textqualität und Stil

**B1.1 Knappe Formulierung.**
Jeder Satz muss seinen Platz verdienen.
Studierende sind lesefaul.
Füllphrasen, unnötig lange Hintergrundabschnitte und wortreiche Konstruktionen streichen.

**B1.2 Nicht zu saloppen oder plauderhaften Ton verwenden.**
Sachliche, knappe Sprache verwenden.
Humor, Slang oder rhetorische Schnörkel erzeugen Mehrdeutigkeit,
besonders für Nicht-Muttersprachler.

**B1.3 Einheitliche Terminologie innerhalb und über Aufgaben hinweg.**
Innerhalb einer Aufgabe und über die Taskgroup hinweg denselben Begriff
für dasselbe Konzept verwenden.
Nicht ohne Erklärung das Vokabular wechseln.

**B1.4 Unnötige Wortfülle um Code-Bezeichner vermeiden.**
"`describe()`" schreiben, nicht "die Methode `describe()`".
Die Backtick-Formatierung signalisiert den Konstrukttyp bereits.

**B1.5 Eindeutschung englischer Begriffe.**
Keine englischen Flexionsformen ("matched") in deutschem Text verwenden.
Das deutsche Äquivalent verwenden oder an deutsche Grammatik anpassen.

**B1.6 Beschreibender Linktext, nicht generisch.**
"JavaScript-Datenstrukturen auf MDN" statt "hier".
Beschreibender Text hilft beim Überfliegen und bei der Barrierefreiheit.

### B2. Formatierung und Struktur

**B2.1 Ein Satz pro Zeile, maximal 100–120 Zeichen.**
Jeder Satz beginnt auf einer neuen Zeile.
Hyperlinks stehen auf eigenen Zeilen.
Leerzeilen nach Überschriften.
Diese Konventionen sorgen für lesbare Diffs.

**B2.2 Überschriftenebenen: sparsam und einheitlich.**
Auf Ebene 3 für mittlere Komplexität beschränken.
Zu viele Unterüberschriften machen die Aufgabe visuell unruhig.
Überschriften sollten informativ sein, nicht generisch
("Nützliche Optionen" -> "Rekursive Suche mit `-r`").

**B2.3 Backticks einheitlich für alle technischen Bezeichner verwenden.**
Alle Schlüsselwörter, Funktionsnamen, Dateipfade und technischen Bezeichner
müssen in Backticks stehen. Keine Ausnahmen.
Bezeichner in Backticks nicht flektieren (z.B. "des `DataFrame`s" vermeiden).

**B2.4 Gerenderte HTML-Ausgabe vor dem Einreichen prüfen.**
`sedrila author` ausführen und sowohl Studierenden- als auch Instruktorenausgabe inspizieren.
Kaputte Formatierung, sichtbare Backticks, defekte Links, verirrte Makronamen finden.

**B2.5 Template-/Startercode in separate INCLUDE-Dateien auslagern.**
Templates in separate Dateien extrahieren und INCLUDE verwenden,
statt sie in das Markdown einzubetten.

### B3. Benennung und Metadaten

**B3.1 Aufgabennamen müssen Projektkonventionen folgen.**
Der Dateinamenpräfix muss zur Taskgroup-Konvention passen.
Der Rest sollte sprachspezifische Konstrukte widerspiegeln.

**B3.2 Aufgabennamen müssen aussagekräftig sein.**
Der Name sollte das Thema klar vermitteln.
Vage Namen wie "misc" (wenn mehrfach verwendet) sind nicht hilfreich.

**B3.3 Zielabschnitt-Typ muss zum Lernziel passen.**
Prüfen, ob der `SECTION::goal`-Typ (product, idea, experience, trial) die Aufgabe korrekt beschreibt.

**B3.4 Timevalue braucht Schätzungen pro Abschnitt.**
Bei Aufgaben > 1h `<!-- time estimate: X min -->`-Kommentare nach jedem Abschnitt hinzufügen
und die Gesamtsumme überprüfen.

**B3.5 Taskgroup-Indexseiten sollten knapp sein.**
Kurzer Überblick plus wichtige Dokumentationslinks. Kein ausführliches Tutorial.

### B4. Qualitätssicherung durch Autoren

**B4.1 Autor muss die fertige Aufgabe selbst testen.**
Die gesamte Aufgabe von Anfang bis Ende durcharbeiten.
Befehle, Ausgaben, Links und Dateipfade müssen intern konsistent sein.

**B4.2 Glossareinträge für Schlüsselbegriffe.**
Fachspezifische Terminologie braucht Glossareinträge mit TERMREF-Links.

**B4.3 Plattformvielfalt.**
Prüfen, ob die Anweisungen auf allen unterstützten Plattformen funktionieren
(Windows/WSL, Linux, macOS). Einschränkungen deklarieren, falls nicht.

**B4.4 INCLUDE-Dateiverweise müssen auflösbar sein.**
Alle INCLUDE-Direktiven auf existierende Dateien prüfen, einschließlich altdir-Dateien.

---

*Konsolidiert aus Review-Diskussionen zu SQL-, Go-, Web-, Werkzeuge-, Bibliotheken-, C-, Python-, RegExp- und Testen-Aufgaben.*
