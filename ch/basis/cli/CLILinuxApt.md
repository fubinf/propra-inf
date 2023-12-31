title: Linux-Kommandozeile auf Linux mit Apt
timevalue: 0.5
difficulty: 1
---

## Bash-Shell sicherstellen

- Starten Sie ein Terminal. 
  Das Programm, das den darin laufenden Kommandozeilen-Interpretierer realisiert,
  nennt man Shell.
- Geben Sie `echo $SHELL` ein, gefolgt vom Drücken der Return-Taste.
  Wir werden diese Notation häufig verkürzt verwenden und nur schreiben: `echo $SHELL`.
  Sie müssen dann selbständig verstehen, dass ein Kommando auf der Kommandozeile gemeint ist.
- Wenn Sie als Ausgabe `/bin/bash` erhalten haben, ist alles in Ordnung: 
  Es gibt auf Linux zahlreiche verschiedene Shells und wir nehmen hier immer die Bash
  als Shell an.
- Haben Sie etwas anderes bekommen, dann haben Sie nicht die hier angenommene
  Sorte von Linux-System, nämlich ein standardmäßig konfiguriertes Debian oder Ubuntu.
  In diesem Fall müssen Sie folgendes mit Hilfe geeigneter Web-Recherche selbst herausfinden:
  - Wie man darauf Bash aufruft (ggf. einfach mit `bash`)
  - Oder falls keine Bash installiert ist: Was für eine Linux Distribution Sie haben
  - Wie man darauf Pakete installiert (anstatt mit `apt-get` oder `apt` wie auf Debian)
  - Wie man konkret Bash installiert und dann aufruft


## Python sicherstellen

- Probieren Sie `python -V` oder `python3 -V`, um die installierte Python-Version zu bestimmen.
  Wir brauchen mindestens Python 3.9.
  Merken Sie sich, welches der beiden Kommandos bei Ihnen funktioniert; evtl. sind beide äquivalent.
  Wir bevorzugen `python3`, weil das unter Umständen Verwirrung vermeidet, wenn auch Python 2
  installiert sein sollte.
- Wenn keines der Kommandos funktioniert, dann haben Sie wiederum nicht die hier angenommene
  Sorte von Linux-System und müssen analog wie oben weiter verfahren.
