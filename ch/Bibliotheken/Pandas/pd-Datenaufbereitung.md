title: "Aufbereitung von Datensätzen"
stage: beta
timevalue: 1.25
difficulty: 2
assumes: pd-Datenselektion2
---

[SECTION::goal::idea]
Ich kann fremde Datensätze mithilfe von Metadaten verstehen.

Ich verstehe, wie ich neue Daten für mich formatiere, sodass sie verständlich sind.
[ENDSECTION]


[SECTION::background::default]
Datensätze, insbesondere aus externen Quellen, liegen oft noch nicht in der Form vor,
wie man sie gerne hätte, und ohne Beschreibung versteht man sie oft gar nicht.
Hier erschließen wir einen solchen Datensatz mithilfe seiner Metadaten und machen seine Spalten lesbar.
Um fehlende und unpassende Werte geht es danach in [PARTREF::pd-Datenbereinigung].
[ENDSECTION]


[SECTION::instructions::detailed]

### Datensatz in den Hilfsbereich

Für diesen Aufgabenblock werden wir mit echten Wetterdaten arbeiten, die der 
[Deutsche Wetterdienst](https://opendata.dwd.de/climate_environment/CDC) 
bereitstellt.
Wer dort rumstöbert, wird wahrscheinlich schnell überfordert sein mit der Menge an
Daten und den teilweise kryptischen Bezeichnungen.
Wir beschäftigen uns hier mit den Monatswerten der Wetterstation `Berlin-Dahlem (FU)` (Stations-ID `00403`),
die bis 1719 zurückreichen.
Damit alle mit denselben Daten arbeiten, benutzen wir eine Kopie des Datenstands bis Ende 2025:
[PARTREF::wetter-dahlem.zip] enthält den Download des DWD unverändert
(Quelle: Deutscher Wetterdienst, Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)).

Erstellen Sie einen Ordner `wetter-dahlem` im [TERMREF::Hilfsbereich],
laden Sie die Datei herunter und extrahieren Sie sie in den erstellten Ordner.

[ER] Laden Sie die `produkt_klima_monat_17....txt` als `wetter_df` in Ihre Python-Umgebung.
Benutzen Sie dafür
[`read_table()`](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html#pandas.read_table).
Prüfen Sie das Ergebnis: `wetter_df` muss 17 Spalten haben.

[HINT::Mein `wetter_df` hat nur eine einzige Spalte]
Öffnen Sie die Datei in einem Editor und sehen Sie nach, welches Zeichen die Spalten trennt.
`read_table()` erwartet ohne weitere Angabe ein anderes Trennzeichen.
Den nötigen Parameter kennen Sie von `read_csv()`.
[ENDHINT]
<!-- time estimate: 15 min -->


### Datensatz verstehen (Metadaten)

Betrachten Sie den `DataFrame`.
Die ersten 3 Spalten sind wahrscheinlich recht verständlich, 
die `STATIONS_ID` gibt an, um welche Station es sich handelt, und
`MESS_DATUM_BEGINN` und `MESS_DATUM_ENDE` geben den Zeitraum der Messung an.

[EQ] Wie lang ist der Messzeitraum pro Eintrag?

[EQ] Die anderen Spalten (`QN_4 ... MX_RS`) haben kryptische Namen und daher ist nicht direkt
klar, um was für Messungen es sich hier handelt.
Finden Sie mit Hilfe der [TERMREF::Metadaten] (die anderen Dateien und die
[Datensatzbeschreibung des DWD](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/monthly/kl/BESCHREIBUNG_obsgermany-climate-monthly-kl_de.pdf)) 
heraus, was in diesen Spalten gespeichert wird.
Was steht in den Spalten `MO_N`, `MO_TT`, `MO_FK` und `MO_RR`?

[NOTICE]
Die Spalte `eor` wird nicht erklärt.
Sie markiert das Zeilenende ("end of row").
[ENDNOTICE]

Wie Sie merken, sind Metadaten unverzichtbar, um Daten zu verstehen, die man noch nicht kennt.
Sie wissen nun also, dass es sich hierbei um regelmäßige Messungen der genannten Werte handelt.

[EQ] Kaum zu glauben, dass alle diese Werte seit 1719 gemessen worden sein sollen. 
Außerdem komisch, wie viele Werte in den ersten Jahren der Messungen `-999` als Wert haben.
Wofür steht hier `-999` wahrscheinlich?

[EQ] Keine Datei erklärt `-999` ausdrücklich, Sie können Ihre Vermutung aber indirekt prüfen:
`Metadaten_Parameter_klima_monat_00403.txt` nennt in `Von_Datum`, ab wann es für welchen Parameter Messungen gibt.
Vergleichen Sie für `MO_N` und `MX_FX` das früheste `Von_Datum` mit dem frühesten Monat im `wetter_df`,
in dem die Spalte nicht `-999` enthält.
Was schließen Sie daraus?

[HINT::Wie finde ich den frühesten Monat ohne `-999`?]
Selektieren Sie mit `loc[]` und einem logischen Ausdruck die Zeilen, in denen die Spalte ungleich `-999` ist.
Bilden Sie davon das `min()` von `MESS_DATUM_BEGINN`.
[ENDHINT]
<!-- time estimate: 30 min -->


### Spalten bearbeiten

[ER] Beim Arbeiten mit diesen Daten ist es lästig, ständig nachzuschlagen, wofür `QN_4`
überhaupt steht. 
Erstellen Sie ein Dictionary `spaltennamen`, das den Spaltennamen (`QN_4...MX_RS`) aussagekräftige Namen zuordnet. 
Eine sinnvolle Benennung für das Mittel der Minimum-Lufttemperatur in Celsius wäre z.B. `Lufttemp_C_min_mean`.

[ER] Benennen Sie mithilfe des Dictionarys die Spalten um.
Nutzen Sie hierfür die Methode
[`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename).

[ER] Die Spalte `eor` ist für uns nicht relevant, denn sie enthält in jeder Zeile denselben Wert.
Entfernen Sie sie aus dem `wetter_df`, indem Sie mit `loc[]` alle übrigen Spalten auswählen
und das Ergebnis wieder `wetter_df` zuweisen.

[HINT::Wie wähle ich mit `loc[]` alle Spalten außer der letzten aus?]
`eor` ist die letzte Spalte.
Geben Sie also einen Spaltenbereich an, der bei der vorletzten Spalte endet.
Beachten Sie, dass diese Spalte jetzt ihren neuen Namen trägt.
[ENDHINT]

[ER] Bequemer geht es, wenn man direkt benennt, was wegfallen soll.
Entfernen Sie `STATIONS_ID` aus dem `wetter_df` mit der Methode
[`drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop).
`wetter_df` muss danach 15 Spalten haben.

[EQ] Angenommen, Sie wollen später langfristige Temperaturtrends berechnen:
Sollten die Spalten `QN_4` und `QN_6` dann im `wetter_df` bleiben oder ebenfalls entfernt werden?
Was sie bedeuten, steht unter "Qualitätsinformation" in der Datensatzbeschreibung des DWD.
Begründen Sie.

Damit ist der `DataFrame` lesbar und frei von irrelevanten Spalten.
In [PARTREF::pd-Datenbereinigung] lernen Sie, seine Daten zu bereinigen.
<!-- time estimate: 30 min -->
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kann sich in den Datensatz einarbeiten]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
