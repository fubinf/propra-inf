title: Uhrzeiten suchen
stage: draft
timevalue: 1.0
difficulty: 2
---
Erzeugen Sie einen PCRE mit dem valide Uhrzeiten gefunden werden. Eine Uhrzeit ist valide,
wenn sie aus einem Teil für Stunden und Minuten besteht, getrennt durch einen Doppelpunkt.
Der Stunden-Teil darf Werte zwischen 00 und 23 haben und der Minuten-Teil zwischen 00 und 59.
Beide Teile sollen immer zweistellig sein.

!!! submission "Abgabe"
    Geben Sie einen Befehl an, der Text aus der der Standardeingabe liest und nur valide
    Uhrzeiten daraus ausgibt. Verwenden Sie das Kommando `grep`.
