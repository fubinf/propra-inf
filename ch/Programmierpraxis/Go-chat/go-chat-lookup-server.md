title: "HTTP Chat: Lookup-Server"
stage: draft
timevalue: 2.5
difficulty: 3
assumes: go-http-client, go-http-server, go-json
---

[SECTION::goal::experience,product]
Ich habe einen Lookup-Server implementiert, wo sich Benutzer des Chats ein- und ausloggen können.
[ENDSECTION]

[SECTION::background::default]
Der Lookup-Server behält den Überblick über alle eingeloggten Benutzer des Chats.
Will Person A mit Person B schreiben, so fragt "Peer A" beim Lookup-Server nach, was die Adresse vom
"Peer B" ist.

Ist die Person B zu diesem Zeitpunkt im Chat eingeloggt, so bekommt Person A die Adresse und kann Person B
direkt anschreiben.

In dieser Aufgabe implementieren Sie nur das Ein- und Ausloggen sowie das Nachschlagen.
[ENDSECTION]

[TOC]

[SECTION::instructions::loose]

### IP-Adresse des Rechners ermitteln

Als Erstes müssen Sie herausfinden, was die IP-Adresse Ihres Rechners im WLAN ist.
Das wird die IP-Adresse des Lookup-Servers sein, welche die Peer-Programme dann als
Kommandozeilenargument übergeben bekommen.

[FOLDOUT::MacOS oder ein Ubuntu-ähnliches Linux]
Führen Sie im Terminal `ifconfig | grep inet` aus.
Ihre IP-Adresse im WLAN ist die erste `inet` (nicht `inet6`!) Adresse, die nicht `127.0.0.1`
(localhost) ist.

Im folgenden Beispiel ist das die Adresse `192.168.178.76`:

```terminaloutput
$ ifconfig | grep inet
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	inet6 fe80::14f4:cfcf:6f29:aae%en0 prefixlen 64 secured scopeid 0xf
	inet6 2a02:2455:87d9:9b00:1071:2941:2539:32ab prefixlen 64 autoconf secured
	inet6 2a02:2455:87d9:9b00:f460:1fe9:146d:f3a1 prefixlen 64 autoconf temporary
	inet6 2a02:2455:87d9:9b00:14f4:cfcf:6f29:aae prefixlen 64 deprecated dynamic
	inet 192.168.178.76 netmask 0xffffff00 broadcast 192.168.178.255
	inet6 fe80::345d:b9ff:fe02:13a8%awdl0 prefixlen 64 scopeid 0x11
	inet6 fe80::345d:b9ff:fe02:13a8%llw0 prefixlen 64 scopeid 0x12
	inet6 fe80::7643:cb2b:4a8e:936d%utun0 prefixlen 64 scopeid 0x13
	inet6 fe80::10b2:bfc4:a2bb:2adc%utun1 prefixlen 64 scopeid 0x14
	inet6 fe80::63e1:13f7:7af5:b15f%utun2 prefixlen 64 scopeid 0x15
	inet6 fe80::ce81:b1c:bd2c:69e%utun3 prefixlen 64 scopeid 0x16
```
[ENDFOLDOUT]

[FOLDOUT::WSL (Windows)]
TODO_Brandes
[ENDFOLDOUT]

<!-- time estimate: 10 min -->


### Funktionalität implementieren

[ER] Registrieren Sie einen POST-Endpunkt `/register`, der aus dem JSON-Payload Felder `username`
und `port` ausliest und in einer Tabelle `address map[string]string` als Paare (`username`
— `ip_addr:port`) speichert.
`ip_addr` kann der Server aus der `r *http.Request` auslesen.
Beachten Sie die Unterschiede zwischen IPv4 und IPv6 Adressen.

Soll ein solcher Name bereits vergeben sein, so gibt der Server Statuscode `400` und eine
informative Fehlermeldung zurück.

(Einen Auffrischer zu Servern und JSON finden Sie in den Aufgaben [PARTREF::go-http-server] und
[PARTREF::go-json]).

<!-- time estimate: 30 min -->

[ER] Registrieren Sie einen GET-Endpunkt `/{username}`, der entweder ein JSON zurückgibt, wo im Feld
`addr` die Adresse von `username` steht, oder den Statuscode `404` ("Not Found"), falls es keinen
solchen Benutzer gibt.

<!-- time estimate: 15 min -->

[ER] Implementieren Sie abschließend noch einen POST-Endpunkt `/unregister`.
Dieser soll aus dem JSON-Payload Felder `username` und `port` auslesen und den entsprechenden
Eintrag aus der Tabelle entfernen, sofern ein solches Benutzername-Adresse-Paar existiert.

<!-- time estimate: 15 min -->

[HINT::Wie teste ich das?]
<!-- TODO_2_Brandes: add link to task about `curl` once it is live -->
Die Funktionsfähigkeit vom Lookup-Server können Sie mittels `curl` überprüfen:

```bash
curl -X POST -d '{"username":"Alice","port":"8081"}' http://localhost:8083/register
```
— eine POST-Anfrage mit JSON-Payload.

```bash
curl -X GET http://localhost:8083/Alice
```
— eine GET-Anfrage.

Probieren Sie ein paar Kombinationen aus um sicherzustellen, dass Ihr Lookup-Server tatsächlich
funktioniert.
[ENDHINT]


### Firewall einstellen

Jetzt ist ein guter Zeitpunkt, um zu überprüfen, ob Ihr Lookup-Server von den anderen Rechnern
erreichbar ist.

Führen Sie __auf einem anderen Rechner im selben WLAN__ folgendes Befehl aus:

```bash
curl http://lookup_server_ip_address:8083/alice
```

Falls Sie direkt eine Antwort von Ihrem Lookup-Server bekommen — Klasse!

(Das ist nämlich dem Autor bei einer Anfrage von MacOS zum Lookup-Server auf PopOS passiert.)

Ansonsten müssen Sie die Firewall des Rechners einstellen, wo der Lookup-Server läuft.

[FOLDOUT::MacOS]
Läuft Ihr Lookup-Server auf MacOS, so bekommen Sie wahrscheinlich eine Pop-Up-Nachricht, ob Ihr Lookup-Programm
eingehende Verbindungen akzeptieren soll.

Klicken Sie in diesem Fenster "Erlauben".
[ENDFOLDOUT]

[FOLDOUT::WSL (Windows)]
__1. Eingehende Anfragen im Windows-Firewall erlauben.__
Öffnen Sie PowerShell mit Admin-Rechten und führen Sie folgendes Kommando aus:

```bash
netsh advfirewall firewall add rule name="Go Chat Lookup Server 8083" dir=in action=allow protocol=TCP localport=8083
```

Das Kommando kreiert eine neue Firewall-Regel, die eingehende TCP-Anfragen auf Port 8083 erlaubt.

__2. Virtuelle IP-Adresse von WSL-Umgebung ermitteln.__
Führen Sie folgendes Kommando in _WSL-Terminal_ aus:

```bash
ip addr | grep eth0
```

Die Ausgabe soll ähnlich aussehen:

```terminaloutput
$ ip addr | grep eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1280 qdisc mq state UP group default qlen 1000
    inet 172.29.96.181/20 brd 172.29.111.255 scope global eth0
```

Die IP-Adresse der WSL-Umgebung steht hinter `inet`, in dem Fall also `172.29.96.181`.

__3. Virtuelle IP-Adresse von WSL-Umgebung und die lokale IP-Adresse des Rechners verbinden.__
Führen Sie dieses Kommando __im PowerShell__ aus:

```bash
netsh interface portproxy add v4tov4 listenport=8083 listenaddress=0.0.0.0 connectaddress=172.29.96.181 connectport=8083
```

`0.0.0.0` ist eine andere Schreibweise für "dieser Rechner".

Dies kreiert eine Port-Forwarding-Regel in Windows:
Eingehende Anfragen auf Port `8083` werden nach `172.29.96.181:8083` (WSL-Umgebung, Port 8083)
weitergeleitet.
[ENDFOLDOUT]

Nun soll Ihr Lookup-Server von anderen Rechnern erreichbar sein.

<!-- time estimate: 30 min -->


### Testen

Starten Sie Ihren Lookup-Server und führen Sie in einem anderen Terminal folgende Kommandos aus:

- [EC] `curl -X GET http://localhost:8083/alice`
- [EC] `curl -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/register`
- [EC] `curl -X GET http://localhost:8083/alice`
- [EC] `curl -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/unregister`
- [EC] `curl -X GET http://localhost:8083/alice`

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]

**Kommandoprotokoll**
[PROT::ALT:go-chat-lookup-server.prot]

**Lösungen**
[INCLUDE::ALT:]

Quellcode als Teil des Projekts siehe unter [TREEREF::lookup].
[ENDINSTRUCTOR]
