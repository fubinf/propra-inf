title: SSH-Agent
stage: draft
timevalue: 1.0
difficulty: 3
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::...]

Ich verstehe wie der ssh-agent funktioniert und wie ich diesen anwende.

[ENDSECTION]
[SECTION::background::default]

Man muss vor jedem Verbinden mit einem entfernten Rechner seine Passphrase eingeben, wenn man den SSH-Schlüssel hinterlegt hat.
Es gibt jedoch ein Verfahren, das Sicherheit und Bequemlichkeit kombiniert: SSH-Authentifizierungsagenten (`ssh-agent`). Der Agent hält Ihre privaten Schlüssel - für die Authentifizierung mit öffentlichen Schlüsseln - für den Rest der Sitzung im Speicher.

[ENDSECTION]
[SECTION::instructions::...]

### `ssh-agent` ausführen

Finden Sie heraus, wie man den `ssh-agent` auf dem System ausführt.

### Schlüssel hinzufügen

Starten sie den SSH-Agent und fügen Sie ihre Schlüssel dem Agenten hinzu.

### Mit entferntem Rechner verbinden

Verbinden Sie sich jetzt mit `andorra.imp.fu-berlin.de`.
Was hat sich geändert? Beschreiben Sie es in 1-2 Saetzen.

[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::...]

Geben Sie eine .md Datei ab, in der die Befehle und Erläuterungen enthalten sind.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
