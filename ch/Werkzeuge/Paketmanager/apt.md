title: APT Paketverwaltung
stage: alpha
timevalue: 1.0
difficulty: 2
---
TODO_1_condric:
    - Wenn Sie eine so umfassende Quelle benutzen wie https://wiki.ubuntuusers.de/apt/apt/,
      machen Sie bitte hinterher eine Guided Tour durch die relevanten Teile,
      damit man das alles mal ausprobiert hat:
      neben dem jetzigen Umfang fehlt mir da derzeit search, show, und list.
    - X11 Apps auf WSL? Haben Sie das mal ausprobiert? 
      Das ist ein Alptraum, auf Win10 anders als auf Win11, sicher nicht ohne Anleitung zu schaffen,
      ganz sicher nicht in einer Stunde zu schaffen.
   - Sie wollen doch hoffentlich nicht jemanden eine Software installieren lassen,
     die ersie nicht ausprobieren kann, oder? Bitte wählen Sie ein anderes Beispiel.

[SECTION::goal::idea]
Ich verstehe wie apt funktioniert und wie ich es anwenden kann
[ENDSECTION]

[SECTION::background::default]
apt ist bei Debian Systemen das standardmäßige Paketverwaltungssystem. Mit apt werden Pakete 
beispielsweise installiert, deinstalliert und aktualisiert.
[ENDSECTION]

[SECTION::instructions::detailed]
Lesen Sie sich diesen [Beitrag](https://wiki.ubuntuusers.de/apt/apt/) von ubuntuusers durch.
### System aktualisieren

Systeme sollten immer aktuell sein, also fangen wir auch mit einem aktuellen System an.

- [EC] Aktualisieren Sie ihr System.

### Pakete installieren

In dieser Aufgabe nehmen wir als Beispiel die X11 Apps, die eine Reihe von kleinen graphischen Programmen bietet.

- [EC] Suchen Sie nach den X11 Apps.
- [EC] Geben Sie die Informationen von den X11 Apps aus.
- [EC] Installieren Sie die X11 Apps.
- [EC] Geben Sie die Liste von installierten Paketen aus und filtern Sie nach den X11 Apps.

### Installation von Paketen manipulieren

Lesen Sie sich diesen [Beitrag](https://wiki.ubuntuusers.de/apt/apt-Kommandos/) von ubuntuusers durch.

Manchmal passiert es, dass die neueste Version eines Paketes Probleme mit ihrem System verursachen. 

- [EC] Installieren Sie eine alte Version von X11 Apps.
- [EC] Stellen Sie ein, dass X11 Apps nicht mehr aktualisiert wird.

Angenommen, Sie haben schon viel herumprobiert ihr Problem zu lösen, und als letzten Ausweg sehen Sie nur noch die Neuinstallation des Pakets.

- [EC] Installieren Sie die X11 Apps neu.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]
