# Viikkoraportti 5

Tällä viikolla olen ohjelmoinut graafista käyttöliittymää ja saanut otettua käyttöön sen ensimmäisen version. Laskuja voi syöttää joko käyttöliittymästä löytyvien nappien avulla, tai sitten suoraan kenttiin kirjoittamalla.

Projektin koodi on myös kauttaaltaan refaktoroitu, jossa toiminnallisuuksia on siirretty omiin luokkiinsa sekä lisätty uusi luokka `Calculate`, joka pitää sisällään kaikki laskennan aikana tarvittavat tiedot. Tähän työhön meni suurin osa tämän viikon tunneista.

Haastavinta tällä viikolla on ollut koodissa olevien virheiden metsästäminen sekä niiden korjaaminen ja tkinter kirjastoa hyödyntävien käyttöliittymien luomista helpottavan Pygubu kirjaston sekä käyttöliittymän visuaaliseen suunnitteluun tarkoitetun Pygubu-designer ohjelmaan tutustuminen. Pygubu ei aivan taipunut siihen, että olisin saanut sen kutsumaan funktioita argumenteilla, vaan jouduin keksimään tähän ongelmaan hieman niin sanotun purkkaratkaisun (löytyy `call_numpad` -metodista). 

Seuraavalla viikolla lisään laskimeen funktiot (cos, sin, tan, sqrt) sekä kirjoitan lisää testejä.

`Käytetyt tunnit: 20`

