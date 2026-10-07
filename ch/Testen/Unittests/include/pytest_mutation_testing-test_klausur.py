from klausur import gesamtpunkte, modul_bestanden, note


def test_gesamtpunkte_mit_bonus():
    assert gesamtpunkte(70, 5) == 75


def test_gesamtpunkte_bonus_wird_gekappt():
    assert gesamtpunkte(70, 15) == 80


def test_gesamtpunkte_ohne_bonus_bei_nichtbestehen():
    assert gesamtpunkte(40, 8) == 40


def test_gesamtpunkte_hoechstens_100():
    assert gesamtpunkte(95, 10) == 100


def test_note():
    assert note(95) == 1
    assert note(85) == 2
    assert note(70) == 3
    assert note(55) == 4
    assert note(30) == 5


def test_modul_bestanden():
    assert modul_bestanden(60, True)
    assert not modul_bestanden(30, False)
