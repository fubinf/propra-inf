title: Suchen und Finden passender Frameworks
description: |
  Man programmiert deutlich schneller, wenn man das Rad nicht ständig neu erfindet. 
timevalue: 2
difficulty: 3
assumes: framework_vs_library
---
!!! goal
    Gängige Frameworks helfen dabei, bestimmte Strukturen effizient abzubilden.
    In dieser Aufgabe geht es darum, die Suche zu einem Framework zu bestreiten und zu beschreiben.

Stellen Sie sich folgendes Szenario vor: Ihnen wird die Aufgabe gestellt, ein Blog zu gestalten. 
Die Wahl der Programmiersprache ist Ihnen hier selbst überlassen.
Damit Sie mit der Aufgabe beginnen können, müssen Sie sich für ein Framework entscheiden.
Ihr Auftraggeber gibt Ihnen hierbei einige Anforderungen mit, die bei der Suche nach einem 
Framework entscheidend sein können.

- Sie sollen ein geläufiges Framework wählen, damit bei späterer Wartung der Webseite auch ein 
  anderer Programmierer schnell versteht, wie diese funktioniert.
- Sie benötigen für die Speicherung der Daten des Blogs eine Datenbank. 
  Es ist dem Auftraggeber wichtig, dass die genaue Datenbankimplementierung austauschbar sein soll.
  Das meint hier beispielsweise die Wahl zwischen SQLite, MySQL, PostgreSQL etc.
- Der Auftraggeber glaubt, dass er in Zukunft die Webseite durch zusätzliche Funktionalitäten 
  erweitern möchte. 
  Es ist also eine Voraussetzung, dass eine Erweiterung einfach ist.
- Der Auftraggeber möchte nach Möglichkeit das Frontend und das Backend in derselben 
  Programmiersprache gestaltet haben.

Recherchieren Sie, ob Ihre Programmiersprache Frameworks zum Thema Web-Programmierung anbietet.
Sollten Ihnen mehrere Frameworks zur Verfügung stehen, müssen Sie diese vergleichen.
Versuchen Sie, alle der oben genannten Anforderungen zu erfüllen.
Sollte Ihr Framework nicht alle Punkte abdecken können, gibt es vielleicht die Möglichkeit durch 
weitere Bibliotheken die gewünschte Funktionalität nachzurüsten. 

Es wird nicht erwartet, einen detaillierten Vergleich aller Frameworks anzufertigen. Teil der
Aufgabenstellung ist, eine sinnvolle Vorauswahl zu treffen und diese auch zu begründen.

!!! submission 
    Beschreiben Sie Ihre Recherche: Haben Sie nur Google benutzt oder standen Ihnen auch andere 
    Werkzeuge zur Verfügung?
    Gehen Sie auch darauf ein, warum Sie sich für ein bestimmtes Framework entschieden haben, 
    wenn Ihnen mehrere zur Verfügung standen.

!!! instructor
    In der Aufgabe geht es vor allem um die Suche und Entscheidung, mit genügender Argumentation 
    könnte fast jedes Web-Framework benutzt werden.
    Nur als kleiner unvollständiger Überblick über verschiedene Sprachen gedacht: 

    In Python sind `Django` und `Flask` geeignet, wobei `Flask` mehr Programmieraufwand 
    beinhalten kann. 

    In Scala spielt `Play` eine große Rolle, ebenso `Cask`, welche beide vom Funktionsumfang mit 
    `Django` und `Flask` vergleichbar sind. Die Community ist hier allerdings noch mehr im Wandel.
    Beispielsweise wird Laminar auch direkt auf der Webseite von scala-js verlinkt.
