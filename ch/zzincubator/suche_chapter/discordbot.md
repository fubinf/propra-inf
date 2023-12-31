title: Beispielanwendung -- Erstellung eines Discord Bots
timevalue: 2
difficulty: 3
assumes: async
---

!!! warning
    Um diese Aufgabe bearbeiten zu können, benötigen Sie einen Discord-Account.

!!! goal
    Mithilfe dieser Aufgabe werden Sie lernen, sich in eine Bibliothek einzuarbeiten und ein 
    funktionierendes Programm zu erstellen. 
    In diesem Beispiel wird es um die Erstellung eines Discord-Bots gehen, der eine Aufgabe 
    Ihrer Wahl übernehmen soll.
    Um das Hosting von Discord-Bots geht es in dieser Aufgabe explizit **nicht**.

Lesen Sie sich in die Dokumentation von Discord ein.
Ziel der Aufgabe ist es, einen Discord-Bot zu erstellen, der einige Aufgaben für Sie erledigen soll.
Erstellen Sie idealerweise einen neuen Discord-Server, auf den Ihr Bot sich verbinden soll.
So haben Sie die volle Kontrolle und alle Rechte zur Verfügung.

Eine Auswahl an Beispielen für Aufgaben, die Ihr Bot erledigen können soll:

- Wenn der Bot online kommt, soll er sein Erscheinen in einem Textchannel ankündigen. Er soll außerdem auf Antworten oder Reactions auf diese Ankündigung reagieren.
- Erstellen Sie einen Befehl für einen einfachen Taschenrechner. Das erste Zeichen soll eine 
  Operation der Grundrechenarten sein, darauf dürfen beliebig viele Zahlen folgen. Der Bot soll 
  als Antwort das Ergebnis zurückgeben.
- Erstellen Sie einen Befehl der Form `!MdN`, bei der "M" für eine Anzahl und "N" für die Größe 
  eines Würfels steht. 
  `2d8` wirft also zwei achtseitige Würfel. 
  Der Bot soll ausgeben, welche Würfel geworfen worden sind und welche Summe die Augenzahlen 
  ergeben.
- Lassen Sie den Bot einen Textkanal überwachen. 
  Wenn ein Nutzer den Befehl `!wetter STADT` eingibt, soll dem Nutzer der Inhalt der Webseite 
  "https://wttr.in/STADT" ausgegeben werden, wobei "STADT" für eine beliebige Stadt stehen 
  soll.
  
  Beispiel: [https://wttr.in/Berlin](https://wttr.in/Berlin)

Wählen Sie mindestens eine dieser Beispiele oder eine von mindestens vergleichbarem Aufwand.
Sollten Sie sich unsicher sein, ob Ihre Idee der geforderten Mindestanforderung entspricht,
fragen Sie bei Ihrem/Ihrer Tutor\_in vorher nach.

!!! instructor
    Hier geht es im Wesentlichen nur um I/O. Solange der Vorschlag ein Lesen und ein Schreiben
    beinhaltet, ist das okay. Nur eines von beiden ist prinzipiell auch denkbar, wenn der Rest
    ausreichend komplex ist.

Die Dokumentation von Discord klärt viele Begriffe über die Funktionen von Discord selbst.
Die Dokumentation von Discord davon aus, dass Sie Javascript benutzen.
Es gibt aber auch Bibliotheken für viele andere Sprachen, recherchieren Sie nach bezüglich einer 
Bibliothek in Ihrer gewünschten Sprache.

[Discord - Building your first Discord app](https://discord.com/developers/docs/intro)

!!! submission
    Die Abgabe besteht aus dem Code des Discord Bots.
    Schreiben Sie außerdem eine kurze Dokumentation zu den Befehlen des Bots.
    
