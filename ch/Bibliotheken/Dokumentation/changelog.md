title: Aufbau von Changelog oder Relase Notes
stage: beta
timevalue: 0.75
difficulty: 2
---

[SECTION::goal::idea]

Ich verstehe, wie man Nutzer_innen über Änderungen an einer Software informiert.

[ENDSECTION]

[SECTION::background::default]

Früher wurden mit jeder neuen Version einer (ordentlichen) Software so genannte
"Release Notes" herausgegeben, die mehr oder weniger genau beschrieben, was sich geändert hat.

Heute haben sich im Open-Source-Bereich schlanke und etwas besser standardisierte Formate
für den gleichen Zweck herausbildet, bei denen das Dokument meistens
CHANGELOG (also "change log", Protokoll von Änderungen) genannt wird.

Da man sowas tunlichst auch selber führen sollte, wenn man Software entwickelt
(selbst, wenn es nur für persönliche Zwecke wäre), wollen wir uns hier
damit vertraut machen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Wissen anlesen

Arbeiten Sie [HREF::https://keepachangelog.com/de/1.0.0/] durch.

### Mit Realität vergleichen

- Betrachten Sie das Changelog von [freezegun](https://github.com/spulec/freezegun).
- [EQ] Nennen Sie einen Aspekt, der Ihnen daran gut gefällt
- [EQ] und einen zweiten, der verbesserungswürdig wäre.
- Betrachten Sie das Changelog von [Django](https://github.com/django/django).
  Django ist ein weitaus älteres und viel größeres Projekt als freezegun.
  Äh, wo haben die denn überhaupt das Changelog?

[HINT::Ort des Django-Changelogs]
GitHub: `docs/releases`  
Gerendert: [HREF::https://django.readthedocs.io/en/stable/]
[ENDHINT]

### Reflektion darüber

- [EQ] Warum benutzt Django wohl diese Form?
- [EQ] Angenommen, Sie entwickeln eine Webanwendung mit Django, die derzeit
  mit Django Version 4.1.7 läuft und wollen jetzt ein Upgrade auf die
  Version 5.0.4 machen.  
  Welche Dateien müssen Sie studieren, um die wichtigsten Dinge (nicht jede Einzelheit) zu überschauen,
  die bei dieser Umstellung schiefgehen könnten und vielleicht Änderungen an Ihrer
  Webanwendungen verlangen? Welche Abschnitte in diesen Dateien müssen Sie beachten?
- [EQ] Welche Abschnitte in welchen Dateien brauchen Sie zusätzlich, wenn Sie auch noch
  tolle neue Funktionalität mitbekommen möchten, die Sie vielleicht in Ihrer Webanwendung
  benutzen wollen?
- [EQ] Inwiefern ist dieses Format bei Django gut?
  Wäre ein normales Changelog besser?

[ENDSECTION]
[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Hauptsachen: Neues, Geändertes, Korrekturen]

Die Antworten müssen erkennen lassen, dass den Studierenden klar geworden ist,
was die wesentlichen Sorten von Informationen in Changelogs sind und
welche unterschiedliche Relevanz die haben:

- Neu hinzugekommene Funktionalität, wo es also Chancen zu nutzen gibt
- Änderungen am vorherigen Bestand, die existierende Software zum Stolpern bringen können
- Defektkorrekturen, die meist(!) nicht so viel Beachtung benötigen.

[ENDINSTRUCTOR]
