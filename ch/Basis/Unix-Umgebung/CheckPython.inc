### Python prüfen

Rufen Sie `python -V` auf, um die Python-Version zu prüfen.
Wir brauchen mindestens Python 3.11.

Rufen Sie `pip -V` auf, um die Version von Pip zu prüfen.
Die genaue Version ist nicht wichtig, aber `pip` muss funktionieren.
Pip ist der Paketmanager von Python und dient dazu, zusätzliche Python-Bibliotheken zu installieren.

Sind Python oder Pip nicht installiert, so holen Sie dies mittels
`sudo apt python3 python3-pip python3-venv python-is-python3`
nach und wiederholen Sie dann die obigen beiden Tests.

Sobald Sie im nächsten Abschnitt des Basiskapitels gelernt haben, wie das geht, 
geben Sie die Ausgabe des folgenden Kommandos als Textdatei ab:
`uname -a; cat /etc/os-release|grep PRETTY; python -V; pip -V`  
(Sie sollten sich jetzt also eine Notiz machen, um das nicht zu vergessen.)
