title: Konvention für Commit-Nachrichten zwecks Arbeitszeiterfassung
stage: beta
timevalue: 0.5
difficulty: 2
requires: Git101
---
[SECTION::goal::trial]

Ich verstehe, wie strukturierte Commit-Nachrichten mir das Leben erleichtern können
und habe eine solche Erleichterung (nämlich die halbautomatische Arbeitsbuchführung des ProPra)
ausprobiert.

[ENDSECTION]
[SECTION::background::default]

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
`%Zeiterfassung 2.5h Commit-Format ausprobieren`

Das Ganze hat ein genau festgelegtes Format, das es von anderen Commit-Nachrichten unterscheidet.
Das Prozentzeichen ist der Start dieses Formats.
`Zeiterfassung` ist der Name der aktuellen Aufgabe (laut Dateiname, 
siehe im Adressfeld des Browsers) und `2.5h` besagt, dass wir für die Arbeiten,
die zu diesem Commit geführt haben, insgesamt zweieinhalb Stunden investiert haben.
Für unsere Zwecke reicht eine Granularität von z.B. 15 Minuten, also 0.25h, 0.5h, 0.75h, 1h etc.
Der Teil dahinter ist beliebig und kann auch leer sein.

Mit diesen Daten kann uns später ein Skript eine Aufstellung machen, welche Aufgaben wie
lange gedauert haben und wie sich das mit den Zeitwerten der Aufgaben vergleicht.

[NOTICE]
Unser Skript würde auch die Angabe `2:30h`, also mit Stunden und Minuten verstehen.
Aber Vorsicht: Wenn man Punkt und Doppelpunkt verwechselt, bekommt man ungültige Daten!
Entscheiden Sie sich für eine Notation und verwenden Sie diese konsequent.
[ENDNOTICE]

Sollten Sie mehrere Commits zu derselben Aufgabe anfertigen, geben Sie jeweils die Zeit an,
die dieser Commit beansprucht hat. Das Ausrechnen der Summe der Commits erfolgt automatisch.
Auf diesem Weg ist es auch möglich, Zeiten nachträglich einzutragen. 

Die angegebene Zeit spielt keinerlei Rolle für die Anrechnung von Aufgaben.
Sie dient lediglich zwei Zwecken:

1. Sie gibt Ihnen selbst ein Gefühl dafür, wie viel Zeit Sie tatsächlich in weiteren Aufgaben
   benötigen könnten.
2. Sie ermöglicht es uns, den eingeplanten Zeitwert von Aufgaben in zukünftigen Iterationen des
   Programmierpraktikums anzupassen.

In diesem Sinne tragen Sie besser gar keine Zeit ein, als sich einen Wert auszudenken,
der weit von der Realität abweicht, falls Sie keine Erfassung gemacht haben oder nicht
machen wollen.

Es gibt oben rechts auf jeder Seite ein einfaches Timing-Script, das Sie verwenden können.
Es zeigt beim Stoppen den Eintrag für die Commit-Nachricht der aktuellen Aufgabe.

[ENDSECTION]
[SECTION::instructions::loose]

Treffen Sie anhand der unten angegebenen Fragen eine Entscheidung, 
ob Sie diese Form der Arbeitszeiterfassung nutzen möchten.

Wir raten, es zu tun, denn Sie können dabei viel lernen und der Aufwand ist gering.
Sie werden in der Praxis häufig vor dem Problem stehen, den Zeitaufwand einer Aufgabe von vornherein einzuschätzen. 
Dabei ist konkrete Erfahrung, wie sie hier erworben werden kann, sehr hilfreich.

Zusatznutzen: Mit Zeiterfassung macht Ihnen das im ProPra verwendete Werkzeug `sedrila` 
(das lernen Sie in der nächsten Aufgabe kennen) 
automatisch die Liste von möglichen Einreichungen bei der Tutor_in.
Ohne Zeiterfassung müssen Sie die Einträge in Ihrer Einreichungsdatei
manuell machen.

[ENDSECTION]
[SECTION::submission::reflection,snippet]

Legen Sie die Markdown-Datei `Zeiterfassung.md` an.  
Tragen Sie die Antworten auf folgende Fragen ein:  

- [EQ] Haben Sie jemals zuvor eine systematische Zeiterfassung gemacht?
  War das einfach? War es hilfreich?
- [EQ] Haben Sie Scheu davor, Ihre Arbeitszeiten schriftlich festzuhalten? Warum?
- [EQ] Haben Sie Scheu davor, dass Ihre Tutor_innen diese Zeiten einsehen können? 
  Warum, wenn die doch dafür da sind, Ihnen Lernhilfe und Rückmeldung zu geben?
- [EQ] Werden Sie im ProPra die beschriebene Arbeitszeiterfassung machen?
  Falls ja: Was vermuten Sie, wie oft Sie vergessen werden, das Eintragsformat einzuhalten?

Machen Sie einen Commit im obigen Format mit Ihrer tatsächlichen Arbeitszeit.

Wenn Sie sich für Arbeitszeiterfassung entschieden haben, sollten Sie die für die
bisher bereits von Ihnen bearbeiteten Aufgaben nun nachholen:
Man kann bei git mit der [Option `--allow-empty`](https://git-scm.com/docs/git-commit) 
einen Commit machen, ohne eine Datei hinzuzufügen.
Machen Sie also einen separaten solchen Commit für jede bislang bearbeitete Aufgabe,
mit einer geschätzten Arbeitszeit.
[ENDSECTION]

[INSTRUCTOR::Bitte ggf. zureden]
Für diese Aufgabe verlangen wir einmalig einen Commit im korrekten Format:

- `%` zu Beginn
- richtig geschriebene Dateinamen (Groß-/Kleinschreibung zählt auch)
- Dezimalpunkt (nicht Dezimalkomma) mit Dezimalstunden oder Doppelpunkt mit Minuten, 
- 'h' ohne Leerzeichen 

Wenn die Antwort der vierten Frage ja lautet, ist alles in Ordnung.  
Dann bitte die Arbeitszeit-Listenausgabe in der Webapp auf Plausibilität prüfen.

Lautet sie nein, dann bitte die Antworten zu Fragen 2 und 3 sichten und allen, die sich offenbar nicht ganz sicher sind,
ermutigend zureden: Wir sind auf Ihrer Seite! Arbeitszeiterfassung hilft beim Lernen!  

Wenn die sich dann umentscheiden, bitte eine korrigierte Einreichung fordern,
damit dem Gedanken wirklich die schriftliche Erklärung folgt und sich der Gedanke 
dadurch hoffentlich festsetzt.
[ENDINSTRUCTOR]
