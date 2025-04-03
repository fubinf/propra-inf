title: "Pytest: Wie bringe ich Pytest dazu das auszuführen, was ich brauche?"
stage: alpha
timevalue: 0.75
difficulty: 2
assumes: m_pytest
---

[SECTION::goal::idea]

- Ich kann nützliche Pytest Parameter verwenden, um effektiver meine Tests auszuführen.

[ENDSECTION]
[SECTION::background::default]

Pytest selbst führt normalerweise alle vorhandenen Testfälle aus.
Mit Pytest-Parametern kann man gezielt steuern, welche Tests ausgeführt werden,
was besonders in großen Projekten viel Zeit spart und die Übersicht verbessert.

[ENDSECTION]
[SECTION::instructions::loose]

### Testgrundlage beschaffen

Bedienen wir uns zunächst einer frei zugänglichen Repository-Version von einer hilfreichen
Python-Tool Sammlung. Klonen Sie folgendes Repository in Ihren [TERMREF::Hilfsbereich]:

```shell
git clone https://github.com/pytoolz/toolz.git --tag 1.0.0
```

Eine version 1.0.0 wird i.d.R. dann bereitgestellt, wenn diese Version auch aus Sicht der Entwickler
stabil ist. Leider hilft uns eine stabile Version vorerst nicht weiter, weshalb wir ein klein wenig
Nachhelfen müssen, um ein Problem zu erzeugen. Um die Spannung nicht vorweg zu nehmen, wurde diese
Manipulation verschleiert. Diese Art der Änderung nennt sich auch [TERMREF::Mutationstests].

Stellen Sie sicher, dass Sie sich im geklonten Verzeichnis `1.0.0` befinden. Bitte führen Sie
folgenden Befehl aus:

```shell
encoded_command="c2VkICIyLDdkIiBiZW5jaC90ZXN0X3dvcmRjb3VudC5weSA+IGJlbmNoL3Rlc3Rfd29yZGNvdW50X3RtcCAmJiBtdiBiZW5jaC90ZXN0X3dvcmRjb3VudF90bXAgYmVuY2gvdGVzdF93b3JkY291bnQucHk="
echo "$encoded_command" | base64 --decode | bash
```

Sie wissen sicherlich bereits, dass wir mit `python -m pytest` oder einfach `pytest` alle
existierenden Pytest-Testfälle ausführen können.
Manchmal möchte man diese Ausführung erweitern, aber auch einschränken. Wie wir das umsetzen können,
lesen Sie bitte auf der offiziellen [Pytest-Seite](https://docs.pytest.org/en/6.2.x/usage.html) nach.
Anschließen - gerne auch parallel dazu - erstellen Sie folgende Befehle und dokumentieren das
jeweilige Ergebnis.

### Tests ausführen

Wenn Sie Pytest ohne weitere Informationen ausführen, sollte Ihnen direkt etwas am Ergebnis
aufgefallen sein. Sie haben einen Fehler als Antwort erhalten und diesen direkt gefixt - so glauben
Sie es zumindest. Um das zu überprüfen, wollen Sie den Test erneut laufen lassen, aber dieses Mal
nur den zuvor fehlgeschlagenen Test.

[ER] Starten Sie den Test nur auf die fehlgeschlagene Datei.

Wenn sehr viele Testfälle im Spiel sind, könnten bestimmte Fehler auch Effekte auf andere Testfälle
haben. In diesem Fall möchte man den Test nach einem Fehler gar nicht erst weiter laufen lassen,
sondern abbrechen.

[ER] Lassen Sie den Testlauf beim Auftreten des _ersten_ Fehlers abbrechen.

Manchmal kann ein Fehlschlag auch nur durch eine zeitliche Abhängigkeit auftreten, wie zum Beispiel
beim Abfragen eines TOTP, der beim Verwenden seine Gültigkeit verloren hat. In diesem Fall bietet es
sich an einen Testfall erneut auszuführen.

[ER] Lassen Sie einen fehlgeschlagenen Testfall wiederholt durchführen.

Es soll einfach nicht sein, der Testfall wird einfach nicht grün. Sie beschließen erst einmal auf Grund
mangelnden Risikos diesen Testfalls zu überspringen, bis Sie sich mit gleichgesinnten austauschen
können, um dieses Problem zu beheben.

[ER] Skippen Sie den fehlgeschlagenen Testfall beim ausführen aller Tests.

Natürlich dürfen wir diese leichtfertige Ignoranz nicht aus den Augen verlieren und sollten uns hin
und wieder vergewissern, dass wir beim fixen unsere Anwendung auch voran kommen und die entsprechenden
Testfälle wieder frei geben.

[ER] Verschaffen Sie sich einen Überblick über die geskippten Testfälle.

Sie haben weiterhin versucht dieses Problem zu beheben. Nach Ihrer Änderung hat sich der Test leider
nicht zu einem Besseren bewegt. Bevor Sie weiter machen, wollen Sie jedoch noch einmal alle Tests
mit detaillierteren Informationen ausführen, um zu prüfen, ob Ihre Codeanpassung keine Seiteneffekte
beinhaltet.

[ER] Starten Sie Pytest mit detaillierter Ausgabe.

Toll, diese Übersicht bietet Ihnen dir Möglichkeit wiederum in die gezielte Ansteuerung eines
Testfalls zu gehen.

[ER] Starten Sie Pytest nur für den Testfall `test_complement`.

Nachdem Sie jetzt die Gelegenheit hatten über das Problem des Fehlschlags zu diskutieren, haben Sie
sicherlich eine Lösung gefunden, alle Testfälle erfolgreich ausführen zu lassen, ohne einen Testfall
zu überspringen. Löschen Sie, falls noch vorhanden, die Skip-Anweisung.

[ER] Beseitigen Sie den Fehler und führen Sie Pytest ohne weitere Parameter aus. Wie sieht die Ausgabe
jetzt aus?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Kontrollhilfen]

Das initiale Kommando zum Manipulieren des Repository beinhaltet folgenden Befehl:

```shell
sed "2,7d" bench/test_wordcount.py > bench/test_wordcount_tmp && mv bench/test_wordcount_tmp bench/test_wordcount.py
```

Dieser sorgt dafür, dass ein Download der `bench/shakespear.txt` nicht durchgeführt wird, was zu einem
gewollten Fehler führen wird, wenn die Testfälle ausgeführt werden.

Nach Ausführung von Pytest erhält man in der Clone-Version 1.0.0 folgende Ausgabe:

```shell
======================================= test session starts =======================================
platform darwin -- Python 3.9.19, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/student/Downloads/github/toolz
collected 204 items                                                                               

bench/test_curry.py .                                                                       [  0%]
bench/test_curry_baseline.py .                                                              [  0%]
bench/test_first.py ..                                                                      [  1%]
bench/test_first_iter.py ..                                                                 [  2%]
bench/test_frequencies.py ..                                                                [  3%]
bench/test_get.py .                                                                         [  4%]
bench/test_get_list.py .                                                                    [  4%]
bench/test_groupby.py .                                                                     [  5%]
bench/test_join.py ...                                                                      [  6%]
bench/test_memoize.py .                                                                     [  7%]
bench/test_memoize_kwargs.py .                                                              [  7%]
bench/test_pluck.py .                                                                       [  8%]
bench/test_sliding_window.py .                                                              [  8%]
bench/test_wordcount.py F                                                                   [  9%]
toolz/sandbox/tests/test_core.py ....                                                       [ 11%]
toolz/sandbox/tests/test_parallel.py .                                                      [ 11%]
toolz/tests/test_compatibility.py .                                                         [ 12%]
toolz/tests/test_curried.py ..........                                                      [ 17%]
toolz/tests/test_curried_doctests.py .                                                      [ 17%]
toolz/tests/test_dicttoolz.py ...............................................               [ 40%]
toolz/tests/test_functoolz.py ......................................                        [ 59%]
toolz/tests/test_inspect_args.py .................                                          [ 67%]
toolz/tests/test_itertoolz.py ..................................................            [ 92%]
toolz/tests/test_recipes.py ..                                                              [ 93%]
toolz/tests/test_serialization.py .........                                                 [ 97%]
toolz/tests/test_signatures.py ...                                                          [ 99%]
toolz/tests/test_tlz.py .                                                                   [ 99%]
toolz/tests/test_utils.py .                                                                 [100%]

============================================ FAILURES =============================================
________________________________________ test_shakespeare _________________________________________

    def test_shakespeare():
>       with open('bench/shakespeare.txt') as f:
E       FileNotFoundError: [Errno 2] No such file or directory: 'bench/shakespeare.txt'

bench/test_wordcount.py:17: FileNotFoundError
===================================== short test summary info =====================================
FAILED bench/test_wordcount.py::test_shakespeare - FileNotFoundError: [Errno 2] No such file or directory: 'bench/shakespeare.txt'
================================== 1 failed, 203 passed in 1.63s ==================================
```

Dabei nethält die Datei `bench/test_wordcount.py` einen Fehler.

[EREFR::1] pytest bench/test_wordcount.py
Der folgende Wert bezieht sich auf die Anzahl gefundener Fehler
[EREFR::2] pytest --maxfail=1
[EREFR::3] pytest --last-failed, pytest --first-failed
[EREFR::4] In der Datei `test_wordcount.py` folgendes ergänzen:

 - Zeile 3: `import pytest`
 - Zeile 15: `@pytest.mark.skip(reason="Unbekannter Fehler")`

Mit `pytest -m "not skip"` kann die Ausgabe ohne übersprungenen Test angezeigt werden. Ohne Parameter
wird der Testfall mit `s` markiert und nicht ausgeführt.

[EREFR::5] pytest -rs
[EREFR::6] pytest -v
[EREFR::7] pytest toolz/tests/test_serialization.py::test_complement
[EREFR::8] Erstellen einer Datei `shakespeare.txt` im Verzeichnis `bench\`.
Ausgabe sieht wie folgt aus:

```shell
==================================== test session starts ====================================
platform darwin -- Python 3.9.19, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/student/Downloads/github/toolz
plugins: cov-5.0.0
collected 204 items                                                                         

bench/test_curry.py .                                                                 [  0%]
bench/test_curry_baseline.py .                                                        [  0%]
bench/test_first.py ..                                                                [  1%]
bench/test_first_iter.py ..                                                           [  2%]
bench/test_frequencies.py ..                                                          [  3%]
bench/test_get.py .                                                                   [  4%]
bench/test_get_list.py .                                                              [  4%]
bench/test_groupby.py .                                                               [  5%]
bench/test_join.py ...                                                                [  6%]
bench/test_memoize.py .                                                               [  7%]
bench/test_memoize_kwargs.py .                                                        [  7%]
bench/test_pluck.py .                                                                 [  8%]
bench/test_sliding_window.py .                                                        [  8%]
bench/test_wordcount.py .                                                             [  9%]
toolz/sandbox/tests/test_core.py ....                                                 [ 11%]
toolz/sandbox/tests/test_parallel.py .                                                [ 11%]
toolz/tests/test_compatibility.py .                                                   [ 12%]
toolz/tests/test_curried.py ..........                                                [ 17%]
toolz/tests/test_curried_doctests.py .                                                [ 17%]
toolz/tests/test_dicttoolz.py ...............................................         [ 40%]
toolz/tests/test_functoolz.py ......................................                  [ 59%]
toolz/tests/test_inspect_args.py .................                                    [ 67%]
toolz/tests/test_itertoolz.py ..................................................      [ 92%]
toolz/tests/test_recipes.py ..                                                        [ 93%]
toolz/tests/test_serialization.py .........                                           [ 97%]
toolz/tests/test_signatures.py ...                                                    [ 99%]
toolz/tests/test_tlz.py .                                                             [ 99%]
toolz/tests/test_utils.py .                                                           [100%]

==================================== 204 passed in 1.64s ====================================
```

[ENDINSTRUCTOR]
