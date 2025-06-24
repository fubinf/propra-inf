title: "linkcheck mit mehreren Warteschlangen" 
stage: beta
timevalue: 1.0
difficulty: 3
requires: linkcheck-fullscreen
---

[SECTION::goal::product]
Ich mache den Linkprüfer potenziell um ein Mehrfaches schneller. 
[ENDSECTION]

[SECTION::background::default]
Das `--ratelimit` dient dazu, den einzelnen angesprochenen Server nicht zu überlasten
(manche Server würden einen dann sogar aussperren).
Aber wenn es mehrere verschiedene Server anzufragen gibt, könnte man die Begrenzung auf jeden
davon einzeln anwenden und also ein mehrfaches an Requests pro Zeiteinheit losschicken.
Das tun wir in dieser Aufgabe.
[ENDSECTION]


[SECTION::instructions::loose]
Wir arbeiten weiter an der Datei `linkcheck.py`.

Wir wollen, dass `State.maxfreq` für jeden Server in unserer `State.queue` separat gilt,
nicht für die ganze Warteschlange auf einmal.
Dafür teilen wir die Warteschlange in viele Warteschlangen auf.

[ER] Ändern Sie `queue` in `queues: dict[str, collections.deque[QEntry]]`.
Das bildet von einem Servernamen ab auf eine Warteschlange (wie gehabt).

[ER] Passen Sie alle bisherigen Benutzungen von `queue` entsprechend an.
Das betrifft als erstes `queue_length`, `enqueue()`, `dequeue()`.
Bei `enqueue()` muss man eine neue Warteschlange anlegen, wenn es sie noch nicht gibt
(allerdings nur, wenn unser Lauf ein Aufruf mit `--mode multiqueue` ist; 
 andernfalls arbeiten wir weiter nur mit einer Warteschlange);
bei `dequeue()` muss man sie löschen, wenn sie leerläuft.

[ER] `check_one_block()` iteriert nun also nicht nur einmal bis `maxfreq`,
sondern einmal für jeden Server. 
Schreiben Sie eine Hilfsoperation `State.servers()`, 
um diese äußere Schleife mit Werten zu versorgen.
Bedenken Sie, dass die Liste der Server sich unterwegs ändern kann.
<!-- time estimate: 40 min -->

Das war schon alles für diese potenziell gewaltige Verbesserung!

[EQ] Was vermuten Sie, wie viele Male so schnell die Linkprüfung laufen wird,
wenn Sie den Lauf für die ProPra-Homepage aus Aufgabe [PARTREF::linkcheck-core]
mit der Option `--mode multiqueue` wiederholen? 
Wie kommen Sie auf diesen Wert?

[EC] Führen Sie diesen Lauf durch.
Verwenden Sie auch `--fullscreen`, um die informative Summenzeile zu bekommen.
Beobachten Sie diese beim Ablauf.

[EQ] Vergleichen Sie die Zeiten. 
Wie viele Male so schnell war die neue Version wirklich?
Wie erklären Sie sich die Abweichung?
[ENDSECTION]


[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Fokus auf den Probelauf]
Wenn die bisherigen linkcheck-Aufgaben OK waren, relaxen wir hier bei der Kontrolle
und erwarten, dass auch hier alles glattgeht.
### Markdown
[INCLUDE::ALT:linkcheck/linkcheck-multiqueue.md]

### Quellcode (gültig zugleich für mehrere der linkcheck-Aufgaben) 
siehe [TREEREF::linkcheck/linkcheck.py]

### Kommandoprotokoll
(aber das gilt nur als Beispiel; die Probleme müssen natürlich alle nicht mehr aktuell sein)
[PROT::ALT:linkcheck/linkcheck-multiqueue.prot]
[ENDINSTRUCTOR]
