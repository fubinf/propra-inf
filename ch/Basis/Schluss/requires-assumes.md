title: Abhängigkeiten zwischen Aufgaben
stage: beta
timevalue: 0.5
difficulty: 2
---
[SECTION::goal::idea]

Ich verstehe, was "requires"- und "assumes"-Abhängigkeiten zwischen Aufgaben bedeuten
und kann das bei meiner Aufgabenauswahl berücksichtigen.

[ENDSECTION]
[SECTION::background::default]

Im wirklichen Leben muss man selber rausfinden, in welcher Reihenfolge man 
gegebene Aufgaben sinnvoll bearbeiten kann oder 
welches Vorwissen man dafür mitbringen sollte.

Im ProPra machen wir es Ihnen leichter und schreiben das ausdrücklich dazu.
Beachten Sie diese Markierungen sorgfältig, 
sonst kann eine Aufgabe weitaus schwieriger werden als vorgesehen.

[ENDSECTION]
[SECTION::instructions::loose]

### assumes, assumed by

Manche Aufgaben B setzen das Wissen voraus, das man entweder in einer anderen Aufgabe A erworben 
oder schon mitgebracht hat.
Im ProPra heißt das "assumes-Beziehung".

Bevor man B macht, sollte man sich also vergewissern, dass man das Wissen,
das in A erworben wird, schon hat -- egal ob dadurch, dass man A schon bearbeitet hat,
oder als ins ProPra mitgebrachtes Vorwissen. 


### requires, required by

Manche Aufgaben B setzen das konkrete Arbeitsergebnis (z.B. Programmcode) einer anderen Aufgabe A voraus,
bauen also direkt auf A auf.
Im ProPra heißt das "requires-Beziehung".

Bevor man B machen kann, muss man also _in jedem Fall_ A bearbeiten.
Eine Einreichung von B wird nur akzeptiert, wenn man auch A einreicht oder eingereicht hat.


### Siehe Inhaltsverzeichnis

Beide Arten von Beziehungen kann man im Inhaltsverzeichnis sehen, wenn man mit dem Mauszeiger
über den entsprechenden Markierungen schwebt, die hinter einer Aufgabe zu sehen sind.
Probieren Sie dies aus.

- [EQ] Geben Sie den Namen einer Aufgabe an, die zwei oder mehr "assumes"-Beziehungen hat.
- [EQ] Geben Sie den Namen einer Aufgabe an, die drei oder mehr "assumed by"-Beziehungen hat.
- [EQ] Geben Sie den Namen dreier Aufgaben an, die miteinander eine "required"-Kette bilden,
  die man also in genau dieser Reihenfolge bearbeiten muss, wenn man die letzte davon bearbeiten will.


### Siehe die Aufgabe selbst

Öffnet man eine Aufgabe, so findet man deren Voraussetzungen oben als Hyperlinks.
Wenn einem davon etwas fehlt oder wenn man sich bei "assumes" vergewissern möchte,
kann man also sehr bequem zu den betreffenden anderen Aufgaben gelangen.

Nachlaufende Aufgaben, die die aktuelle als Voraussetzung haben,
findet man hingegen ganz unten auf der Seite.
Damit kann man also bei Interesse sofort bei etwas eng Verwandtem weiterarbeiten.

Vollziehen Sie das mit den Aufgaben Ihrer oben gefundenen "required"-Kette
nach. Starten Sie beim vorletzten Element, navigieren Sie mit den oberen Links
zurück zum Start und dann mit den unteren Links nach und nach bis zum Ende der Kette.

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Korrektheit prüfen]

Die Antworten müssen stimmen; auch Tippfehler akzeptieren wir nicht,
denn Aufgabennamen sind technische Bezeichner, z.B. in `submission.yaml`.    
Die Studis müssen sich an präzises Arbeiten gewöhnen.

[ENDINSTRUCTOR]
