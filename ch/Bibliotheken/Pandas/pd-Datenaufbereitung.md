title: "Aufbereitung von Datensätzen"
stage: alpha
timevalue: 1.25
difficulty: 2
requires: pd-Gruppierung
---

[SECTION::goal::idea]
Ich kann fremde Datensätze mithilfe von Metadaten verstehen.

Ich verstehe, wie ich neue Daten für mich formattiere, sodass sie verständlich sind.
[ENDSECTION]


[SECTION::background::default]
Datensätze, insbesondere aus externen Quellen, liegen oft noch nicht in der Form vor,
wie man sie gerne hätte. Wie man mit Lücken, ungewünschten Wertebereichen und anderen Unreinheiten
umgeht wird in dieser Aufgabe behandelt.
[ENDSECTION]


[SECTION::instructions::loose]
# Datensatz in den Hilfsbereich

Für diesen Aufgabenblock werden wir mit echten Wetterdaten arbeiten, die der 
[Deutsche Wetterdienst](https://opendata.dwd.de/climate_environment/CDC) 
bereitstellt.
Wer auf dieser Seite rumstöbert wird wahrscheinlich schnell überfordert sein mit der Menge an
Daten und den teilweise kryptischen Bezeichnungen.
Wir beschäftigen uns hier mit den
[historischen Daten der Dahlem-Dorf Wetterstation](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/monthly/kl/historical/monatswerte_KL_00400_18890101_20241231_hist.zip)
von 1719 bis Ende 2024.

Erstellen Sie einen Ordner `wetter-dahlem` im [TERMREF::Hilfsbereich],
laden Sie die Daten herunter und extrahieren Sie diese in den erstellen Ordner.

[ER] Laden Sie die `produkt_klima_monat_17....txt` als `wetter_df` in ihre Python-Umgebung.
Ähnlich wie bei `read_csv()` gibt es hierfür eine Funktion
[`read_table()`](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html#pandas.read_table).

# Datensatz verstehen (Metadaten)

Betrachten Sie den `DataFrame`.
Die ersten 3 Spalten sind wahrscheinlich recht verständlich, 
die `STATIONS_ID` gibt an um welche Station es sich handelt und
`MESS_DATUM_BEGINN` und `MESS_DATUM_ENDE` geben den Zeitraum der Messung an.

[EQ] Wie lang ist der Messzeitraum pro Eintrag?

[EQ] Die anderen Spalten (`QN_4 ... MX_RS`) haben eher kryptische Namen und daher ist nicht direkt
klar, um was für Messungen es sich hier handelt.
Finden Sie mit Hilfe der [TERMREF::Metadaten] (die anderen Dateien und 
[hier](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/monthly/kl/BESCHREIBUNG_obsgermany-climate-monthly-kl_de.pdf)) 
heraus, was in diesen Spalten gespeichert wird.
Geben Sie für `MO_N`, `MO_TT`, `MO_FK` und `MO_RR` an, was in diesen gespeichert ist.

[NOTICE]
Die Spalte `eor` wird nicht erklärt, es handelt sich hierbei um einen Indikator um das Zeilende
zu markieren ("end of row").
[ENDNOTICE]

Wie Sie merken, sind Metadaten unglaublich wichtig, um Daten zu verstehen, die man noch nicht kennt.
Sie wissen nun also das es sich hierbei um regelmäßige Messungen der genannten Werte handelt.

[EQ] Nicht zu fassen das all diese Werte seit 1719 gemessen worden sein sollen. 
Außerdem komisch, wie viele Werte in den ersten Jahren der Messungen `-999` als Wert haben.
Wofür steht hier `-999` wahrscheinlich?

[EQ] Können Sie Ihre Vermutung mit Hilfe der Metadaten bestätigen? Falls ja mit welcher Datei?

# Spalten bearbeiten

[ER] Dass die Metadaten Auskunft über die Spaltennamen geben, ist erstmal schön und gut.
Beim Arbeiten mit diesen Daten, ist es allerdings müßig jedes Mal nachzuschlagen wofür "QN_4"
überhaupt steht. 
Erstellen Sie deshalb ein `Dictionary`, das die Spaltennamen  (`QN_4 ... MX_RS`) 
auf aussagekräftige Namen mapped.

[NOTICE]
Eine sinnvolle Benennung für das Mittel der Minimum-Lufttemperatur in Celsius wäre z.B. "Lufttemp_Min_C".
[ENDNOTICE]

[ER] Benennen mithilfe des `Dictionary` die Spalten um.
Nutzen Sie hierfür die Methode
[`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename).

[ER] Die Spalte `eor` ist für uns nicht relevant. 
Entfernen Sie diese aus dem `wetter_df` mithilfe von `iloc()` oder `loc()`.

[ER] Es gibt auch Methoden die extra für diese Zwecke gedacht sind.
Entfernen Sie `STATIONS_ID` mit der Methode 
[`drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop)
aus dem `wetter_df`.

[EQ] Sind die Spalten `QN4` und `QN6` relevant für uns oder sollten wir sie droppen?
Begründen Sie.

Nun haben Sie den Datensatz kennengelernt und mithilfe der Metadaten verstanden.
Sie haben außerdem angefangen das `DataFrame` zu formattieren, indem Sie Spalten lesbar umbenannt
haben und für uns irrelevante Spalten gedropped haben.
In [PARTREF::pd-Datenbereinigung] lernen Sie, die Daten des `DataFrame` richtig zu bereinigen.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kann sich in den Datensatz einarbeiten]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
