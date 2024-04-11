title: Selber ein Changelog schreiben
stage: draft
timevalue: 0.5
difficulty: 2
assumes: changelog
---

[SECTION::goal::experience]

Ich habe an meiner eigenen Software nachvollzogen, wie man ein Changelog schreibt.

[ENDSECTION]
[SECTION::background::default]

Sie haben doch [PARTREF::changelog] bearbeitet, oder?
Wenn nicht, bitte jetzt nachholen.

[ENDSECTION]
[SECTION::instructions::loose]

[WARNING]
1. Achtung, von den folgenden Abschnitten brauchen Sie **nur einen** zu bearbeiten,
   um diese Aufgabe zu absolvieren.
2. Diese Aufgabe hat faktisch "requires"-Abhängigkeiten, aber wegen der obigen Wahlmöglichkeit
   sind die nicht formell benannt.
[ENDWARNING]


### Changelog zu `mlh` schreiben

- Diesen Teil können Sie bearbeiten, wenn (und nur wenn) Sie von den
  `mlh`-Aufgaben in der Gruppe [PARTREF::Pythonpraxis] mindestens vier bearbeitet haben.
- Betrachten Sie das Ergebnis jeder `mlh`-Aufgabe ([PARTREF::argparse_subcommand] zählt auch mit)
  als eine Release von `mlh` und dokumentieren Sie, was da jeweils passiert ist.
    - Schreiben Sie das in eine Datei `CHANGELOG.md` im `mlh`-Dateibaum.
    - Vergeben Sie nachträglich künstliche Versionsnummern
    - Schlagen Sie das jeweilige Datum in der 
      [Commit-Historie](https://git-scm.com/docs/git-log) nach.
    - Wenn Sie für eine Aufgabe mehrere Commits gemacht haben, betrachten Sie jeden
      Commit als eine Release und verwenden Sie [semantische Versionsnummern](https://semver.org/).
- [EQ] Welchen Verzeichnispfad hat die Changelog-Datei, die Sie soeben geschrieben haben?


### Changelog zu `xxx` schreiben

- Diesen Teil können Sie bearbeiten, wenn (und nur wenn) Sie von den
  `xxx`-Aufgaben mindestens !!! bearbeitet haben.
- Folgen Sie den gleichen Anweisungen wie oben bei `mlh` beschrieben analog.


### Changelog zu `yyy` schreiben

- Diesen Teil können Sie bearbeiten, wenn (und nur wenn) Sie von den
  `yyy`-Aufgaben mindestens !!! bearbeitet haben.
- Folgen Sie den gleichen Anweisungen wie oben bei `mlh` beschrieben analog.

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
`changelog2.md` enthält also nur den Dateinamen der eigentlichen Abgabedatei.

[ENDSECTION]
[INSTRUCTOR::Sind Neues, Geändertes und Defektkorrekturen klar getrennt?]

Dieses Changelog kann natürlich u.U. recht simpel ausfallen, aber die drei
obigen Sorten von Eintrag sollten korrekt markiert und klar getrennt sein.
Außerdem der Detailgrad vernünftig: 
Nicht jedes Komma erwähnt, aber separate Teile in separaten Einträgen.

[ENDINSTRUCTOR]