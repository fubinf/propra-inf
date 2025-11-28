# Prompts für die Bearbeitung von ProPra-Text mit LLMs


## Verwendungsweise

Die nachfolgenden Prompts sind modular, man benutzt also in der Regel für einen konkreten
Prompt mehrere davon zusammen.

Typischer Aufbau eines konkreten Prompts:  
Kontext  
Anweisung 1  
Anweisung 2  
ProPra-Text-Ausschnitt

Man macht sich also für jede Anweisungsart (z.B. Sprachkorrektur) eine Datei, 
in die man die entsprechenden Abschnitte kopiert (z.B. A, B1, C, aber ohne die Überschriften)
und kopiert dann für jede Anwendung seinen zu bearbeitenden Aufgabentext(-teil) zwischen
die beiden Marker und pastet den so enstandenen Gesamt-Dateiinhalt in einen LLM-Prompt.

## A. Kontext

Der nachfolgende Text ab nach der Zeile "PROPRA-TEXT ANFANG" bis vor die Zeile "PROPRA-TEXT ENDE"
gehört zu einer Lehrveranstaltung "Programmierpraktikum" im Rahmen
eines Bachelorstudiengangs Informatik und beschreibt (Teile von) Aufgaben, die die Studierenden
selbständig bearbeiten sollen.
Die Sprache sollte dementsprechend gewählt sein: Präzise, unter Beachtung üblicher Fachterminologie,
aber ansonsten eher einfach; jedenfalls nicht komplizierter als nötig.
Der Text verwendet Markdown-Notation; diese sollte erhalten bleiben, aber nötigenfalls auch 
Gegenstand der Überarbeitung sein.
Es handelt sich um erweitertes Markdown. Ausdrücke mit folgenden Formen sind Makroaufrufe:
- [MYMACRO]
- [ENDMYMACRO]
- [OTHERMACRO::bezeichner]
- [YETOTHERMACRO::mehrere Wörter Text]
- [MACRO5::argument1::argument2]

Solche Makroaufrufe sollten in der Regel unverändert bleiben.
Allenfalls Argumente mit Text aus mehreren Wörtern können ggf. mit angepasst werden.

Drei dieser Makros jeweils einen Absatz ein, in dem eine einzelne konkrete Aufgabe gestellt wird:
[EQ] ("Question") ist ein Absatz mit einer Sachfrage oder Reflektionsfrage.
[EC] ("Command") ist ein Auftrag, wo die Studierenden ein Kommando (evtl. mehrere) auf der 
Unix-Kommandozeile ausführen sollen.
[ER] ("Requirement") ist ein Auftrag, das Programm zu ergänzen oder zu modifizieren, um das es in dieser Aufgabe geht.


## B. Anweisungen

Von den hiesigen Unterabschnitten benutzt man einen, aber nicht mehrere zugleich.


### B.1. Anweisung: Sprachkorrektur

Korrigiere in dem Text Fehler bei Orthografie und Zeichensetzung.
Vereinfache unnötig komplexe Satzkonstruktionen, insbesondere durch Anwendung der folgenden Konstruktionen:
- Satzanteile ohne eigenen Sinngehalt ggf. weglassen
- Unschöne Passivkonstruktionen durch Aktiv ersetzen
- Unnötig lange Sätze in kürzere zerlegen (aber bitte kein Stakkato-Stil)
- Tiefe Schachtelsätze möglichst "flachklopfen", in dem die Aspekte der Reihe nach besprochen werden
- Sätze mit längeren Aufzählungen (ab drei langen oder vier mittellangen Elementen) in Spiegelstrich-Listen verwandeln.
  Unser Markdown-Prozessor benötigt vor dem ersten Spiegelstrich eine Leerzeile.

Wir sprechen die Studierenden mit "Sie" und im Imperativ (bzw. mit Fragen) an.
Vorsicht bei Änderungen der Wortwahl: Wir benutzen viele technische Ausdrücke, die nicht
variiert werden dürfen.
Sei nicht übereifrig: Wenn ein Satz akzeptabel aussieht, darf er so bleiben; 
wir streben keine Perfektion an, sondern nur die Vermeidung deutlicher Mängel.


## C. ProPra-Text

Führe nur diese Anweisungen aus, gebe keine zusätzlichen Erläuterungen.
Deine Ausgabe ist also bitte ausschließlich der überarbeitete Text.

PROPRA-TEXT ANFANG

PROPRA-TEXT ENDE


