def bonuspunkte(blattpunkte):
    """
    Berechnet die Bonuspunkte aus den Punktzahlen der Übungsblätter.
    Auf jedem Blatt sind 0 bis 20 Punkte möglich;
    kleinere oder größere Werte führen zu einem ValueError.
    Ein Blatt mit mindestens 10 Punkten bringt 1 Bonuspunkt,
    ein Blatt mit voller Punktzahl 2 Bonuspunkte.
    """
    bonus = 0
    for punkte in blattpunkte:
        if punkte < 0 or punkte > 20:
            raise ValueError(f"Ungültige Punktzahl: {punkte}")
        if punkte == 20:
            bonus += 2
        elif punkte >= 10:
            bonus += 1
    return bonus
