title: "linkcheck ohne Warten auf jede einzelne Antwort"
stage: beta
timevalue: 4.0
difficulty: 4
explains: async, await
requires: linkcheck-multiqueue
---

[SECTION::goal::product,idea,trial]

- Ich lerne die Grundzüge der asynchronen Programmierung in Python kennen und
- mache damit meinen Linkprüfer nochmals weitaus schneller 
[ENDSECTION]


[SECTION::background::default]
Die meiste Zeit verbringt unser Linkprüfer mit Warten darauf, dass die Antwort eines Servers
ankommt. 
Je weiter die Server weg sind (mehr Latenzzeit), desto höher wird dieser Anteil.
Wenn ein Server gar nicht antwortet, wird es richtig gruselig, denn dann passiert sehr lange
(meist 30 Sekunden) gar nichts, bis es zum Timeout kommt.

Könnte man nicht mehrere Anfragen losschicken und dann erst auf die Antworten warten?
Man kann! Wie es geht, lernen wir hier.
[ENDSECTION]


[SECTION::instructions::tricky]

### Grundkonzepte aneignen

Lesen Sie sich in die Konzepte der asynchronen Programmierung mit `async`/`await` in Python ein.
Suchen Sie selbst nach einer guten Quelle.
Achtung: Es gibt zahlreiche Quellen, aber die meisten sind nicht gut, weil sie die Grundideen
nicht herausarbeiten.

Hier sind die wichtigsten Grundideen in kurz und vereinfacht:

- Das **Ziel** ist, nicht auf den Abschluss einer Ein-/Ausgabe (hier: HTTP GET Request) zu warten,
  sondern in der Zwischenzeit andere Aufgaben voranzutreiben (hier: weitere HTTP-Requests
  losschicken oder Seiteninhalte durcharbeiten und Links daraus extrahieren).
- Das zentrale Programmierkonstrukt dafür ist die **Koroutine (coroutine)**:
  Ein Unterprogramm, dass an beliebigen Stellen die Kontrolle abgeben kann, auf dass eine andere
  Koroutine fortgesetzt werde, und später an der gleichen Stelle im Ablauf weitermachen kann.
  Der Zustand (Programmzeiger und lokale Variablen) in der Koroutine bleibt also in der
  Zwischenzeit erhalten.
- **`async def getpage(url: str) -> str`** definiert eine Python-Funktion `get()` als Koroutine.
  Der Aufruf `coro = getpage("https://google.com")` liefert in `coro` dann nicht etwa einen String, 
  sondern ein Objekt vom Typ `typing.Coroutine[Any,Any,str]`.
- Mit **`html = await coro`** bittet man das Laufzeitsystem, dieses Koroutinen-Exemplar bei Gelegenheit
  auszuführen und bei jedem Warten auf Ein-/Ausgabe mit anderen Koroutinen-Exemplaren abzuwechseln
  (event loop).
- Ein solches Laufzeitsystem liefert das Modul **`asyncio`** aus der Standardbibliothek.
- Eine Koroutine gibt die Kontrolle bei jedem `await` ab, insbesondere also dann, 
  wenn sie eine andere Koroutine aufruft. 
  Das gilt also stets quasi als Warten auf Ein-/Ausgabe.
- In unserem Fall könnte `getpage()` zum Beispiel `ClientSession.get()` aus der externen Bibliothek
  **`aiohttp`** aufrufen, was einen HTTP-GET-Request als Koroutine realisiert.
- Nur eine Koroutine kann eine andere Koroutine aufrufen; 
  in einer normalen Funktion ist `await` unzulässig.
  Wie macht man unter diesen Umständen den ersten Koroutinen-Aufruf?
  Um in die Koroutinen-Welt hineinzukommen, benutzt man **`asyncio.run(coro)`**.
  Außerhalb von Koroutinen ist also `asyncio.run()` der Ersatz für `await`.
- Bis hierhin würde das Ganze noch keinen Zusatznutzen bringen, denn die oben erwähnten
  "anderen Koroutinen" mit denen man sich abwechseln könnte, gibt es gar nicht:
  Während `ClientSession.get()` darauf wartet, dass die Antwort kommt, ist einzig
  `getpage()` als andere Koroutine aktiv -- aber die wartet darauf, dass `ClientSession.get()`
  fertig wird, und kann also auch nichts machen. 
  Unser Programm wartet also _doch_ auf das Ende des Requests.
- Um das zu ändern, müssen wir Koroutinen losschicken, _ohne_ darauf zu warten.
  Das erledigt `asyncio.create_task(coro)`.
- Ganz wichtig: Unser bisheriges "Warten auf das Ende der aktuellen Sekunde"
  dürfen wir jetzt nicht mehr mit `time.sleep()` realisieren, sondern mit -- genau! -- einer
  speziellen Koroutine für diesen Zweck: `asyncio.sleep()`, damit die erzeugten Tasks
  ihre Chance bekommen und abgearbeitet werden, anstatt sich nur anzusammeln.

[EQ] Welche 2 Quellen haben Sie gefunden, die schlecht waren, um ein Verständnis zu erlangen?
Was war jeweils der _konkrete_ Mangel daran?
Bitte geben Sie für beide Fragen URLs und weitere Ortsangaben an.

[EQ] Welche Quelle(n) hat oder haben es dann gebracht?
Wodurch waren die besser?
<!-- time estimate: 60 min -->


### Erste Koroutine: `linkchecker_async()`

Stellt man ein bisher sequentielles Programm auf asynchrone Programmierung um,
muss man regelmäßig diverse Funktionen in einer Aufrufverschachtelung auf `async` umstellen,
vom äußersten Aufruf, wo auf Ein-/Ausgabe nicht abgewartet werden soll, bis zu dem oder den innersten.
Ob man damit innen oder außen anfängt, ist Geschmackssache.
Wir fangen außen an.

Wir lassen bei uns jeweils die bisherige Funktion `xyz()` stehen (denn `--mode ratelimit` und 
`--mode multiqueue` sollen weiter funktionieren) und ergänzen die neue als `xyz_async`.

[ER] Kopieren Sie `def linkcheck()` nach `async def linkchecker_async()`.
Machen Sie folgende Anpassungen:

- Installieren und importieren Sie `aiohttp`, die asynchrone HTTP-Bibliothek.
  Sie ersetzt im Modus `async` die Verwendung von `requests`.  
  [Dokumentation von aiohttp](https://docs.aiohttp.org)
- Extrahieren Sie ggf. alle Initialisierungsschritte am Anfang in eine separate Funktion
  `linkchecker_prepare()`.
- Extrahieren Sie ggf. alle Nachbereitungsschritte am Ende in eine separate Funktion
  `linkchecker_finalize()`.
- Legen Sie eine `aiohttp.ClientSession` an und lesen Sie nach, was es damit auf sich hat.
  Speichern Sie sie im `State`-Objekt.
- Ersetzen Sie den bisherigen Schleifenrumpf durch 
  `await check_one_block_async(state)` plus `await wait_for_end_of_second_async(state)`.

[ER] Rufen Sie das in `execute()` im Zweig für `--mode async` auf mittels `asyncio.run()`.

Vielleicht dämmert Ihnen schon eine Eigenschaft solcher Umstellungen:
Das ist unterwegs leider nicht gerade besonders einfach zu testen.
<!-- time estimate: 30 min -->


### `check_one_block_async()`, `State.request_add()`, `State.request_done()`

[ER] Implementieren Sie `check_one_block_async()` wie folgt:

- Lagern Sie ggf. den Kernteil (1 Seite abrufen und verarbeiten) aus in eine Koroutine
  `check_one_url_async()`.
- Dies ist die Stelle, wo wir unsere Parallelität erzeugen wollen, damit es überhaupt mehrere 
  Koroutinen-Exemplare gibt, zwischen denen gewechselt werden kann.
  Deshalb müssen wir `check_one_url_async()` mittels
  `asyncio.create_task()` aufrufen anstatt einfach mit `await`.
- Wir erzeugen zwar mit der aktuellen Logik nur `maxfreq` neue Requests pro Server,
  aber falls die lange dauern, könnten sich sehr viele davon ansammeln.
  Das wollen wir verhindern und maximal `2*maxfreq` Requests pro Server gleichzeitig offen haben.
- Dafür bauen wir ein paar von Operationen `request_add()`/`request_done()` in `State`,
  die mitzählen: Wir rufen `request_add()`, wenn wir einen Request losschicken und 
  `request_done()` wenn er fertig ist.  
  `request_add()` zählt entweder für diesen Server um 1 hoch und liefert `True` oder,
  wenn die `2*maxfreq` Requests für diesen Server gerade ausgeschöpft sind, liefert `False`.
  `requests_done()` zählt 1 herunter und löscht den Zähler, wenn er bei 0 ankommt.  
  Die Zähler speichern wir in einem Attribut `State.requests_underway: dict[str, int]`.  
  Den Wert `2*maxfreq` speicher wir der Klarheit halber in `State.servercapacity`.
- Nicht wundern: den Aufruf von `request_done()` schreiben wir erst gleich hin.
<!-- time estimate: 30 min -->


### `wait_for_end_of_second_async()`

[ER] Implementieren Sie `wait_for_end_of_second_async` wie oben erwähnt.
<!-- time estimate: 10 min -->


### `check_one_url_async()`

[ER] Implementieren Sie `check_one_url_async()` wie folgt:

- Wie schon oben: Lagern Sie den Teil, den `check_one_url()` und `check_one_url_async()`
  gemeinsam haben, in eine separate Funktion `process_page` aus.
- Realisieren Sie den eigentlichen Seitenabruf als `await get_page_async()`.
<!-- time estimate: 10 min -->


### `get_page_async()`

[ER] Implementieren Sie `get_page_async()` wie folgt:

- Die eigentlichen Abrufe erfolgen jetzt mit `await state.aiosession.head(url)` oder
  `await state.aiosession.get(url)`.
  Das Resultat ist nun eine `aiohttp.ClientResponse`, die deutlich anders funktioniert als
  die Response bei `requests`.
- Die bisherigen Ausgaben mit `report_url()` vor dem Request und `report_url_outcome()` danach
  funktionieren jetzt nicht mehr, weil in der Regel mehrere Requests losgeschickt werden, bevor
  die erste Antwort kommt.
  Wir lassen `report_url()` einfach weg.
  (Wenn Ihr Programm nicht richtig funktioniert und Sie Debugging-Ausgaben brauchen,
  kann eine Variante von `report_url_outcome()` hilfreich sein.)
<!-- time estimate: 60 min -->


### Korrekter Abschluss des Linkprüfens

Bisher war es so, dass bei leerer Warteschlange alles erledigt war,
denn wir haben jede Seite direkt fertig verarbeitet, wenn wir sie aus der Warteschlange geholt haben.
Das ist jetzt nicht mehr so: Die zugehörigen Requests sind eventuell (sogar meistens) noch unterwegs!

[ER] Ergänzen Sie in `linkchecker_async()` eine zweite Schleife, die so lange 
`wait_for_end_of_second_async()` wiederholt, bis keine Tasks mehr anhängig sind.
<!-- time estimate: 20 min -->


### Einsatz

[EQ] Was vermuten Sie, wie viele Male so schnell die Linkprüfung laufen wird,
wenn Sie den Lauf für die ProPra-Homepage aus Aufgabe [PARTREF::linkcheck-multiqueue]
mit der Option `--mode async` wiederholen? 
Wie kommen Sie auf diesen Wert?

[EC] Führen Sie diesen Lauf durch.
Verwenden Sie auch `--fullscreen`, um die informative Summenzeile zu bekommen.
Beobachten Sie diese beim Ablauf.

[EQ] Vergleichen Sie die Zeiten. 
Wie viele Male so schnell war die neue Version wirklich?
Wie erklären Sie sich die Abweichung?
<!-- time estimate: 20 min -->
[ENDSECTION]


[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Schneller? `get_page_async()` plausibel?]
Diese Aufgabe genau zu kontrollieren wäre schwierig.
In der Erwartung, dass sich hier ohnehin nur Könner_innen hintrauen, prüfen wir nur drei Belange:

- Taugen die Antworten auf [EREFQ::1] etwas? Wir wollen jeweils eine Grundidee hören, die 
  in der angegebenen Quelle nicht erwähnt oder nicht verständlich genug ist.
- Ist die Laufzeit gegenüber dem Kommandoprotokoll von [PARTREF::linkcheck-multiqueue] nennenswert
  gesunken? 20% sollten es schon sein.
- Sieht der Programmcode von `get_page_async()` plausibel aus, wenn man ihn mit der Musterlösung in 
  [TREEREF::linkcheck/linkcheck.py] vergleicht?
[ENDINSTRUCTOR]
