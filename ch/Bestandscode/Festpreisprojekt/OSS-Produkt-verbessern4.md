title: "Festpreisangebot für mehrere Issues eines Open-Source-Projekts"
stage: beta
timevalue: 4.0
difficulty: 4
---

[SECTION::goal::trial,experience]

- Ich erfahre aus eigener Anschauung, wie schwierig das Schätzen von Aufwand bei der Softwareentwicklung ist.
- Ich löse einige reale Probleme einer relevanten und nichttrivialen Open-Source-Anwendung.
[ENDSECTION]


[SECTION::background::default]
Festpreisprojekte sind in jedem Fall schwierig zu schätzen.
Aber wenn Sie dann auch noch in einer fremden Codebasis stattfinden...
[ENDSECTION]


[SECTION::instructions::tricky]

Der Kontext dieser Aufgabe ist das Open-Source-Projekt, in dem das beim ProPra verwendete
Werkzeug `sedrila` entwickelt wird:

[HREF::https://github.com/fubinf/sedrila/]

### Zeitumfang dieser Aufgabe

Diese Aufgabe durchbricht die Regel, dass jede Aufgabe im ProPra maximal 4 Stunden Zeitwert hat.
Sie können sie auch in einem Umfang bearbeiten, der einem Vielfachen von 4 Stunden entspricht,
bis zu einem Gesamtumfang von 48 Stunden -- insoweit die Kundin das für die von Ihnen
angebotene Leistung für angemessen hält.

"Die Kundin" bei einem echten Festpreisprojekt ist meist eine Firma oder Behörde,
deshalb bei uns weiblich.


### Vorbereitung

- Sichten Sie die offenen Einträge des
  [Issue-Trackers](https://github.com/fubinf/sedrila/issues)
  und überlegen Sie grob, welche davon Sie sich _vermutlich_ zu lösen zutrauen.
- Lesen Sie sich für Hintergrundwissen grob in die
  [sedrila-Dokumentation](https://sedrila.readthedocs.io/)
  ein, insbesondere zur 
  [Architektur](https://sedrila.readthedocs.io/en/latest/internal_notes/)
  und zum Kommando 
  ['author'](https://sedrila.readthedocs.io/en/latest/authors/).
- Machen Sie einen Fork des GitHub-Projekts,
  klonen Sie diesen in Ihren Hilfsbereich (oder anderswohin, ganz nach Geschmack),
  richten Sie die Codebasis in Ihrer IDE ein.
- Führen sie die Testsuite aus: `pytest`
- Orientieren Sie sich grob in der Codebasis.
  Identifizieren Sie die Hauptteile der Software und deren ungefähre jeweilige Zuständigkeit.


### Angebot schreiben

- Legen Sie die Datei `Festpreisprojekt-sedrila.md` an.
  Dies wird die einzige Datei sein, die Sie für diese Aufgabe auf dem normalen Weg einreichen,
  alle anderen Dateien nehmen den Weg über GitHub.
- Legen Sie fest, welche Issues Sie bearbeiten wollen und schätzen Sie, wie viele Stunden
  Sie für jede davon zu benötigen erwarten.
  Schätzen Sie in vollen Stunden, nicht feiner.
- Beschreiben Sie Ihr Leistungsangebot wie folgt:
    - Beginnen Sie mit `# Angebot <datum>`, z.B. `# Angebot 2026-07-19` (mit aktuellem Datum)
    - Für jede zu bearbeitende Issue fügen Sie eine Level-2-Überschrift im Markdown ein
      mit der Issue-Nummer, dem Issue-Namen und dem geplanten Zeitaufwand, z.B.:  
      `## #123: author: Crashes on full moon (9h)`
    - Für Issues mit einem eindeutigen, scharf definierten Profil notieren Sie im Rumpf des
      Abschnitts einfach "Wird erledigt".
    - Für Issues mit einem offene(re)n Zuschnitt, bei denen man von einem umfangreichen Problem
      nur einen Teil löst oder wo sehr verschieden gestaltete Lösungen infrage kommen,
      beschreiben Sie im Rumpf, was Sie lösen wollen, was nicht und wie man sich die spätere
      Lösung ungefähr vorstellen sollte.


### Angebot einreichen

- Machen Sie einen Commit der Markdown-Datei in der üblichen Art und Weise.
- Schicken Sie prechelt@inf.fu-berlin.de eine Email mit dem Betreff
  "Festpreisprojekt-sedrila".
  Der Rumpf sollte so aussehen wie sonst für eine Aufgabeneinreichung.

[NOTICE]
Wenn Sie im Paar arbeiten und auch schon vorherige Abgaben entsprechend gemeinsam
gemacht haben, gilt hier eine Ausnahme von der üblichen Regel,
dass Markdown-Abgaben alleine formuliert werden sollen.  
Ganz im Gegenteil: **Eine Person übernimmt die alleinige Führung bei dieser Aufgabe**
(Firmensprech: "One face to the customer").

- Nur diese Person reicht den Markdowntext ein.
- Alle Pull-Requests (siehe unten) kommen ebenfalls nur von dieser Person.
- Die Partner_in kopiert lediglich im letzten Schritt (der endgültigen Einreichung zur
  Zeitgutschrift) die Markdowndatei und ergänzt zuoberst  
  "Gemeinsame Abgabe mit &lt;accountname&gt; (&lt;voller Name&gt;)".
[ENDNOTICE]


### Stellungnahme prüfen

- Waren Sie auf Email-Antwort. (Wie schnell eine Kundin reagiert, kann man leider nie wissen.)
- Sie finden dann in Ihrem Repo eine ergänzte Fassung Ihrer Markdown-Datei mit
  einem zusätzlichen Abschnitt  
  `# Stellungnahme <datum>`
- Darin ist erklärt, welche Teile Ihres Angebots die Kundin annehmen möchte (und welche also nicht)
  und wo sie ggf. nur mit einem geringeren (angegebenen) Stundenumfang dazu bereit ist.
- Im einfachsten Fall steht dort einfach "Angebot angenommen".


### Verhandlungsphase

Der gleiche Prozess kann nun **ein- oder zweimal** wiederholt werden:

- Führen Sie die Markdown-Datei nach unten weiter, indem Sie eine Kopie Ihres
  bisherigen Angebots mit aktuellem Datum anfügen und es so überarbeiten
  (durch Streichen, Zufügen, Ändern),
  dass Ihre Chancen auf Annahme vermutlich steigen.
- Dazu sollten Sie in der Regel das vorhandene Angebot vor allem passend zur Stellungnahme abspecken:
  Stundenumfänge reduzieren, wo Sie das als tragbar empfinden, 
  und Abschnitt/Issue komplett streichen, wo nicht.
- Sie könnten aber in manchen Fällen auch den Zuschnitt ändern, wenn Sie hoffen,
  damit doch mit dem vorgesehenen Stundenumfang für dieses Issue beauftragt zu werden.
  Erläutern Sie Ihre Erwägungen, damit die Kundin das Manöver versteht, anstatt womöglich
  verärgert zu reagieren.
- Falls die Kundin auf Abhängigkeiten hingewiesen hat, die in Ihrem Angebot 
  nicht oder nicht gut gelöst sind (und nur dann), 
  kommt auch infrage, ganz neue Teile in das Angebot zu ergänzen.
- Reichen Sie das neue Angebot auf die gleiche Weise ein wie das vorherige.

(In der Markdown-Datei entsteht also eine lehrreiche Historie des Verhandlungsverlaufs.)

Im Erfolgsfall haben Sie nun also im ersten, zweiten oder dritten Angebotsschritt ein
"Angebot angenommen" erhalten.
Andernfalls war Ihre gesamte bisherige Investition vergebens,
denn mehr als drei Durchläufe gibt es nicht.


### Auftrag durchführen

Entwickeln Sie nun Ihre Beiträge wie im Auftrag vereinbart.

Lesen Sie ggf. nach
[wie man mit Pull-Requests arbeitet](https://docs.github.com/en/pull-requests)

Legen Sie die Pull-Requests (PRs) zu Ihren Issues an:

- Verkehrssprache bei `sedrila` ist Englisch, sowohl im Quellcode als auch bei
  Commit-Nachrichten und PR-Dialog.
- Der PR muss das Issue erwähnen.
- Zu jedem Issue gehört nur ein PR.
- Für kleine und mittlere Issues enthält der PR nur _einen_ Commit.  
  Für große Issues enthält der PR je einen Commit für jeden Belang
  (der dann in der Commit-Nachricht erläutert sein sollte).
- Der PR-Zweig sollte auf dem _aktuellen_ Stand von `sedrila/main` basieren.

[HINT::So zu arbeiten ist wahnsinnig schwierig!]
Ja, stimmt. Es ist aber mit git nicht nötig, die Commits von vornherein in dieser Form zu bauen,
sondern:

- Legen Sie einen Zweig Z für die ganze Entwicklung an (natürlich mit einem sinnvollen Namen).
- Entwickeln Sie darauf die Beiträge zu allen Ihren Issues, egal ob hintereinander oder durcheinander.
- Machen Sie genügend kleine Commits, damit Sie ggf. auch nachträglich Arbeitsschritte zurücksetzen
  können, die sich als unsinnig herausstellen.
- Achten Sie darauf, dass jeder Commit nur _einen_ Belang betrifft.

Dann können Sie nach Fertigstellung der Entwicklungsarbeit die PRs einen nach dem anderen 
aus dem Entwicklungszweig Z heraus zusammenstellen:

- Legen Sie einen Zweig P für den PR an.
- Übernehmen Sie die passenden Commits von Z nach P mittels `git cherry-pick`
- Fügen Sie dann auf P Ihre vielen kleinen Commits zu einem oder wenigen großen zusammen
  mittels `git rebase --interactive`.
[ENDHINT]


### Ergebnisse zur Akzeptanzprüfung vorlegen

- Reichen Sie die PRs alle am selben Tag beim sedrila-Projekt ein,
  nicht über mehrere Tage verstreut.
- Ergänzen Sie in Ihrer Markdowndatei einen Abschnitt  
  `# Vorlage Arbeitsergebnisse <datum>`  
  und listen Sie darin die URLs zu Ihren PRs auf, jeweils mit der Issue-Nummer, z.B.  
  `- #47: https://github.com/fubinf/sedrila/pull/123`
- Machen Sie dann die Abgabe wie unten beschrieben.


### Zweite Verhandlungsphase

- Die Kundin reagiert (und auch diesmal kann man wieder nicht wissen, wie schnell das passiert)
  ggf. auf einzelne PRs mit Nachbesserungswünschen.
  Diese sollten Sie entweder erfüllen oder den kompletten PR aus Ihrer Abgabe streichen,
  indem Sie  
  a) in der Markdown-Datei einen weiteren Abschnitt  
  `# Vorlage Arbeitsergebnisse <datum>`  
  mit einer entsprechend reduzierten URL-Liste ergänzen und  
  b) im PR einen entsprechenden Vermerk ergänzen, z.B.  
  "I give up. I will not complete this PR. It can be closed."
- Die Kundin kann im PR auch darauf verweisen, dass sie die geleistete Arbeit zwar brauchbar findet,
  aber auch unvollständig gegenüber dem, wie sie die entsprechenden Punkte der Vereinbarung
  versteht, und dass sie deshalb dafür 
  einen geringeren (dann benannten) Zeitwert veranschlagen möchte.
- Darauf können Sie mit weiteren Nachbesserungen reagieren oder mit "OK".
- Und irgendwann reagiert hoffentlich die Kundin mit "OK". 


### Annahme und Zeitgutschrift

- Ist obiger Prozess für alle PRs abgeschlossen, ergänzen Sie möglichst bald in
  Ihrer Markdown-Datei einen Abschnitt    
  `# Erzielte Übereinkunft <datum>`  
  und listen Sie darin die akzeptierten PRs mit dem akzeptierten Zeitwert auf, z.B.  
  `- #47 (5h): https://github.com/fubinf/sedrila/pull/123`
- Ergänzen Sie ferner einen letzten Abschnitt  
  `# Reflektion <datum>`  
  und beantworten Sie darin folgende Fragen:  
  [EQ] Was habe ich bei dieser Aufgabe über das technische Arbeiten mit Bestandscode gelernt?  
  [EQ] Was habe ich über Festpreisprojekte gelernt und wie gern möchte ich welche machen?
- Machen Sie nun eine neue Einreichung (die erste ist kurioserweise nie bewertet worden!) mit dem 
  gleichen oder einem passend geänderten Satz von Aufgaben.
- Wenn Sie keinen Fehler gemacht haben, ist die Annahme nun reine Formsache.

**Herzlichen Glückwunsch, Sie haben ein Festpreisprojekt überlebt!**


[SECTION::submission::program]
Alle Pull-Requests losgeschickt?
Dann reichen Sie nun Ihr Markdowndokument ein.

Geben Sie bei dieser Abgabe nur die betreffenden Aufgaben _dieser_ Aufgabengruppe an,
keine weiteren. 
Wählen Sie die Aufgaben so aus, dass deren Zeitwert-Summe der Summe der vereinbarten Leistungen
entspricht, die Sie erfüllt zu haben glauben.
Das ist ggf. weniger als im Angebot vereinbart,
falls Sie doch nicht alles erledigt haben.

Es kann also passieren, dass die hiesige Aufgabe selbst gar nicht dabei ist, sondern nur 
eine oder mehrere der Dummy-Aufgaben.
Ist die Zeitwert-Summe nicht durch 4 teilbar, dürfen Sie auf die nächsten vollen 4 Stunden aufrunden.
[ENDSECTION]

[INSTRUCTOR::Spezialfall!]
Diese Aufgabengruppe wird nur von der in der Aufgabe genannten Person bewertet.

Worauf ist zu achten?

- Wir akzeptieren einen Pull-Request nur im Ganzen oder lehnen ihn ab.
- Auf Gleichbehandlung der Teilnehmer achten.
- Nichttriviale Änderungen müssen durch einen Test abgesichert sein.
- Falls relevant, muss die Doku angepasst sein.
- Geht ein PR erheblich über die zugehörige Issue hinaus, Abspaltung in separaten PR verlangen.
- Der Code sollte idiomatisch sein und der Benennungsstil zum restlichen Code passen.
[ENDINSTRUCTOR]
