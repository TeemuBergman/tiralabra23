# Viikkoraportti 2

Tällä viikolla olen ohjelmoinut Shunting yard -algoritmia ja olen onnistunut saamaan sen toimimaan peruslaskutoimituksilla. Haasteita tässä ohjelmointityössä oli saada algoritmin sijoittamaan tulosteessa olevat laskutoimitusten symbolit niiden oikeaan "reverse Polish notation" -järjestykseen. Löysin tähän liittyen Dijkstran alkuperäistä julkaisua hieman selkeämmän materiaalin [1], jossa löytyvä algoritmin pseudokoodiesitys avasi sen toiminnan hieman ymmärrettävämmin.

```pseudocode
# Shunting Yard Algorithm
While there are tokens to be read:
	Read a token
    If it's a number add it to queue
    If it's an operator
    	While there's an operator on the top of the stack with greater precedence:
        	Pop operators from the stack onto the output queue
		Push the current operator onto the stack
     If it's a left bracket push it onto the stack
     If it's a right bracket 
     	While there's not a left bracket at the top of the stack:
        	Pop operators from the stack onto the output queue.
        Pop the left bracket from the stack and discard it
While there are operators on the stack, pop them to the queue
```

Myös lukujen suurempi kuin yhdeksän ryhmittely omiin osajoukkoihin algoritmin tulosteessa oli pienoinen haaste, mutta ratkesi lopulta.

Projektiin on myös lisätty riippuvuuksien hallintaa hoitamaan Poetry, johon on asetettu muun muassa projektin kehityksen aikana käytettävät riippuvuudet: Pytest, Coverage, Autopep8 ja Pylint.

Olen lisäksi kirjoittanut projektin ensimmäiset yksikkötestit, jotka vertailevat eri syötteitä ja tulosteita Shunting yard -algoritmin suhteen ja ne menevät tällä hetkellä kaikki läpi. Tulen kuitenkin seuraavalla viikkolla lisäämään testikattavuutta ja otan siitä myös Coveragen tuottaman raportoinnin käyttöön.

Seuraavalla viikolla on tarkoitus laajentaa projektia ohjelmomalla Postfix expression stack evaluator -algoritmi, joka suorittaa varsinaiset laskutoimitukset Shunting yard -algoritmin tulosteista.

Käytetty tuntimäärä: 18

[1]: https://brilliant.org/wiki/shunting-yard-algorithm/	"Brilliant: Shunting Yard Algorithm"
