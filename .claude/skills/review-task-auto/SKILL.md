---
description: Begutachte eine Task oder Taskgroup-Indexseite und erledige dabei auch die technischen Begleitschritte (git, sedrila, GitHub, Discord-Entwurf)
---

# Aufgaben-Review, automatisiert

Teilautomatisiert den Review-Workflow für die in $ARGUMENTS angegebene Aufgabendatei (oder
Taskgroup-Indexseite) um die technischen Begleitschritte herum, die sonst manuell erledigt werden:
`git pull` anfordern, Review erzeugen, warten auf Bearbeitung, `sedrila`-Build, Commit anfordern, `git push` anfordern,
GitHub-Kommentar posten, Discord-Ankündigung entwerfen.

Dieser Skill ruft für die inhaltliche Begutachtung selbst den Skill `review-task` auf und ändert
an dessen Verhalten nichts. Er wird typischerweise über den Shell-Alias `claude_review`
(`claude --permission-mode auto`) gestartet.

Halte dich strikt an die Reihenfolge unten. Nach Schritt 2 gibt es **keinen** weiteren
Rückfrage-Punkt mehr außer bei echten Fehlern (Build schlägt fehl, echter Merge-Konflikt) --
dort wird angehalten und nachgefragt statt geraten.

## Schritt 0: Vorbereitung

1. `git status` prüfen. Falls unerwartete uncommittete Änderungen vorhanden sind, die nichts mit
   dieser Review zu tun haben, diese mit `git stash` und `git stash pop` aus dem Pull ausklammern und
   bei den späteren Commit-Schritten ignorieren.
2. `git pull --rebase` anfordern (oder falls möglich selber machen; meist hast Du aber keinen ssh-agent dafür).
   Falls dabei ein Konflikt bei `altdir` als Gitlink auftritt (`both modified: altdir`),
   die im Memory `submodule_pull_conflict_runbook` dokumentierte mechanische Auflösung anwenden --
   das deckt den Fall ab, dass beide Seiten sich zu einem gemeinsamen Nachfolgestand mergen lassen.
   Falls stattdessen ein echter Inhaltskonflikt auftritt (in einer Datei in `altdir` selbst oder
   in einer gespiegelten Datei im Hauptrepo), keine Auflösung raten, sondern anhalten, die konkurrierenden Änderungen
   zeigen und den Nutzer fragen, wie aufgelöst werden soll.

## Schritt 1: Review erzeugen

Rufe den Skill `review-task` mit denselben $ARGUMENTS auf (über das Skill-Werkzeug).
Das erzeugt bzw. aktualisiert `.claude/draft-reviews/r-<taskname>.md` genau wie beim direkten
Aufruf von `/review-task`.

## Schritt 2: Review kommentieren

Halte an und bitte den Nutzer, jetzt

- `.claude/draft-reviews/r-<taskname>.md` zu bearbeiten/kommentieren, und/oder
- direkt Korrekturen an der Aufgabendatei (bzw. an `altdir`-Dateien) vorzunehmen,

und dann in einer einzigen Antwort sowohl zu bestätigen, dass es weitergehen soll, als auch
anzugeben, welcher der Fälle unten zutrifft:

- **Fall A**: Die Aufgabe braucht noch eine weitere Überarbeitungsrunde.
- **Fall B**: Die Aufgabe ist jetzt reif für `stage: beta`.
- **Fall C**: Stop, die restlichen Schritte finden nicht oder nur manuell statt.

Fahre erst fort, wenn diese Antwort vorliegt. Ist aus der Antwort nicht eindeutig erkennbar,
welcher Fall gemeint ist, frage gezielt nach, bevor du weitermachst.

## Fall A: weitere Überarbeitungsrunde nötig

1. Poste den (jetzt vom Nutzer bearbeiteten) Inhalt von `.claude/draft-reviews/r-<taskname>.md`
   als Kommentar in das zugehörige GitHub-Issue:
   `gh issue comment <issue-nummer> --body-file .claude/draft-reviews/r-<taskname>.md`
2. Falls dabei direkt Korrekturen an der Aufgabendatei vorgenommen wurden (Kategorie
   "Schon erledigt" aus dem Review, plus ggf. weitere manuelle Änderungen des Nutzers), committe sie:
   Commit-Message `<taskfile>.md: #<issue-nummer>, minor changes`.
   Falls dabei auch `altdir`-Dateien geändert wurden, committe zuerst innerhalb von `altdir`,
   dann den aktualisierten Submodul-Pointer im Hauptrepo mit derselben Commit-Message.
   Falls eine substanzielle Änderung an Aufgabe oder altdir-Pendant dabei war,
   ersetze "minor changes" durch eine sehr knappe Charakterisierung (in English!) dieser Änderung.
3. `git push` machen (wenn oben `git pull` ging) bzw. anfordern.
4. Zeige dem Nutzer folgende Zeile zum manuellen Einfügen in Discord (Du kannst sie nicht selbst posten;
   wir haben keine Discord-Automatisierung):

   ```
   `<taskname>` begutachtet: <https://github.com/fubinf/propra-inf/issues/<issue-nummer>>.
   ```

## Fall B: bereit für `stage: beta`

1. Setze im YAML-Vorspann der Aufgabendatei `stage: beta`.
2. Ergänze in `ch/changes.md` eine neue Zeile im Stil der vorhandenen Einträge, mit heutigem Datum,
   z.B. `- **YYYY-MM-DD**: Aufgabe [PARTREF::taskname] freigegeben.` bzw. passend zum tatsächlichen
   Inhalt der Änderung. Berichte danach knapp, welche Zeile geschrieben wurde.
   Ausnahme: Falls die taskgroup (also `index.md`) im Topmatter `stage: draft` oder  `stage: alpha`
   stehen hat, unterbleibt der Eintrag (weil die Aufgabe noch gar nicht sichtbar wird; sie ist also nur
   latent freigegeben).
3. Baue die Website: `sedrila author --config sedrila.yaml --include_stage beta out`.
   Schlägt der Build fehl, nicht versuchen, den Fehler selbständig inhaltlich zu beheben, sondern
   anhalten und den Build-Fehler im Wortlaut berichten. In dem Fall ist der Skill-Ablauf beendet.
   Im Erfolgsfall hingegen:
4. Committe (Aufgabendatei, `ch/changes.md`, ggf. `altdir`-Submodul-Pointer/-Commits, falls in
   Schritt 2 dort etwas geändert wurde): Commit-Message `<taskfile>.md: #<issue-nummer>; final changes; stage: beta`.
5. `git push`.
6. Poste einen kurzen Abschluss-Kommentar ins GitHub-Issue, z.B. "Änderungen umgesetzt, Aufgabe ist
   jetzt `stage: beta`.":
   `gh issue comment <issue-nummer> --body "..."`.
   Schließe das Issue NICHT automatisch -- das bleibt eine manuelle Entscheidung des Nutzers.
7. Zeige dem Nutzer folgende Zeile zum manuellen Einfügen in Discord (nicht selbst posten):

   ```
   `<taskname>` freigegeben.
   ```
