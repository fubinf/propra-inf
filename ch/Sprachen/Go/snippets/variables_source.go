package main

import "fmt"

func main() {
	/*
	   hier müssen die fehlenden Variablen initialisiert werden.
	*/

	fmt.Printf(`
        An einem %s Morgen, genau um %d:%d Uhr, entdeckte ein mutiger Entdecker namens Jack eine mysteriöse %s.
        Er %s einen Weg durch den dichten Dschungel, und spürte sowohl %s als auch Aufregung.
        Plötzlich erreichte er die legendäre %s, in der %d alte Artefakte verborgen sein sollten.
        Ein %s beobachtete ihn von einem nahe gelegenen Baum und steigerte die Aufregung des Abenteuers. 
        Jack bemerkte auch einige riesige Fußspuren etwa %d Fuß entfernt
        (für die europäischen Freunde - ein Fuß entspricht genau %.4f Metern). 
        Obwohl verängstigt, beschloss er, tiefer in die %s vorzudringen. Wird er jemals zurückkehren?..
        `,
		adjective, hours, minutes, place, verb, state, landmark, number, animal, feet, metersInAFoot, landmark,
	)
}
