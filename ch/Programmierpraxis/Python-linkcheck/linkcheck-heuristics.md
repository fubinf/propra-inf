title: "linkcheck mit weniger vermeidbaren Abrufen"
stage: beta
timevalue: 2.0
difficulty: 3
requires: linkcheck-fullscreen
---

[SECTION::goal::product]
Ich vermeide manche Abrufe des Linkprüfers durch heuristische Regeln.
[ENDSECTION]


[SECTION::background::default]
Wenn man `https://www.someserver.org` schon geprüft hat, lohnt es dann noch, 
`http://www.someserver.org` zu prüfen (also das gleiche per unverschlüsseltem HTTP)?
Theoretisch kann das zwar schiefgehen, praktisch ist das aber selten und man kann manchmal
riesige Mengen von Abrufen einsparen, wenn man es weglässt.
Solche Regeln gibt es noch mehr und die werden wir hier unserem Linkprüfer beibringen.
[ENDSECTION]


[SECTION::instructions::loose]

### Die Optionen `-H`, `-Q`, `-S`

Wir hatten in [PARTREF::linkcheck-getlinks] obige drei Optionen eingeführt,
die wir noch nicht realisiert haben.
Lesen Sie deren Beschreibung und vollen Namen in jener Aufgabe nochmal nach.


### `-H` / `--ignore-httpsness`

Wir arbeiten weiter an `linkcheck.py`.

[ER] Führen Sie eine Klasse `Heuristics` ein, die mit den drei Bool-Werten für diese Optionen
initialisiert wird und diese speichert:  
`__init__(self, ignore_queryargs: bool, ignore_httpsness: bool, guess_from_suffix: bool)`  
(Der Name `suffix` für ist `-S` ist zu nichtssagend, deshalb weichen wir davon ab.)

[ER] Führen Sie darin eine Methode `canonical_form_of(self, url: URL) -> str` ein.
Diese benutzt wie gehabt `urllib.parse.urlparse(url)` und baut URLs um,
indem sie `https://` durch `http://` ersetzt, wenn (und nur wenn) `ignore_httpsness` eingestellt ist.  
Widerstehen Sie der Versuchung, das mit String-Ersetzung zu erledigen,
denn für `-Q` brauchen wir `urlparse` sowieso noch und solche Bibliotheksoperationen
sind in der Regel die bessere Lösung.
Sie berücksichtigen Spezialfälle, an die man selbst nicht denkt.

[ER] Fügen Sie ein `Heuristics`-Objekt dem `State`-Objekt zu und 
initialisieren Sie es passend beim Erzeugen des `State`-Objekts.

[ER] Rufen Sie `canonical_form_of()` passend in `enqueue()` und `dequeue()` auf.
Dafür könnten Hilfsoperationen nützlich sein, etwa ein Prädikat `outcome_is_known()`
und eine Speicheroperation `record_outcome()`, 
falls Sie derartige Funktionen nicht ohnehin längst haben.
<!-- time estimate: 30 min -->


### `-Q` / `--ignore-queryargs`

(Falls Sie nicht wissen, was "query parameters" bei URLs sind, <!-- TODO 3 PARTREF HTTP-Queryparams ergänzen --> 
lesen sie das auf
[HREF::https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Query]
nach.)

[ER] Erweitern Sie `canonical_form_of()`:
Wenn (und nur wenn) `ignore_queryargs` gesetzt ist,
lassen Sie beim Wiederzusammensetzen des URLs aus den von `urllib.parse.urlparse()`
gelieferten Einzelteilen den `query`-Teil weg.
<!-- time estimate: 15 min -->


### `-S` / `--suffix`

[ER] Fügen Sie in `Heuristics` ein Prädikat `is_likely_not_html(url: URL) -> bool` zu.
Dieses soll den Suffix im Pfadteil des URLs betrachten, falls es einen gibt.
Es liefert `True`, wenn der Suffix höchstwahrscheinlich zu einer Ressource gehört,
die keine HTML-Seite ist.  
Beispielsweise sind `*.pdf`-URLs von dieser Art.  
Umgekehrt sind `*.php`-URLs es _nicht_, denn eine PHP-Quellcodedatei (auf die dieser Suffix
verweist) ist zwar keine HTML-Seite, aber viele mit 
[PHP](https://en.wikipedia.org/wiki/PHP) gebaute Webauftritte benutzen URLs, 
in denen der Dateiname des für die Erzeugung zuständigen PHP-Moduls angegeben ist.

[ER] Wir streben bei der Liste dieser Suffixe keine Vollständigkeit an.
Suchen Sie 6-10 Suffixe, die Sie für sicher halten 
(also: Es gibt (fast) keine HTML-Seiten, deren URL solch einen Suffix hat) und 
die Sie zugleich als häufig einschätzen 
(also: Auf HTML-Seiten gibt es viele solche Links).
Bauen Sie diese Suffixe-Liste in `is_likely_not_html()` ein.

[EQ] Nennen Sie zwei Suffixe, bei denen Sie länger überlegt haben, ob sie in die Liste gehören,
sich dann aber dagegen entschieden.

[EQ] Nennen Sie weitere zwei, bei denen Sie länger überlegt haben, ob sie in die Liste gehören,
und sich dann dafür entschieden.

[ER] Jetzt fehlt uns noch der Aufruf von `is_likely_not_html()`.
Wo passt der hin?  
Zur Unterscheidung von internen und externen Links müsste `get_page()` bei Ihnen
inzwischen schon einen bool-Parameter `head_only` oder ähnlich haben.
Für den gibt es bereits zwei Kriterien: 
Ist der URL extern?
Ist der `rtype` eine `PAGE` oder etwas anderes?  
Diese Kriterien sollte man sinnvollerweise in einer Hilfsfunktion verstaut haben,
vielleicht in dieser Art:
`use_head_only(state: State, qentry: QEntry) -> bool`.  
Dann ist diese Funktion der Ort, wo wir als drittes Kriterium nun 
`is_likely_not_html()` heranziehen.
Andernfalls führen wir so eine Hilfsfunktion erst ein und tun es dann.
<!-- time estimate: 30 min -->


### Huch, ganz vergessen: `-1` / `--nofollow`

Es gibt noch eine weitere Option, die in [PARTREF::linkcheck-getlinks] postuliert wurde,
aber anschließend noch nicht implementiert: `--nofollow`, die die Prüfung
auf die angegebene Seite beschränkt, anstatt einen ganzen URL-Baum zu durchwandern.

Zu deren Realisierung haben wir bereits das Attribut `QEntry.depth`,
das auf der Startseite auf 1 gesetzt wird und auf jeder per Link erreichten
Seite um 1 höher ist als auf der Seite, die den Link enthielt.

[ER] Realisieren Sie `--nofollow`, indem Sie  
(1) `State.maxdepth` korrekt initialisieren,  
(2) `QEntry.depth` für jedes Exemplar korrekt mitzählen und  
(3) bei `State.enqueue()` den Eintrag nur aufnehmen, wenn er die Maximaltiefe nicht überschreitet.
<!-- time estimate: 15 min -->

[EQ] Man könnte auch erst alle Einträge aufnehmen (dann bekommt man bei `--fullscreen` beeindruckende
Warteschlangenlängen zu sehen) und die Prüfung bei `dequeue()` machen.
Dann müsste man Einträge mit "zu tief"-Eigenschaft wegwerfen und `dequeue()` z.B. rekursiv aufrufen, 
bis man einen gültigen Eintrag erreicht.
Die dadurch längere Warteschlange ist kein Problem, denn diese Datenmengen sind nicht groß.
Warum ist dieser Ansatz dennoch keine gute Idee?


### Ausprobieren

Finden Sie auf den Webseiten der Universität eine Seite `xyz`, die sowohl ein paar
HTML-Links als auch ein paar Nicht-HTML-Links enthält.
(Idealerweise kommen auch Query-Parameter vor, aber das kann mühsam zu finden sein.)

[EC] `python linkcheck.py --mode mymode --fullscreen -H -Q -S -1 xyz`  
Benutzen Sie als `mymode` die schnellste Betriebsart, die sie bislang realisiert haben.

[EC] `python linkcheck.py --mode mymode --fullscreen -1 xyz`  
Hier müsste die Zahl von GET-Requests nun größer sein.
<!-- time estimate: 15 min -->

[EQ] Unter welchem Commit-Hash ist der aktuelle Stand von `linkcheck.py` zu finden?

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Wenig streng prüfen]
[INCLUDE::ALT:linkcheck-heuristics.md]
[TREEREF::linkcheck/linkcheck.py]
[ENDINSTRUCTOR]
