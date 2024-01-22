title: Fertige Aufgaben einreichen und angerechnet bekommen
stage: draft TODO_1_hofmann
timevalue: 1.0
difficulty: 2
requires: Zeiterfassung
---
[SECTION::goal::idea]

Ich habe gelernt, wie ich etwas bei der Tutor_in einreiche und habe das einmal ausprobiert.

[ENDSECTION]
[SECTION::background::default]

Das ProPra ist eine ideale Gelegenheit, das ordentliche Arbeiten mit git zu lernen.

In der Softwareentwicklung hat es zahlreiche Vorteile, jeden logischen Arbeitsschritt
(nicht selten ist das eine Änderung an nur einer einzigen Zeile)
in einem separaten Commit zu verpacken.
Dann kann man mit solchen Arbeitsschritten anschließend nämlich sehr flexibel hantieren
und z.B. die gleiche Änderung (etwa eine Defektkorrektur) auf ältere Versionsstände
anwenden, die noch weitergepflegt werden. 
(Bitte vollziehen Sie diesen Gedanken unbedingt nach. 
Er hat in der modernen Softwareentwicklung eine erhebliche Bedeutung.)

Deshalb wollen wir uns eine solche Disziplin auch im ProPra angewöhnen:
Jede Aufgabe wird in einem separaten Commit (oder ggf. mehreren) eingecheckt,
niemals mehrere Aufgaben zugleich.
Dann kann man in der Commit-Nachricht die betreffende Aufgabe so markieren,
dass sich das automatisch verarbeiten lässt.

[ENDSECTION]
[SECTION::instructions::detailed]

### ...

### ...

[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::snippet]

TODO_1

[ENDSECTION]

[INSTRUCTOR::submission.yaml OK?]
Wenn eine wohlgeformte und sinnvolle `submission.yaml` im commit liegt, sind wir schon zufrieden.
[ENDINSTRUCTOR]

_Alter Inhalt (von vor der Einführung der Abschnittstruktur, zu konsolidieren):_

Zur Anrechnung von erledigten Aufgaben kann mit sedrila eine Liste aller Aufgaben erzeugt
werden, für die bereits Commits vorliegen, aber noch keine Anrechnung vorliegt. Aus dieser
Liste können dann Einträge entfernt werden, die noch nicht kontrolliert werden sollen, weil
sie beispielsweise noch nicht vollständig bearbeitet sind.

Diese angepasste Liste wird dann in einem eigenen Commit zum Repository hinzugefügt.
Anschließend wird der/die Tutor\_in mit der URL des Repos darüber informiert, dass Aufgaben
zur Kontrolle vorliegen. Dieser trägt Feedback in diese Datei ein und markiert akzeptierte
Aufgaben. Das wird als **signierter** Commit in das Repository hinzugefügt. Für die
Abschlussbewertung zählen ausschließlich diese Commits.
<!-- Es gab hier mal die Idee, auch nicht angesehene Aufgaben zu bewerten.
Grundlegend gar keine schlechte Idee, aber ich würde das vermutlich einfach derart
handhaben, dass Tutor\_innen einfach 3 Feedback-Möglichkeiten haben.
Sowas wie "fehlerhaft", "okay" und "akzeptiert" oder sowas.
Ich sehe allerdings ein Problem darin, dass ohne klare Ansage, wann das gestattet ist und
in welchem Umfang, die Tutoren eher ein "Okay" geben würde, ohne die Aufgabe zu prüfen. -->

Sedrila kann dann den Kontostand auf Studierendenseite aktualisieren.



Weil es so viele Aufgaben gibt, die Bearbeitungsreihenfolge so frei ist und dann auch noch
mehrere Tutor_innen zuständig sein können, muss die Buchführung darüber, welche
Aufgaben schon erledigt sind, softwaregestützt sein.
Der Vorgang ist recht technisch und muss präzise eingehalten werden, damit Ihre Leistungen
verlässlich registriert werden.

Deshalb lernen wir den genauen Prozess erst im Kapitel "Basis" kennen (und probieren ihn dabei
aus und bekommen dafür Zeit gutgeschrieben).

Grob gesagt funktioniert er so:

1. Aufgaben zur Einreichung auswählen
2. Diese Menge in einer Datei !!! spezifizieren
3. Einchecken (`git commit`; für all dieses `git`-Zeug siehe nächster Abschnitt)
4. Zum GitLab-Server hochladen (`git push`)
5. Bei der Tutor_in um Kontrolle bitten
6. Tutor_in holt sich den Arbeitsstand (`git pull`)
7. Tutor_in kontrolliert die Einreichungen und vermerkt Gutschriften und Probleme in der Datei.
   Dabei fragt die Tutor_in eventuell mündlich nach, um Unklarheiten aufzulösen oder 
   das Verständnis zu überprüfen.
8. Tutor_in checkt die Datei ein (`git commit`) und lädt sie hoch (`git push`). 
   Dadurch werden die Gutschriften wirksam.
9. Sie holen die Datei (`git pull`), freuen sich an den Gutschriften, sichten
   die Probleme und arbeiten weiter am restlichen ProPra.

Im allgemeinen besteht eine Abgabe entweder aus _einer einzelnen_ Datei (üblicherweise
Markdown, aber gegebenenfalls auch Code, sofern der Umfang dies zulässt) oder
_einem einzelnen_ Verzeichnis, jeweils mit dem Namen der bearbeiteten Aufgabe.
