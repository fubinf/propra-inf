title: Movie Rental - Refaktorierung
stage: beta
timevalue: 4.0
difficulty: 4
requires: refactor_movierental_planning
---

[SECTION::goal::experience,trial]

- Ich bin in der Lage auf Basis meines Plans einen Code zu refaktorieren.
- Ich kann erklären, wie mein Code funktioniert.

[ENDSECTION]

[SECTION::instructions::tricky]

[WARNING]
In vielen Aufgaben funktioniert es gut, immer nur den nächsten Arbeitsschritt zu lesen, um die 
Anforderung genau zu erfüllen.  
Bei dieser Aufgabe ist sinnvoller, zuerst _alle_ Arbeitsschritte zu lesen.
[ENDWARNING]

- [ER] Setzen Sie Ihren in [PARTREF::refactor_movierental_planning] formulierten Plan 
  in die Tat um.
  Dies beinhaltet die Refaktorierung _und_ die Implementierung der HTML-Ausgabe.
  Für die Abgabe müssen sie bereitstellen:
    - Quellcode
    - Tests
    - Dokumentation des Codes
- [EQ] Dokumentieren Sie während des Arbeitens an dieser Aufgabe kurz Ihre Arbeitsschritte.  
  Dokumentieren Sie vor allem auch Schritte, die Sie später wieder rückgängig machen!  
  Wenn es solche Schritte gibt: Wieso haben Sie diese wieder rückgängig gemacht?
- [EQ] Schreiben Sie eine kurze Dokumentation zum fertigen Produkt:
    - Erklären Sie, welche Funktion von welchem Teil des Codes abgedeckt wird.
    - Erklären Sie, wo und wie Ihre Lösung Vorteile gegenüber dem originalen Quellcode besitzt.
- [EC] Zeigen Sie eine Ausgabe Ihres überarbeiteten Programms.
  Übernehmen Sie hierfür die Beispiel-Eingabe aus dem originalen Testskript.

[FOLDOUT::Eingabewerte für die Abgabe]

Name: Bob  
Ausgeliehene Filme:

- Jaws, Regular , 2 Tage
- Golden Eye, Regular, 3 Tage
- Short New, New Release, 1 Tage
- Long New, New Release, 2 Tage
- Bambi, Childrens, 3 Tage
- Toy Story, Childrens, 4 Tage

[ENDFOLDOUT]

[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kein fester Lösungsweg vorgebbar]

[INCLUDE::/_include/Instructor-Auseinandersetzung.md]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
