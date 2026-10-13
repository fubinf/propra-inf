title: "Lasttests mit Locust: Wie viele Nutzer verkraftet mein Server?"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: Lasttest, Perzentil
assumes: http-GET, venv
---

[SECTION::goal::trial]

- Ich kann mit Locust einen einfachen [TERMREF::Lasttest] für einen Webserver schreiben
  und ausführen.
- Ich kann Durchsatz und Antwortzeiten eines Lasttests deuten
  und daraus einen Engpass des Servers begründen.

[ENDSECTION]


[SECTION::background::default]

Ein Webserver, der beim Ausprobieren flott antwortet, kann trotzdem in die Knie gehen,
sobald viele Menschen ihn gleichzeitig benutzen:
beim Vorverkauf von Konzertkarten, bei der Kursanmeldung zu Semesterbeginn
oder wenn ein Link plötzlich überall geteilt wird.
Solche Probleme findet kein Unittest, denn der prüft, ob einzelne Aufrufe das Richtige liefern,
nicht, wie schnell viele gleichzeitige Aufrufe bedient werden.

Ein Lasttest simuliert deshalb viele gleichzeitige Nutzer und misst,
wie schnell der Server antwortet und wie viele Anfragen er pro Sekunde schafft.
Locust ist ein Werkzeug dafür, in dem man das Verhalten der simulierten Nutzer
in ganz normalem Python beschreibt.

[ENDSECTION]


[SECTION::instructions::detailed]

### Der Testgegenstand: ein kleiner Webshop

Legen Sie für diese Aufgabe ein frisches [PARTREF::venv] an und aktivieren Sie es.
Installieren Sie Locust mit `pip install locust`.

- [EC] `locust --version`

Unser Testgegenstand ist ein winziger Webshop mit nur zwei Seiten:
der Startseite `/`, die sofort antwortet,
und der Suche `/search`, die für jede Anfrage eine Zehntelsekunde braucht.
In einem echten Shop würde dort eine Datenbank durchsucht; wir simulieren das mit `time.sleep`.
Der Server benutzt `HTTPServer` aus der Python-Standardbibliothek,
der die Anfragen strikt nacheinander bearbeitet.

Legen Sie die Datei `shopserver.py` mit folgendem Inhalt an:

```python
import time
from http.server import HTTPServer, BaseHTTPRequestHandler


class ShopHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = "Willkommen im Shop!\n"
        elif self.path.startswith("/search"):
            time.sleep(0.1)  # simuliert eine langsame Datenbankabfrage
            body = "Suchergebnisse\n"
        else:
            self.send_error(404)
            return
        data = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format, *args):
        pass  # keine Ausgabe pro Anfrage


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), ShopHandler)
    print("Shop läuft auf http://127.0.0.1:8000")
    server.serve_forever()
```

Öffnen Sie ein zweites Terminalfenster, aktivieren Sie dort dasselbe venv,
wechseln Sie in das Verzeichnis von `shopserver.py`
und starten Sie den Server mit `python shopserver.py`.
Lassen Sie ihn dort laufen.
Probieren Sie ihn im ersten Terminalfenster mit `curl` aus,
das eine URL abruft und die Antwort ausgibt:

- `curl http://127.0.0.1:8000/`
- `curl "http://127.0.0.1:8000/search?q=buch"`

[NOTICE]
Benutzen Sie hier `curl` und nicht den Browser.
Browser öffnen manchmal vorsorglich Verbindungen, über die sie zunächst keine Anfrage schicken.
Unser Server wartet dann auf diese Anfrage und bedient so lange niemand anderen.
[ENDNOTICE]

<!-- time estimate: 15 min -->


### Simulierte Nutzer beschreiben

In Locust beschreibt man in einer Python-Klasse, was ein typischer Nutzer tut.
Locust erzeugt davon dann beliebig viele Exemplare, die gleichzeitig arbeiten.
Jeder simulierte Nutzer wählt immer wieder zufällig einen seiner "Tasks"
(Methoden mit `@task`) aus, führt ihn aus und wartet danach eine Weile,
so wie ein Mensch, der eine Seite erst einmal liest, bevor er weiterklickt.

Lesen Sie in der Locust-Dokumentation den Abschnitt "Your first test" im Quickstart:
[HREF::https://docs.locust.io/en/stable/quickstart.html]
Lesen Sie außerdem auf der Seite "Writing a locustfile" die Abschnitte "wait_time attribute",
"host attribute" und "@task decorator":
[HREF::https://docs.locust.io/en/stable/writing-a-locustfile.html]

- [ER] Legen Sie im selben Verzeichnis wie `shopserver.py` die Datei `locustfile.py` an.
  Darin soll eine Klasse `ShopUser` die simulierten Nutzer unseres Shops beschreiben:
    - Sie greifen auf den Server `http://127.0.0.1:8000` zu.
    - Nach jedem Task warten sie zufällig zwischen 1 und 2 Sekunden.
    - Sie rufen die Startseite `/` auf.
    - Sie suchen mit `/search?q=buch`, aber nur ein Drittel so oft,
      wie sie die Startseite aufrufen.

[HINT::Wie lege ich fest, wie oft ein Task drankommt?]
`@task` kann ein Gewicht als Argument bekommen.
Ein Task mit `@task(3)` wird im Mittel dreimal so oft ausgewählt wie einer mit `@task(1)`.
[ENDHINT]

<!-- time estimate: 15 min -->


### Ein erster Test in der Weboberfläche

[WARNING]
Richten Sie Lasttests nur gegen Server, die Ihnen gehören oder deren Betreiber zugestimmt haben.
Für die Betreiber sieht ein Lasttest genauso aus wie ein Angriff,
der den Server lahmlegen soll (engl. _denial of service_).
[ENDWARNING]

Starten Sie im ersten Terminalfenster im Verzeichnis Ihrer `locustfile.py` einfach `locust`.
Locust findet die Datei dort von selbst und startet eine Weboberfläche.
Öffnen Sie im Browser `http://localhost:8089`.
Tragen Sie bei "Number of users (peak concurrency)"
und bei "Ramp up (users started/second)" jeweils 1 ein;
bei "Host" sollte schon Ihr Server stehen.
Klicken Sie auf "Start" und lassen Sie den Test etwa eine Minute laufen.
Sehen Sie sich währenddessen die Reiter "Statistics" und "Charts" an.
Prüfen Sie im Reiter "Statistics" an der Spalte "# Requests",
ob `/` etwa dreimal so oft aufgerufen wurde wie die Suche.
Falls nicht, stimmen die Gewichte in Ihrer `locustfile.py` nicht.

- [EQ] Wie lange brauchen die beiden Seiten laut Spalte "Median (ms)"?
  Passt das zum Code des Servers?
- [EQ] Der Server antwortet in Sekundenbruchteilen,
  trotzdem schickt der simulierte Nutzer insgesamt nicht einmal eine Anfrage pro Sekunde
  (Spalte "Current RPS", _requests per second_).
  Woran liegt das?
  Wie viele Anfragen pro Sekunde erwarten Sie demnach bei 10 Nutzern?

Beenden Sie danach den Test mit "Stop" und Locust im Terminal mit <kbd>Strg</kbd>+<kbd>c</kbd>.

<!-- time estimate: 20 min -->


### Mehr Last

Für das Kommandoprotokoll lassen wir Locust nun ohne Weboberfläche laufen.
Die Optionen bedeuten:

- `--headless`: ohne Weboberfläche;
- `-u 10`: 10 simulierte Nutzer;
- `-r 10`: pro Sekunde 10 neue Nutzer starten, bis alle laufen;
- `-t 30s`: nach 30 Sekunden aufhören;
- `--only-summary`: die Statistik nur am Ende ausgeben statt alle paar Sekunden.

Der Server muss dabei weiterhin im anderen Terminalfenster laufen.

- [EC] `locust --headless -u 10 -r 10 -t 30s --only-summary`

Locust gibt am Ende zwei Tabellen aus.
Die Zeile `Aggregated` fasst darin jeweils alle Anfragen zusammen.
Die erste Tabelle enthält unter anderem
die Zahl der Anfragen (`# reqs`) und der Fehler (`# fails`),
Durchschnitt (`Avg`) und Median (`Med`) der Antwortzeiten in Millisekunden
sowie den "Durchsatz" (engl. _throughput_) in Anfragen pro Sekunde (`req/s`).
Die zweite Tabelle enthält [TERMREF2::Perzentil::-e] (engl. _percentiles_) der Antwortzeiten:
In der Spalte `95%` steht die Antwortzeit, die 95 % der Anfragen nicht überschritten haben.
Der Median ist also dasselbe wie das 50%-Perzentil.

- [EC] `locust --headless -u 50 -r 10 -t 30s --only-summary`
- [EQ] Vergleichen Sie die beiden Läufe:
  Wie haben sich Median und 95%-Perzentil der beiden Seiten verändert?
- [EQ] Die Startseite tut fast nichts und ist bei 50 Nutzern trotzdem viel langsamer geworden.
  Erklären Sie, wie das kommt.

[HINT::Ich habe keine Idee, woran das liegen könnte]
Der Server bearbeitet eine Anfrage nach der anderen.
Was passiert mit einer Anfrage nach `/`,
die ankommt, während der Server gerade eine Suche bearbeitet?
Und was, wenn währenddessen noch weitere Anfragen eintreffen?
[ENDHINT]

- [EQ] Betrachten Sie den Durchsatz (`req/s` in der Zeile `Aggregated`).
  Passt er beim Lauf mit 10 Nutzern zu Ihrer Vorhersage aus dem ersten Test?
  Ist er beim Lauf mit 50 Nutzern im selben Verhältnis gewachsen wie die Zahl der Nutzer?
  Warum (nicht)?

[HINT::Ich verstehe nicht, warum der Durchsatz nicht im selben Verhältnis wächst]
Wann schickt ein simulierter Nutzer seine nächste Anfrage?
Was bedeutet es dafür, wenn er länger auf Antworten warten muss?
[ENDHINT]

Nun schätzen wir ab, wie nah unser Server an seiner Grenze ist.
Eine Suche hält den Server eine Zehntelsekunde lang beschäftigt,
die Startseite fällt daneben kaum ins Gewicht.
Den Anteil jeder Sekunde, in dem der Server beschäftigt ist,
nennt man seine "Auslastung" (engl. _utilization_).

- [EQ] Wie viele Suchen pro Sekunde kann der Server höchstens beantworten?
  Berechnen Sie für beide Läufe aus dem Durchsatz der Suche die Auslastung des Servers.
  Was erwarten Sie demnach bei 100 Nutzern für den Durchsatz und für die Antwortzeiten?

[HINT::Wie berechne ich die Auslastung?]
Bei 3 Suchen pro Sekunde ist der Server 3 · 0,1 s = 0,3 s jeder Sekunde mit Suchen beschäftigt,
also zu 30 % ausgelastet.
[ENDHINT]

[HINT::Wie komme ich auf eine Vorhersage für 100 Nutzer?]
Wie viele Suchen pro Sekunde würden 100 Nutzer verlangen, wenn der Server mithalten könnte?
Vergleichen Sie das mit Ihrer Höchstzahl.
Was geschieht mit den Anfragen, die der Server nicht sofort bearbeiten kann?
[ENDHINT]

Wenn Sie mögen, prüfen Sie Ihre Vorhersage mit `-u 100`;
dieser Lauf gehört nicht ins Kommandoprotokoll.
Je nach Betriebssystem meldet Locust dabei sogar Fehler,
weil der Server neue Verbindungen nicht mehr schnell genug annimmt.

<!-- time estimate: 30 min -->


### Den Engpass beseitigen

`HTTPServer` hat einen nahen Verwandten namens `ThreadingHTTPServer`.
Der bearbeitet jede Anfrage in einem eigenen [TERMREF::Thread],
sodass mehrere Anfragen gleichzeitig in Arbeit sein können.
Während ein Thread in `time.sleep` wartet, können andere weiterarbeiten.
Dokumentation:
[HREF::https://docs.python.org/3/library/http.server.html#http.server.ThreadingHTTPServer]

- [ER] Ändern Sie `shopserver.py` so, dass der Server `ThreadingHTTPServer` benutzt.
  Beenden Sie den laufenden Server mit <kbd>Strg</kbd>+<kbd>c</kbd> und starten Sie ihn neu.
- [EC] `locust --headless -u 50 -r 10 -t 30s --only-summary`
- [EQ] Vergleichen Sie mit dem vorigen Lauf mit 50 Nutzern.
  Was hat sich bei den Antwortzeiten von Startseite und Suche geändert, was nicht?
  Warum dauert eine Suche immer noch gut 100 ms?

<!-- time estimate: 10 min -->


### Einordnen

Nehmen Sie an, in den Anforderungen an den Shop steht:
"Bei 50 gleichzeitigen Nutzern antwortet die Startseite in 95 % der Fälle in höchstens 200 ms."

- [EQ] Erfüllt Ihr Server diese Anforderung vor und nach der Änderung?
- [EQ] Nehmen Sie an, die Anforderung verlangte stattdessen nur einen Durchschnitt von höchstens 200 ms.
  Wäre sie vor der Änderung erfüllt gewesen?
  Welcher Anteil der Anfragen nach `/` hat in diesem Lauf trotzdem länger als 200 ms gedauert?
  Lesen Sie das ungefähr in der Perzentil-Tabelle ab.
  Warum formuliert man solche Anforderungen besser mit einem Perzentil als mit dem Durchschnitt?

[HINT::Was ist am Durchschnitt so schlecht?]
Stellen Sie sich vor, 94 % der Anfragen dauern 5 ms und 6 % dauern 3 Sekunden.
Wie groß sind Durchschnitt und 95%-Perzentil,
und was erleben die Menschen, die den Shop benutzen?
[ENDHINT]

Ein echter Shop würde natürlich nicht auf `HTTPServer` laufen,
sondern auf einem Server, der von vornherein viele Anfragen gleichzeitig bearbeitet.
Der Engpass verschiebt sich dadurch aber nur:
Irgendwann ist die Datenbank, das Netzwerk oder der Prozessor ausgelastet.
Wo das passiert und ab wie vielen Nutzern, findet man am zuverlässigsten mit einem Lasttest heraus.

<!-- time estimate: 15 min -->

[ENDSECTION]


[SECTION::submission::reflection,trace,snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Gemeint sind `locustfile.py` und `shopserver.py` im Endzustand.)

[ENDSECTION]


[INSTRUCTOR::Warteschlange als Ursache der langen Antwortzeiten erkannt?]

[INCLUDE::ALT:]

### Kommandoprotokoll

[PROT::ALT:Locust.prot]

[ENDINSTRUCTOR]
