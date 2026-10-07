"""
Bewertung einer Klausur mit Bonuspunkten aus dem Übungsbetrieb.
Alle Punktzahlen sind ganze Zahlen.
"""

BESTEHENSGRENZE = 50
MAX_BONUS = 10
MAX_PUNKTE = 100


def gesamtpunkte(klausurpunkte, bonuspunkte):
    """
    Liefert die Punktzahl, aus der die Note berechnet wird.
    Bonuspunkte zählen nur, wenn die Klausurpunkte allein schon die BESTEHENSGRENZE erreichen,
    und dann höchstens MAX_BONUS Punkte.
    Mehr als MAX_PUNKTE Punkte gibt es nicht.
    """
    if klausurpunkte < BESTEHENSGRENZE:
        return klausurpunkte
    if bonuspunkte > MAX_BONUS:
        bonuspunkte = MAX_BONUS
    return min(klausurpunkte + bonuspunkte, MAX_PUNKTE)


def note(punkte):
    """
    Vereinfachter Notenschlüssel: ab 90 Punkten 1, ab 80 Punkten 2, ab 65 Punkten 3,
    ab BESTEHENSGRENZE Punkten 4, darunter 5.
    """
    if punkte >= 90:
        return 1
    if punkte >= 80:
        return 2
    if punkte >= 65:
        return 3
    if punkte >= BESTEHENSGRENZE:
        return 4
    return 5


def modul_bestanden(klausurpunkte, uebungsschein):
    """Bestanden hat, wer mindestens BESTEHENSGRENZE Klausurpunkte und den Übungsschein hat."""
    return klausurpunkte >= BESTEHENSGRENZE and uebungsschein
