title: Konvention für Commit-Nachrichten zwecks Arbeitszeiterfassung
description: |
  Wir hinterlegen mit wenig Mühe super nützliche Metadaten in unseren
  Commit-Nachrichten, damit wir später nachvollziehen können, 
  was wie lange gedauert hat.
timevalue: 1
difficulty: 1
assumes: Git101
---
Viele Teams geben sich Konventionen für das Format der Commit-Nachrichten,
damit sie mehr Nutzen aus dem git-Repo ziehen können.

Zum Beispiel ist es sehr verbreitet, bei jedem Commit anzugeben, zum Lösen
welcher Aufgabenstellung er beiträgt. Diese Aufgabenstellungen sind bei Softwareteams
dann meist in einer "Bug tracker" oder "Issue tracker" genannten Datenbank beschrieben,
in der jeder Eintrag eine Nummer hat, z.B. 4711, und das Team schreibt sich selbst
ein genaues Format vor, wie dann die erste Zeile der Commit-Nachricht aussehen soll, z.B.
`[#4711] repair XYZ output format corruption`.

Das gleiche machen wir hier im ProPra auch und erweitern es sogar auf eine Weise,
die auch für Softwareteams nützlich wäre, dort aber wenig gebräuchlich ist:
Wir geben immer die betreffende Aufgabe an und die investierte Arbeitszeit.

Hier ist ein Beispiel:  
`#Zeiterfassung 2.5h Commit-Format ausprobieren`

Dabei ist `Zeiterfassung` der Name der aktuellen Aufgabe (laut Dateiname, 
siehe im Adressfeld des Browsers) und `2.5h` besagt, dass wir für die Arbeiten,
die zu diesem Commit geführt haben, insgesamt zweieinhalb Stunden investiert haben.
Wir benutzen eine Granularität von 15 Minuten, also 0.25h, 0.5h, 0.75h, 1h etc.

Mit diesen Daten kann uns später ein Skript (und wir haben ein solches Skript!)
eine hübsche Aufstellung machen, welche Aufgaben wie lange gedauert haben
und wie sich das mit den Zeitwerten der Aufgaben vergleicht.
Es können beliebig viele Commits zur selben Aufgabe existieren, die jeder
einen weiteren Zeitschnipsel zur Summe dieser Aufgabe beitragen.

- Haben Sie jemals zuvor eine systematische Zeiterfassung gemacht?
  War das einfach? War es hilfreich?
- Was vermuten Sie, wie oft sie vergessen werden, das Eintragsformat einzuhalten?

Die angegebene Zeit spielt keinerlei Rolle für die Anrechnung von Aufgaben.
Sie dient lediglich Ihnen selbst, um gegebenenfalls Ihren realistischen Zeitaufwand für
weitere Aufgaben besser abzuschätzen, als auch für eine mögliche Anpassung der gegebenen
Einschätzung für zukünftige Semester.
In diesem Sinne tragen Sie besser gar keine Zeit ein, als sich einen Wert auszudenken,
der weit von der Realität abweicht, falls Sie keine Erfassung gemacht haben oder nicht
machen wollen.

Wenn Sie bereits einen Commit für eine Aufgabe gemacht haben, können Sie diese Angabe
dennoch mit einem zusätzlichen Commit auch mit Werten aus dem Gedächtnis nachtragen.
Tun Sie dies bitte für möglicherweise bereits von Ihnen bearbeitete Aufgaben.
(Man kann bei git [mit der Option `--allow-empty`](https://git-scm.com/docs/git-commit) 
einen Commit machen, ohne eine Datei hinzuzufügen.)

!!! instructor
    Achten auf 
    - `#` zu Beginn
    - richtig geschriebene Namen (Groß-/Kleinschreibung zählt auch)
    - Dezimalpunkt (nicht Dezimalkomma) mit Dezimalstunden oder Doppelpunkt mit Minuten, 
    - 'h' ohne Leerzeichen 
    
    Natürlich könnte man den Parser für diese Einträge weniger pingelig machen, 
    aber wir wollen die Studis an die präzise Einhaltung von Standards gewöhnen.
