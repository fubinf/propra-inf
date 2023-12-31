---
Das WWW ist schon seit einiger Zeit dermaßen relevant, dass es oft Synonym zum Internet
verstanden wird. Im Laufe der Zeit sind die Fähigkeiten von Webseiten so weit gewachsen,
dass es Anwendungen gibt, die nichts weiter sind als kleine Browser mit eingeschränkten
Webseiten. Diese Praxis ist auch bei Smartphone-Apps geläufig.

Der Vorteil der Entwicklung einer Webanwendung, die dann für verschiedene Zielsysteme
als Anwendung ausgeliefert werden kann, liegt auf der Hand: Es reicht, eine Anwendung
mit nur einem Ziel zu entwickeln, statt für jedes Ziel separat zu entwickeln.

Historisch gesehen waren Webseiten mit jedweder Form von Benutzerinteraktion stark vom
Backend getrieben. Neue Beiträge in einem Gästebuch, Forum oder ähnlichem werden hier an einen
Server gesendet, dieser kümmert sich um die Persistenz dieser Daten und sorgt dafür, dass
zukünftige Aufrufe von Besuchern diesen neuen Beitrag auch zu sehen bekommen.

Der große Nachteil dieses Verfahrens ist, dass jede Interaktion dieser Art es nötig machte,
die Webseite komplett neu zu laden, da auch der eigene Beitrag nur dann zu sehen war, wenn man
die aktuelle Seite vom Server angefragt hat.

Einen großen Wechsel weg von diesem Verfahren wurde mit einer neuen API in Javascript möglich.
Der sogenannte XML Http Request (XHR) bildet die Grundlage davon, nur Teile einer Webseite
mit Daten des Servers zu verändern.

Als Konsequenz daraus hat die Wahl der Sprache im Backend drastisch an Relevanz verloren.
Es gibt sogar die Möglichkeit, Javascript als Sprache, die eigentlich strikt für das Frontend
gedacht war, im Backend einzusetzen.

Aus diesem Grund liegt der Fokus hier auf dem Frontend:

 * HTML (HyperText Markup Language) zur Beschreibung der Struktur und Inhalte einer Webseite
 * CSS (Cascading Style Sheets) zum Styling der Webseite
 * Javascript für Interaktivität
