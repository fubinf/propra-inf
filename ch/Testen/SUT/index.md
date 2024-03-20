title: Betriebsumgebung für ein System-under-Test
---
Das Testen eines [TERMREF::SUT] soll idealerweise unter so realistischen Bedingungen wie möglich
durchgeführt werden, um die Funktionalität, Leistung und Zuverlässigkeit eines Produkts 
zutreffend überprüfen und sicherzustellen zu können. 
Bei umfangreichen Anwendungssystemen stellt das ein erhebliches Problem dar.

Bei dem heute häufigsten Fall, einer Webanwendung, gibt es folgende typische Sorten
von Betriebsumgebung für das Testen:

- Entwickler_innen-Rechner, zum automatischen und manuellen Testen durch die 
  Entwickler_innen direkt während der Entwicklung.
- Build-Umgebung, zum automatisierten Testen, wenn neue Codebeiträge in die Versionsverwaltung
  gepusht wurden.
- Staging- oder Qualitätssicherungsumgebung, wo man versucht, die endgültige Betriebsumgebung
  ("Produktionsumgebung") ziemlich genau zu duplizieren.

Für unser einfaches SUT (siehe die Einführung unter [PARTREF::SystemUnderTest])
ist das noch nicht sehr kompliziert.
Zudem fallen die Fälle 1 und 3 weitgehend zusammen.

Dennoch gibt es dazu einiges zu lernen und das ist der Zweck dieser Aufgabengruppe.
