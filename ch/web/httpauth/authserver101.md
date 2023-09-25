title: Einfacher HTTP-Proxy
description: |
  Einfacher HTTP-Proxy als Grundlage für die späteren Authentifizierungsprobleme
timevalue: 2
difficulty: 2
---
!!! goal
    Hier wird bei der Erstellung eines einfachen HTTP-Proxys Verständnis für das allgegenwärtige
    Protokoll HTTP geschaffen.

Im Kontext dieser Aufgabe sind die gültige und ungültige Session-ID jeweils die Zeichenkette
"gültig" beziehungsweise "ungültig". Sowohl der GET-Parameter als auch der Cookie haben den
Namen "sessioid".

Im Verlauf der Aufgaben werden sich die gültigen Sessions allerdings verändern und es ist
ratsam, das Programm jetzt bereits darauf auszulegen, dass das möglich ist und zu den jeweiligen
Sessions auch Daten hinterlegt werden können.

<div id="httpauth"></div>
<script src="httpauth.js" defer></script>

!!! warning "CORS - Cross-Origin Resource Sharing"
    Das gegebene Test-Interface unten macht Anfragen gegen den andere Rechner vom Webserver.
    Diese sind aus Sicherheitsgründen standardmäßig nicht zugelassen. Auf Seite des Proxys
    müssen Vorkehrungen vorgenommen werden, damit diese Anfragen gültig sind.

!!! submission
    Hier wird als Abgabe Code erwartet, der fehlerfrei durch alle gegebenen Tests läuft.
