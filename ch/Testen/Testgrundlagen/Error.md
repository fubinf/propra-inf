title: Fehlerarten
stage: draft
timevalue: 0.75
difficulty: 2
---

TODO_1_ruhe:

- Die ganze Terminologie gehört ins Glossar (und wir müssen alle Stellen finden, wo sie benutzt wird
  und für einheitliche Verwendung sorgen). In dieser Aufgabe sollten nur Verweise und ein Leseauftrag stehen. 
- Was haben Sie bei F4 im Sinn? Falls der Test alle Aspekte des Verhaltens erfasst, ja, sonst nein.
  Möglich ist es, aber nur bei sehr einfachen Fällen auch praktikabel.
- "Fehlerbericht" müsste Defektbericht oder Versagensbericht heißen.
- Die Aufgabe sollte vermutlich Fehler-Defekt-Versagen heißen, Titel auch so ähnlich.

[SECTION::goal::idea]

- Ich kann den Begriff Fehler definieren
- Ich kann die Ursache eines Fehlers genauer definieren

[ENDSECTION]
[SECTION::background::default]

In der Qualitätssicherung werden unterschiedliche Begriffe verwendet, die einen Fehlerzustand
beschreiben. Die richtige Verwendung der definierten Begriffe kann nur funktionieren, wenn man die
feinen Unterschiede kennengelernt hat. Durch ein präzises Verständnis dieser Begriffe können
Entwickler und Tester effektiver zusammenarbeiten, um Fehler zu identifizieren und in einem
Dokumentenmanagementsystem zu klassifizieren, zu isolieren und zu beheben, was letztendlich zu
einer höheren Qualität der Software führt. Darüber hinaus ermöglicht ein solides Verständnis der
Fehlerbegriffe, fundierte Entscheidungen darüber zu treffen, welche Fehler priorisiert werden
müssen, um Ressourcen optimal zu nutzen und den Entwicklungs- und Testzeitplan einzuhalten.

[ENDSECTION]
[SECTION::instructions::loose]

Wenn Sie das Modul `Softwaretechnik` besucht haben, sind Ihnen die Bergiffe Fehler, Defekt,
Fehlerzustand und Versagen sicherlich noch bekannt. Falls nein, hier ein kleiner Refresher:

- Fehler: Programmierer machen Fehler (error: Ereignis).
  Hierbei handelt es sich um eine Abweichung oder Unstimmigkeit zwischen dem beabsichtigten
  Verhalten eines Systems und seinem tatsächlichen Verhalten. Diese Fehler können aufgrund von
  menschlichem Versagen, unklaren Anforderungen oder unvorhergesehenen Umständen auftreten.
  - Falschtun: So ein Fehler kann durch eine falsche Umsetzung erfolgen (commission)
  - Versäumnis: oder dadurch, das etwas gar nicht erst umgesetzt wurde (omission)
  - Irrtum: Weil man sich dessen nicht bewusst war (misconception)
  - Versehen: oder es anders machen wollte (blunder)
- Defekt: Daraufhin entsteht im Produkt ein Defekt (defect: Struktur).
  So werden fehlerhafte Implementierung oder eine Abweichung von den Spezifikationen
  eines Systems bezeichnet. Defekte können aufgrund von Fehlern im Design, in der Codierung oder
  während des Entwicklungsprozesses auftreten.
- Fehlerzustand: Daraufhin macht das Programm beim Ablaufen ebenfalls Fehler  (error: Ereignis)
  und kommt intern in Fehlerzustände (invalid state, fault: Zustand).
  Ein Fehlerzustand tritt auf, wenn das System aufgrund eines Fehlers in einen nicht beabsichtigten
  oder inkonsistenten Zustand gerät. Das kann dazu führen, dass das System unerwartete Ergebnisse
  produziert oder nicht ordnungsgemäß funktioniert.
- Versagen: Daraufhin entsteht ein beobachtbares Versagen des Programms (failure: Ereignis).
  Das tritt auf, wenn ein Fehlerzustand zu einem beobachtbaren Fehler oder einer
  Beeinträchtigung der Systemfunktionalität führt, die vom Benutzer oder einem externen Beobachter
  wahrgenommen werden kann. Versagen können dazu führen, dass das System nicht mehr den
  Anforderungen oder Erwartungen entspricht und somit seine Aufgabe nicht mehr erfüllen kann.

Diese Ereignisse können auftreten, wenn ein Fehler gemacht wurde. Müssen aber nicht.

- [EQ] Was haben Fehlerwirkungen und Fehlhandlungen mit dem Thema zu tun? [Recherchieren Sie in diesem Lehrplan](https://www.german-testing-board.info/wp-content/uploads/2022/01/GTB-CTFL_Lehrplan_v3.1_DE.pdf).
- [EQ] Diskutieren Sie: Ist jeder Softwarefehler auf eine 'falsche' Programmierung zurückzuführen?
- [EQ] Welche Informationen sollte ein [Fehlerbericht](https://search.ebscohost.com/login.aspx?direct=true&db=nlebk&AN=1170217&site=ehost-live&ebv=EB&ppid=pp_110) enthalten?
- [EQ] Angenommen, Sie haben einen Testfall erstellt, der ein bestimmtes Szenario testet. Kann
  dieser Testfall jedes Versagen in diesem Szenario entdecken?
- [EQ] Können Sie sich ein Programm größeres Programm vorstellen, dass keine Fehlerzustände hat?

[ENDSECTION]
[SECTION::submission::information,reflection]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]
