---
Reguläre Ausdrücke basierend auf dem Konzept der endlichen Automaten aus der theoretischen
Informatik finden weite Anwendung in der Softwareentwicklung. Das beschränkt sich hierbei
nicht nur auf die Verwendung in Code, sondern auch in den verwendeten Werkzeugen.

Hervorzuheben sind hier neben oft vorhandenen erweiterten Suchfunktionen auch die POSIX-
Anwendungen `grep` (global/regular expression/print) und `sed` (stream editor).

Es gibt zwei verbreitetere Syntax-Varianten zur Darstellung regulärer Ausdrücke:
Die "Basic Regular Expressions" (BRE) nach POSIX und die "Perl Compatible Regular
Expressions" (PCRE), die wie man dem Namen entnehmen ihren Ursprung in der Programmiersprache
Perl hatte.

Beide haben einige Erweiterungen (beispielsweise GNU-sed mit GNU-BCE und PHP mit einer
nichtnäher benannten Erweiterung von PCRE), wir werden hier aber im Kern die Basis von
PCRE behandeln.
