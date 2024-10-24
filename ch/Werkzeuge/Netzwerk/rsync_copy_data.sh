#!/bin/bash

# Verzeichnis festlegen
unterordner="$HOME/rsync_copy_data/"

# Sicherstellen, dass der Unterordner existiert
if [ ! -d "$unterordner" ]; then
    mkdir -p "$unterordner"
fi

# 20 Dateien erstellen
for i in {1..5}; do
    echo "Inhalt der Datei $i" > "$unterordner/datei_$i"
done

echo "$i Dateien wurden im Unterordner erstellt: $unterordner"
