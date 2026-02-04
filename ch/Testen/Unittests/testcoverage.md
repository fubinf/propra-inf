title: Code Coverage mit pytest-cov - Von Tool-Nutzung zur kritischen Bewertung
stage: draft
timevalue: 2.5
difficulty: 3
assumes: m_pytest
requires: pytest_call
---

[SECTION::goal::idea]

- Ich kann Code Coverage mit pytest-cov für bestehende und neue Codebasis anwenden
- Ich kann Coverage-Reports interpretieren und systematisch 100% Coverage erreichen
- Ich verstehe die Grenzen und Fallstricke von Coverage-Metriken
- Ich kann angemessene Coverage-Ziele für verschiedene Projekttypen definieren

[ENDSECTION]
[SECTION::background::default]

Code Coverage misst, welcher Anteil Ihres Codes von Tests ausgeführt wird. Während hohe Coverage-Werte beruhigend wirken können, sind sie kein Garant für Testqualität.

Eine 100%ige Zeilenabdeckung kann existieren, ohne dass ein einziger sinnvoller Test geschrieben wurde. Umgekehrt können gut durchdachte Tests mit 80% Coverage mehr Vertrauen schaffen als oberflächliche Tests mit 100% Coverage.

In dieser Aufgabe lernen Sie pytest-cov zunächst an bestehender Codebasis kennen, bevor wir ein realitätsnahes Beispiel entwickeln und ein kritisches Verständnis für Coverage-Metriken aufbauen.

Schön ist es, wenn man zusätzlich zu seinem Testergebnis auch sieht, dass sich die Testabdeckung verbessert. Um diese Abfrage nicht separat durchführen zu müssen, verwenden wir das pytest-cov Plugin.

[ENDSECTION]
[SECTION::instructions::detailed]

## Teil A: pytest-cov Grundlagen mit bestehender Codebasis

Zunächst lernen Sie pytest-cov an einer bestehenden Codebasis kennen und erreichen systematisch 100% Coverage.

### pytest-cov Setup

pytest-cov ist ein pytest-Plugin, das Coverage-Messung nahtlos in Ihren Test-Workflow integriert.

[EC] Installieren Sie pytest-cov: `pip install pytest-cov`

[EC] Verifizieren Sie die Installation: `pytest --version` und `pytest --help | grep cov`

### Anwendung auf bestehende Codebasis

Wenden Sie pytest-cov auf die `toolz`-Bibliothek aus [PARTREF::pytest_call] an.

[EC] Wie sieht der Kommandobefehl zum Ausführen einer Testabdeckungsanalyse für das Verzeichnis `toolz` aus?

[EQ] Wie hoch ist die aktuelle Coverage der toolz-Bibliothek? Was sagt Ihnen das über die Testqualität?

[EC] Wie finden Sie heraus, welche spezifischen Zeilen nicht abgedeckt sind?

[HINT::Missing Lines anzeigen]
Der `--cov-report` Parameter bietet verschiedene Optionen. Suchen Sie in der pytest-cov Dokumentation nach "missing".
[ENDHINT]

[ER] Ergänzen Sie die fehlenden Testfälle so, dass die Testabdeckung der relevanten Module auf 100% steht.

[EQ] Erläutern Sie, warum Sie gerade diese Ergänzungen und Testfälle hinzugefügt haben. Was war schwer zu testen?

## Teil B: Coverage-Bewertung mit realitätsnahem Beispiel

Nun entwickeln wir ein komplexeres Verständnis von Coverage-Qualität mit einem eigenen Beispiel.

Lesen Sie zunächst diesen Artikel: [Code Coverage – Kein zuverlässiges Qualitätsmaß](https://blog.ordix.de/code-coverage-kein-zuverlaessiges-qualitaetsmass), um die kritischen Aspekte von Coverage zu verstehen.

### Realitätsnahes Beispiel: E-Mail Validator

Wir arbeiten mit einer E-Mail-Validierungsklasse - ein typisches Real-World-Szenario mit verschiedenen Edge Cases.

Erstellen Sie `email_validator.py`:

```python
import re
from typing import List, Optional

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
        except ValueError:
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
            errors.append('Domain must contain at least one dot')
            
        # Validate each domain part
        parts = domain.split('.')
        for part in parts:
            if not part:
                continue
            if len(part) > 63:
                errors.append(f'Domain part {part} too long (max 63 characters)')
            if not part.replace('-', '').replace('_', '').isalnum():
                if not self.allow_internationalized:
                    errors.append(f'Domain part {part} contains invalid characters')
                    
        return errors
        
    def _regex_validate(self, email: str) -> bool:
        """Führt regex-basierte Validierung durch."""
        if self.allow_internationalized:
            # Simplified international pattern
            pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
        else:
            # ASCII only pattern
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
        return bool(re.match(pattern, email))
        
    def validate_batch(self, emails: List[str]) -> dict:
        """Validiert mehrere E-Mails auf einmal."""
        results = []
        stats = {'valid': 0, 'invalid': 0, 'errors_by_type': {}}
        
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

### Erste Tests und Coverage-Messung

Erstellen Sie `test_email_validator.py`:

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

[EQ] Wie hoch ist die aktuelle Coverage? Was sagt Ihnen das über die Testqualität?

### Coverage-Konfiguration für eigenes Projekt

Nach der Analyse bestehender Codebasis erstellen Sie nun eigene Coverage-Konfiguration.

Erstellen Sie eine `pyproject.toml` für bessere Coverage-Einstellungen:

```toml
[tool.pytest.ini_options]
addopts = "--cov=email_validator --cov-report=term-missing --cov-report=html"

[tool.coverage.run]
omit = [
    "test_*.py",
    "*test*.py"
]
branch = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError"
]
```

[EC] Führen Sie Tests erneut aus: `pytest`. Was hat sich geändert?

[EC] Öffnen Sie den HTML-Report in `htmlcov/index.html`. Welche Code-Bereiche werden nicht getestet?

### Systematischer Testausbau

[ER] Erweitern Sie die Tests, um verschiedene Edge Cases abzudecken:
- Leere/None-Eingaben
- Verschiedene Domain-Validierungsfehler  
- Blocked/Required Domains
- Batch-Validierung
- Internationale Zeichen

[EQ] Nach dem Testausbau: Wie hat sich die Coverage verändert? Gibt es Code-Bereiche, die schwer zu testen sind?

### Coverage-Kritik

Jetzt werden Sie die Grenzen von Coverage-Metriken verstehen:

[ER] Erstellen Sie einen Test, der 100% Line Coverage erreicht, aber trotzdem fehlerhaft ist:

```python
def test_fake_coverage():
    """Dieser Test erreicht hohe Coverage, testet aber nichts Sinnvolles."""
    validator = EmailValidator()
    # Ruft alle Code-Pfade auf, aber ohne sinnvolle Assertions
    validator.validate('')  # Empty string
    validator.validate('user@example.com')  # Valid
    validator.validate('invalid')  # No @
    validator.block_domain('spam.com')
    validator.require_domain('company.com')
    # ... weitere Aufrufe ohne Assertions
```

[EQ] Was zeigt dieser Test über die Aussagekraft von Coverage-Metriken?

[ER] Erstellen Sie jetzt einen Test mit niedriger Coverage, aber hoher Qualität:

```python
def test_security_critical_validation():
    """Testet kritische Sicherheitsaspekte mit wenigen, aber wichtigen Assertions."""
    validator = EmailValidator()
    
    # SQL Injection Attempt
    result = validator.validate("'; DROP TABLE users; --@evil.com")
    assert not result['valid']
    
    # XSS Attempt
    result = validator.validate('<script>alert("xss")</script>@evil.com')
    assert not result['valid']
```

### Reflexion und Best Practices

[EQ] **Coverage-Ziele festlegen:** Basierend auf Ihrer Erfahrung:
1. Welche Coverage-Ziele würden Sie für verschiedene Projekttypen setzen?
2. Wann ist 80% Coverage besser als 95%?
3. Welche Code-Bereiche sollten immer 100% Coverage haben?

[EQ] **Quality Gates:** Stellen Sie sich vor, Sie implementieren Coverage-Requirements in einer CI/CD-Pipeline:
1. Welche Metriken würden Sie überwachen? (Line/Branch/Function Coverage?)
2. Bei welchen Coverage-Abfällen würden Sie Builds fehlschlagen lassen?
3. Wie würden Sie mit Legacy-Code umgehen?

[EQ] **Mutation Testing:** Research-Frage: Informieren Sie sich über "Mutation Testing" und vergleichen Sie es mit Coverage-Testing. Was sind die Vor-/Nachteile?

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
