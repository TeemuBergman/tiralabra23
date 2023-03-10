# Tieteellinen laskin

[![Github Actions](https://github.com/TeemuBergman/tiralabra23/workflows/CI/badge.svg)](https://github.com/TeemuBergman/tiralabra23/actions/workflows/main.yml) [![codecov](https://codecov.io/gh/TeemuBergman/tiralabra23/branch/master/graph/badge.svg?token=3LZ03KXZAA)](https://codecov.io/gh/TeemuBergman/tiralabra23)

<img src="documentation/images/readme/screencap_scientific_calculator.png" style="zoom: 67%;" />

"Tieteellinen laskin" on Helsingin yliopiston "Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit" -kurssille tehty harjoitustyö. Sen keskeisin toiminta perustuu Edsger Dijkstran "Shuntig Yard" -algoritmiin, joka muuttaa syötetyn yhtälön postfix-muotoon, joka tunnetaan myös nimellä Reverse Polish Notation (RPN). Syötetyissä yhtälöissä on mahdollista käyttää myös funktioita sekä muuttujia (lisätiedot [käyttöohjessa](documentation/käyttöohje.md)).

## Dokumentaatio

- [Käyttöohje](documentation/käyttöohje.md)
- [Määrittelydokumentti](documentation/määrittelydokumentti.md)
- [Toteutusdokumentti](documentation/toteutusdokumentti.md)
- [Testausdokumentti](documentation/testausdokumentti.md)

#### Viikkoraportit

- [1. Viikkoraportti](documentation/viikkoraportit/viikkoraportti_1.md)
- [2. Viikkoraportti](documentation/viikkoraportit/viikkoraportti_2.md)
- [3. Viikkoraportti](documentation/viikkoraportit/viikkoraportti_3.md)
- [4. Viikkoraportti](documentation/viikkoraportit/viikkoraportti_4.md)
- [5. Viikkoraportti](documentation/viikkoraportit/viikkoraportti_5.md)
- [6. Viikkoraportti](documentation/viikkoraportit/viikkoraportti_6.md)

## Pikaohje

Ohjelmisto on toteutettu ja testattu [Python](https://www.python.org/)-versiolla `3.10` sekä riippuvuuksien hallintaan käytettävällä [Poetry](https://python-poetry.org/)-versiolla `1.3`. Vanhemmilla versioilla ohjelmiston toiminnassa saattaa esiintyä ongelmia. 

### Asentaminen ja käyttäminen

- [Ohjeet Pythonin asentamiseksi](https://www.python.org/downloads/).
- [Ohjeet Poetryn asentamiseksi](https://python-poetry.org/docs/).
- Lataa tämä repositorio koneellesi ja pura se haluamaasi paikkaan.
- Navigoi komentoriviä käyttäen purkamasi kansion juureen.
- Asenna projektin käyttämät riippuvuudet komennolla: `poetry install`.
- Siirry virtuaaliympäristöön komennolla: `poetry shell`.
- Käynnistä projekti komennolla: `invoke start`.
- Poistu virtuaaliympäristöstä komennolla `exit`.

### Ongelmatilanteet

Testauksessa on ilmennyt joidenkin Linux jakelujen sisältämä puuttellinen asennus Python 3:sta, joka ei jostain syystä sisällä kirjastoa `tkinter`. Jos projekti ei käynnisty `invoke start` komennolla, asenna kirjasto tkinter Poetry-virtuaaliympäristön ulkopuolella komennolla `sudo apt install python3-tk`.
