# Semesterwechsel: Organisatorische Schritte

Diese Datei beschreibt stichwortartig, was zu tun ist, wenn ein neues ProPra beginnt.
Die Schritte spiegeln einige Spezifika der Verwendung an der
Freien Universität Berlin wider und sind ggf. entsprechend anzupassen.

## Annahmen

Es liegen folgende Annahmen zugrunde:
- Jedes ProPra läuft zwei Semester lang
- Jedes Semester startet ein neues; es sind also fast ständig zwei verschiedene
  Exemplare zugleich unterwegs, hier genannt "altes ProPra" und "neues ProPra".
- Beide zusammen werden von potenziell mehreren Tutor_innen betreut,
  die potenziell jedes Semester wechseln können.
- Laufende Änderungen (Ergänzungen, Korrekturen) am Aufgabenbestand erfährt jedes
  ProPra nur in seinem ersten Semester, um zwischen den Semestern strukturelle
  Änderungen am ProPra zu erlauben ohne dafür Branches benutzen zu müssen.

## Abkürzungen

- LMS: Lern-Managementsystem
- ...

## Schritte im alten ProPra

- zwei Wochen vor Semesterende: an Termin und Modalitäten für letzte Abgaben erinnern.
- ggf. neue Tutoren zu den Vorbereitungsschritten gemäß
  https://sedrila.readthedocs.io/en/latest/instructors/
  auffordern und die resultierenden `instructors` Einträge in `sedrila.yaml` machen.  
  Ggf. ausgeschiedene Tutoren von `instructors` nach `former_instructors` verschieben.
- kurz vor Semesterende: in `ch/changes.md` ankündigen, dass keine weiteren Änderungen erfolgen und 
  man ggf. bei `sedrila`-Updates darauf achten möge, bei derselben Major-Version zu bleiben.  
  Im LMS darauf hinweisen, dass ein erneuter Besuch der Startveranstaltung nicht nötig und ein Eintragen
  ins neue ProPra nicht anzuraten ist (wg. Verwirrung!).

## Schritte im neuen ProPra

- Ggf. die publizierten allgemeinen Regeln anpassen
  (Beispiel: https://www.mi.fu-berlin.de/w/SE/Programmierpraktikum)
- Im LMS ankündigen, dass die Startveranstaltung keinesfalls versäumt werden darf.
- `cmd/propra.sh` anpassen für Publikation des neuen und keiner Publikation des alten ProPra.
- Vor der Startveranstaltung ggf. strukturelle Änderungen am ProPra abschließen.
- `sedrila.yaml` anpassen und neues ProPra publizieren.
- Neue Tutor_innen einweisen
- Startveranstaltung abhalten
