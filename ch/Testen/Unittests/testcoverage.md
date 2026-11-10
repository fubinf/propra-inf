title: Code Coverage mit pytest-cov - Von Tool-Nutzung zur kritischen Bewertung
stage: alpha
timevalue: 2.0
difficulty: 3
assumes: m_pytest, pytest-Methodik-Whitebox
requires: pytest_call
---

[SECTION::goal::idea]

- Ich kann Code Coverage mit `pytest-cov` messen und Coverage-Reports interpretieren
- Ich kann gezielt Tests für nicht abgedeckte Codezeilen ergänzen
- Ich verstehe, dass Coverage misst, welcher Code ausgeführt wird, aber nicht, ob sein Verhalten geprüft wird
- Ich kann ein begründetes Coverage-Ziel für ein konkretes Modul festlegen
[ENDSECTION]


[SECTION::background::default]
Code Coverage ([TERMREF::Überdeckung]) misst,
welcher Anteil Ihres Codes von Tests ausgeführt wird.
Während hohe Coverage-Werte beruhigend wirken können, sind sie kein Garant für Testqualität.

In dieser Aufgabe lernen Sie `pytest-cov` zunächst an einer bestehenden Codebasis kennen.
Anschließend testen Sie ein realitätsnahes Beispiel
und bauen dabei ein kritisches Verständnis für Coverage-Metriken auf.

[ENDSECTION]


[SECTION::instructions::detailed]

Im Folgenden verwenden wir „Testabdeckung“ und „Coverage“ synonym.

## Teil A: `pytest-cov`-Grundlagen mit bestehender Codebasis


### Vorbereitung

Arbeiten Sie in Teil A im `requests`-Repository und dessen `venv` aus [PARTREF::pytest_call].
`pytest-cov` ist dort bereits installiert,
weil es zu den Entwicklungsabhängigkeiten von `requests` gehört.

Machen Sie dort zuerst mit `git restore tests/` Ihre Änderungen an den Testdateien rückgängig,
beispielsweise die `@pytest.mark.fixme`-Markierungen.
Dann zeigt `git diff` später nur Ihre neuen Tests.


### Anwendung auf bestehende Codebasis

[EC] Ermitteln Sie den Befehl zur Coverage-Analyse für das Paket `requests` und führen Sie ihn aus.
Falls einzelne Tests fehlschlagen, ignorieren Sie das; die Coverage wird trotzdem gemessen.

[HINT::Wie starte ich die Coverage-Analyse?]
`pytest --help | grep cov` zeigt alle verfügbaren `--cov`-Optionen.
Ausführlicher gibt es das in der
[`pytest-cov`-Dokumentation](https://pytest-cov.readthedocs.io/).
[ENDHINT]

[EQ] Wie hoch ist die aktuelle Coverage der `requests`-Bibliothek?

[EC] Ermitteln Sie den Befehl, der zusätzlich die nicht abgedeckten Zeilen anzeigt,
und führen Sie ihn aus.

[HINT::Wie zeige ich die fehlenden Zeilen an?]
Der Parameter `--cov-report` bietet verschiedene Optionen.
Suchen Sie in der `pytest-cov`-Dokumentation nach `missing`.
[ENDHINT]

Wählen Sie ein Modul von `requests`, das nicht vollständig abgedeckt ist.
Ergänzen Sie in der passenden Testdatei unter `tests/` Testfälle,
die mindestens drei der bisher fehlenden Zeilen dieses Moduls abdecken.

[EC] Wiederholen Sie die Messung aus [EREFC::2]
und prüfen Sie, dass die gewählten Zeilen nicht mehr unter `Missing` stehen.

[EC] Zeigen Sie Ihre Ergänzungen mit `git diff tests/`.

[EQ] Erläutern Sie, warum Sie gerade diese Testfälle ergänzt haben.
Was war schwer zu testen?
<!-- time estimate: 45 min -->


## Teil B: Coverage-Bewertung mit realitätsnahem Beispiel


### Beispiel: E-Mail-Validator

Sie arbeiten mit einer E-Mail-Validierungsklasse, die viele Randfälle unterscheidet.

Legen Sie dafür in Ihrem [TERMREF::Arbeitsbereich] ein Verzeichnis `testcoverage/` an
und arbeiten Sie dort mit dem `venv` aus Teil A weiter.
Bleiben Sie nicht im `requests`-Repository:
Das hat bereits eine eigene `pyproject.toml` mit `pytest`-Einstellungen,
die mit Ihrer Konfiguration weiter unten kollidieren würde.

Damit die Dateien, die `pytest` und `pytest-cov` erzeugen, nicht eingecheckt werden,
legen Sie in `testcoverage/` eine Datei `.gitignore` mit folgendem Inhalt an:

```text
.coverage
htmlcov/
__pycache__/
.pytest_cache/
```

[ER] Erstellen Sie die Datei `email_validator.py` mit folgendem Inhalt:

```python
import re
from typing import List

class EmailValidator:
    """Validiert E-Mail-Adressen nach verschiedenen Kriterien."""
    
    def __init__(self, allow_internationalized: bool = False):
        self.allow_internationalized = allow_internationalized
        self._blocked_domains = set()
        self._required_domains = set()
        
    def block_domain(self, domain: str) -> None:
        """Blockiere eine Domain."""
        self._blocked_domains.add(domain.lower())
        
    def require_domain(self, domain: str) -> None:
        """Erlaube nur bestimmte Domains."""
        self._required_domains.add(domain.lower())
        
    def validate(self, email: str) -> dict:
        """Validiert eine E-Mail-Adresse."""
        if not email or not isinstance(email, str):
            return {'valid': False, 'errors': ['Email must be a non-empty string']}
            
        email = email.strip().lower()
        errors = []
        
        # Basic format check
        if '@' not in email:
            return {'valid': False, 'errors': ['Email must contain @']}
            
        try:
            local, domain = email.split('@', 1)
        except ValueError:  # pragma: no cover
            return {'valid': False, 'errors': ['Invalid email format']}
            
        # Validate local part
        if not local:
            errors.append('Local part cannot be empty')
        elif len(local) > 64:
            errors.append('Local part too long (max 64 characters)')
        elif '..' in local:
            errors.append('Local part cannot contain consecutive dots')
        elif local.startswith('.') or local.endswith('.'):
            errors.append('Local part cannot start or end with dot')
            
        # Validate domain
        domain_errors = self._validate_domain(domain)
        errors.extend(domain_errors)
        
        # Check blocked/required domains
        if domain in self._blocked_domains:
            errors.append(f'Domain {domain} is blocked')
            
        if self._required_domains and domain not in self._required_domains:
            errors.append(f'Domain {domain} not in allowed list')
            
        # Advanced regex validation
        if not errors and not self._regex_validate(email):
            errors.append('Email format invalid')
            
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'email': email,
            'local': local,
            'domain': domain
        }
        
    def _validate_domain(self, domain: str) -> List[str]:
        """Validiert Domain-spezifische Regeln."""
        errors = []
        
        if not domain:
            errors.append('Domain cannot be empty')
            return errors
            
        if len(domain) > 253:
            errors.append('Domain too long (max 253 characters)')
            
        if '..' in domain:
            errors.append('Domain cannot contain consecutive dots')
            
        if domain.startswith('.') or domain.endswith('.'):
            errors.append('Domain cannot start or end with dot')
            
        # Check for at least one dot
        if '.' not in domain:
            errors.append('Domain must contain at least one dot')
            
        # Check individual domain parts
        parts = domain.split('.')
        for part in parts:
            if len(part) > 63:
                errors.append(f'Domain part {part} too long (max 63 characters)')
            if not self.allow_internationalized and not part.isascii():
                errors.append(f'Domain part {part} contains invalid characters')
                    
        return errors
        
    def _regex_validate(self, email: str) -> bool:
        """Führt regex-basierte Validierung durch."""
        if self.allow_internationalized:
            # Simplified international pattern
            pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        else:
            # ASCII-only pattern
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
        return bool(re.match(pattern, email))
        
    def validate_batch(self, emails: List[str]) -> dict:
        """Validiert mehrere E-Mails auf einmal."""
        results = []
        stats = {'total': len(emails), 'valid': 0, 'invalid': 0, 'errors_by_type': {}}
        
        for email in emails:
            result = self.validate(email)
            results.append(result)
            
            if result['valid']:
                stats['valid'] += 1
            else:
                stats['invalid'] += 1
                for error in result['errors']:
                    stats['errors_by_type'][error] = stats['errors_by_type'].get(error, 0) + 1
                    
        return {
            'results': results,
            'stats': stats
        }
```

Der Kommentar `# pragma: no cover` hinter `except ValueError:` sorgt dafür,
dass `coverage.py` diesen Zweig in seinen Berichten nicht als fehlend zählt.
Das ist für Code gedacht, von dem man weiß, dass die Tests ihn nicht ausführen;
hier kann der `ValueError` gar nicht auftreten,
weil nach der Prüfung auf `@` immer zwei Teile entstehen.
Näheres in der
[`coverage.py`-Dokumentation zum Ausschließen von Code](https://coverage.readthedocs.io/en/7.17.2/excluding.html).

### Erste Tests und Coverage-Messung

[ER] Erstellen Sie die Datei `test_email_validator.py` mit folgenden Starttests:

```python
import pytest
from email_validator import EmailValidator

class TestEmailValidator:
    
    def test_valid_email(self):
        validator = EmailValidator()
        result = validator.validate('user@example.com')
        assert result['valid'] is True
        assert result['email'] == 'user@example.com'
        
    def test_invalid_email_no_at(self):
        validator = EmailValidator()
        result = validator.validate('invalid-email')
        assert result['valid'] is False
        assert 'Email must contain @' in result['errors']
```

[EC] Führen Sie die Tests mit Coverage aus: `pytest --cov=email_validator test_email_validator.py`

[EQ] Wie hoch ist die aktuelle Coverage?
Was sagt Ihnen das über die Testqualität?
<!-- time estimate: 15 min -->

### Coverage-Konfiguration in `pyproject.toml`

Damit Sie die Optionen nicht bei jedem Aufruf angeben müssen,
legen Sie im Verzeichnis `testcoverage/` eine `pyproject.toml` mit folgendem Inhalt an:

```toml
[tool.pytest.ini_options]
addopts = "--cov=email_validator --cov-report=term-missing --cov-report=html"

[tool.coverage.run]
branch = true
```

`addopts` hängt die angegebenen Optionen an jeden `pytest`-Aufruf an;
`--cov-report=html` erzeugt zusätzlich einen HTML-Report im Verzeichnis `htmlcov/`.
`branch = true` schaltet wie `--cov-branch` aus [PARTREF::pytest-Methodik-Whitebox]
die Zweigüberdeckung (Branch Coverage) ein.
Weitere Einstellungen beschreibt die
[`coverage.py`-Dokumentation zur Konfiguration](https://coverage.readthedocs.io/en/7.17.2/config.html).

[EC] Führen Sie die Tests erneut aus: `pytest`

[EQ] Was hat sich an der Ausgabe geändert?
Warum ist die Coverage-Prozentzahl jetzt eine andere als vorher, obwohl die Tests gleich geblieben sind?

Öffnen Sie den HTML-Report in `htmlcov/index.html`.

[EQ] Welche Code-Bereiche werden nicht getestet?
<!-- time estimate: 15 min -->


### Systematischer Testausbau

[ER] Erweitern Sie die Tests, um verschiedene Randfälle abzudecken:

- Leere/None-Eingaben
- Verschiedene Domain-Validierungsfehler
- Blocked/Required Domains
- Batch-Validierung
- Internationale Zeichen

[EQ] Nach dem Testausbau: Wie hat sich die Coverage verändert?
Gibt es Code-Bereiche, die schwer zu testen sind?
<!-- time estimate: 25 min -->


### Coverage-Kritik

[ER] Legen Sie die Datei `test_fake_coverage.py` an
und ergänzen Sie darin den folgenden Testrahmen so,
dass `pytest test_fake_coverage.py` danach 100% Line Coverage für `email_validator.py` meldet —
aber ohne eine einzige sinnvolle Assertion:

```python
from email_validator import EmailValidator

def test_fake_coverage():
    """Dieser Test erreicht hohe Coverage, testet aber nichts Sinnvolles."""
    validator = EmailValidator()
    # Rufe alle Code-Pfade auf, prüfe aber nie die Korrektheit:
    validator.validate('')  # Empty string
    validator.validate('user@example.com')  # Valid
    validator.validate('invalid')  # No @
    # ... weitere Aufrufe ohne Assertions
    validator.block_domain('spam.com')
    validator.require_domain('company.com')
```

[EC] Führen Sie diesen Test allein aus: `pytest test_fake_coverage.py`

[EQ] Was zeigt dieser Test über die Aussagekraft von Coverage-Metriken?

Nun die Gegenrichtung: ein Test mit wenigen, aber wichtigen Assertions.
Ein E-Mail-Validator steht oft vor Code, der die Adresse weiterverarbeitet,
z.B. in eine Datenbankabfrage einsetzt oder in eine Webseite einbaut.
Vor Angriffen schützt dort vor allem dieser Code selbst,
z.B. mit parametrisierten Abfragen gegen [TERMREF::SQL Injection]
und mit Escaping beim Einbau in HTML.
Der Validator ist eine zusätzliche Verteidigungslinie:
Er sollte Eingaben ablehnen, die dort Schaden anrichten könnten.

[ER] Schreiben Sie in `test_email_validator.py` einen Test `test_security_critical_validation`,
der für mindestens drei solche gefährlichen Eingaben prüft, dass `validate()` sie als ungültig ablehnt.
Beispiel für eine solche Eingabe: `"'; DROP TABLE users; --@evil.com"` (ein SQL-Injection-Versuch).

[HINT::Mir fallen keine gefährlichen Eingaben ein]
Denken Sie an Zeichen, die in anderen Sprachen eine Sonderbedeutung haben:
HTML-Tags wie `<script>...</script>`, Pfadangaben wie `../../`
oder Shell-Befehle wie `; rm -rf /`.
[ENDHINT]

[EQ] Führen Sie `pytest test_email_validator.py` aus, also ohne `test_fake_coverage`.
Um wie viel erhöht der neue Test die Coverage gegenüber Ihrem Stand nach dem Testausbau?
Warum ist er trotzdem wertvoller als `test_fake_coverage`?
<!-- time estimate: 20 min -->


### Reflexion

[EQ] Welches Coverage-Ziel hätten Sie für den `EmailValidator` gesetzt und warum?
<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
