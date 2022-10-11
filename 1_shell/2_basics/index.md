title: Prompt und Navigation

#Prompt

Als Prompt (deutsch "Eingabeaufforderung") werden die Zeilen bezeichnet, die dem Benutzer der Shell signalisieren, dass er eine Eingabe tätigen kann. Üblicherweise handelt es sich hierbei um eine einzelne Zeile mit einer Reihe an Informationen, gefolgt von einem (ggf. blinkenden) Text-Cursor.

Informationen, die man in Prompts häufig findet, sind:
* Name des Benutzers
* Name des Computers
* Aktueller Pfad (`pwd` - present working dir)
* Superuser-Indikator

Selbst bei Shells, die standardmäßig auf nahezu alle Informationen im Prompt verzichten, existiert der Superuser-Indikator. Dieser ist das letzte Symbol vor dem Beginn der Benutzereingabe (außer gegebenenfalls Leerzeichen). Es gibt hier das `$` oder `%`, das bedeutet, dass man aktuell keine Superuser-Rechte hat, und das `#`, das Superuser-Rechte symbolisiert.

Das ist besonders wichtig, da man bei Anleitungen, die Shell-Befehle beinhalten, häufig diesen Indikator sehen kann. Findet man hier Befehle, die mit einem Indikator anfangen, sollte man zunächst einmal wissen, dass dieser nicht Teil des Befehls ist und daher auch nicht eingegeben/kopiert werden sollte, und außerdem, dass Befehle, denen ein `#` vorangestellt sind, nicht oder nicht vollständig funktionieren werden, wenn man nicht selbst Superuser-Rechte besitzt.

Es gibt je nach Shell noch eine Vielzahl an zusäztlich darstellbaren Informationen. Geläufig sind beispielsweise Informationen zu git oder einen Indikator darüber, ob der vorherige Befehl erfolgreich war oder nicht.

#Navigation

cd, ls, pwd, history, tab completion, ggf. z, mc, ranger
