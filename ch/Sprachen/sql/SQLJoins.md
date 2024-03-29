title: Zusammenführen von Tabellen mittels JOIN
stage: draft
timevalue: 0.1
difficulty: 2
assumes: SQLBasics, SQLSelect
---
!!! goal
    Wenn die benötigten Informationen in verschiedenen Tabellen liegen, müssen diese 
    zusammengeführt werden. In dieser Aufgabe geht es darum, eine Intuition für die verschiedenen 
    "JOIN"-Ausdrücke zu bekommen.

Zum Verknüpfen mehrerer Tabellen in einer Abfrage stellt SQL "Join" bereit.
Recherchieren Sie verschiedene Varianten des Join-Kommandos.

Es gibt darüber hinaus noch die Möglichkeit, ein Kreuzprodukt mittels kommaseparierter Listen
im *FROM* und entsprechenden Einschränkungen im *WHERE* ein identisches Ergebnis zu erreichen:

```sql
SELECT table1, table2, table3 WHERE table1.id = table2.t1_id AND table2.id = table3.t2_id;
```

In modernen Datenbanken wird das zu Joins optimiert. Was ist die Optimisierung, die hier
vorgenommen werden kann?

!!! submission
    Erläutern sie kurz, was Join tut und wodurch sich die verschiedenen Varianten unterscheiden.
    Für die Optimisierungsfrage reicht wahlweise eine kurze Begründung oder eine äquivalente
    Abfrage aus.
