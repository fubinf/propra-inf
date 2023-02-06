description: Programmierwissen mit starkem Praxisbezug 
---
Willkommen beim Programmierpraktikum (ProPra)!

Auf dieser Seite ist erklärt, was das ProPra soll und wie es funktioniert.
Bitte sehr sorgfältig lesen und verstehen; bei Verständnisproblemen: fragen!

!!! instructor
    Die Hinweise für die Tutor_innen stehen hier (und meist auch sonst)
    überwiegend hinter den Informationen für die Studierenden.

[TOC]


## 1. Was sind die Ziele des ProPra?

Das Informatikstudium vermittelt in den ersten Semestern hauptsächlich sehr theoretisches Wissen.
Das ist gut, weil dieses Wissen sehr breit anwendbar und sehr langlebig ist.
Das ist aber auch schlecht, weil für professionelle Softwareentwicklung auch
bergeweise praktisches Wissen und technologisches Detailwissen benötigt wird.

Solches praktisches und Detailwissen will das ProPra vermitteln.
Genauer gesagt: Es gibt Ihnen die Gelegenheit, solches Wissen zu erwerben.
Das ProPra ist nämlich sehr offen angelegt: Sie können aus einer großen Palette möglicher Aufgaben
selbst auswählen, was Ihnen am lohnenswertesten erscheint.
Es gibt Aufgaben aus verschiedenen Themenbereichen und mit unterschiedlichem Schwierigkeitsgrad.

Eine Warnung gleich vorab: Softwareentwicklung ist eine sehr komplexe Fertigkeit und gut darin
zu werden dauert tausende Stunden des Lernens und Erfahrungsammelns.
Natürlich kann das Programmierpraktikum dazu nur einen kleinen Teil beisteuern.
Aber gerade wer bislang noch nicht sehr viel kann, kann hier gewaltige Fortschritte machen.


## 2. Wie läuft das ProPra ab?


### 2.1 Grober Gesamtablauf

1. Arbeitsumgebung einrichten (Kapitel "Basis")
2. Aufgabe auswählen
3. Aufgabe bearbeiten
4. Aufgabe einchecken (wie das geht, lernt man im Kapitel "Basis")
5. Weiter bei 2 bis man ein geeignetes Paket Aufgaben beisammen hat.
6. Aufgabenpaket beschreiben (auch das lernt man im Kapitel "Basis")
7. Aufgabenpaket bei der Tutor_in einreichen
8. Wenn der Soll-Umfang (siehe unten) noch nicht erreicht ist, weiter bei 2.


### 2.2 Wie kann oder soll ich aus den Aufgaben auswählen?


#### 2.2.1 Kapitel, Aufgabengruppe, Aufgabe

Die Aufgaben sind in einem dreistufigen Schema angeordnet:
Kapitel, Aufgabengruppe, Aufgabe.

**Kapitel** beschreiben große Themenkreise.
Ein Sonderfall ist das erste Kapitel. 
Hier werden die unverzichtbaren Arbeitsgrundlagen geschaffen, ohne die man am ProPra
gar nicht teilnehmen kann.

**Aufgabengruppen** fassen mehrere verwandte Aufgaben zusammen.
Die Verwandtschaft kann unterschiedlicher Art sein, z.B.
ein Themenkreis, eine Sequenz voneinander abhängiger Aufgaben,
eine Auswahl alternativer Aufgaben (1-aus-N-Auswahl).

**Aufgaben** sind die kleinsten in sich abgeschlossenen Einheiten des Lernens im ProPra.
Manche Aufgaben sind von anderen unabhängig.
Manche Aufgaben B setzen das Wissen voraus, das man in einer anderen Aufgabe A erworben 
oder schon mitgebracht hat ("assumes-Beziehung").
Manche Aufgaben B setzen das konkrete Arbeitsergebnis einer anderen Aufgabe A voraus,
bauen also direkt auf A auf ("requires-Beziehung").
Eine fertig absolvierte Aufgabe kann zur Anrechnung eingereicht werden.


#### 2.2.2 Schwierigkeitsgrade

Jede Aufgabe ist im Inhaltsverzeichnis durch ein farbiges Symbol mit einem 
Schwierigkeitsgrad wie folgt gekennzeichnet:

- Sehr Einfach[DIFF::1]
- Einfach[DIFF::2]
- Mittel[DIFF::3]
- Schwierig[DIFF::4]

Die Idee ist, dass man mit Aufgaben des Schwierigkeitsgrades beginnt, der zu den eigenen
Vorkenntnissen passt (siehe unten) und sich dann zum nächst höheren vorarbeitet.

Schwierigkeit bedeutet dabei nicht unbedingt, dass man die Aufgabe mit zu wenig Vorkenntnissen
nicht schaffen kann, sondern oft nur, 
dass das sehr viel länger dauert als für die Aufgabe geplant ist, weil die Anleitung
viel grober ist und erheblich mehr Selbstständigkeit verlangt.


#### 2.2.3 Die drei Zielgruppen

Dem entsprechend stellen wir uns beim Konzipieren der Aufgaben drei verschiedene Zielgruppen
des ProPra vor, die mit unterschiedlich guten Vorkenntnissen kommen:

- Wenig Vorkenntnisse:
  Diese Studierenden sind mehr oder weniger ohne Programmier-Vorkenntnisse ins Studium gekommen
  und haben im Studium Abkürzungen genommen, z.B. manche Übungsaufgaben nicht selber
  gemacht oder wenig gründlich bearbeitet.  
  Wenn Sie zu dieser Gruppe gehören, sollten Sie mit den als "Sehr Einfach"[DIFF::1]
  gekennzeichneten Aufgaben anfangen und sich erst dann zu "Einfach"[DIFF::2] vorarbeiten.
  Gegen Ende sollte die eine oder andere Aufgabe der Stufe "Mittel"[DIFF::3]
  möglich sein, aber "Schwierig"[DIFF::4] ist wahrscheinlich für Ihren Lernerfolg wenig dienlich.
- Normal viele Vorkenntnisse:
  Diese Studierenden sind mit einigen Programmier-Vorkenntnissen ins Studium gekommen
  oder haben im Studium konsequent mitgearbeitet und die Übungsgelegenheiten wahrgenommen.    
  Wenn Sie zu dieser Gruppe gehören, sollten Sie mit den als "Einfach"[DIFF::2]
  gekennzeichneten Aufgaben anfangen und sich erst dann zu "Mittel"[DIFF::3] vorarbeiten.
  Gegen Ende sollte die eine oder andere Aufgabe der Stufe "Schwierig"[DIFF::4] möglich sein.
  Aufgaben der Sorte "Sehr Einfach"[DIFF::1] sollten unter Ihrer Würde sein.
- Viele Vorkenntnisse:
  Diese Studierenden haben viel mehr Programmiererfahrung als man sie allein im Studium erwirbt.
  Häufig sind sie richtige Fans und haben das Programmieren als Hobby oder haben schon
  länger einen Nebenjob, der viel mit Programmieren zu tun hat.  
  Wenn Sie zu dieser Gruppe gehören, sollten Sie mit den als "Mittel"[DIFF::3]
  gekennzeichneten Aufgaben anfangen und sich zügig zu "Schwierig"[DIFF::4] vorarbeiten.
  Aufgaben der Sorte "Einfach"[DIFF::2] sollten unter Ihrer Würde sein.


### 2.2.4 Hinweise in, Zeitwerte für und das Lesen-und-Ausprobieren bei Aufgaben

Die meisten Aufgaben enthalten neben der eigentlichen Aufgabenstellung
Hinweise zum Vorgehen und Verweise auf umfangreiche externe Quellen.

Bei den einfachen Aufgaben[DIFF::2] sind die Hinweise recht präzise und vollständig
und sagen auch, was Sie in den Quellen nachlesen sollten.
Wissensdurst und Darüber-Hinaus-Lesen sind erwünscht und nützlich,
behalten Sie aber dabei den für die Aufgabe angegebenen Zeitwert im Auge.

Bei schwierigen Aufgaben[DIFF::4] ist das ganz anders:
Die Hinweise sind nur grob und es ist viel selbstgesteuertes Lesen nötig,
um die Aufgabe zu lösen.
Wie viel da jeweils mindestens nötig ist, ergibt sich wiederum aus dem Zeitwert
der Aufgabe.
Liegt der hoch, sollte neben das bloße Lesen ein Ausprobieren treten.


### 2.2.5 Voraussetzungen der Aufgaben

Neben dem Schwierigkeitsgrad und dem Zeitwert gibt es bei vielen Aufgaben weitere Angaben:

- `Assumes`: Dies ist eine Liste von Aufgaben oder Aufgabengruppen, 
  deren Lernergebnisse (Wissen und Können) bei dieser Aufgabe als vorhanden unterstellt werden.
  Man sollte diese Aufgabe also nur in Angriff nehmen, nachdem man sich vergewissert hat,
  über das nötige Vorwissen zu verfügen.
  Bearbeiten muss man diese anderen Aufgaben aber nicht unbedingt.
- `Requires`: Dies ist eine Liste von Aufgaben oder Aufgabengruppen, 
  deren konkrete Arbeitsergebnisse (z.B. erstellter Programmcode) bei dieser Aufgabe benötigt werden.
  Man muss also zuvor die anderen Aufgaben bearbeiten.
  Eine Einreichung der jetzigen Aufgabe ohne die vorherige oder gleichzeitige Einreichung
  der anderen wird nicht akzeptiert.


### 2.3 Was mache ich, wenn ich alleine nicht weiterkomme?

1. Sie dürfen fast alle Aufgaben auch **zu zweit bearbeiten** ("Paarprogrammierung").
   Jede_r macht am Ende eine eigene Abgabe (und formuliert, wo als Ergebnis Text gefragt ist,
   eigenen Text) und muss sich voll und ganz mit dem Ergebnis auskennen,
   aber erarbeiten können Sie dieses Ergebnis gemeinsam.
   Das viele Sprechen über die Aufgabe, das sich dabei ergibt, erleichtert das Verständnis nicht nur,
   sondern verbessert es sogar.
2. Die **Tutor_innen** stehen für (kurze!) **Hilfestellung** zur Verfügung.
   Orte und Zeiten siehe im Whiteboard.
   Formulieren Sie eine präzise Frage.
   Also nicht _"Ich komme hier irgendwie nicht weiter"_ oder 
   _"Ich habe keine Ahnung, was ich hier machen soll"_.
   Sondern z.B. _"Wo finde ich die-und-die Information?"_ oder
   _"Was bedeutet diese Meldung?"_ oder
   _"Warum passiert hier das-und-das?"_


### 2.4 Wie reiche ich gelöste Aufgaben ein?  TODO 2

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

!!! submission
    Boxen wie diese hier, spezifizieren, was genau in die Abgabe gehört.
    Es kann vorkommen, dass Sie in Aufgaben Code oder Ausgabe produzieren, die für die
    Bewertung unerheblich sind. Darauf werden Sie dann hier hingewiesen.


### 2.5 Wann habe ich das ProPra bestanden? (Soll-Umfang)

Im Inhaltsverzeichnis wird für jede Aufgabe ein Zeitwert angegeben, z.B. 1.5h.
Das ist die erwartete Arbeitszeit für diese Aufgabe.
Wenn Sie diese Aufgabe einreichen und die Tutor_in akzeptiert die Einreichung, 
wird dieser Wert Ihrem ProPra-Konto gutgeschrieben (Ausnahme siehe unten).
Sobald die Summe dieser Werte mindestens dem Kursumfang entspricht (30 Stunden pro Leistungspunkt)
und Sie die Tutor_in darauf hinweisen, ist das ProPra erfolgreich absolviert.

Ihre tatsächliche Arbeitszeit kann darunter liegen.
Das kommt vor, wenn Sie Aufgaben wählen, die zu einfach für Ihre vorhandenen Fertigkeiten sind
oder wenn mal alles schön glatt läuft.

Ihre tatsächliche Arbeitszeit kann aber auch darüber liegen.
Das kommt vor, wenn Sie Aufgaben wählen, die zu schwierig für Ihre vorhandenen Fertigkeiten sind
oder wenn bei Aufgaben der richtigen Schwierigkeitsstufe mehr schiefgeht, als wir
eingeplant haben. Das kommt beim Programmieren leider oft vor und passiert auch hoch kompetenten
Softwareentwickler_innen.

Um Sie zum sorgfältigen Arbeiten zu animieren und die Tutor_innen vor Überlastung zu schützen,
wird der Zeitwert einer Aufgabe nur angerechnet, wenn sie bei der ersten oder zweiten Kontrolle
dieser Aufgabe akzeptiert wird.


## 3. Ein Wort zum Gendern

[Eigentlich](https://www.fu-berlin.de/sites/diversity/antidiskriminierung/sprache/gender/index.html#Regelung)
soll an der Freien Universität mit dem Genderstern gegendert werden:
**Tutor*innen.**

Aber leider ist der Stern in den meisten Programmiersprachen ein Operator und kann deshalb
nicht als Bestandteil von Bezeichnern auftreten.
Deshalb gendern wir hier mit dem Unterstrich, denn der ist in den meisten Programmiersprachen 
in Bezeichnern erlaubt:
**Tutor_innen**.

Die Bedeutung ist dieselbe.

!!! instructor
    Liebe Tutor_innen,
    
    herzlich willkommen beim Programmierpraktikum (ProPra).
    Diese Seite funktioniert im FAQ-Stil und ist bitte gründlich durchzuarbeiten.
    
    # Tutor_innenteil
    ## 1. Was ist das Ziel des ProPra?

    Das ProPra soll

    - praktische Programmierkenntnisse und -fertigkeiten vielerlei Art aufbauen
    - dabei für Studierende mit sehr unterschiedlichem Vorkönnen geeignet sein
    - motivierender sein als die meisten Veranstaltungen, indem
      - die Aufgaben erkennbar praxisorientiert sind
      - viel weniger Zwang ausgeübt wird als meist üblich

    Wir wollen denen, die hier viel lernen wollen, die beste Unterstützung geben.
    Diejenigen zu stoppen, die sich nur durchmogeln wollen, hat dagegen viel weniger Priorität.
    Wir haben die Hoffnung, dass das ProPra cool und deshalb die Zahl der Mogelinteressierten klein ist.
    
    
    ## 2. Was ist hier mein Job?
    
    Wir haben an die Tutor_innen folgende Erwartungen:

    - solide Kenntnisse in der Programmierung mitbringen (guter Mittelstand, kein Expertenniveau)
    - solide Kenntnisse in Shell und git mitbringen (guter Mittelstand, kein Expertenniveau)
    - einen guten Überblick über die Aufgaben des ProPra haben:
      Was gibt es alles; wo stecken jeweils dabei die Schwierigkeiten?
    - Problemdiagnose können:
      Wenn ein Studi mit einer Fehlermeldung ankommt oder (weitaus schwieriger)
      mit einer diffusen Frage, erkennen wo _vermutlich_ das Problem steckt und 
      einen Hinweis geben, wie man zur Lösung gelangt -- nicht, was die Lösung ist.
    
    Der konkrete Arbeitsauftrag besteht aus zwei Teilen:

    1. Anwesend sein und für Fragen zur Verfügung stehen.
       Dabei immer nur gerade so viel Hinweis geben, dass die Studierenden danach
       wieder alleine weiter vorankommen.
       Bei allein arbeitenden kann der Hinweis auch sein, sich eine Partner_in zu suchen.
    2. Eingereichte Aufgaben kontrollieren und zurückweisen und/oder akzeptieren.
       Das Akzeptieren führt zur Zeitgutschrift für die Studis.
       Die Buchführung erfolgt im Git-Repo der Studierenden und wird dadurch gegen
       Manipulation abgesichert, dass die Commits der Tutor_innen digital signiert werden.

    
    ## 3. Was muss ich vor Beginn vorbereiten?  TODO 2

    - GPG-Signaturen verstehen und GPG einrichten.
    - Ein Schlüsselpaar erzeugen.
    - Den Fingerprint an die Veranstalter melden.
    - sedrila installieren. Das ist die technische Infrastruktur, auf der das ProPra basiert.
    
    Der öffentliche Schlüssel wird im Webauftritt des ProPra vermerkt.
    Beim Aufruf des Skripts gibt man diesen Webauftritt an und
    sedrila akzeptiert dann als gutgeschrieben nur solche Einträge, 
    deren Commits so signiert sind, dass die Signatur zu einem der vermerkten Schlüssel passt. 
    
    
    ## 4. Wie funktioniert der Einreichungsprozess genau?  TODO 2
    
    ...
