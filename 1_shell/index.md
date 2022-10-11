title: Shell

# Shell

Als kurze Einordnung des Themengebietes gibt es zunächst einmal eine Abgrenzung zweier verwandter Begriffe. nämlich **Shell** und **Terminal** bzw. **Terminal-Emulator**.

Als Shell wird ganz allgemein eine Schnittstelle zwischen Computer und Benutzer verstanden. Im speziellen handelt es sich hier um Textshells, das sind Anwendungen, in die Benutzer Befehle eingeben können und eine Textausgabe als Ergebnis des entsprechenden Befehles erhalten.

Erwähnenswerte Vertreter sind hier:

* Sh als Standard (im Sinne von Standardisierung) und kleinster gemeinsamer Nenner

* Ksh als Erweiterung zum Standard von Sh

* Bash als Standard-Shell vieler Distributionen (im Sinne von vorinstalliert und ggf. voreingestellt)

    Bash wird auch im Verlauf des Kurses als gegeben angenommen. Von der Verwendung von Funktionalitäten, die Bash nicht hat, sollte Abstand genommen werden.

* Dash als Standard-Shell von Debian-Derivaten

* Fish als Shell mit Benutzerfreundlichkeit als Fokus

* Zsh als Shell mit Funktionsvielfalt und Konfigurierbarkeit als Fokus

    Bekannt hierfür ist beispielsweise die Zsh-Konfiguration der Distribution `grml`, die für viele weitere ebenfalls verfügbar ist, oder das Shell-Framework "Oh My Zsh".

* Xonsh als Shell, die mit Python anpassbar und konfigurierbar ist.

    Xonsh ist unter Umständen besonders interessant für diejenigen Studierenden, die ohnehin Python als Programmiersprache ihrer Wahl haben und sich auf dieser Ebene austoben wollen, es kann allerdings nicht gewährleistet werden, dass sie sich bei Mehrdeutigkeit korrekt verhält. Das sollte bei einer Verwendung im Hinterkopf behalten werden.

Im Gegensatz zu einer Shell, deren Aufgabe darin liegt, Benutzereingaben zu interpretieren und Ausgaben zurückzuliefern, sind die Aufgabe eines Terminals oder Terminal-Emulators eher technischer Natur.
Ein Terminal kümmert sich grundlegend erstmal nur darum, wie Benutzereingaben zur Shell übertragen werden und wie die Ausgabe der Shell dem Nutzer präsentiert wird.
Das mag im ersten Moment sehr banal klingen, aber es gibt eine große Menge an Terminal-Befehlen, die man als Benutzer üblicherweise nie zu Gesicht bekommt, wie beispielsweise das Übertragen von Fenstergröße an die Shell, die Positionierung des Cursors, der nicht immer einfach hinter dem Text sein muss, aber auch beispielsweise Unterstützung für Eingaben per Maus oder Ausgabe von Bildern.
Unter einem Terminal-Emulator bezeichnet man eine Anwendung, die eben diese Aufgaben in Software löst. Die konkrete Software spielt für diesen Kurs keine Rolle, es gibt allerdings unterschiede im Funktionsumfang. Typische erweiterte Funktionen sind beispielsweise die Bereitstellung von Tabs aber auch (ggf. konfigurierbare) Farbpaletten und Unterstützung von verschiedener Menge an Terminal-Befehlen.

!subtoc

!resources
