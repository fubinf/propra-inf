title: Logdateien Bereinigen
stage: alpha
timevalue: 0.75
difficulty: 2
assumes:
---
[SECTION::goal::trial]
Ich lerne wie ich regex beim "Suche und Ersetzen" meiner IDE nutze.
[ENDSECTION]

[SECTION::background::default]
Im Programmieralltag kann es öfter vorkommen, dass man Log-Dateien zum debuggen von Problemen an 
andere Personen sendet. Gute Datenschutzhygiene sagt uns, dass wir vor dem Übersenden der Datei 
sensible Daten wie z.b. IP-Adressen, personenbezogene Daten o.ä. entfernen sollten. Dafür eignen 
sich reguläre Ausdrücke hervorragend, da die meisten IDEs inzwischen regex als Teil der "Find & 
Replace" bzw. "Suchen & Ersetzen" Funktion unterstützen.
[ENDSECTION]

TODO_1_hüster: Bitte Aufgabe selber mal durchführen, ob das so alles funktioniert.
Es fehlt noch ein `assumes: regex_groups` oder sowas.
Oder das wird das Thema hier (dann reichen 0.75h nicht) und man fügt passende Leseaufträge zu.

[SECTION::instructions::detailed]

### Daten vorbereiten

- Speichern Sie nachfolgende Logdaten in die Datei `log_sanitizer-ide.log` und 
  ein zweites Mal identisch in die Datei `log_sanitizer-orig.log`.

```
31.220.1.83 - - [12/Mar/2024:00:09:47 +0100] "GET / HTTP/1.1" 200 282 "-" "Mozilla/5.0 zgrab/0.x"
216.144.248.19 - - [12/Mar/2024:00:13:26 +0100] "HEAD /gitea HTTP/1.1" 200 3500 "https://j.mycompany.de/gitea" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
117.212.236.135 - - [12/Mar/2024:00:36:28 +0100] "GET / HTTP/1.1" 200 282 "-" "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
216.144.248.19 - - [12/Mar/2024:01:13:26 +0100] "HEAD /gitea HTTP/1.1" 200 3500 "https://j.mycompany.de/gitea" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
167.248.133.35 - - [12/Mar/2024:01:14:16 +0100] "GET / HTTP/1.1" 200 3573 "-" "-"
167.248.133.35 - - [12/Mar/2024:01:14:20 +0100] "GET / HTTP/1.1" 200 3573 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
167.248.133.35 - - [12/Mar/2024:01:14:21 +0100] "GET /favicon.ico HTTP/1.1" 404 3751 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
34.231.240.212 - - [12/Mar/2024:01:21:09 +0100] "GET / HTTP/1.1" 200 3596 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
212.70.149.134 - - [12/Mar/2024:01:53:45 +0100] "GET /cgi/conf.bin HTTP/1.1" 404 498 "http://94.134.33.182:80/mainFrame.htm" "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
112.94.252.96 - - [12/Mar/2024:01:55:42 +0100] "GET /~mycompany HTTP/1.1" 200 282 "-" "-"
112.94.252.96 - - [12/Mar/2024:01:55:42 +0100] "GET /~root HTTP/1.1" 200 282 "-" "-"
124.89.89.151 - - [12/Mar/2024:01:55:52 +0100] "GET / HTTP/1.1" 200 301 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
112.94.252.202 - - [12/Mar/2024:01:55:56 +0100] "GET /favicon.ico HTTP/1.1" 404 459 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
87.236.176.201 - - [12/Mar/2024:02:01:57 +0100] "GET / HTTP/1.1" 200 301 "-" "Mozilla/5.0 (compatible; InternetMeasurement/1.0; +https://internet-measurement.com/)"
216.144.248.19 - - [12/Mar/2024:02:13:26 +0100] "HEAD /gitea HTTP/1.1" 200 3500 "https://j.mycompany.de/gitea" "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
182.106.184.185 - - [12/Mar/2024:02:36:38 +0100] "POST /cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh HTTP/1.1" 400 3783 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:36:53 +0100] "POST /cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh HTTP/1.1" 400 3783 "-" "Custom-AsyncHttpClient"
182.106.184.185 - - [12/Mar/2024:02:38:02 +0100] "GET /show/detail/page/~unit/chapter/4 HTTP/1.1" 404 3790 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
182.106.184.185 - - [12/Mar/2024:02:38:06 +0100] "GET /vendor/phpunit/phpunit/Util/PHP/eval-stdin.php HTTP/1.1" 404 520 "-" "Custom-AsyncHttpClient"
```

- Stellen Sie sich vor, diese Logdatei wäre in Wirklichkeit 129.000 Zeilen lang
  und entsprechend variantenreicher als oben zu sehen.


### Bereinigen in der IDE

- Es gilt nun, alle IP-Adressen durch `123.0.0.0` zu ersetzen und
  für alle URLs, die auf eine User-Homepage weisen (also mit so etwas wie `/~username` beginnen),
  den angegebenen Namen durch `username` zu ersetzen.
- Machen Sie das zuerst mittels Ihrer IDE für die Datei `log_sanitizer-ide.log`.  
  Verwenden Sie reguläre Ausdrücke.
  Wenn Sie nicht sehen, wie das geht, verwenden Sie die Hilfe oder recherchieren Sie im Netz.
  Verwenden Sie nicht die interaktive Rückfrage bei jeder Ersetzung, sondern machen Sie alle
  Ersetzungen zu einem Ausdruck in einem Rutsch. Dann brauchen Sie zwei Durchgänge.


### Bereinigen mittels Skript

- Schreiben Sie nun ein kleines Skript `log_sanitizer.py`für den gleichen Zweck.
- Am einfachsten geht das als Filter mit folgendem Idiom: 
  `for line in sys.stdin:`, 
  dann Ersetzen mittels zweimal `re.sub()`, 
  dann `print(line, end='')`. 
- [EC] rufen Sie  
  `python log_sanitizer.py <log_sanitizer-orig.log >log_sanitizer-script.log` auf.


### Auswerten

- [EC] rufen Sie   
  `diff log_sanitizer-ide.log log_sanitizer-script.log` auf.
  Die beiden Dateien sollten identisch sein.
- [EC] rufen Sie `grep '~' log_sanitizer-ide.log` auf.

[ENDSECTION]

[SECTION::submission::reflection]
Geben Sie ihrem Tutor die bereinigte Datei sowie alle regulären Ausdrücke, welche Sie für die 
Bereinigung verwendet haben und erklären Sie, warum Sie sich für diese Entschieden haben.
[ENDSECTION]

[INSTRUCTOR::Letzten Schritt prüfen]
Das `grep` sollte im Kommandoprotokoll zwei Treffer ergeben, nicht etwa drei,
denn die Notation `/~username` gilt nur für die erste Pfadkomponente und 
der reguläre Ausdruck sollte deshalb davor ein Blank erwarten.
[ENDINSTRUCTOR]
