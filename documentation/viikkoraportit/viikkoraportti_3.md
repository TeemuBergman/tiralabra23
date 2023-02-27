# Viikkoraportti 3

Tällä viikolla olen ohjelmoinut algoritmia (postfix_evaluator), joka suorittaa RPN-muotoisista syötteistä niissä olevat laskutoimitukset.

Haasteita tällä hetkellä tuottavat peruslaskuissa olevat negatiiviset luvut `1+(-1)`, jotka aiheuttavat virheitä algoritmin suorituksen aikana.

Myös suurien lukujen käsittely aiheuttaa tällä hetkellä ongelmia, vaikkakin käsiteltävät luvut eivät ole float() muodossa, vaan käyttävät tähän tarkoitukseen paremmin soveltuvaa decimal -kirjastoa.

Olen myös ottanut käyttöön automaattista testausta ja raportointia varten GitHub Actions sekä Codecov -alustat.

Seuraavalla viikolla lisään laskimeen mahdollisuuden käyttää muuttujia, jonkinlaisen yksinkertaisen käyttöliittymän (ennen mahdollista graafista käyttöliittymää) sekä laajennan testikattavuutta.

`Käytetyt tunnit: 16`