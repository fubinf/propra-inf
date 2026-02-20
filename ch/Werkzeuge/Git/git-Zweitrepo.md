title: Zweit-Repo einrichten zum Experimentieren mit git
stage: beta
timevalue: 0.25
difficulty: 2
---

[SECTION::goal::product]

Wir bereiten ein zweites git-Repo für den erweiterten git-Aufgabenbereich vor, das auch mal 
kaputtgehen darf, ohne das übliche Repo für unsere Abgaben zu gefährden.

[ENDSECTION]
[SECTION::background::default]

Normalerweise benutzen wir für unsere Abgaben das zu Beginn aufgesetzte git-Repo. 
Allerdings führen wir in der [PARTREF2::Git::Git-Aufgabengruppe] 
manchmal git-Befehle aus, die massive Veränderungen an unserem repo vornehmen. 
Bei Fehlern entsteht dann ein Durcheinander, das nicht immer leicht zu reparieren ist.
Um Datenverlust zu vermeiden, setzen wir deshalb hier ein zusätzliches Repo auf,
das nur unwichtige Daten enthält.

[ENDSECTION]
[SECTION::instructions::loose]

- Folgen Sie nochmals demjenigen Teil von Aufgabe [PARTREF::Git101],
  in dem das ProPra-Repo angelegt wird.
  Vergeben Sie diesmal aber einen Namen, der die Unwichtigkeit der Daten anzeigt,
  z.B. `propra-scratch`, `propra-spielwiese` oder ähnlich.
- Geben Sie anstelle der Tutor_innen (die brauchen auf dieses Chaos-Repo keinen Zugriff) 
  Ihrer Paarpartner_in zusätzliche Schreibrechte.
- [EC] Klonen Sie Ihr Repo.

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Fast keine Kontrolle nötig]

Wenn der Output für das `git clone` OK aussieht, sind wir zufrieden.
Jedes Paarmitglied braucht sein eigenes Zweitrepo.
Wenn die Studis etwas anderes falsch gemacht haben, merken sie das irgendwann selbst.

[ENDINSTRUCTOR]
