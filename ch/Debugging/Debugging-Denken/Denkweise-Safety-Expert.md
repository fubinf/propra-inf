title: Der Weg des Sicherheitsexperten
stage: beta
timevalue: 1.5
difficulty: 3
---
[SECTION::goal::idea]
Ich verstehe, welche Methoden Sicherheitsexperten verwenden, um aus Problemen zu lernen,
um damit den Lösungsaufwand abschätzen oder sogar künftige Probleme verhindern zu können.
[ENDSECTION]

[SECTION::background::default]
Diese Herangehensweise wird Ihnen gefallen, wenn Sie gern Daten sammeln und analysieren.
[ENDSECTION]

[SECTION::instructions::detailed]
Lesen Sie Kapitel 11 (S. 361-384) im Buch _Debugging by Thinking_. 

[WARNING]
**Aussagen skeptisch hinterfragen**

Es gibt in dem Kapitel einiges, das für unsere Zwecke nicht passend ist.
Beispiele:

- Probleme beim Binden (linking) oder mit dem Compiler (beides Abschnitt 11.4.2 unten)
  treten bei uns kaum jemals auf.
  Auch diverse der Teilprobleme in 11.4.4.x gibt es kaum oder gar nicht bei Python, 
  sondern nur in Sprachen wie C oder C++.
- Die im Buch ausgeklammerten Probleme mit den Anforderungen (11.4.3 oben) sollte man sehr
  wohl nach den gleichen Verfahrensweisen mit behandeln.
- Manches ist übertrieben kleinteilig, etwa 11.4.3.1, 11.4.3.5, 11.4.4.3 u.v.a.m.

Passen Sie deshalb die Vorschläge nach eigenem Ermessen an Ihre Bedürfnisse an
beziehungsweise suchen Sie die für Sie nützlichen Teile heraus.
[ENDWARNING]

[WARNING]
**Diese "root causes" sind nicht wirklich Urgründe**

Der Begriff "root cause" im Buch sollte in 11.3 und 11.4 besser nur "cause" heißen,
denn ein wirklicher [TERMREF::root cause] ("Urgrund") ist etwas anderes.
[ENDWARNING]

[EQ] Angenommen, Sie würden sich im Sinne von 11.3 entschließen, einige der Ideen von 11.4
aufzugreifen und Defektepisoden damit zu protokollieren.
Welche Teile von 11.4 würden Sie dann benutzen?

[EQ] Welche scheinen Ihnen davon am vermutlich nützlichsten? Warum glauben Sie das?

[EQ] Sichten Sie die Aufgaben der Gruppe [PARTREF::Python-mlh] oder
der Gruppe [PARTREF::Python-linkcheck].
Haben Sie die Neigung, die oben benannten Teile von 11.4 tatsächlich einzusetzen,
wenn (und falls) Sie diese Aufgaben bearbeiten?  
Wenn nein: Was hält Sie ab?  
Wenn ja: Denken Sie, dass es tatsächlich dazu kommen wird?

[EQ] Wenn eben die Antwort "ja" gelautet hat, besuchen Sie bitte die Webseite Ihres
Git-Repos und sichten Sie dort die Funktionalität des [TERMREF2::Issue Tracker::-s].
Bei einem Repo, an dem man wie hier allein arbeitet, könnte man den ja für
die Datensammlung einsetzen.  
Welche Stärken hätte das? Welche Schwächen?  
Welche Lösung käme alternativ in Frage? Vorteile? Nachteile?

[EQ] Unter welchen Umständen hielten Sie die Anwendung der Ideen aus 11.5 oder 11.6
für sinnvoll?
Erwarten Sie, dass Sie je solche Umstände haben werden?
[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
    
[INSTRUCTOR::Echte Auseinandersetzung sichtbar?]
Man kann bei 11.4 abstruse Dinge aussuchen, die wir nicht akzeptieren sollten.
Aber:
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

Eine Zusammenfassung des Kapitels steht auf S. 384-385.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]