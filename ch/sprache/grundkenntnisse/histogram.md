title: Histogramm
description: |
  Übe hier das Laden von Dateien und den Umgang mit Schleifen und Strings.
timevalue: 1.0
difficulty: 2
assumes: PythonBasics101, PythonBasics102, PythonBasics103, PythonNumBoolString
---
!!! goal
    Viele Programmieraufgaben bestehen daraus Dateien einzulesen, die darin enthaltenen Daten zu
    bewerten und/oder zu transformieren und dann einen Output zu erhalten, der einen
    Informationsgewinn zu erhalten. 

In dieser Aufgabe soll eine `.txt`-Datei eingelesen werden. 
Es handelt sich hierbei um [die gesammelten Werke von
Shakespeare](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt). 
Es ist Ihnen überlassen, ob sie die Datei auf ihrer Festplatte speichern (leicht) oder ob Sie die
Datei aus einer Internetquelle einlesen (schwieriger).

Nachdem Sie die Datei eingelesen haben, sollen Sie ausgeben, welche Worte in dem Dokument vorhanden
sind und wie häufig diese vorkommen.
Überlegen Sie sich, welche Datenstruktur sich hierfür eignet.
Beachten Sie, dass Groß-/Kleinschreibung existiert; suchen Sie eine Funktion, die Ihnen die Worte in
Kleinschreibung umformt.
Als letzten Schritt geben Sie die Zählung als `.csv`-Datei wieder aus.

!!! notice "Format der .csv-Datei"
    `csv` steht für "Comma-separated values".
    Es gibt keinen allgemeingültigen Standard für das Dateiformat und viele Bibliotheken.
    Für unseren einfachen Fall benötigen wir aber keine Bibliothek.
    Es reicht, wenn in jeder Zeile ein Wort und seine absolute Häufigkeit von einem Komma getrennt
    aufgelistet werden.


<!-- Food for thought:

- Diese Aufgabe lässt sich auch mit Kommandozeilenprogrammen lösen. Sie können in der Aufgabe 
`AUFGABENNAME` im Shell-Bereich mehr dazu erfahren. 
- Überlegen Sie sich, wie sie die zehn am häufigsten vorkommenden Worte ausgeben können.
- Überlegen Sie sich, wie sie die zehn am häufigsten vorkommenden Worte mit echt mehr als drei 
Buchstaben ausgeben können. --> 

!!! submission "Abgabeformat"
    Die Abgabe besteht dem lauffähigen Programm und der erzeugten `.csv`-Datei.